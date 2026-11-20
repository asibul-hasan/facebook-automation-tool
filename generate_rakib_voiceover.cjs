const { convertTextToSpeech } = require("./elevenlabs_client.js");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const scenes = [
  { id: "s1", delayMs: 0, text: "রাত ৮টা ১৫। কাউন্টারে ১০ জন সিরিয়ালে—স্ক্রিন হ্যাং!" },
  { id: "s2", delayMs: 4500, text: "ট্যাবের ঝামেলায় কাস্টমার ফেরত, আর এক্সপায়ার্ড স্টকে লস হয় আপনার লাভ।" },
  { id: "s3", delayMs: 9500, text: "পিক আওয়ারে আর কোনো টেনশন নয়। নিয়ে আসুন Aidly PMS।" },
  { id: "s4", delayMs: 14000, text: "ক্লিন POS-এ ওষুধ সার্চ, জেনেরিক চেক আর ৩ সেকেন্ডে দ্রুত ক্যাশ মেমো।" },
  { id: "s5", delayMs: 20000, text: "অটো ব্যাচ অ্যালার্ট আগেভাগেই জানাবে এক্সপায়ারি—১ টাকাও লস নয়।" },
  { id: "s6", delayMs: 25000, text: "লাইন এগোবে দ্রুত, হিসাব থাকবে ক্লিয়ার। ফ্রি ডেমোর জন্য কমেন্ট করুন AIDLY!" }
];

const sfxDir = "/home/asibul/app/features/automation/ai-product-video/template/public/audio";
const sfx = [
  { path: `${sfxDir}/ui/chime-crystal.mp3`, delayMs: 9500, vol: 0.35 },
  { path: `${sfxDir}/ui/ui-confirm-tone.mp3`, delayMs: 14000, vol: 0.30 },
  { path: `${sfxDir}/ui/ui-notify-tech.mp3`, delayMs: 20000, vol: 0.35 },
  { path: `${sfxDir}/ui/ui-success-soft.mp3`, delayMs: 25000, vol: 0.35 }
];

async function main() {
  const workDir = "/tmp/rakib_audio_build";
  fs.mkdirSync(workDir, { recursive: true });

  const voiceInputs = [];
  const voiceFilters = [];

  for (let i = 0; i < scenes.length; i++) {
    const s = scenes[i];
    const target = path.join(workDir, `${s.id}.mp3`);
    console.log(`Generating ElevenLabs Rakib voice for ${s.id}: "${s.text}"`);
    await convertTextToSpeech(s.text, target);

    const dur = parseFloat(
      execSync(`~/.local/bin/ffprobe -i "${target}" -show_entries format=duration -v quiet -of csv="p=0"`)
        .toString()
        .trim()
    );
    console.log(`-> ${s.id} duration: ${dur.toFixed(2)}s`);

    voiceInputs.push(`-i "${target}"`);
    voiceFilters.push(`[${i}:a]adelay=${s.delayMs}|${s.delayMs}[v${i}]`);
  }

  // SFX inputs
  const sfxInputs = [];
  const sfxFilters = [];
  let sfxStartIndex = scenes.length;

  for (let j = 0; j < sfx.length; j++) {
    const item = sfx[j];
    const streamIdx = sfxStartIndex + j;
    sfxInputs.push(`-i "${item.path}"`);
    sfxFilters.push(`[${streamIdx}:a]volume=${item.vol},adelay=${item.delayMs}|${item.delayMs}[sfx${j}]`);
  }

  const allLabels = [
    ...scenes.map((_, i) => `[v${i}]`),
    ...sfx.map((_, j) => `[sfx${j}]`)
  ].join("");

  const totalInputs = scenes.length + sfx.length;
  const amix = `${allLabels}amix=inputs=${totalInputs}:dropout_transition=0,volume=2.8[aout]`;
  const filterComplex = [...voiceFilters, ...sfxFilters, amix].join(";");

  const outAudio = "/home/asibul/app/features/automation/aidly-story-01-bn/assets/voiceover.mp3";
  const ffmpegCmd = `~/.local/bin/ffmpeg -y ${voiceInputs.join(" ")} ${sfxInputs.join(" ")} -filter_complex "${filterComplex}" -map "[aout]" -t 30.0 "${outAudio}"`;

  console.log("\nMixing master Rakib audio track with SFX...");
  execSync(ffmpegCmd, { stdio: "inherit" });

  console.log(`\nMaster Rakib voiceover successfully written to: ${outAudio}`);
}

main().catch(console.error);
