#!/usr/bin/env python3
"""
Aidly PMS & Info AidTech High-Converting Banner Generator
---------------------------------------------------------
Renders authentic software UI mockups into pixel-perfect 1200x630
marketing banners using headless Google Chrome.
"""

import os
import subprocess
import tempfile

BANNERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "banners")
os.makedirs(BANNERS_DIR, exist_ok=True)

TEMPLATES = {
    "aidly_pos_billing.png": """
<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200, height=630">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Hind+Siliguri:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; }
    .en { font-family: 'Plus Jakarta Sans', sans-serif; }
  </style>
</head>
<body class="w-[1200px] h-[630px] bg-gradient-to-br from-slate-950 via-slate-900 to-emerald-950 text-white p-10 flex flex-row items-center justify-between overflow-hidden relative select-none">
  <div class="absolute -top-32 -left-32 w-[500px] h-[500px] bg-emerald-500/15 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-[600px] h-[600px] bg-teal-500/15 rounded-full blur-3xl pointer-events-none"></div>

  <!-- Left Content -->
  <div class="w-[480px] z-10 flex flex-col justify-between h-full py-2">
    <div>
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-semibold en">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        Aidly PMS · Smart Pharmacy POS
      </div>

      <h1 class="text-[34px] font-bold leading-[1.25] text-white mt-4">
        কাউন্টারে লম্বা লাইন? মাত্র <span class="text-emerald-400 font-extrabold">৩ সেকেন্ডে</span> বারকোড POS বিলিং!
      </h1>
      
      <p class="text-slate-300 text-[15px] leading-relaxed mt-3">
        ম্যানুয়ালি ওষুধ খোঁজা আর খাতায় হিসাব লেখার দিন শেষ। ক্যাশিয়ারের ভুল এড়ান এবং কাস্টমারকে দিন সুপারফাস্ট সার্ভিস।
      </p>
    </div>

    <div class="space-y-2.5 my-2">
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">বারকোড স্ক্যান ও ইনস্ট্যান্ট জেনেরিক সার্চ</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">অটোমেটিক থার্মাল রিসিপ্ট ও SMS ইনভয়েস</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">Cash, bKash ও Card ইনস্ট্যান্ট পেমেন্ট</span>
      </div>
    </div>

    <div class="flex items-center justify-between pt-2 border-t border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-emerald-600 flex items-center justify-center font-bold text-white en text-xs">IA</div>
        <div>
          <p class="text-xs text-slate-400 leading-none">Developed by</p>
          <p class="text-sm font-bold text-white leading-tight en">Info AidTech</p>
        </div>
      </div>
      <div class="px-4 py-2 bg-emerald-500 text-slate-950 font-bold text-xs rounded-xl shadow-lg shadow-emerald-500/20 en flex items-center gap-1.5">
        <span>Get Free Demo</span> ➔
      </div>
    </div>
  </div>

  <!-- Right UI Frame -->
  <div class="w-[620px] h-[550px] z-10 rounded-2xl bg-slate-900 border border-slate-700/60 shadow-2xl shadow-black/80 flex flex-col overflow-hidden relative">
    <div class="h-9 bg-slate-800/90 px-4 flex items-center justify-between border-b border-slate-700/60">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-rose-500"></span>
        <span class="w-3 h-3 rounded-full bg-amber-500"></span>
        <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
        <span class="ml-2 text-xs text-slate-400 en font-medium">aidlypms.infoaidtech.net/customer/pos</span>
      </div>
      <span class="text-[11px] px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-semibold en">POS Active</span>
    </div>

    <div class="bg-slate-900 px-4 py-2.5 border-b border-slate-800 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="w-6 h-6 rounded bg-emerald-600 flex items-center justify-center text-xs font-bold text-white">✚</span>
        <span class="text-sm font-bold text-white en">Aidly POS Terminal</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="px-2.5 py-1 rounded bg-teal-600 text-white text-xs font-semibold en">Retail Mode</span>
        <span class="px-2 py-1 rounded bg-slate-800 text-slate-300 text-xs en">F1: Print ON</span>
      </div>
    </div>

    <div class="p-3.5 grid grid-cols-12 gap-3 flex-1 bg-slate-950/60 overflow-hidden text-xs">
      <div class="col-span-8 flex flex-col justify-between">
        <div class="bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 flex items-center gap-2 mb-2 text-slate-400">
          <span>🔍</span>
          <span>Scan Barcode or type (Napa, Seclo, Cef-3)...</span>
        </div>

        <div class="bg-slate-900/90 border border-slate-800 rounded-lg overflow-hidden flex-1">
          <table class="w-full text-left">
            <thead class="bg-slate-800/80 text-[11px] text-slate-400 uppercase font-semibold border-b border-slate-700/50">
              <tr>
                <th class="p-2">Item / Generic</th>
                <th class="p-2 text-center">Qty</th>
                <th class="p-2 text-right">Price</th>
                <th class="p-2 text-right">Total</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 text-slate-200">
              <tr>
                <td class="p-2">
                  <p class="font-semibold text-white">Napa 500mg Tab</p>
                  <p class="text-[10px] text-slate-400">Paracetamol · Beximco</p>
                </td>
                <td class="p-2 text-center font-bold text-emerald-400">20</td>
                <td class="p-2 text-right en">৳ 1.20</td>
                <td class="p-2 text-right font-semibold en">৳ 24.00</td>
              </tr>
              <tr>
                <td class="p-2">
                  <p class="font-semibold text-white">Seclo 20mg Cap</p>
                  <p class="text-[10px] text-slate-400">Omeprazole · Square</p>
                </td>
                <td class="p-2 text-center font-bold text-emerald-400">14</td>
                <td class="p-2 text-right en">৳ 7.00</td>
                <td class="p-2 text-right font-semibold en">৳ 98.00</td>
              </tr>
              <tr>
                <td class="p-2">
                  <p class="font-semibold text-white">Cef-3 250mg Cap</p>
                  <p class="text-[10px] text-slate-400">Cefixime · Renata</p>
                </td>
                <td class="p-2 text-center font-bold text-emerald-400">10</td>
                <td class="p-2 text-right en">৳ 35.00</td>
                <td class="p-2 text-right font-semibold en">৳ 350.00</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="mt-2 flex items-center justify-between text-[11px] text-slate-400 bg-slate-900/60 px-3 py-1.5 rounded border border-slate-800">
          <span>Items: 3 · Total Pieces: 44</span>
          <span class="text-emerald-400 font-medium">✓ Stock Auto-Synced</span>
        </div>
      </div>

      <div class="col-span-4 bg-slate-900 border border-slate-800 rounded-lg p-3 flex flex-col justify-between">
        <div>
          <h4 class="text-xs font-bold text-white uppercase tracking-wider mb-2.5 pb-1 border-b border-slate-800 en">Order Summary</h4>
          <div class="space-y-1.5 text-xs">
            <div class="flex justify-between text-slate-400">
              <span>Subtotal:</span>
              <span class="text-white en font-medium">৳ 472.00</span>
            </div>
            <div class="flex justify-between text-emerald-400">
              <span>Discount (5%):</span>
              <span class="en font-medium">- ৳ 23.60</span>
            </div>
            <div class="pt-2 border-t border-slate-800 flex justify-between items-baseline">
              <span class="text-sm font-bold text-white">Net Total:</span>
              <span class="text-lg font-extrabold text-emerald-400 en">৳ 448.40</span>
            </div>
          </div>

          <div class="mt-3 p-2 bg-slate-950/70 rounded border border-slate-800 space-y-1 text-[11px]">
            <div class="flex justify-between text-slate-400">
              <span>Paid (Cash):</span>
              <span class="text-white en font-bold">৳ 500.00</span>
            </div>
            <div class="flex justify-between text-amber-400 font-semibold">
              <span>Change Due:</span>
              <span class="en">৳ 51.60</span>
            </div>
          </div>
        </div>

        <div class="mt-3 space-y-1.5">
          <button class="w-full py-2 bg-emerald-600 text-white font-bold rounded-lg text-xs en shadow-lg shadow-emerald-600/30">
            ⚡ Quick Print Bill [F2]
          </button>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
""",

    "aidly_expiry_fefo.png": """
<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200, height=630">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Hind+Siliguri:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; }
    .en { font-family: 'Plus Jakarta Sans', sans-serif; }
  </style>
</head>
<body class="w-[1200px] h-[630px] bg-gradient-to-br from-slate-950 via-slate-900 to-rose-950 text-white p-10 flex flex-row items-center justify-between overflow-hidden relative select-none">
  <div class="absolute -top-32 -left-32 w-[500px] h-[500px] bg-rose-500/15 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-[600px] h-[600px] bg-amber-500/15 rounded-full blur-3xl pointer-events-none"></div>

  <!-- Left Content -->
  <div class="w-[480px] z-10 flex flex-col justify-between h-full py-2">
    <div>
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-rose-500/10 border border-rose-500/30 text-rose-400 text-xs font-semibold en">
        <span class="w-2 h-2 rounded-full bg-rose-400 animate-pulse"></span>
        Aidly PMS · Expiry & FEFO Control
      </div>

      <h1 class="text-[33px] font-bold leading-[1.25] text-white mt-4">
        মেয়াদোত্তীর্ণ ওষুধে লোকসান? বন্ধ করুন <span class="text-rose-400 font-extrabold">অটোমেটিক FEFO</span> ট্র্যাকিংয়ে!
      </h1>
      
      <p class="text-slate-300 text-[15px] leading-relaxed mt-3">
        কোন ওষুধের মেয়াদ কবে শেষ হবে সফটওয়্যার আগেই জানাবে। মেয়াদ শেষ হওয়ার আগেই কোম্পানির কাছে রিটার্ন পাঠান।
      </p>
    </div>

    <div class="space-y-2.5 my-2">
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-rose-500/20 text-rose-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">First-Expiry-First-Out স্বয়ংক্রিয় সেলস রুল</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-rose-500/20 text-rose-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">১৫/৩০/৬০ দিনের অ্যাডভান্স এক্সপায়ারি অ্যালার্ট</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-rose-500/20 text-rose-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">কোম্পানি ওয়াইজ ১-ক্লিক রিটার্ন রিকুইজিশন</span>
      </div>
    </div>

    <div class="flex items-center justify-between pt-2 border-t border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-rose-600 flex items-center justify-center font-bold text-white en text-xs">IA</div>
        <div>
          <p class="text-xs text-slate-400 leading-none">Developed by</p>
          <p class="text-sm font-bold text-white leading-tight en">Info AidTech</p>
        </div>
      </div>
      <div class="px-4 py-2 bg-rose-500 text-white font-bold text-xs rounded-xl shadow-lg shadow-rose-500/20 en flex items-center gap-1.5">
        <span>Protect Your Profit</span> ➔
      </div>
    </div>
  </div>

  <!-- Right UI Frame -->
  <div class="w-[620px] h-[550px] z-10 rounded-2xl bg-slate-900 border border-slate-700/60 shadow-2xl shadow-black/80 flex flex-col overflow-hidden relative">
    <div class="h-9 bg-slate-800/90 px-4 flex items-center justify-between border-b border-slate-700/60">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-rose-500"></span>
        <span class="w-3 h-3 rounded-full bg-amber-500"></span>
        <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
        <span class="ml-2 text-xs text-slate-400 en font-medium">aidlypms.infoaidtech.net/products/expired</span>
      </div>
      <span class="text-[11px] px-2 py-0.5 rounded bg-rose-500/20 text-rose-400 font-semibold en">Expiry Shield Active</span>
    </div>

    <div class="p-4 flex-1 bg-slate-950/60 flex flex-col justify-between text-xs">
      <div>
        <div class="flex items-center justify-between mb-3">
          <div>
            <h3 class="text-sm font-bold text-white en">Expiring Items & Batch Records</h3>
            <p class="text-slate-400 text-[11px]">Real-time batch lifecycle & return requisition generator</p>
          </div>
          <div class="flex gap-2">
            <span class="px-2.5 py-1 bg-rose-500/20 border border-rose-500/40 text-rose-400 rounded-lg text-xs font-semibold en">4 Critical Batches</span>
          </div>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden">
          <table class="w-full text-left">
            <thead class="bg-slate-800/80 text-[11px] text-slate-400 uppercase font-semibold border-b border-slate-700/60">
              <tr>
                <th class="p-2.5">Medicine & Batch</th>
                <th class="p-2.5">Manufacturer</th>
                <th class="p-2.5 text-center">Expiry Date</th>
                <th class="p-2.5 text-center">Stock</th>
                <th class="p-2.5 text-center">Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 text-slate-200">
              <tr>
                <td class="p-2.5">
                  <p class="font-bold text-white">Cef-3 250mg Capsule</p>
                  <p class="text-[10px] text-slate-400 en">Batch: CF-2024-91</p>
                </td>
                <td class="p-2.5 text-slate-300">Renata Limited</td>
                <td class="p-2.5 text-center text-rose-400 font-bold en">30 Nov 2026</td>
                <td class="p-2.5 text-center font-bold en">120 Pcs</td>
                <td class="p-2.5 text-center">
                  <span class="px-2 py-0.5 rounded bg-rose-500/30 text-rose-300 text-[10px] font-bold en">14 Days Left</span>
                </td>
              </tr>
              <tr>
                <td class="p-2.5">
                  <p class="font-bold text-white">Azimex 500mg Tablet</p>
                  <p class="text-[10px] text-slate-400 en">Batch: AZ-8841-B</p>
                </td>
                <td class="p-2.5 text-slate-300">Beximco Pharma</td>
                <td class="p-2.5 text-center text-amber-400 font-bold en">15 Dec 2026</td>
                <td class="p-2.5 text-center font-bold en">48 Pcs</td>
                <td class="p-2.5 text-center">
                  <span class="px-2 py-0.5 rounded bg-amber-500/30 text-amber-300 text-[10px] font-bold en">29 Days Left</span>
                </td>
              </tr>
              <tr>
                <td class="p-2.5">
                  <p class="font-bold text-white">Sergel 20mg Capsule</p>
                  <p class="text-[10px] text-slate-400 en">Batch: SG-4410-C</p>
                </td>
                <td class="p-2.5 text-slate-300">Healthcare Pharma</td>
                <td class="p-2.5 text-center text-amber-400 font-bold en">28 Dec 2026</td>
                <td class="p-2.5 text-center font-bold en">60 Pcs</td>
                <td class="p-2.5 text-center">
                  <span class="px-2 py-0.5 rounded bg-amber-500/30 text-amber-300 text-[10px] font-bold en">42 Days Left</span>
                </td>
              </tr>
              <tr>
                <td class="p-2.5">
                  <p class="font-bold text-white">Amoxil 250mg Syrup</p>
                  <p class="text-[10px] text-slate-400 en">Batch: AM-9012-S</p>
                </td>
                <td class="p-2.5 text-slate-300">Square Pharma</td>
                <td class="p-2.5 text-center text-emerald-400 font-bold en">15 Jan 2027</td>
                <td class="p-2.5 text-center font-bold en">24 Bottles</td>
                <td class="p-2.5 text-center">
                  <span class="px-2 py-0.5 rounded bg-blue-500/30 text-blue-300 text-[10px] font-bold en">65 Days Left</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="mt-3 p-3 bg-slate-900 border border-slate-800 rounded-xl flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-400 flex items-center justify-center text-base">⚠️</div>
          <div>
            <p class="font-semibold text-white">Supplier Return Requisition Ready</p>
            <p class="text-slate-400 text-[11px]">Total Returnable Value: <span class="text-rose-400 font-bold en">৳ 18,740.00</span></p>
          </div>
        </div>
        <button class="px-3.5 py-1.5 bg-rose-600 text-white font-bold rounded-lg text-xs en">
          Export Return Sheet
        </button>
      </div>
    </div>
  </div>
</body>
</html>
""",

    "aidly_pharma_dashboard.png": """
<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200, height=630">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Hind+Siliguri:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; }
    .en { font-family: 'Plus Jakarta Sans', sans-serif; }
  </style>
</head>
<body class="w-[1200px] h-[630px] bg-gradient-to-br from-slate-950 via-slate-900 to-teal-950 text-white p-10 flex flex-row items-center justify-between overflow-hidden relative select-none">
  <div class="absolute -top-32 -left-32 w-[500px] h-[500px] bg-teal-500/15 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-[600px] h-[600px] bg-blue-500/15 rounded-full blur-3xl pointer-events-none"></div>

  <!-- Left Content -->
  <div class="w-[480px] z-10 flex flex-col justify-between h-full py-2">
    <div>
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-teal-500/10 border border-teal-500/30 text-teal-400 text-xs font-semibold en">
        <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
        Aidly PMS · Real-time Analytics
      </div>

      <h1 class="text-[34px] font-bold leading-[1.25] text-white mt-4">
        ফার্মেসি ব্যবসা চালান <span class="text-teal-400 font-extrabold">১০০% স্বচ্ছতায়</span> ও সম্পূর্ণ নিয়ন্ত্রণে!
      </h1>
      
      <p class="text-slate-300 text-[15px] leading-relaxed mt-3">
        দৈনিক বিক্রি, নিট লাভ, ক্যাশ ড্রয়ার এবং ইনভেন্টরি স্টক — সব হিসাব মোবাইল বা ল্যাপটপে এক স্ক্রিনে লাইভ দেখুন।
      </p>
    </div>

    <div class="space-y-2.5 my-2">
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-teal-500/20 text-teal-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">লাইভ প্রফিট মার্জিন ও দৈনিক সেলস রিপোর্ট</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-teal-500/20 text-teal-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">ক্যাশ কাউন্টার ট্যালি ও শিফট হ্যান্ডওভার</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-teal-500/20 text-teal-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">লো স্টক অ্যালার্ট ও সাপ্লায়ার অটো রিকুইজিশন</span>
      </div>
    </div>

    <div class="flex items-center justify-between pt-2 border-t border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-teal-600 flex items-center justify-center font-bold text-white en text-xs">IA</div>
        <div>
          <p class="text-xs text-slate-400 leading-none">Developed by</p>
          <p class="text-sm font-bold text-white leading-tight en">Info AidTech</p>
        </div>
      </div>
      <div class="px-4 py-2 bg-teal-500 text-slate-950 font-bold text-xs rounded-xl shadow-lg shadow-teal-500/20 en flex items-center gap-1.5">
        <span>Explore Live Dashboard</span> ➔
      </div>
    </div>
  </div>

  <!-- Right UI Frame -->
  <div class="w-[620px] h-[550px] z-10 rounded-2xl bg-slate-900 border border-slate-700/60 shadow-2xl shadow-black/80 flex flex-col overflow-hidden relative">
    <div class="h-9 bg-slate-800/90 px-4 flex items-center justify-between border-b border-slate-700/60">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-rose-500"></span>
        <span class="w-3 h-3 rounded-full bg-amber-500"></span>
        <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
        <span class="ml-2 text-xs text-slate-400 en font-medium">aidlypms.infoaidtech.net/dashboard</span>
      </div>
      <span class="text-[11px] px-2 py-0.5 rounded bg-teal-500/20 text-teal-400 font-semibold en">Live Pharmacy v2.4</span>
    </div>

    <div class="p-4 flex-1 bg-slate-950/60 flex flex-col justify-between text-xs">
      <!-- 4 Stat Cards -->
      <div class="grid grid-cols-4 gap-2.5">
        <div class="bg-slate-900 border border-slate-800 p-2.5 rounded-xl">
          <p class="text-slate-400 text-[10px] uppercase font-semibold">Today's Sales</p>
          <p class="text-base font-extrabold text-white mt-1 en">৳ 84,250</p>
          <span class="text-[10px] text-emerald-400 font-medium">+14.2% vs yesterday</span>
        </div>
        <div class="bg-slate-900 border border-slate-800 p-2.5 rounded-xl">
          <p class="text-slate-400 text-[10px] uppercase font-semibold">Net Profit</p>
          <p class="text-base font-extrabold text-emerald-400 mt-1 en">৳ 18,420</p>
          <span class="text-[10px] text-slate-400 font-medium">Margin: 21.8%</span>
        </div>
        <div class="bg-slate-900 border border-slate-800 p-2.5 rounded-xl">
          <p class="text-slate-400 text-[10px] uppercase font-semibold">Invoices</p>
          <p class="text-base font-extrabold text-white mt-1 en">164</p>
          <span class="text-[10px] text-teal-400 font-medium">Avg: ৳ 513/bill</span>
        </div>
        <div class="bg-slate-900 border border-slate-800 p-2.5 rounded-xl">
          <p class="text-slate-400 text-[10px] uppercase font-semibold">Low Stock Alert</p>
          <p class="text-base font-extrabold text-rose-400 mt-1 en">7 Items</p>
          <span class="text-[10px] text-rose-300 font-medium">Reorder required</span>
        </div>
      </div>

      <!-- Center Mini Chart & Top Selling -->
      <div class="grid grid-cols-2 gap-3 flex-1 mt-3">
        <!-- Sales Trend -->
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 flex flex-col justify-between">
          <div class="flex justify-between items-center">
            <h4 class="font-bold text-white text-xs en">Weekly Revenue Trend</h4>
            <span class="text-[10px] text-teal-400 font-semibold en">Last 7 Days</span>
          </div>
          <!-- Bar Visualization -->
          <div class="flex items-end justify-between h-28 pt-4 px-2 gap-2">
            <div class="flex-1 flex flex-col items-center gap-1">
              <div class="w-full bg-teal-600/40 rounded-t h-[60%]"></div>
              <span class="text-[9px] text-slate-400 en">Sat</span>
            </div>
            <div class="flex-1 flex flex-col items-center gap-1">
              <div class="w-full bg-teal-600/50 rounded-t h-[75%]"></div>
              <span class="text-[9px] text-slate-400 en">Sun</span>
            </div>
            <div class="flex-1 flex flex-col items-center gap-1">
              <div class="w-full bg-teal-600/60 rounded-t h-[65%]"></div>
              <span class="text-[9px] text-slate-400 en">Mon</span>
            </div>
            <div class="flex-1 flex flex-col items-center gap-1">
              <div class="w-full bg-teal-600/70 rounded-t h-[85%]"></div>
              <span class="text-[9px] text-slate-400 en">Tue</span>
            </div>
            <div class="flex-1 flex flex-col items-center gap-1">
              <div class="w-full bg-teal-500 rounded-t h-[95%] shadow-lg shadow-teal-500/30"></div>
              <span class="text-[9px] text-teal-300 font-bold en">Today</span>
            </div>
          </div>
          <p class="text-[10px] text-slate-400 text-center">Peak Hour: 6:00 PM – 9:30 PM</p>
        </div>

        <!-- Top Selling Medicines -->
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3 flex flex-col justify-between">
          <h4 class="font-bold text-white text-xs en mb-1">Top Fast Moving Items</h4>
          <div class="space-y-1.5 flex-1">
            <div class="flex justify-between items-center text-[11px] p-1.5 bg-slate-950/60 rounded border border-slate-800">
              <div>
                <p class="font-semibold text-white">Napa 500mg</p>
                <p class="text-[9px] text-slate-400">Beximco · 1,240 sold</p>
              </div>
              <span class="text-emerald-400 font-bold en">৳ 12,400</span>
            </div>
            <div class="flex justify-between items-center text-[11px] p-1.5 bg-slate-950/60 rounded border border-slate-800">
              <div>
                <p class="font-semibold text-white">Seclo 20mg</p>
                <p class="text-[9px] text-slate-400">Square · 860 sold</p>
              </div>
              <span class="text-emerald-400 font-bold en">৳ 15,480</span>
            </div>
            <div class="flex justify-between items-center text-[11px] p-1.5 bg-slate-950/60 rounded border border-slate-800">
              <div>
                <p class="font-semibold text-white">Cef-3 250mg</p>
                <p class="text-[9px] text-slate-400">Renata · 520 sold</p>
              </div>
              <span class="text-emerald-400 font-bold en">৳ 14,040</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
""",

    "aidly_due_sms.png": """
<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200, height=630">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Hind+Siliguri:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; }
    .en { font-family: 'Plus Jakarta Sans', sans-serif; }
  </style>
</head>
<body class="w-[1200px] h-[630px] bg-gradient-to-br from-slate-950 via-slate-900 to-indigo-950 text-white p-10 flex flex-row items-center justify-between overflow-hidden relative select-none">
  <div class="absolute -top-32 -left-32 w-[500px] h-[500px] bg-indigo-500/15 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-[600px] h-[600px] bg-sky-500/15 rounded-full blur-3xl pointer-events-none"></div>

  <!-- Left Content -->
  <div class="w-[480px] z-10 flex flex-col justify-between h-full py-2">
    <div>
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-semibold en">
        <span class="w-2 h-2 rounded-full bg-indigo-400 animate-pulse"></span>
        Aidly PMS · Due Ledger & SMS
      </div>

      <h1 class="text-[34px] font-bold leading-[1.25] text-white mt-4">
        বাকি খাতার ঝামেলা শেষ! <span class="text-indigo-400 font-extrabold">অটোমেটিক SMS</span> অ্যালার্টে দ্রুত টাকা তুলুন!
      </h1>
      
      <p class="text-slate-300 text-[15px] leading-relaxed mt-3">
        কোন কাস্টমারের কত টাকা বাকি তা মুখস্থ রাখতে হবে না। এক ক্লিকে কাস্টমারের মোবাইলে প্রফেশনাল SMS রিমাইন্ডার পাঠান।
      </p>
    </div>

    <div class="space-y-2.5 my-2">
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">কাস্টমার ওয়াইজ ডিজিটাল বাকি লেজার ও হিস্ট্রি</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">১-ক্লিকে বাংলা/ইংরেজি কাস্টম SMS রিমাইন্ডার</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">আংশিক পেমেন্ট কালেকশন ও ইনস্ট্যান্ট মানি রিসিপ্ট</span>
      </div>
    </div>

    <div class="flex items-center justify-between pt-2 border-t border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-white en text-xs">IA</div>
        <div>
          <p class="text-xs text-slate-400 leading-none">Developed by</p>
          <p class="text-sm font-bold text-white leading-tight en">Info AidTech</p>
        </div>
      </div>
      <div class="px-4 py-2 bg-indigo-500 text-white font-bold text-xs rounded-xl shadow-lg shadow-indigo-500/20 en flex items-center gap-1.5">
        <span>Recover Due Faster</span> ➔
      </div>
    </div>
  </div>

  <!-- Right UI Frame -->
  <div class="w-[620px] h-[550px] z-10 rounded-2xl bg-slate-900 border border-slate-700/60 shadow-2xl shadow-black/80 flex flex-col overflow-hidden relative">
    <div class="h-9 bg-slate-800/90 px-4 flex items-center justify-between border-b border-slate-700/60">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-rose-500"></span>
        <span class="w-3 h-3 rounded-full bg-amber-500"></span>
        <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
        <span class="ml-2 text-xs text-slate-400 en font-medium">aidlypms.infoaidtech.net/due</span>
      </div>
      <span class="text-[11px] px-2 py-0.5 rounded bg-indigo-500/20 text-indigo-400 font-semibold en">Due Recovery Module</span>
    </div>

    <div class="p-4 flex-1 bg-slate-950/60 flex flex-col justify-between text-xs">
      <div>
        <div class="flex items-center justify-between mb-3">
          <div>
            <h3 class="text-sm font-bold text-white en">Customer Due Collection & Ledger</h3>
            <p class="text-slate-400 text-[11px]">Track balances, send reminders & collect partial payments</p>
          </div>
          <span class="px-2.5 py-1 bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 rounded-lg text-xs font-semibold en">Total Due: ৳ 42,650</span>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden">
          <table class="w-full text-left">
            <thead class="bg-slate-800/80 text-[11px] text-slate-400 uppercase font-semibold border-b border-slate-700/60">
              <tr>
                <th class="p-2.5">Customer Name</th>
                <th class="p-2.5">Mobile Number</th>
                <th class="p-2.5 text-right">Total Due</th>
                <th class="p-2.5 text-center">Last Bill</th>
                <th class="p-2.5 text-center">Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-800 text-slate-200">
              <tr>
                <td class="p-2.5">
                  <p class="font-bold text-white">Md. Rafiqul Islam</p>
                  <p class="text-[10px] text-slate-400">Regular Customer · Dhanmondi</p>
                </td>
                <td class="p-2.5 en text-slate-300">01712-XXXXXX</td>
                <td class="p-2.5 text-right font-extrabold text-rose-400 en">৳ 3,450.00</td>
                <td class="p-2.5 text-center text-slate-400 en">02 Nov 2026</td>
                <td class="p-2.5 text-center">
                  <span class="px-2.5 py-1 rounded bg-indigo-600 text-white text-[10px] font-bold en">📲 Send SMS</span>
                </td>
              </tr>
              <tr>
                <td class="p-2.5">
                  <p class="font-bold text-white">Anowar Hossain</p>
                  <p class="text-[10px] text-slate-400">Account #C-1092</p>
                </td>
                <td class="p-2.5 en text-slate-300">01911-XXXXXX</td>
                <td class="p-2.5 text-right font-extrabold text-rose-400 en">৳ 1,820.00</td>
                <td class="p-2.5 text-center text-slate-400 en">05 Nov 2026</td>
                <td class="p-2.5 text-center">
                  <span class="px-2.5 py-1 rounded bg-indigo-600 text-white text-[10px] font-bold en">📲 Send SMS</span>
                </td>
              </tr>
              <tr>
                <td class="p-2.5">
                  <p class="font-bold text-white">Dr. Farhana Yasmin</p>
                  <p class="text-[10px] text-slate-400">Clinic Account</p>
                </td>
                <td class="p-2.5 en text-slate-300">01819-XXXXXX</td>
                <td class="p-2.5 text-right font-extrabold text-rose-400 en">৳ 6,900.00</td>
                <td class="p-2.5 text-center text-slate-400 en">09 Nov 2026</td>
                <td class="p-2.5 text-center">
                  <span class="px-2.5 py-1 rounded bg-indigo-600 text-white text-[10px] font-bold en">📲 Send SMS</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- SMS Preview Card -->
      <div class="mt-3 p-3 bg-slate-900 border border-slate-800 rounded-xl flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-indigo-500/20 text-indigo-400 flex items-center justify-center text-base">💬</div>
          <div>
            <p class="font-semibold text-white">SMS Notification Preview</p>
            <p class="text-slate-400 text-[11px] font-mono">"প্রিয় কাস্টমার, আপনার ফার্মেসি বকেয়া ৩,৪৫০ টাকা। পরিশোধের জন্য ধন্যবাদ।"</p>
          </div>
        </div>
        <span class="px-2.5 py-1 bg-emerald-500/20 text-emerald-400 text-[11px] font-bold rounded">Instant Delivery</span>
      </div>
    </div>
  </div>
</body>
</html>
""",

    "agency_meta_ads.png": """
<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200, height=630">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Hind+Siliguri:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; }
    .en { font-family: 'Plus Jakarta Sans', sans-serif; }
  </style>
</head>
<body class="w-[1200px] h-[630px] bg-gradient-to-br from-slate-950 via-slate-900 to-blue-950 text-white p-10 flex flex-row items-center justify-between overflow-hidden relative select-none">
  <div class="absolute -top-32 -left-32 w-[500px] h-[500px] bg-blue-500/15 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-[600px] h-[600px] bg-cyan-500/15 rounded-full blur-3xl pointer-events-none"></div>

  <!-- Left Content -->
  <div class="w-[480px] z-10 flex flex-col justify-between h-full py-2">
    <div>
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-500/10 border border-blue-500/30 text-blue-400 text-xs font-semibold en">
        <span class="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>
        Info AidTech · Performance Marketing
      </div>

      <h1 class="text-[34px] font-bold leading-[1.25] text-white mt-4">
        বিজ্ঞাপনে টাকা খরচ হচ্ছে, কিন্তু <span class="text-blue-400 font-extrabold">আশানুরূপ সেলস</span> আসছে না?
      </h1>
      
      <p class="text-slate-300 text-[15px] leading-relaxed mt-3">
        সাধারণ বুস্টিং নয়! হাই-কনভার্টিং সেলস ফানেল, ডাটা-ড্রিভেন অডিয়েন্স টার্গেটিং ও রিটার্গেটিংয়ে নিয়ে আসুন ৫x থেকে ৮x পর্যন্ত ROAS।
      </p>
    </div>

    <div class="space-y-2.5 my-2">
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-blue-500/20 text-blue-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">Meta (Facebook & IG) অ্যাডস ও প্রিসাইজ পিক্সেল ট্র্যাকিং</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-blue-500/20 text-blue-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">Google Search Ads ও YouTube ভিডিও ক্যাম্পেইন</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-blue-500/20 text-blue-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">A/B টেস্টেড ক্রিয়েটিভ ডিজাইন ও হাই-কনভার্টিং কপিরাইটিং</span>
      </div>
    </div>

    <div class="flex items-center justify-between pt-2 border-t border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-blue-600 flex items-center justify-center font-bold text-white en text-xs">IA</div>
        <div>
          <p class="text-xs text-slate-400 leading-none">Your Growth Partner</p>
          <p class="text-sm font-bold text-white leading-tight en">Info AidTech</p>
        </div>
      </div>
      <div class="px-4 py-2 bg-blue-500 text-white font-bold text-xs rounded-xl shadow-lg shadow-blue-500/20 en flex items-center gap-1.5">
        <span>Get Free Marketing Audit</span> ➔
      </div>
    </div>
  </div>

  <!-- Right UI Frame -->
  <div class="w-[620px] h-[550px] z-10 rounded-2xl bg-slate-900 border border-slate-700/60 shadow-2xl shadow-black/80 flex flex-col overflow-hidden relative">
    <div class="h-9 bg-slate-800/90 px-4 flex items-center justify-between border-b border-slate-700/60">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-rose-500"></span>
        <span class="w-3 h-3 rounded-full bg-amber-500"></span>
        <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
        <span class="ml-2 text-xs text-slate-400 en font-medium">business.facebook.com/adsmanager</span>
      </div>
      <span class="text-[11px] px-2 py-0.5 rounded bg-blue-500/20 text-blue-400 font-semibold en">Campaigns Active</span>
    </div>

    <div class="p-4 flex-1 bg-slate-950/60 flex flex-col justify-between text-xs">
      <div class="grid grid-cols-3 gap-3 mb-3">
        <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl">
          <p class="text-slate-400 text-[10px] uppercase font-semibold">Average ROAS</p>
          <p class="text-xl font-extrabold text-emerald-400 mt-1 en">6.84x</p>
          <span class="text-[10px] text-emerald-300">Revenue: $14,280</span>
        </div>
        <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl">
          <p class="text-slate-400 text-[10px] uppercase font-semibold">Cost Per Purchase</p>
          <p class="text-xl font-extrabold text-white mt-1 en">$2.14</p>
          <span class="text-[10px] text-blue-400">-34% lower CPA</span>
        </div>
        <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl">
          <p class="text-slate-400 text-[10px] uppercase font-semibold">Total Purchases</p>
          <p class="text-xl font-extrabold text-white mt-1 en">1,894</p>
          <span class="text-[10px] text-slate-400">High-intent conversion</span>
        </div>
      </div>

      <div class="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden flex-1 flex flex-col justify-between">
        <div class="p-3 border-b border-slate-800 flex justify-between items-center">
          <h4 class="font-bold text-white text-xs en">Active Client Campaigns</h4>
          <span class="px-2 py-0.5 bg-emerald-500/20 text-emerald-400 rounded text-[10px] font-semibold en">3 Active Scaling</span>
        </div>
        <table class="w-full text-left">
          <thead class="bg-slate-800/60 text-[10px] text-slate-400 uppercase font-semibold border-b border-slate-800">
            <tr>
              <th class="p-2.5">Campaign Name</th>
              <th class="p-2.5 text-center">Status</th>
              <th class="p-2.5 text-right">Spend</th>
              <th class="p-2.5 text-right">ROAS</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800 text-slate-200">
            <tr>
              <td class="p-2.5 font-semibold text-white">E-Commerce Retargeting [Catalog]</td>
              <td class="p-2.5 text-center"><span class="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 text-[9px] font-bold">ACTIVE</span></td>
              <td class="p-2.5 text-right en">$840</td>
              <td class="p-2.5 text-right font-extrabold text-emerald-400 en">7.8x</td>
            </tr>
            <tr>
              <td class="p-2.5 font-semibold text-white">B2B SaaS Lead Generation [BD]</td>
              <td class="p-2.5 text-center"><span class="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 text-[9px] font-bold">ACTIVE</span></td>
              <td class="p-2.5 text-right en">$520</td>
              <td class="p-2.5 text-right font-extrabold text-emerald-400 en">5.4x</td>
            </tr>
            <tr>
              <td class="p-2.5 font-semibold text-white">Brand Expansion & Awareness</td>
              <td class="p-2.5 text-center"><span class="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 text-[9px] font-bold">ACTIVE</span></td>
              <td class="p-2.5 text-right en">$350</td>
              <td class="p-2.5 text-right font-extrabold text-emerald-400 en">6.1x</td>
            </tr>
          </tbody>
        </table>
        <div class="p-2 bg-slate-950/80 text-[11px] text-slate-400 text-center border-t border-slate-800">
          Scale your business with Info AidTech's proven performance marketing blueprint.
        </div>
      </div>
    </div>
  </div>
</body>
</html>
""",

    "agency_custom_software.png": """
<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1200, height=630">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Hind+Siliguri:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Hind Siliguri', 'Plus Jakarta Sans', sans-serif; }
    .en { font-family: 'Plus Jakarta Sans', sans-serif; }
  </style>
</head>
<body class="w-[1200px] h-[630px] bg-gradient-to-br from-slate-950 via-slate-900 to-purple-950 text-white p-10 flex flex-row items-center justify-between overflow-hidden relative select-none">
  <div class="absolute -top-32 -left-32 w-[500px] h-[500px] bg-purple-500/15 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-[600px] h-[600px] bg-indigo-500/15 rounded-full blur-3xl pointer-events-none"></div>

  <!-- Left Content -->
  <div class="w-[480px] z-10 flex flex-col justify-between h-full py-2">
    <div>
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-purple-500/10 border border-purple-500/30 text-purple-400 text-xs font-semibold en">
        <span class="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
        Info AidTech · Custom Software & Cloud
      </div>

      <h1 class="text-[34px] font-bold leading-[1.25] text-white mt-4">
        আপনার বিজনেসের জন্য দরকার <span class="text-purple-400 font-extrabold">কাস্টম সফটওয়্যার</span> বা ERP?
      </h1>
      
      <p class="text-slate-300 text-[15px] leading-relaxed mt-3">
        রেডিমেড সফটওয়্যারে আপনার ব্যবসার সব প্রয়োজন পূরণ হয় না? আধুনিক ক্লাউড আর্কিটেকচার ও এআই-পাওয়ার্ড কাস্টম সল্যুশন নিন।
      </p>
    </div>

    <div class="space-y-2.5 my-2">
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-purple-500/20 text-purple-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">কাস্টম ওয়েব অ্যাপ্লিকেশন ও বিজনেস অটোমেশন পোর্টাল</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-purple-500/20 text-purple-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">ক্লাউড বেসড ERP, ইনভেন্টরি ও POS সিস্টেম</span>
      </div>
      <div class="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-3.5 py-2">
        <div class="w-6 h-6 rounded-lg bg-purple-500/20 text-purple-400 flex items-center justify-center font-bold text-xs">✓</div>
        <span class="text-sm font-medium text-slate-200">হাই-সিকিউরিটি, স্কেলেবল ডাটাবেস ও 24/7 টেক সাপোর্ট</span>
      </div>
    </div>

    <div class="flex items-center justify-between pt-2 border-t border-white/10">
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-lg bg-purple-600 flex items-center justify-center font-bold text-white en text-xs">IA</div>
        <div>
          <p class="text-xs text-slate-400 leading-none">Engineering Excellence</p>
          <p class="text-sm font-bold text-white leading-tight en">Info AidTech</p>
        </div>
      </div>
      <div class="px-4 py-2 bg-purple-500 text-white font-bold text-xs rounded-xl shadow-lg shadow-purple-500/20 en flex items-center gap-1.5">
        <span>Request Consultation</span> ➔
      </div>
    </div>
  </div>

  <!-- Right UI Frame -->
  <div class="w-[620px] h-[550px] z-10 rounded-2xl bg-slate-900 border border-slate-700/60 shadow-2xl shadow-black/80 flex flex-col overflow-hidden relative">
    <div class="h-9 bg-slate-800/90 px-4 flex items-center justify-between border-b border-slate-700/60">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-rose-500"></span>
        <span class="w-3 h-3 rounded-full bg-amber-500"></span>
        <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
        <span class="ml-2 text-xs text-slate-400 en font-medium">infoaidtech.net/services/custom-software</span>
      </div>
      <span class="text-[11px] px-2 py-0.5 rounded bg-purple-500/20 text-purple-400 font-semibold en">Enterprise Grade</span>
    </div>

    <div class="p-4 flex-1 bg-slate-950/60 flex flex-col justify-between text-xs">
      <div class="grid grid-cols-2 gap-3 mb-3">
        <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl flex items-center gap-3">
          <div class="w-10 h-10 rounded-lg bg-purple-500/20 text-purple-400 flex items-center justify-center text-lg">⚡</div>
          <div>
            <h4 class="font-bold text-white text-xs">Fast & Responsive UI</h4>
            <p class="text-[11px] text-slate-400">Angular 21, React 19, Next.js</p>
          </div>
        </div>
        <div class="bg-slate-900 border border-slate-800 p-3 rounded-xl flex items-center gap-3">
          <div class="w-10 h-10 rounded-lg bg-indigo-500/20 text-indigo-400 flex items-center justify-center text-lg">🔒</div>
          <div>
            <h4 class="font-bold text-white text-xs">High Security & Cloud</h4>
            <p class="text-[11px] text-slate-400">Multi-tenant, PostgreSQL, Docker</p>
          </div>
        </div>
      </div>

      <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 flex-1 flex flex-col justify-between">
        <div>
          <h4 class="font-bold text-white text-xs en mb-2">Our Software Architecture Stack</h4>
          <div class="grid grid-cols-3 gap-2 text-center text-[11px]">
            <div class="bg-slate-950/80 p-2 rounded border border-slate-800">
              <p class="font-bold text-emerald-400">SaaS Products</p>
              <p class="text-[10px] text-slate-400 mt-0.5">Aidly PMS, ERP, CRM</p>
            </div>
            <div class="bg-slate-950/80 p-2 rounded border border-slate-800">
              <p class="font-bold text-sky-400">E-Commerce</p>
              <p class="text-[10px] text-slate-400 mt-0.5">Multi-vendor & Gateways</p>
            </div>
            <div class="bg-slate-950/80 p-2 rounded border border-slate-800">
              <p class="font-bold text-purple-400">APIs & Cloud</p>
              <p class="text-[10px] text-slate-400 mt-0.5">FastAPI, Node, Microservices</p>
            </div>
          </div>
        </div>

        <div class="mt-3 p-2.5 bg-purple-500/10 border border-purple-500/30 rounded-lg flex items-center justify-between">
          <p class="text-purple-300 text-[11px] font-medium">Have a software idea? Get a tailored architecture plan today.</p>
          <span class="text-xs font-bold text-purple-400 en">infoaidtech.net ➔</span>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""
}

def generate_banners():
    chrome_bin = "/usr/bin/google-chrome"
    for filename, html_content in TEMPLATES.items():
        out_path = os.path.join(BANNERS_DIR, filename)
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
            tmp.write(html_content)
            tmp_path = tmp.name

        try:
            cmd = [
                chrome_bin,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--window-size=1200,630",
                f"--screenshot={out_path}",
                f"file://{tmp_path}",
            ]
            print(f"Generating banner: {filename}...")
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"  -> Generated {out_path} ({os.path.getsize(out_path)} bytes)")
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

if __name__ == "__main__":
    generate_banners()
