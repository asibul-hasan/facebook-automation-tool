#!/usr/bin/env python3
"""
Populates posts.json with the 7-Day Content Schedule Matrix (14 Posts).
Preserves existing published posts for auditing history.
"""
import json
import os

POSTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts.json")

NEW_POSTS = [
    # =========================================================================
    # DAY 1 (Cycle A)
    # =========================================================================
    {
        "id": "day1_slot1_agency_roi_funnel",
        "day": "Day 1",
        "cycle": "Cycle A",
        "slot": "Post 1 (12:00 PM)",
        "category": "Digital Marketing",
        "topic": "ROI & Funnel Education",
        "scheduled_time": "12:00 PM BST",
        "image_url": "banners/day1_agency_roi_funnel.png",
        "message": (
            "📉 **বিজ্ঞাপনে টাকা ঢালছেন, কিন্তু কাঙ্ক্ষিত সেলস বা প্রফিট কোথায়?** 💸\n\n"
            "বাংলাদেশের বেশিরভাগ অনলাইন বিজনেস শুধু ফেসবুকের নীল 'Boost Post' বাটনে ক্লিক করে অ্যাড চালায়। "
            "ফলাফল? প্রচুর লাইক-কমেন্ট আসে, কিন্তু পকেটে কোনো সেলস ঢোকে না! **Stop Blind Boosting!**\n\n"
            "স্মার্ট গ্লোবাল ব্র্যান্ডগুলো অ্যাড চালায় **৩-ধাপের ফুল-ফানেল সিস্টেমে (Full-Funnel Marketing)**:\n\n"
            "🎯 **১. Top of Funnel (TOFU) — Brand Awareness:**\n"
            "কাস্টমারকে সরাসরি কিনতে না বলে তাদের সমস্যার সমাধান নিয়ে হাই-হুমিং ভিডিও ও ইনফরমেটিভ কনটেন্ট দিন।\n\n"
            "⚡ **২. Middle of Funnel (MOFU) — Consideration & Trust:**\n"
            "যারা ভিডিওটি দেখেছে বা পেজে এনগেজ হয়েছে, তাদের রিয়েল কাস্টমার রিভিউ ও সোশ্যাল প্রুফ দেখিয়ে ট্রাস্ট তৈরি করুন।\n\n"
            "💰 **৩. Bottom of Funnel (BOFU) — Conversion & Retargeting:**\n"
            "আগ্রহী ক্রেতাদের জন্য লিমিটেড টাইম ডিসকাউন্ট ও ক্লিয়ার কল-টু-অ্যাকশন দিয়ে সেলস ক্লোজ করুন।\n\n"
            "📈 **রেজাল্ট?** আমাদের ক্লায়েন্টদের ক্যাম্পেইনে এই ফানেল স্ট্র্যাটেজি নিশ্চিত করেছে **5X থেকে 8X পর্যন্ত ROAS (Return On Ad Spend)**!\n\n"
            "🚀 আপনার বিজনেসের জন্য কি সঠিক সেলস ফানেল তৈরি করতে চান?\n"
            "📲 **ফ্রি সেলস ফানেল অডিটের জন্য এখনই ইনবক্স করুন অথবা ভিজিট করুন:** https://infoaidtech.net\n\n"
            "#DigitalMarketingBD #SalesFunnel #PerformanceMarketing #ROAS #GrowthStrategy #FacebookAdsBD #AgencyMarketing #InfoAidTech"
        ),
        "published": False,
    },
    {
        "id": "day1_slot2_aidly_pain_point",
        "day": "Day 1",
        "cycle": "Cycle A",
        "slot": "Post 2 (8:30 PM)",
        "category": "AidlyPMS SMM Post",
        "topic": "Pain-Point Agitation",
        "scheduled_time": "8:30 PM BST",
        "image_url": "banners/day1_aidly_pain_point.png",
        "message": (
            "🚨 **দিনশেষে ক্যাশ ড্রয়ারের হিসাব মিলছে না? বাকির খাতায় টাকা আটকে আপনার ঘুম হারাম?** ⏳\n\n"
            "ফার্মেসি ব্যবসা দেখতে সহজ মনে হলেও ৩টি গোপন ভুলের কারণে প্রতি মাসে হাজার হাজার টাকা নিঃশব্দে গলে যায়:\n\n"
            "❌ **১. সেলফে ডেট ওভার হওয়া ওষুধ:** কোন ড্রাগের মেয়াদ কবে শেষ হচ্ছে তা না জানার কারণে প্রতি মাসে বড় অঙ্কের পুঁজি নষ্ট হয়।\n"
            "❌ **২. ছেঁড়াখোঁড়া কাগজের বাকি খাতা:** কাস্টমার হয়তো বাকি নিয়ে ভুলে গেছে, কিন্তু ডায়রির পাতা হারিয়ে যাওয়ায় আপনার আর টাকা তোলা হয় না।\n"
            "❌ **৩. কাউন্টারে লম্বা লাইন ও ভুল মেমো:** ভিড়ের সময় ম্যানুয়ালি ড্রাগ খুঁজতে গিয়ে কাস্টমার বিরক্ত হয়ে পাশের দোকানে চলে যায়।\n\n"
            "🛑 **এই সব ঝামেলার স্থায়ী সমাধান এনেছে Aidly PMS — Smart Cloud Pharmacy ERP!**\n\n"
            "⚡ **৩ সেকেন্ডে বারকোড POS বিলিং:** কাউন্টারের ভিড় সামলান সুপারফাস্ট গতিতে।\n"
            "🛡️ **অটোমেটিক FEFO এক্সপায়ারি গার্ড:** মেয়াদ শেষ হওয়ার আগেই কোম্পানি রিটার্ন রিকুইজিশন রেডি।\n"
            "📲 **ডিজিটাল বাকি খাতা ও ১-ক্লিক SMS:** কাস্টমার ফোনে প্রফেশনাল SMS তাগাদায় দ্রুত বকেয়া কালেকশন।\n"
            "📊 **লাইভ প্রফিট ড্যাশবোর্ড:** কম্পিউটার বা মোবাইলে দেখুন আজকের নিট বিক্রি ও লাভ।\n\n"
            "👉 আপনার ফার্মেসিকে আজই করুন ১০০% লাভজনক ও আধুনিক।\n"
            "🎁 **ফ্রি লাইভ ডেমো দেখতে এখনই ইনবক্স করুন অথবা ভিজিট করুন:** https://infoaidtech.net\n\n"
            "#AidlyPMS #PharmacyManagement #PharmacySoftware #PharmacyBusiness #BanglaPharma #HealthTechBD #SmartPOS #InfoAidTech"
        ),
        "published": False,
    },

    # =========================================================================
    # DAY 2 (Cycle B)
    # =========================================================================
    {
        "id": "day2_slot1_agency_algorithm",
        "day": "Day 2",
        "cycle": "Cycle B",
        "slot": "Post 1 (12:00 PM)",
        "category": "Social Media Marketing",
        "topic": "Algorithm & Engagement",
        "scheduled_time": "12:00 PM BST",
        "image_url": "banners/day2_agency_algorithm.png",
        "message": (
            "📉 **পেইজের রিচ কি হঠাৎ করে তলানিতে নেমে গেছে? বিজ্ঞাপন ছাড়া লাইক-কমেন্ট প্রায় শূন্য?** 🧐\n\n"
            "২০২৬ সালে এসে মেটা অ্যালগরিদম পুরো বদলে গেছে। মেটা এখন সাধারণ পোস্টকে রিচ দেয় না, বরং নির্দিষ্ট ৩টি মেট্রিক দেখে কনটেন্ট পুশ করে:\n\n"
            "⏱️ **১. Dwell Time (থেমে থাকার সময়):** ইউজার আপনার ফটো বা ইনফোগ্রাফিকে কত সেকেন্ড চোখ আটকে রাখল। ছবি যত ডিটেইলড হবে, রিচ তত বাড়বে।\n"
            "🔄 **২. Private Shares & Saves (শেয়ার ও সেভ):** ইউজার পোস্টটি সেভ করল কিনা বা ফ্রেন্ডকে ইনবক্সে পাঠাল কিনা। এটি অ্যালগরিদমের জন্য #1 ট্রাস্ট সিগন্যাল!\n"
            "💬 **৩. Meaningful Comments:** শুধু 'Price please' নয়, বাস্তব আলোচনা বা মতামত কমেন্টে থাকলে পোস্ট অর্গানিকালি ভাইরাল হয়।\n\n"
            "💡 **প্রো টিপ:** শুধুমাত্র 'আমাদের কাছে পণ্য আছে' টাইপ বোরিং পোস্ট বন্ধ করুন। কাস্টমারদের ইনফরমেটিভ ভ্যালু ও প্রবলেম সলভিং গাইড উপহার দিন।\n\n"
            "🚀 আপনার সোশ্যাল মিডিয়া পেজের অর্গানিক রিচ ও সেলস ৩ গুণ বাড়াতে চান?\n"
            "💬 **আমাদের সোশ্যাল গ্রোথ টিমের সাথে আজই ইনবক্সে আলোচনা করুন:** https://infoaidtech.net\n\n"
            "#MetaAlgorithm #SocialMediaMarketing #FacebookGrowth #ContentEngagement #OrganicReach #SMMStrategy #InfoAidTech"
        ),
        "published": False,
    },
    {
        "id": "day2_slot2_aidly_walkthrough_video",
        "day": "Day 2",
        "cycle": "Cycle B",
        "slot": "Post 2 (8:30 PM)",
        "category": "AidlyPMS Bengali Video",
        "topic": "Product Walkthrough",
        "scheduled_time": "8:30 PM BST",
        "image_url": "aidly_bangla_promo.mp4",
        "message": (
            "🎬 **সম্পূর্ণ ফার্মেসি ব্যবসা এখন হাতের মুঠোয়! দেখুন Aidly PMS-এর ফুল ড্যাশবোর্ড ও সুপারফাস্ট পিওএস ভিডিও।** 📹\n\n"
            "দিনশেষে বিক্রি কত হলো? কোন ওষুধের মেয়াদ কবে শেষ হবে? আর বাকির খাতায় কার কাছে কত টাকা পাওনা?\n"
            "সবকিছু এক সফটওয়্যারে কীভাবে মাত্র ৩ সেকেন্ডে সমাধান হয় — দেখুন এই লাইভ ওয়াকথ্রু ভিডিওতে!\n\n"
            "🔥 **ভিডিওর প্রধান ফিচারসমূহ:**\n"
            "📊 **০১. এক্সিকিউটিভ ড্যাশবোর্ড (1st Screen):** আজকের মোট বিক্রি, নিট প্রফিট ও ক্যাশ কাউন্টারের লাইভ আপডেট।\n"
            "⚡ **০২. সুপারফাস্ট POS কাউন্টার (2nd Screen):** মাত্র ৩ সেকেন্ডে বারকোড স্ক্যান ও ইনস্ট্যান্ট থার্মাল প্রিন্ট।\n"
            "🚨 **০৩. জিরো লস এক্সপায়ারি গার্ড:** ওষুধ নষ্ট হওয়ার আগেই স্বয়ংক্রিয় FEFO অ্যালার্ট ও কোম্পানি রিটার্ন শিট।\n"
            "📲 **০৪. ডিজিটাল বাকি খাতা ও SMS:** কাস্টমার মোবাইলে ১-ক্লিকে প্রফেশনাল SMS তাগাদা পাঠিয়ে দ্রুত টাকা আদায়।\n\n"
            "👉 পুরো ভিডিওটি দেখে আপনার মতামত কমেন্টে জানান।\n"
            "🎁 **আপনার ফার্মেসিতে ফ্রি ডেমো টেস্ট করতে কমেন্টে লিখুন 'Demo' অথবা এখনই ইনবক্স করুন!**\n"
            "🌐 ওয়েবসাইট: https://infoaidtech.net\n\n"
            "#AidlyPMS #PharmaERP #PharmacyVideo #POSSoftware #MedicalStoreBD #HealthcareIT #BanglaSoftware #InfoAidTech"
        ),
        "published": False,
    },

    # =========================================================================
    # DAY 3 (Cycle A)
    # =========================================================================
    {
        "id": "day3_slot1_agency_leadgen_seo",
        "day": "Day 3",
        "cycle": "Cycle A",
        "slot": "Post 1 (12:00 PM)",
        "category": "Digital Marketing",
        "topic": "Lead Generation & SEO",
        "scheduled_time": "12:00 PM BST",
        "image_url": "banners/day3_agency_leadgen_seo.png",
        "message": (
            "🔍 **সোশ্যাল মিডিয়ার বাইরেও কোটি টাকার ক্লায়েন্ট গুগলে আপনার সার্ভিসের জন্য সার্চ করছে! আপনি কি প্রস্তুত?** 🚀\n\n"
            "সোশ্যাল মিডিয়ায় মানুষ আসে অবসর কাটাতে বা এন্টারটেইনমেন্টের জন্য। কিন্তু গুগল সার্চে মানুষ আসে **সরাসরি কেনার তীব্র ইচ্ছা (High Intent) নিয়ে!**\n\n"
            "গুগল র‍্যাঙ্কিংয়ে ১ নম্বরে থাকার ৩টি অপ্রতিদ্বন্দ্বী সুবিধা:\n\n"
            "🎯 **১. হাই-টিকেটিং B2B লিড:** যারা সরাসরি 'Best Software Company' বা 'Wholesale Supplier' খুঁজছে, তারা সরাসরি আপনাকে কল দিবে।\n"
            "💰 **২. Zero Ongoing Ad Spend:** গুগল এডসের পেছনে প্রতি ক্লিকে ডলার না গুনেও প্রতিদিন রেগুলার অর্গানিক কাস্টমার পাবেন।\n"
            "🏆 **৩. মার্কেট অথরিটি ও ট্রাস্ট:** কাস্টমারদের চোখে গুগলের ফার্স্ট পেজে থাকা কোম্পানিগুলোই সবচেয়ে বেশি ভরসাযোগ্য।\n\n"
            "Info AidTech দিচ্ছে সম্পূর্ণ ডাটা-ব্যাকড **Technical SEO, Keyword Research & Local Google Map Dominance** সলিউশন।\n\n"
            "📊 **আপনার ওয়েবসাইটের বর্তমান দুর্বলতা ও ফ্রি টেকনিক্যাল SEO অডিট রিপোর্ট পেতে আজই ইনবক্স করুন!**\n"
            "🌐 ভিজিট করুন: https://infoaidtech.net\n\n"
            "#SEO #GoogleRanking #LocalSEO #B2BLeads #InboundMarketing #OrganicTraffic #SearchEngineMarketing #InfoAidTech"
        ),
        "published": False,
    },
    {
        "id": "day3_slot2_aidly_pos_spotlight",
        "day": "Day 3",
        "cycle": "Cycle A",
        "slot": "Post 2 (8:30 PM)",
        "category": "AidlyPMS SMM Post",
        "topic": "Feature Spotlight",
        "scheduled_time": "8:30 PM BST",
        "image_url": "banners/day3_aidly_pos_spotlight.png",
        "message": (
            "⚡ **কাউন্টারে কাস্টমারের লম্বা লাইন? ভিড়ের চাপে ভুল ক্যাশ মেমো বা ভুল দাম নেওয়া বন্ধ করুন!** 🧾\n\n"
            "ব্যস্ত ফার্মেসি কাউন্টারে প্রতি সেকেন্ডের মূল্য অপরিসীম। ড্রাগের স্ট্রিপ খুঁজতে দেরি হলে বা ক্যালকুলেটরে ভুল হিসাব কষলে ক্ষতি কেবল আপনারই!\n\n"
            "🔥 **Aidly PMS Superfast Barcode POS বিলিং যেভাবে আপনার কাউন্টার রাখে ১০০% গতিশীল:**\n"
            "⚡ **৩ সেকেন্ডে বারকোড স্ক্যান:** কোনো ড্রাগ নাম টাইপ ছাড়াই সাথে সাথে ব্যাচ, রেট ও অটোমেটিক ডিসকাউন্ট ক্যালকুলেট।\n"
            "🖨️ **ইনস্ট্যান্ট থার্মাল প্রিন্ট ও SMS মেমো:** সেকেন্ডের মধ্যে প্রিন্ট মেমো রেডি এবং কাস্টমার ফোনে ডিজিটাল SMS ইনভয়েস।\n"
            "💳 **ক্যাশ ও মোবাইল ব্যাংকিং:** ক্যাশ, কার্ড, বিকাশ বা নগদে ওয়ান-ক্লিকে পেমেন্ট রিসিভ ও ড্রয়ার ব্যালেন্স আপডেট।\n"
            "🔄 **রিয়েল-টাইম মাল্টি-কাউন্টার সিঙ্ক:** ৫ জন সেলসম্যান একই সাথে বিলিং করলেও স্টকে ০.০১% ও গরমিলের সুযোগ নেই।\n\n"
            "🛑 পুরনো কায়দায় সময় ও কাস্টমার নষ্ট করবেন না। কাউন্টার রাখুন সুপার স্মুথ ও প্রফেশনাল!\n"
            "📲 **ফ্রি লাইভ POS ডেমো টেস্ট করতে এখনই ইনবক্স করুন অথবা ভিজিট করুন:** https://infoaidtech.net\n\n"
            "#AidlyPOS #FastBilling #PharmacyPOS #BarcodeScanner #PharmaRetail #PharmacyCounter #PharmacyManagement #InfoAidTech"
        ),
        "published": False,
    },

    # =========================================================================
    # DAY 4 (Cycle B)
    # =========================================================================
    {
        "id": "day4_slot1_agency_social_commerce",
        "day": "Day 4",
        "cycle": "Cycle B",
        "slot": "Post 1 (12:00 PM)",
        "category": "Social Media Marketing",
        "topic": "Social Commerce BD",
        "scheduled_time": "12:00 PM BST",
        "image_url": "banners/day4_agency_social_commerce.png",
        "message": (
            "🛒 **ইনবক্সে শত শত মেসেজ আসে, কিন্তু দাম শুনেই কাস্টমার গায়েব? সোশ্যাল কমার্সে সেলস ডাবল করার সিক্রেট!** 📦\n\n"
            "বাংলাদেশে ই-কমার্স বা এফ-কমার্সে সেলস না আসার প্রধান কারণ বাজে পণ্য নয়, বরং **ইনবক্স কনভার্সন ফ্রেমওয়ার্কের ভুল**!\n\n"
            "কনভার্সন রেট ৩৫% থেকে ৫০% বাড়াতে এই ৩টি সাইকোলজিক্যাল কৌশল আজই প্রয়োগ করুন:\n\n"
            "⚡ **১. ১ মিনিটের গোল্ডেন উইন্ডো:** কাস্টমার যখন মেসেজ দেয়, তখন সে কেনার মুডে থাকে। ১ মিনিটের মধ্যে উত্তর দিলে কনভার্সন রেট ৩ গুণ বৃদ্ধি পায়।\n"
            "🤝 **২. ট্রাস্ট সিগন্যাল ও সিওডি গ্যারান্টি:** 'প্যাকেট দেখে পেমেন্ট করুন' এবং আসল কাস্টমারদের আনবক্সিং ভিডিও ইনবক্সে শেয়ার করলে সন্দেহ দূর হয়।\n"
            "🎁 **৩. স্মার্ট আপসেলিং ও বান্ডেল অফার:** 'ম্যাম, এই আইটেমের সাথে এই কম্বো নিলে ডেলিভারি চার্জ সম্পূর্ণ ফ্রি' — এতে এক অর্ডারে প্রফিট দ্বিগুণ হয়।\n\n"
            "🚀 আপনার অনলাইন ব্র্যান্ডের ইনবক্স অটোমেশন ও হাই-কনভার্টিং সেলস ফানেল তৈরি করতে চান?\n"
            "📲 **আমাদের কমার্স গ্রোথ এক্সপার্টদের সাথে আজই ইনবক্সে যোগাযোগ করুন:** https://infoaidtech.net\n\n"
            "#SocialCommerce #EcommerceBD #FCommerce #InboxSales #ConversionRateOptimization #GrowthHacking #InfoAidTech"
        ),
        "published": False,
    },
    {
        "id": "day4_slot2_aidly_story_video",
        "day": "Day 4",
        "cycle": "Cycle B",
        "slot": "Post 2 (8:30 PM)",
        "category": "AidlyPMS Bengali Video",
        "topic": "Problem-Solution Story",
        "scheduled_time": "8:30 PM BST",
        "image_url": "aidly_bangla_story.mp4",
        "message": (
            "🎥 **'প্রতি মাসে ২০-৩০ হাজার টাকার ওষুধ নষ্ট হতো!' — শুনুন এক ফার্মেসি ব্যবসায়ীর লোকসান বন্ধের বাস্তব গল্প।** 💔➡️❤️\n\n"
            "ফার্মেসির লাভ কি মেয়াদোত্তীর্ণ ওষুধ আর বাকি টাকার খাতায় হারিয়ে যাচ্ছে?\n"
            "এই ভুল ম্যানেজমেন্টের কারণে প্রতি মাসে হাজার হাজার টাকা নিঃশব্দে গলে যায়।\n\n"
            "💡 কিন্তু সঠিক সময়ে সঠিক প্রযুক্তির ব্যবহার বদলে দিতে পারে পুরো দৃশ্যপট! দেখুন কীভাবে **Aidly PMS** এনে দিয়েছে স্থায়ী সমাধান:\n\n"
            "🛡️ **অটোমেটিক FEFO অ্যালার্ট:** কোন ওষুধ আগে বিক্রি করতে হবে সফটওয়্যার নিজেই জানাবে।\n"
            "📄 **১-ক্লিকে কোম্পানি রিটার্ন শিট:** মেয়াদ শেষ হওয়ার আগেই ভেন্ডরকে ফেরত পাঠিয়ে লোকসান ০%।\n"
            "⚡ **৩ সেকেন্ডে বারকোড বিলিং:** ভুল ড্রাগ এন্ট্রি বা প্রাইস মিসম্যাচের কোনো সুযোগ নেই।\n"
            "📲 **১-ক্লিক SMS তাগাদা:** খাতার ডায়রি বাদ দিয়ে কাস্টমার মোবাইলে রিমাইন্ডার পাঠিয়ে দ্রুত বকেয়া কালেকশন।\n\n"
            "👉 পুরো ভিডিওটি দেখে জেনে নিন কীভাবে আপনার ফার্মেসিও হতে পারে ১০০% লাভজনক।\n"
            "🎁 **ফ্রি লাইভ ডেমো দেখার জন্য এখনই ইনবক্স করুন অথবা কমেন্টে জানান!**\n"
            "🌐 ওয়েবসাইট: https://infoaidtech.net\n\n"
            "#AidlyPMS #PharmaStory #ZeroLoss #ExpiryManagement #PharmacySoftware #PharmaBusinessBD #InfoAidTech"
        ),
        "published": False,
    },

    # =========================================================================
    # DAY 5 (Cycle A)
    # =========================================================================
    {
        "id": "day5_slot1_agency_data_retargeting",
        "day": "Day 5",
        "cycle": "Cycle A",
        "slot": "Post 1 (12:00 PM)",
        "category": "Digital Marketing",
        "topic": "Data & Retargeting",
        "scheduled_time": "12:00 PM BST",
        "image_url": "banners/day5_agency_data_retargeting.png",
        "message": (
            "🎯 **আপনার বিজ্ঞাপনের ৯৭% বাজেট কি স্রেফ অপচয় হচ্ছে? কারণ ৯৭% মানুষ প্রথম দেখায় কখনোই কেনে না!** 📊\n\n"
            "কোল্ড অডিয়েন্সের পেছনে বারবার নতুন বাজেট খরচ করা মানে সমুদ্রে টাকা ঢালা। স্মার্ট মার্কেটাররা জানেন — আসল লাভ লুকিয়ে থাকে **রিটার্গেটিংয়ে (Retargeting)**!\n\n"
            "কেন রিটার্গেটিংয়ে প্রতি অর্ডারের খরচ ৬০% কমে যায়?\n\n"
            "👥 **১. কাস্টম অডিয়েন্স (Custom Audience):** যারা ইতিমধ্যে আপনার পেজে এসেছে, ভিডিও দেখেছে বা অ্যাড টু কার্ট করেছে, তারা আপনার ব্র্যান্ডকে চেনে।\n"
            "🔥 **২. হাই-কনভার্টিং রিলেশনশিপ:** 'আপনি কি প্রোডাক্টটি কার্টে রেখে গেছেন?' — এমন পার্সোনালাইজড মেসেজ নিমেষেই অর্ডার কনফার্ম করায়।\n"
            "📈 **৩. সার্ভার-সাইড ট্র্যাকিং (Meta CAPI):** ব্রাউজার কুকি ব্লক হলেও ১০০% নির্ভুল ডেটা ট্র্যাক করে রিটার্গেটিং শক্তিশালী করা।\n\n"
            "আমাদের ক্লায়েন্টদের ক্ষেত্রে কোল্ড ট্রাফিকের চেয়ে রিটার্গেটিং ক্যাম্পেইনে **ROAS ৩ গুণ বেশি** প্রমাণিত হয়েছে!\n\n"
            "🚀 আপনার বিজনেসে অ্যাডভান্সড মেটা পিক্সেল ও রিটার্গেটিং ফানেল সেটআপ করতে আজই আমাদের ইনবক্স করুন।\n"
            "🌐 বিস্তারিত দেখুন: https://infoaidtech.net\n\n"
            "#Retargeting #MetaPixel #ConversionAPI #PerformanceMarketing #AdSpendEfficiency #DataDrivenMarketing #InfoAidTech"
        ),
        "published": False,
    },
    {
        "id": "day5_slot2_aidly_roi_savings",
        "day": "Day 5",
        "cycle": "Cycle A",
        "slot": "Post 2 (8:30 PM)",
        "category": "AidlyPMS SMM Post",
        "topic": "ROI & Cost Savings",
        "scheduled_time": "8:30 PM BST",
        "image_url": "banners/day5_aidly_roi_savings.png",
        "message": (
            "💰 **হিসাব করে দেখেছেন কি? Aidly PMS ব্যবহারে আপনার ফার্মেসিতে প্রতি মাসে কত টাকা সাশ্রয় হচ্ছে?** 📈\n\n"
            "Aidly PMS কোনো সাধারণ খরচ নয়, এটি আপনার ফার্মেসির একজন নিবেদিত ডিজিটাল ম্যানেজার — যার রিটার্ন অন ইনভেস্টমেন্ট (ROI) তাৎক্ষণিক!\n\n"
            "হিসাবটা নিজেই মিলিয়ে নিন:\n"
            "🛡️ **৳ ১৫,০০০+ ওষুধ মেয়াদোত্তীর্ণ সাশ্রয়:** মেয়াদ শেষ হওয়ার আগেই কোম্পানি রিটার্ন দিয়ে শূন্য লোকসান।\n"
            "⏱️ **৫০+ মূল্যবান কর্মঘণ্টা সাশ্রয়:** ম্যানুয়াল ডায়রি ও খাতা লেখার সময় বাঁচিয়ে ড্রাগ সেলস ও সার্ভিসে ফোকাস।\n"
            "💵 **৯০% দ্রুত বকেয়া কালেকশন:** মোবাইল SMS তাগাদায় আটকে থাকা বাকির টাকা ক্যাশে রূপান্তর।\n"
            "❌ **ভুল মেমো ও চুরি বন্ধ:** স্টক ও ড্রয়ার ব্যালেন্সের নিখুঁত ট্যালি থাকায় অভ্যন্তরীণ গরমিল ০%।\n\n"
            "সফটওয়্যারের সামান্য সাবস্ক্রিপশন ফি দিয়ে প্রতি মাসে ফার্মেসির নিট প্রফিট বাড়ান ২৫,০০০ থেকে ৫০,০০০ টাকা পর্যন্ত!\n\n"
            "👉 বুদ্ধিমান ফার্মেসি মালিকের মতো সঠিক সিদ্ধান্ত নিন আজই।\n"
            "🎁 **ফ্রি লাইভ ডেমো দেখতে ইনবক্স করুন অথবা ভিজিট করুন:** https://infoaidtech.net\n\n"
            "#PharmacyROI #CostSavings #BusinessEfficiency #AidlyPMS #PharmacyProfit #SmartPharma #PharmacySoftware #InfoAidTech"
        ),
        "published": False,
    },

    # =========================================================================
    # DAY 6 (Cycle B)
    # =========================================================================
    {
        "id": "day6_slot1_agency_content_strategy",
        "day": "Day 6",
        "cycle": "Cycle B",
        "slot": "Post 1 (12:00 PM)",
        "category": "Social Media Marketing",
        "topic": "Content Strategy",
        "scheduled_time": "12:00 PM BST",
        "image_url": "banners/day6_agency_content_strategy.png",
        "message": (
            "🪝 **'আমাদের প্রোডাক্ট কিনুন' — এই বোরিং পোস্ট দিয়ে কি কাস্টমারের স্ক্রোল থামানো সম্ভব? একদমই না!** 🚫\n\n"
            "সোশ্যাল মিডিয়ায় মানুষ কেনাকাটা করতে আসে না, আসে বিনোদন বা নতুন কিছু জানতে। আপনি যদি ফিডে দাঁড়িয়ে না থাকতে পারেন, আপনার প্রতিযোগী জিতে যাবে!\n\n"
            "🔥 **থাম্ব-স্টপিং ভাইরাল কনটেন্ট ফ্রেমওয়ার্ক (The 3-Second Hook Rule):**\n\n"
            "🎯 **১. প্রথম ৩ সেকেন্ডের হুক (The Hook):** 'আপনি কি এই ভুলটি করছেন?' বা '৯৯% মানুষ যা জানে না' — এমন শক্তিশালী বাক্য যা ফিডে থামতে বাধ্য করে।\n"
            "📖 **২. প্রবলেম-সলিউশন স্টোরিটেলিং (The Story):** সরাসরি বিক্রি না করে কাস্টমারের বাস্তব সমস্যা তুলে ধরুন এবং জানান কীভাবে তা সহজে সমাধান করা যায়।\n"
            "⚡ **৩. নো-ফ্রিকশন কল টু অ্যাকশন (Frictionless CTA):** কাস্টমারকে জটিল ফর্ম পূরণের কথা না বলে বলুন 'ফ্রি টিপস পেতে কমেন্টে লিখুন Info'।\n\n"
            "আপনার পেজের জন্য কি এমন প্রফেশনাল কনটেন্ট ক্যালেন্ডার ও ক্রিয়েটিভ ভিজুয়াল ডিজাইন চান?\n"
            "📲 **আজই আমাদের ক্রিয়েটিভ কনটেন্ট টিমের সাথে কথা বলুন ইনবক্সে:** https://infoaidtech.net\n\n"
            "#ContentStrategy #Storytelling #ViralMarketing #BrandBuilding #CreativeDesign #SocialMediaGrowth #InfoAidTech"
        ),
        "published": False,
    },
    {
        "id": "day6_slot2_aidly_deepdive_video",
        "day": "Day 6",
        "cycle": "Cycle B",
        "slot": "Post 2 (8:30 PM)",
        "category": "AidlyPMS Bengali Video",
        "topic": "Feature Deep-Dive",
        "scheduled_time": "8:30 PM BST",
        "image_url": "aidly_bangla_deepdive.mp4",
        "message": (
            "🎬 **কাগজের খাতায় বাকি লিখে আর কত টাকা হারাবেন? দেখুন কীভাবে Aidly PMS ১-ক্লিক SMS দিয়ে টাকা তোলে!** 📲\n\n"
            "কাস্টমার হয়তো ভুলে যায়, কিন্তু Aidly PMS প্রতিটি টাকার হিসাব নিখুঁতভাবে মনে রাখে!\n"
            "এই ফিচার ডিপ-ডাইভ ভিডিওতে দেখুন কেন সারা বাংলাদেশের ফার্মেসি মালিকরা কাগজের খাতা ছুড়ে ফেলে Aidly PMS বেছে নিচ্ছেন:\n\n"
            "📒 **০১. ১০০% নির্ভুল ডিজিটাল লেজার:** কাস্টমারের নাম বা মোবাইল দিয়ে মুহূর্তেই দেখুন মোট বকেয়া ও পূর্বের মেমো হিস্ট্রি।\n"
            "📲 **০২. ১-ক্লিক মোবাইল SMS অ্যালার্ট:** 'প্রিয় কাস্টমার, আপনার বকেয়া...' — একটি ক্লিকেই প্রফেশনাল SMS তাগাদা পৌঁছে যাবে গ্রাহকের মোবাইলে।\n"
            "⚡ **০৩. ৩ সেকেন্ডে বারকোড POS বিলিং:** বারকোড স্ক্যান করলেই ব্যাচ নম্বর, ড্রাগ ও ডিসকাউন্ট অটো সিলেক্ট হয়ে সেকেন্ডে মেমো প্রিন্ট।\n"
            "📊 **০৪. রিয়েল-টাইম ক্যাশ ড্রয়ার ট্যালি:** ক্যাশ, কার্ড ও বিকাশ পেমেন্টের শিফট ক্লোজিং নিখুঁতভাবে অটোমেটেড।\n\n"
            "👉 ভিডিওটি দেখুন এবং কমেন্টে জানান আপনার ফার্মেসির অভিজ্ঞতা।\n"
            "🎁 **আপনার ফার্মেসিতে ফ্রি ডেমো টেস্ট করতে এখনই ইনবক্স করুন অথবা ভিজিট করুন:** https://infoaidtech.net\n\n"
            "#AidlyPMS #DigitalLedger #SMSAlert #PharmacyBilling #POSSystem #PharmaBD #SmartBusiness #InfoAidTech"
        ),
        "published": False,
    },

    # =========================================================================
    # DAY 7 (Cycle A)
    # =========================================================================
    {
        "id": "day7_slot1_agency_tool_stack",
        "day": "Day 7",
        "cycle": "Cycle A",
        "slot": "Post 1 (12:00 PM)",
        "category": "Digital Marketing",
        "topic": "Weekly Tool Stack",
        "scheduled_time": "12:00 PM BST",
        "image_url": "banners/day7_agency_tool_stack.png",
        "message": (
            "⚙️ **২০২৬ সালের সেরা ডিজিটাল মার্কেটিং ও এআই টেক স্ট্যাক — যা আমাদের ক্লায়েন্টদের ১০ গুণ রেজাল্ট এনে দেয়!** 🚀\n\n"
            "মার্কেটিংয়ে শুধু পরিশ্রম নয়, আধুনিক প্রযুক্তির সঠিক সমন্বয় বিজনেসের উৎপাদন ক্ষমতা ও সেলস বহু দূর এগিয়ে নেয়।\n\n"
            "আমরা যেসব প্রিমিয়াম টুল ও অটোমেশন নিয়মিত ব্যবহার করি:\n\n"
            "⚡ **১. Meta Ads API & Automated Rules:** মানুষের ভুলের সুযোগ নেই, ২৪/৭ রোবোটিক বাজেট স্কেলিং ও রিটার্গেটিং।\n"
            "🤖 **২. Remotion Programmatic Video:** কোডিংয়ের মাধ্যমে হাই-রেজোলিউশন ডায়নামিক প্রোডাক্ট ভিডিও দ্রুত রেন্ডার।\n"
            "📈 **৩. Google Analytics 4 & Server-Side CAPI:** ব্রাউজার কুকি ছাড়াই ১০০% নির্ভুল ডেটা ও আরওআই ট্র্যাকিং।\n"
            "🧠 **৪. Advanced LLM & Copywriting Frameworks:** নিখুঁত অডিয়েন্স রিসার্চ ও হাই-কনভার্টিং সাইকোলজিক্যাল অ্যাড কপি।\n\n"
            "আপনার প্রতিষ্ঠান কি এই আধুনিক মার্কেটিং অটোমেশনের সুবিধা নিতে প্রস্তুত?\n"
            "📲 **ফ্রি কনসালটেশন ও টেকনোলজি পার্টনারশিপের জন্য আজই ইনবক্স করুন অথবা ভিজিট করুন:** https://infoaidtech.net\n\n"
            "#MarTech #MarketingStack #AIAutomation #DigitalAgency #PerformanceGrowth #TechFirst #InfoAidTech"
        ),
        "published": False,
    },
    {
        "id": "day7_slot2_aidly_social_proof",
        "day": "Day 7",
        "cycle": "Cycle A",
        "slot": "Post 2 (8:30 PM)",
        "category": "AidlyPMS SMM Post",
        "topic": "Social Proof & Trust",
        "scheduled_time": "8:30 PM BST",
        "image_url": "banners/day7_aidly_social_proof.png",
        "message": (
            "🏆 **'হিসাব মেলানো এখন আগের চেয়ে ৫ গুণ সহজ!' — সারা বাংলাদেশের আধুনিক ফার্মেসির আস্থা Aidly PMS!** 🌟\n\n"
            "শত শত ফার্মেসি মালিক প্রতিদিন নিশ্চিন্তে তাদের কোটি টাকার ড্রাগ ইনভেন্টরি, সেলস ও লাভ-লস পরিচালনা করছেন Aidly PMS ক্লাউডে:\n\n"
            "👥 **৫০০+ বিশ্বস্ত ফার্মেসি পার্টনার:** রিটেল ফার্মেসি থেকে শুরু করে মাল্টিপল ব্রাঞ্চ — সবার নির্ভরযোগ্য সমাধান।\n"
            "🔒 **৯৯.৯% ক্লাউড আপটাইম ও ডেটা সিকিউরিটি:** কোনো ডেটা হারানোর ভয় নেই, স্বয়ংক্রিয় ক্লাউড ব্যাকআপ।\n"
            "🎧 **২৪/৭ ডেডিকেটেড বাংলা সাপোর্ট টিম:** যেকোনো প্রয়োজনে সরাসরি কল বা অনলাইনে ইনস্ট্যান্ট সাপোর্ট।\n"
            "💻 **কোনো ভারী কম্পিউটার প্রয়োজন নেই:** সাধারণ ল্যাপটপ বা মোবাইল দিয়েই সম্পূর্ণ নিয়ন্ত্রণ সম্ভব!\n\n"
            "ফার্মেসির হিসাবের ভুল ও ওষুধের লোকসান দূর করে নিজের ব্যবসাকে স্মার্ট করতে আর দেরি করবেন না।\n\n"
            "🎁 **আজই ফ্রি লাইভ ডেমো দেখে সিদ্ধান্ত নিন। ইনবক্স করুন আমাদের ফেসবুক পেইজে!**\n"
            "🌐 ওয়েবসাইট: https://infoaidtech.net\n\n"
            "#AidlyPMS #PharmacyTrust #CustomerReviews #PharmacyCommunity #SmartPharma #PharmacySoftwareBD #InfoAidTech"
        ),
        "published": False,
    },
]

def update_queue():
    existing_published = []
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                existing_published = [p for p in data if p.get("published", False)]
            except Exception as e:
                print("Warning reading existing posts:", e)

    full_queue = existing_published + NEW_POSTS
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(full_queue, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Updated {POSTS_FILE}:")
    print(f"  - Preserved {len(existing_published)} published posts")
    print(f"  - Added {len(NEW_POSTS)} upcoming posts for 7-Day Schedule Matrix")
    print(f"  - Total posts in file: {len(full_queue)}")

if __name__ == "__main__":
    update_queue()
