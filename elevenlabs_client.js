const dotenv = require("dotenv");
dotenv.config({ path: ".env.local" });

const { ElevenLabsClient } = require("@elevenlabs/elevenlabs-js");
const { createWriteStream } = require("fs");
const { Readable } = require("stream");

const client = new ElevenLabsClient();

async function convertTextToSpeech(text, outputPath, voiceId = "JBFqnCBsd6RMkjVDRZzb") {
  const audio = await client.textToSpeech.convert(voiceId, {
    text,
    modelId: "eleven_multilingual_v2",
  });
  return new Promise((resolve, reject) => {
    const stream = Readable.fromWeb(audio);
    const writeStream = createWriteStream(outputPath);
    stream.pipe(writeStream);
    writeStream.on("finish", () => resolve(outputPath));
    writeStream.on("error", reject);
  });
}

module.exports = { client, convertTextToSpeech };
