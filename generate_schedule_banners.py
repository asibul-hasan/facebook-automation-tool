#!/usr/bin/env python3
"""
Generate All 11 Custom Commercial Banners for 7-Day Matrix Schedule
"""
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BANNERS_DIR = os.path.join(BASE_DIR, "banners")
os.makedirs(BANNERS_DIR, exist_ok=True)
CHROME_BIN = "/usr/bin/google-chrome"

def render_banner(filename, html_content):
    temp_html = os.path.join(BASE_DIR, f"temp_{filename}.html")
    out_png = os.path.join(BANNERS_DIR, filename)
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--allow-file-access-from-files",
        "--window-size=1080,1080",
        f"--screenshot={out_png}",
        f"file://{temp_html}",
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if os.path.exists(temp_html):
        os.remove(temp_html)
    print(f"Generated {out_png} ({os.path.getsize(out_png)} bytes)")

# Banner 1: Day 1 Post 1 - Digital Marketing: ROI & Funnel Education
DAY1_AGENCY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#0b132b] via-[#1c2541] to-[#0b132b] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -left-20 w-96 h-96 bg-blue-500/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white font-black text-2xl en">IA</div><div><h2 class="text-2xl font-black en tracking-tight">Info AidTech</h2><p class="text-xs text-blue-400 font-bold uppercase en tracking-wider">Growth & Performance Marketing</p></div></div>
    <div class="px-5 py-2 rounded-full bg-blue-500/10 border border-blue-400/30 text-blue-300 text-xs font-bold en">DAY 1 · DIGITAL MARKETING ROI</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">বিজ্ঞাপনে বাজেট যাচ্ছে, কিন্তু কাঙ্ক্ষিত সেলস নেই?</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-teal-300 to-emerald-400 mt-2">স্কেল করুন ডাটা-ড্রিভেন সেলস ফানেলে</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">ব্লাইন্ড বুস্টিং বন্ধ করে ৩-ধাপের সেলস ফানেলে নিশ্চিত করুন <span class="text-emerald-400 font-extrabold en">5X - 8X ROAS</span></p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-md"><div class="w-12 h-12 rounded-xl bg-blue-500/20 flex items-center justify-center text-2xl mb-4">🎯</div><h4 class="text-xl font-bold text-blue-400 en">Top of Funnel</h4><p class="text-base text-slate-300 mt-2">ব্র্যান্ড অ্যাওয়ারনেস ও হাই-হুমিং ভিডিও ভিউ ক্যাম্পেইন</p></div>
    <div class="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-md border-teal-500/40"><div class="w-12 h-12 rounded-xl bg-teal-500/20 flex items-center justify-center text-2xl mb-4">⚡</div><h4 class="text-xl font-bold text-teal-400 en">Middle of Funnel</h4><p class="text-base text-slate-300 mt-2">এনগেজমেন্ট, ট্রাস্ট বিল্ডিং ও সোশ্যাল প্রুফ টেস্ট</p></div>
    <div class="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-md"><div class="w-12 h-12 rounded-xl bg-emerald-500/20 flex items-center justify-center text-2xl mb-4">💰</div><h4 class="text-xl font-bold text-emerald-400 en">Bottom of Funnel</h4><p class="text-base text-slate-300 mt-2">ডাইনামিক রিটার্গেটিং ও হাই-কনভার্টিং সেলস ক্লোজিং</p></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/80 border border-slate-700/60 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-emerald-500/20 flex items-center justify-center text-2xl text-emerald-400">📈</div><div><div class="text-lg font-bold text-white">আপনার বিজনেসের সেলস ফানেল অডিট করান</div><div class="text-sm text-slate-400">আমাদের এক্সপার্ট টিম দিবে সম্পূর্ণ ফ্রি ফানেল রোডম্যাপ</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-blue-600 to-teal-500 font-extrabold text-white text-base">ফ্রি কনসালটেশন নিন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">Performance Growth Partner</span></div>
</body></html>"""

# Banner 2: Day 1 Post 2 - AidlyPMS: Pain-Point Agitation
DAY1_AIDLY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#180a0a] via-[#2d1215] to-[#120809] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -left-20 w-96 h-96 bg-red-600/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-red-600 to-rose-700 flex items-center justify-center text-white font-black text-2xl en">✚</div><div><h2 class="text-2xl font-black en tracking-tight">Aidly PMS</h2><p class="text-xs text-rose-400 font-bold uppercase en tracking-wider">Smart Pharmacy Cloud ERP</p></div></div>
    <div class="px-5 py-2 rounded-full bg-red-500/10 border border-red-500/30 text-rose-300 text-xs font-bold en">DAY 1 · PAIN-POINT ALERT</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-rose-300">দিনশেষে হিসাব মিলছে না? ক্যাশ কাউন্টারে গরমিল?</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-rose-300 to-amber-300 mt-2">হিসাবের ভুলে ফার্মেসির লাভ কি লসে রূপ নিচ্ছে?</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">কাগজের খাতার দিন শেষ! এইডলি পিএমএস দিয়ে পান নির্ভুল অটোমেটেড ফার্মেসি সলিউশন</p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-red-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">❌</div><h4 class="text-xl font-bold text-rose-400">মেয়াদোত্তীর্ণের লোকসান</h4><p class="text-base text-slate-300 mt-2">অজান্তেই সেলফে ওষুধ মেয়াদ শেষ হয়ে হাজার হাজার টাকা লোকসান</p></div>
    <div class="bg-white/5 border border-red-500/30 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">❌</div><h4 class="text-xl font-bold text-amber-400">বাকির খাতায় জট</h4><p class="text-base text-slate-300 mt-2">কাগজের ডায়রিতে বকেয়া লিখে রাখলে টাকা আদায় হয় না, ভুলে যাওয়া হয়</p></div>
    <div class="bg-white/5 border border-red-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">❌</div><h4 class="text-xl font-bold text-rose-400">কাউন্টারে দীর্ঘ লাইন</h4><p class="text-base text-slate-300 mt-2">ওষুধ খুঁজতে গিয়ে কাস্টমার বিরক্ত হয়ে অন্য ফার্মেসিতে চলে যাওয়া</p></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-emerald-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-emerald-500/20 flex items-center justify-center text-2xl text-emerald-400">🛡️</div><div><div class="text-lg font-bold text-white">সমাধান আছে এইডলি পিএমএস-এ</div><div class="text-sm text-emerald-300">৩ সেকেন্ডে বিলিং · অটো FEFO এক্সপায়ারি · ডিজিটাল SMS বাকি খাতা</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-500 font-extrabold text-white text-base">ফ্রি ডেমো বুক করুন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">By Info AidTech</span></div>
</body></html>"""

# Banner 3: Day 2 Post 1 - Social Media Marketing: Algorithm & Engagement
DAY2_AGENCY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#0a1128] via-[#101f42] to-[#0a1128] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -right-20 w-96 h-96 bg-purple-500/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white font-black text-2xl en">IA</div><div><h2 class="text-2xl font-black en tracking-tight">Info AidTech</h2><p class="text-xs text-purple-400 font-bold uppercase en tracking-wider">Social Growth & SMM Strategy</p></div></div>
    <div class="px-5 py-2 rounded-full bg-purple-500/10 border border-purple-400/30 text-purple-300 text-xs font-bold en">DAY 2 · ALGORITHM & ENGAGEMENT</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">পেইজের রিচ ও এনগেজমেন্ট কি হঠাৎ কমে গেছে?</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-purple-400 via-pink-300 to-indigo-400 mt-2">2026 Meta Algorithm হ্যাক করুন</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">অ্যালগরিদমের সাথে যুদ্ধ না করে শিখুন কোন ৩টি বিষয় মেটা সবচেয়ে বেশি রিওয়ার্ড করে</p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-purple-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">⏱️</div><h4 class="text-xl font-bold text-purple-400 en">Dwell Time Priority</h4><p class="text-base text-slate-300 mt-2">ইউজার আপনার পোস্টে কত সেকেন্ড সময় কাটাচ্ছে সেটাই মূল বিষয়</p></div>
    <div class="bg-white/5 border border-pink-500/30 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🔄</div><h4 class="text-xl font-bold text-pink-400 en">Shares & DMs Ratio</h4><p class="text-base text-slate-300 mt-2">শুধু লাইক নয়, শেয়ার এবং মেসেঞ্জারে শেয়ার পোস্টকে ভাইরাল করে</p></div>
    <div class="bg-white/5 border border-indigo-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">💬</div><h4 class="text-xl font-bold text-indigo-400 en">Meaningful Comments</h4><p class="text-base text-slate-300 mt-2">বিতর্ক ও ভ্যালু ক্রিয়েটিং আলোচনা অর্গানিক রিচ বাড়িয়ে দেয় ৩ গুণ</p></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-purple-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-purple-500/20 flex items-center justify-center text-2xl text-purple-400">🚀</div><div><div class="text-lg font-bold text-white">আপনার সোশ্যাল মিডিয়া গ্রোথ রোডম্যাপ চান?</div><div class="text-sm text-purple-300">আমাদের কনটেন্ট স্ট্র্যাটেজিস্টদের সাথে কথা বলুন</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 font-extrabold text-white text-base">ইনবক্স করুন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">SMM Experts</span></div>
</body></html>"""

# Banner 4: Day 3 Post 1 - Digital Marketing: Lead Generation & SEO
DAY3_AGENCY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#081b29] via-[#0d2d44] to-[#081b29] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -left-20 w-96 h-96 bg-cyan-500/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center text-white font-black text-2xl en">IA</div><div><h2 class="text-2xl font-black en tracking-tight">Info AidTech</h2><p class="text-xs text-cyan-400 font-bold uppercase en tracking-wider">Search Engine & Inbound Leads</p></div></div>
    <div class="px-5 py-2 rounded-full bg-cyan-500/10 border border-cyan-400/30 text-cyan-300 text-xs font-bold en">DAY 3 · SEO & LEAD GENERATION</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">সোশ্যাল মিডিয়ার বাইরেও ক্লায়েন্ট খুঁজছেন?</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-sky-300 to-blue-400 mt-2">গুগল থেকে পান হাই-ইনটেন্ট বিটুবি লিড</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">অর্গানিক সার্চ ইঞ্জিন অপটিমাইজেশন (SEO) দিয়ে আপনার ওয়েবসাইটকে বানান ক্লায়েন্ট ম্যাগনেট</p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-cyan-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🔍</div><h4 class="text-xl font-bold text-cyan-400 en">Local Google SEO</h4><p class="text-base text-slate-300 mt-2">গুগল ম্যাপ ও লোকাল সার্চে ১ নম্বর র‍্যাঙ্কিং নিশ্চিত করুন</p></div>
    <div class="bg-white/5 border border-sky-500/30 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🎯</div><h4 class="text-xl font-bold text-sky-400 en">High-Intent Keywords</h4><p class="text-base text-slate-300 mt-2">যেসব কাস্টমার কেনার জন্য সার্চ করে তাদের ট্রাফিকে কনভার্ট করুন</p></div>
    <div class="bg-white/5 border border-blue-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">📊</div><h4 class="text-xl font-bold text-blue-400 en">0 Ad Spend Leads</h4><p class="text-base text-slate-300 mt-2">বিজ্ঞাপনে ১ টাকাও খরচ না করে প্রতিদিন রেগুলার লিড ও কল</p></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-cyan-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-cyan-500/20 flex items-center justify-center text-2xl text-cyan-400">💎</div><div><div class="text-lg font-bold text-white">আপনার ওয়েবসাইটের ফ্রি SEO অডিট করুন</div><div class="text-sm text-cyan-300">টেকনিক্যাল এরর ও র‍্যাঙ্কিং রিপোর্ট পান ২৪ ঘণ্টায়</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-cyan-600 to-blue-600 font-extrabold text-white text-base">ফ্রি অডিট রিপোর্ট নিন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">Search Marketing</span></div>
</body></html>"""

# Banner 5: Day 3 Post 2 - AidlyPMS: Feature Spotlight (3-Second POS Billing)
DAY3_AIDLY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#021f15] via-[#053826] to-[#021f15] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -right-20 w-96 h-96 bg-emerald-500/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center text-white font-black text-2xl en">✚</div><div><h2 class="text-2xl font-black en tracking-tight">Aidly PMS</h2><p class="text-xs text-emerald-400 font-bold uppercase en tracking-wider">Superfast Cloud POS</p></div></div>
    <div class="px-5 py-2 rounded-full bg-emerald-500/10 border border-emerald-400/30 text-emerald-300 text-xs font-bold en">DAY 3 · FEATURE SPOTLIGHT</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">কাউন্টারে কাস্টমারের লম্বা লাইন ও ড্রাগ খুঁজতে দেরি?</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-300 mt-2">মাত্র ৩ সেকেন্ডে বারকোড POS বিলিং</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">বারকোড স্ক্যান, ক্যাশ/বিকাশ পেমেন্ট রিসিভ ও ইনস্ট্যান্ট থার্মাল প্রিন্ট</p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-emerald-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">⚡</div><h4 class="text-xl font-bold text-emerald-400">৩ সেকেন্ড চেকআউট</h4><p class="text-base text-slate-300 mt-2">ক্যালকুলেটর ছাড়া নিখুঁত বিল, ভুল ড্রাগ সিলেক্ট হওয়ার সুযোগ নেই</p></div>
    <div class="bg-white/5 border border-teal-500/30 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">💳</div><h4 class="text-xl font-bold text-teal-400">ক্যাশ ও মোবাইল ব্যাংকিং</h4><p class="text-base text-slate-300 mt-2">ক্যাশ, কার্ড এবং বিকাশ/নগদে ওয়ান-ট্যাপ ইনস্ট্যান্ট পেমেন্ট রিসিভ</p></div>
    <div class="bg-white/5 border border-cyan-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🔄</div><h4 class="text-xl font-bold text-cyan-400">লাইভ স্টক অটো-সিঙ্ক</h4><p class="text-base text-slate-300 mt-2">একাধিক কাউন্টার থাকলেও স্টক স্বয়ংক্রিয়ভাবে রিয়েল-টাইমে আপডেট</p></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-emerald-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-emerald-500/20 flex items-center justify-center text-2xl text-emerald-400">✨</div><div><div class="text-lg font-bold text-white">আজই টেস্ট করুন লাইভ POS ডেমো</div><div class="text-sm text-emerald-300">কোনো সফটওয়্যার ইনস্টল ছাড়াই ব্রাউজারে ডেমো দেখুন</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-500 font-extrabold text-white text-base">ফ্রি ট্রায়াল নিন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">Aidly PMS</span></div>
</body></html>"""

# Banner 6: Day 4 Post 1 - Social Media Marketing: Social Commerce BD
DAY4_AGENCY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#111827] via-[#1f2937] to-[#111827] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -left-20 w-96 h-96 bg-amber-500/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-amber-500 to-orange-600 flex items-center justify-center text-white font-black text-2xl en">IA</div><div><h2 class="text-2xl font-black en tracking-tight">Info AidTech</h2><p class="text-xs text-amber-400 font-bold uppercase en tracking-wider">Social Commerce Bangladesh</p></div></div>
    <div class="px-5 py-2 rounded-full bg-amber-500/10 border border-amber-400/30 text-amber-300 text-xs font-bold en">DAY 4 · SOCIAL COMMERCE BD</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">ইনবক্সে কাস্টমার আসে, কিন্তু অর্ডার কনফার্ম করে না?</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-orange-300 to-yellow-300 mt-2">সোশ্যাল কমার্সে ডাবল কনভার্সন রেট</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">বাংলাদেশের কাস্টমার সাইকোলজি বুঝে ইনবক্স কনভার্সন রেট বাড়ান <span class="text-amber-400 font-extrabold en">35% - 50%</span></p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-amber-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">💬</div><h4 class="text-xl font-bold text-amber-400">ইনস্ট্যান্ট রেসপন্স বটস</h4><p class="text-base text-slate-300 mt-2">ইনবক্স আসার ১ মিনিটের মধ্যে রেসপন্স দিলে কনভার্সন দ্বিগুণ হয়</p></div>
    <div class="bg-white/5 border border-orange-500/30 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🤝</div><h4 class="text-xl font-bold text-orange-400">ট্রাস্ট ও সিওডি পলিসি</h4><p class="text-base text-slate-300 mt-2">ক্যাশ অন ডেলিভারি ও রিয়েল আনবক্সিং ভিডিও দিয়ে কাস্টমার আস্থা অর্জন</p></div>
    <div class="bg-white/5 border border-yellow-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🛒</div><h4 class="text-xl font-bold text-yellow-400">আপসেল ও ক্রস-সেল</h4><p class="text-base text-slate-300 mt-2">একটি অর্ডারের সাথে কম্বো অফার দিয়ে অ্যাভারেজ অর্ডার ভ্যালু বৃদ্ধি</p></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-amber-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-amber-500/20 flex items-center justify-center text-2xl text-amber-400">📦</div><div><div class="text-lg font-bold text-white">আপনার ই-কমার্স ও পেইজের সেলস বাড়াতে চান?</div><div class="text-sm text-amber-300">আমাদের ফুল-স্ট্যাক কমার্স গ্রোথ টিমের সাথে যুক্ত হোন</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-amber-600 to-orange-600 font-extrabold text-white text-base">ইনবক্স করুন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">Ecommerce BD</span></div>
</body></html>"""

# Banner 7: Day 5 Post 1 - Digital Marketing: Data & Retargeting
DAY5_AGENCY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#0f172a] via-[#1e293b] to-[#0f172a] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -right-20 w-96 h-96 bg-blue-600/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center text-white font-black text-2xl en">IA</div><div><h2 class="text-2xl font-black en tracking-tight">Info AidTech</h2><p class="text-xs text-blue-400 font-bold uppercase en tracking-wider">Performance Data & Pixels</p></div></div>
    <div class="px-5 py-2 rounded-full bg-blue-500/10 border border-blue-400/30 text-blue-300 text-xs font-bold en">DAY 5 · DATA & RETARGETING</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">৯৭% ভিজিটর প্রথম দেখায় কেনে না!</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-300 to-sky-300 mt-2">স্মার্ট রিটার্গেটিংয়ে কমান ৬০% অ্যাড কস্ট</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">যারা পেইজে এসেছে বা ভিডিও দেখেছে তাদের কাছে বিশেষ অফার নিয়ে পৌঁছান</p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-blue-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">👥</div><h4 class="text-xl font-bold text-blue-400 en">Custom Audience</h4><p class="text-base text-slate-300 mt-2">যারা অলরেডি আপনার ব্র্যান্ড চেনে তাদের টার্গেট করে সর্বোচ্চ কনভার্সন</p></div>
    <div class="bg-white/5 border border-indigo-500/30 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🎯</div><h4 class="text-xl font-bold text-indigo-400 en">Lookalike Audience</h4><p class="text-base text-slate-300 mt-2">বর্তমান সেরা বায়ারদের মতো দেখতে নতুন সম্ভাব্য গ্রাহকদের খুঁজে বের করা</p></div>
    <div class="bg-white/5 border border-sky-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">📉</div><h4 class="text-xl font-bold text-sky-400 en">Lowest Cost-Per-Acq</h4><p class="text-base text-slate-300 mt-2">কোল্ড অডিয়েন্সের চেয়ে রিটার্গেটিংয়ে প্রতি অর্ডারের খরচ কমে অর্ধেকের বেশি</p></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-blue-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-blue-500/20 flex items-center justify-center text-2xl text-blue-400">📊</div><div><div class="text-lg font-bold text-white">মেটা পিক্সেল ও কনভার্সন API সেটআপ করান</div><div class="text-sm text-blue-300">১০০% নির্ভুল সার্ভার-সাইড ট্র্যাকিং ও ইভেন্ট সেটআপ</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 font-extrabold text-white text-base">ফ্রি কনসালটেশন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">Data Marketing</span></div>
</body></html>"""

# Banner 8: Day 5 Post 2 - AidlyPMS: ROI & Cost Savings
DAY5_AIDLY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#031d17] via-[#053229] to-[#031d17] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -left-20 w-96 h-96 bg-emerald-500/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center text-white font-black text-2xl en">✚</div><div><h2 class="text-2xl font-black en tracking-tight">Aidly PMS</h2><p class="text-xs text-emerald-400 font-bold uppercase en tracking-wider">Pharmacy ROI & Savings</p></div></div>
    <div class="px-5 py-2 rounded-full bg-emerald-500/10 border border-emerald-400/30 text-emerald-300 text-xs font-bold en">DAY 5 · ROI & COST SAVINGS</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">হিসাব করে দেখুন প্রতি মাসে কত টাকা নষ্ট হচ্ছে!</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-300 mt-2">Aidly PMS বাঁচাবে প্রতি মাসে ৳ ২৫,০০০+</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">সফটওয়্যারের নামমাত্র খরচে ওষুধের অপচয় বন্ধ করুন ও বকেয়া দ্রুত তুলুন</p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-emerald-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🛡️</div><h4 class="text-xl font-bold text-emerald-400">৳ ১৫,০০০+ এক্সপায়ারি সাশ্রয়</h4><p class="text-base text-slate-300 mt-2">মেয়াদ শেষ হওয়ার আগেই কোম্পানি রিটার্ন দিয়ে শূন্য লোকসান</p></div>
    <div class="bg-white/5 border border-teal-500/30 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">⏱️</div><h4 class="text-xl font-bold text-teal-400">৫০+ ঘণ্টার কর্মঘণ্টা সাশ্রয়</h4><p class="text-base text-slate-300 mt-2">ম্যানুয়াল খাতা লেখার সময় বাঁচিয়ে ড্রাগ সেলসে ফোকাস করুন</p></div>
    <div class="bg-white/5 border border-cyan-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">💰</div><h4 class="text-xl font-bold text-cyan-400">৯০% বকেয়া দ্রুত রিকভারি</h4><p class="text-base text-slate-300 mt-2">SMS তাগাদায় আটকে থাকা বকেয়া টাকা তাৎক্ষণিক কালেকশন</p></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-emerald-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-emerald-500/20 flex items-center justify-center text-2xl text-emerald-400">📈</div><div><div class="text-lg font-bold text-white">আজই ফার্মেসিকে লাভজনক করুন</div><div class="text-sm text-emerald-300">কোনো হিডেন ফি নেই · লাইভ ট্রেনিং ও ২৪/৭ বাংলা সাপোর্ট</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-500 font-extrabold text-white text-base">ফ্রি ডেমো বুক করুন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">Aidly PMS</span></div>
</body></html>"""

# Banner 9: Day 6 Post 1 - Social Media Marketing: Content Strategy
DAY6_AGENCY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#1a102f] via-[#241744] to-[#1a102f] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -right-20 w-96 h-96 bg-fuchsia-500/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-fuchsia-500 to-purple-600 flex items-center justify-center text-white font-black text-2xl en">IA</div><div><h2 class="text-2xl font-black en tracking-tight">Info AidTech</h2><p class="text-xs text-fuchsia-400 font-bold uppercase en tracking-wider">Content Strategy & Storytelling</p></div></div>
    <div class="px-5 py-2 rounded-full bg-fuchsia-500/10 border border-fuchsia-400/30 text-fuchsia-300 text-xs font-bold en">DAY 6 · CONTENT STRATEGY</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">বোরিং প্রমোশন বাদ দিয়ে থামান কাস্টমারের স্ক্রোল!</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-fuchsia-400 via-pink-300 to-purple-300 mt-2">থাম্ব-স্টপিং সোশ্যাল কনটেন্ট ফ্রেমওয়ার্ক</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">হুক, রিলেটেবল প্রবলেম এবং ক্লিয়ার কল-টু-অ্যাকশন দিয়ে বানান ভাইরাল কনটেন্ট</p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-fuchsia-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🪝</div><h4 class="text-xl font-bold text-fuchsia-400">প্রথম ৩ সেকেন্ডের হুক</h4><p class="text-base text-slate-300 mt-2">এমন বাক্য বা ভিজুয়াল যা মোবাইল ফিডে থামতে বাধ্য করে</p></div>
    <div class="bg-white/5 border border-pink-500/30 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">📖</div><h4 class="text-xl font-bold text-pink-400">প্রবলেম-সলিউশন স্টোরি</h4><p class="text-base text-slate-300 mt-2">কাস্টমারের দৈনন্দিন সমস্যাকে উপজীব্য করে আবেগী সংযোগ তৈরি</p></div>
    <div class="bg-white/5 border border-purple-500/20 rounded-2xl p-6 backdrop-blur-md"><div class="text-3xl mb-3">🎯</div><h4 class="text-xl font-bold text-purple-400">ক্লিন ও বোল্ড কল টু অ্যাকশন</h4><p class="text-base text-slate-300 mt-2">স্পষ্ট নির্দেশিকা: 'ইনবক্স করুন' অথবা 'ওয়েবসাইট ভিজিট করুন'</p></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-fuchsia-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-fuchsia-500/20 flex items-center justify-center text-2xl text-fuchsia-400">✨</div><div><div class="text-lg font-bold text-white">আপনার ব্র্যান্ডের জন্য কনটেন্ট ক্যালেন্ডার চান?</div><div class="text-sm text-fuchsia-300">আমাদের ক্রিয়েটিভ টিম ডিজাইন করবে মাসিক শিডিউল</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-fuchsia-600 to-purple-600 font-extrabold text-white text-base">কনটেন্ট প্ল্যান নিন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">Creative Studio</span></div>
</body></html>"""

# Banner 10: Day 7 Post 1 - Digital Marketing: Weekly Tool Stack
DAY7_AGENCY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#0b1426] via-[#132240] to-[#0b1426] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -left-20 w-96 h-96 bg-blue-500/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-blue-600 to-indigo-600 flex items-center justify-center text-white font-black text-2xl en">IA</div><div><h2 class="text-2xl font-black en tracking-tight">Info AidTech</h2><p class="text-xs text-blue-400 font-bold uppercase en tracking-wider">MarTech & AI Automation Stack</p></div></div>
    <div class="px-5 py-2 rounded-full bg-blue-500/10 border border-blue-400/30 text-blue-300 text-xs font-bold en">DAY 7 · WEEKLY TOOL STACK</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">আমরা যেসব এআই ও মার্কেটিং টুল ব্যবহার করি!</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-teal-300 to-indigo-300 mt-2">২০২৬ সালের টপ ডিজিটাল মার্কেটিং টেক স্ট্যাক</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">অটোমেশন ও এআই ইন্টিগ্রেশনে ক্লায়েন্টদের এনে দিচ্ছি <span class="text-teal-400 font-extrabold en">10X Production Speed</span></p>
  </div>
  <div class="grid grid-cols-4 gap-4 z-10 my-3">
    <div class="bg-white/5 border border-white/10 rounded-2xl p-4 text-center backdrop-blur-md"><div class="text-3xl mb-2">⚡</div><div class="font-bold text-blue-400 text-base en">Meta Ads API</div><div class="text-xs text-slate-300 mt-1">অটোমেটেড অ্যাড রুলস</div></div>
    <div class="bg-white/5 border border-white/10 rounded-2xl p-4 text-center backdrop-blur-md"><div class="text-3xl mb-2">🤖</div><div class="font-bold text-teal-400 text-base en">Remotion Video</div><div class="text-xs text-slate-300 mt-1">প্রোগ্রামাটিক রেন্ডার</div></div>
    <div class="bg-white/5 border border-white/10 rounded-2xl p-4 text-center backdrop-blur-md"><div class="text-3xl mb-2">📈</div><div class="font-bold text-indigo-400 text-base en">GA4 & CAPI</div><div class="text-xs text-slate-300 mt-1">সার্ভার-সাইড ট্র্যাকিং</div></div>
    <div class="bg-white/5 border border-white/10 rounded-2xl p-4 text-center backdrop-blur-md"><div class="text-3xl mb-2">🧠</div><div class="font-bold text-emerald-400 text-base en">DeepSeek / LLMs</div><div class="text-xs text-slate-300 mt-1">হাই-কনভার্টিং কপি</div></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-teal-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-teal-500/20 flex items-center justify-center text-2xl text-teal-400">⚙️</div><div><div class="text-lg font-bold text-white">আপনার বিজনেসেও এমন অটোমেশন চান?</div><div class="text-sm text-teal-300">মার্কেটিং ও সফটওয়্যার অটোমেশনের জন্য আলোচনা করুন</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-blue-600 to-teal-500 font-extrabold text-white text-base">যোগাযোগ করুন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">Technology First</span></div>
</body></html>"""

# Banner 11: Day 7 Post 2 - AidlyPMS: Social Proof & Trust
DAY7_AIDLY_HTML = """<!DOCTYPE html>
<html lang="bn"><head><meta charset="UTF-8"><script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800;900&family=Hind+Siliguri:wght@600;700;800&display=swap" rel="stylesheet"><style>body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; } .en { font-family: 'Plus Jakarta Sans', sans-serif; }</style></head>
<body class="w-[1080px] h-[1080px] bg-gradient-to-b from-[#021c13] via-[#053323] to-[#021c13] text-white p-10 flex flex-col justify-between overflow-hidden relative select-none">
  <div class="absolute -top-20 -right-20 w-96 h-96 bg-emerald-500/20 rounded-full blur-3xl"></div>
  <div class="flex items-center justify-between z-10">
    <div class="flex items-center gap-3"><div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-emerald-500 to-teal-600 flex items-center justify-center text-white font-black text-2xl en">✚</div><div><h2 class="text-2xl font-black en tracking-tight">Aidly PMS</h2><p class="text-xs text-emerald-400 font-bold uppercase en tracking-wider">Trusted by Pharmacies Across BD</p></div></div>
    <div class="px-5 py-2 rounded-full bg-emerald-500/10 border border-emerald-400/30 text-emerald-300 text-xs font-bold en">DAY 7 · SOCIAL PROOF & TRUST</div>
  </div>
  <div class="text-center z-10">
    <h3 class="text-3xl font-bold text-slate-300">"হিসাব মেলানো এখন আগের চেয়ে ৫ গুণ সহজ!"</h3>
    <h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-300 mt-2">সারা বাংলাদেশের ফার্মেসির আস্থা Aidly PMS</h1>
    <p class="text-xl text-slate-300 mt-3 max-w-2xl mx-auto">শত শত সফল ফার্মেসি প্রতিদিন ভরসা রাখছে ক্লাউড-ফার্স্ট এইডলি পিএমএস-এ</p>
  </div>
  <div class="grid grid-cols-3 gap-6 z-10 my-4">
    <div class="bg-white/5 border border-emerald-500/20 rounded-2xl p-6 text-center backdrop-blur-md"><div class="text-4xl font-extrabold text-emerald-400 en mb-1">500+</div><div class="text-lg font-bold text-white">সফল ফার্মেসি পার্টনার</div><div class="text-sm text-slate-300 mt-1">সারা বাংলাদেশে নিয়মিত ইউজার</div></div>
    <div class="bg-white/5 border border-teal-500/30 rounded-2xl p-6 text-center backdrop-blur-md"><div class="text-4xl font-extrabold text-teal-400 en mb-1">99.9%</div><div class="text-lg font-bold text-white">ক্লাউড আপটাইম</div><div class="text-sm text-slate-300 mt-1">ডেটা সম্পূর্ণ সুরক্ষিত ও ব্যাকআপড</div></div>
    <div class="bg-white/5 border border-cyan-500/20 rounded-2xl p-6 text-center backdrop-blur-md"><div class="text-4xl font-extrabold text-cyan-400 en mb-1">24/7</div><div class="text-lg font-bold text-white">ডেডিকেটেড বাংলা সাপোর্ট</div><div class="text-sm text-slate-300 mt-1">যে কোনো প্রয়োজনে সরাসরি সহায়তা</div></div>
  </div>
  <div class="flex items-center justify-between z-10 bg-slate-900/90 border border-emerald-500/40 rounded-2xl p-5">
    <div class="flex items-center gap-4"><div class="w-12 h-12 rounded-full bg-emerald-500/20 flex items-center justify-center text-2xl text-emerald-400">🏆</div><div><div class="text-lg font-bold text-white">আজই যুক্ত হোন বিশ্বস্ত ফার্মেসি কমিউনিটিতে</div><div class="text-sm text-emerald-300">ফ্রি লাইভ ডেমো দেখে সিদ্ধান্ত নিন</div></div></div>
    <div class="px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-500 font-extrabold text-white text-base">ফ্রি ডেমো বুক করুন ➔</div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3 z-10"><span class="en">🌐 infoaidtech.net</span><span>💬 ইনবক্স করুন Facebook-এ</span><span class="en">Aidly PMS</span></div>
</body></html>"""

ALL_BANNERS = [
    ("day1_agency_roi_funnel.png", DAY1_AGENCY_HTML),
    ("day1_aidly_pain_point.png", DAY1_AIDLY_HTML),
    ("day2_agency_algorithm.png", DAY2_AGENCY_HTML),
    ("day3_agency_leadgen_seo.png", DAY3_AGENCY_HTML),
    ("day3_aidly_pos_spotlight.png", DAY3_AIDLY_HTML),
    ("day4_agency_social_commerce.png", DAY4_AGENCY_HTML),
    ("day5_agency_data_retargeting.png", DAY5_AGENCY_HTML),
    ("day5_aidly_roi_savings.png", DAY5_AIDLY_HTML),
    ("day6_agency_content_strategy.png", DAY6_AGENCY_HTML),
    ("day7_agency_tool_stack.png", DAY7_AGENCY_HTML),
    ("day7_aidly_social_proof.png", DAY7_AIDLY_HTML),
]

def generate_all():
    for name, html in ALL_BANNERS:
        print(f"Rendering banner: {name}...")
        render_banner(name, html)
    print("\nAll 11 schedule banners generated successfully!")

if __name__ == "__main__":
    generate_all()
