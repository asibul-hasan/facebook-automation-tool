# Aidly PMS — Product Marketing Context & Positioning

> **Document Version**: 1.0.0  
> **Last Updated**: November 2026  
> **Target Market**: Bangladesh (Retail Pharmacies, Pharmacy Chains, Hospital Pharmacies, Model Pharmacies)  
> **Canonical Path**: `/home/asibul/app/features/automation/.agents/product-marketing.md`

---

## 1. Product Overview

- **Product Name**: Aidly PMS (Pharmacy Management System & POS)
- **Parent Company**: Info AidTech (`infoaidtech.net`)
- **One-Line Description**: Cloud-first, offline-capable pharmacy management and high-speed POS software engineered specifically for Bangladesh's retail and chain pharmacies.
- **Category Shelf**: Pharmacy Management Software, Retail Pharmacy POS, Healthcare Inventory & ERP SaaS.
- **Product Architecture**: Modern web app built with Angular 21, Nx Monorepo, AG-Grid enterprise data tables, real-time SignalR sync, thermal receipt printing, and local offline queuing.
- **Delivery Model**: B2B Cloud SaaS with on-prem offline resilience.

---

## 2. Target Audience & Ideal Customer Profile (ICP)

### Primary Geographic Focus
- **Dhaka Metro**: Dhanmondi, Gulshan, Banani, Uttara, Mirpur, Mohammadpur, Motijheel, Badda, Elephant Road.
- **Divisional Hubs**: Chittagong, Sylhet, Rajshahi, Khulna, Bogura.

### ICP Segments
1. **High-Volume Independent Retail Pharmacies (Model Pharmacies)**:
   - 1–3 counters, 5,000–25,000 SKUs, daily sales ৳50,000–৳250,000.
   - Core need: Fast rush-hour counter checkout, preventing expired stock write-offs, balancing the cash drawer between shift changes.
2. **Multi-Branch Pharmacy Chains**:
   - 3–15 branches, centralized inventory control, inter-branch stock transfers.
   - Core need: Real-time multi-branch visibility, consolidated P&L, supplier procurement negotiations.
3. **Hospital & Clinic In-House Pharmacies**:
   - High prescription flow, doctor commission tracking, 24/7 continuous operations with rotating staff.

---

## 3. Personas & Stakeholder Dynamics

| Stakeholder | Key Role | What They Care About Most | Biggest Daily Frustration |
| :--- | :--- | :--- | :--- |
| **Pharmacy Owner / Investor** | Economic Buyer | Net profit, zero stock leakage, daily cash tally, ROI | Expired medicines thrown away, untracked staff theft, manual cash mismatch |
| **Store Manager / Chief Pharmacist** | Champion / User | Accurate stock counts, supplier returns, DGDA compliance | Supplier representative disputes, running out of top-selling medicines |
| **Counter Cashier / Sales Staff** | Daily Operator | Speed of search, 1-click thermal printing, keyboard shortcuts | Software freezing while 10 impatient patients wait in line at 8:30 PM |

---

## 4. The 5 Core Pain Points ("Daily Leaks")

1. **The Expiry Date Black Hole (মেয়াদোত্তীর্ণ ওষুধের লোকসান)**:
   - An average retail pharmacy in Bangladesh loses **৳15,000 to ৳45,000 per month** because near-expiry syrups, injections, and tablets sit behind newly stocked batches.
   - *Aidly Fix*: Automated **FEFO (First-Expired, First-Out)** batch recommendation and 30/60/90-day color-coded expiry alerts with 1-click supplier return slips.

2. **Rush-Hour Counter Bottlenecks (কাউন্টার ভিড় ও সফটওয়্যার হ্যাং)**:
   - Between 7:00 PM and 10:00 PM, dozens of customers queue for medicines. Slow search or laggy systems cause lost sales and frustrated patients.
   - *Aidly Fix*: **3-Second Counter POS** with instant barcode scanning, instant brand/generic autocomplete over 50,000+ medicines, and keyboard-only checkout.

3. **Internet Drops & Power Cuts (ইন্টারনেট বা বিদ্যুৎ বিভ্রাট)**:
   - When local broadband goes down, cloud-only POS systems completely lock up.
   - *Aidly Fix*: **Offline-First Resilience** with local queueing. Cashiers continue billing seamlessly; all transactions sync automatically to the cloud once internet restores.

4. **Cash Drawer Mismatches at Shift Handover (শিফট চেঞ্জে ক্যাশ অমিল)**:
   - Day shift hands over to night shift, and the physical cash drawer doesn't match register totals by hundreds or thousands of Taka.
   - *Aidly Fix*: **Shift Opening/Closing Cash Reconciliation** requiring blinded count entry before generating the shift variance report.

5. **Customer Due Ledger & Bad Debt (বাকির হিসাবের খাতা)**:
   - Local neighborhood customers buy on credit (বাকি); paper khata records get lost, disputed, or forgotten.
   - *Aidly Fix*: Digital **Customer Due Ledger** with automated SMS payment reminders and credit limit safeguards.

---

## 5. Differentiating Capabilities

- **50,000+ Pre-Loaded Bangladesh Drug Catalog**: Pre-indexed with generics, brand names, dosage forms, manufacturer names (Square, Beximco, Incepta, Renata, Healthcare, Acme, etc.), and MRPs.
- **Instant Generic Substitute Finder**: When a prescribed brand is out of stock, 1-click shows all in-stock medicines sharing the exact same generic molecule and strength.
- **Doctor Prescription & Commission Tracking**: Track prescribing doctors, prescription serials, and referral commissions accurately.
- **Thermal Printer & Barcode Scanner Agnostic**: Works out of the box with any 80mm/58mm thermal printer (ESC/POS) and USB/Bluetooth barcode scanner.
- **Role-Based Security**: Restrict cashiers from seeing cost prices or profit margins; enforce Manager approval for sales returns or bill cancellations.

---

## 6. Competitive Landscape in Bangladesh

| Competitor Category | Typical Examples | Why They Fall Short |
| :--- | :--- | :--- |
| **Paper Khata / Registers** | Traditional ledger books | Zero expiry alerts, no theft protection, takes 2 hours every night to tally cash. |
| **Generic Grocery POS** | Generic cracked desktop tools | No batch/expiry tracking, no generic medicine substitution, crashes easily. |
| **Legacy Desktop Tools** | Old Windows offline software | No remote owner access from phone, vulnerable to PC hard drive crashes, no auto backup. |
| **Foreign Cloud POS** | Indian/Western SaaS | Not adapted to Bangladesh DGDA formats, no local bKash/Nagad integration, lacks BD medicine database. |

---

## 7. Pricing & Commercial Strategy

- **Starter Plan**: For single-counter community pharmacies (৳999 – ৳1,499 / month).
- **Pro Model Pharmacy Plan**: For high-volume multi-counter stores with full inventory & accounting (৳2,499 – ৳3,499 / month).
- **Chain Enterprise**: Multi-branch centralized license with dedicated account manager.
- **Free Live Demo**: 1-on-1 personalized 15-minute live screen demo (via Google Meet / AnyDesk / In-person visit in Dhaka).

---

## 8. Brand Voice, Language & Contact Rules

### Linguistic Identity
- **Smart Business Bengali (শুদ্ধ ও প্রাঞ্জল বাংলা + Natural Tech English)**:
  - Speak like educated Bangladeshi entrepreneurs and doctors communicate.
  - Keep industry terms in natural English: `Facebook Ads`, `SEO`, `POS Billing`, `Barcode`, `Expiry Date`, `Batch Tracking`, `Stock`, `Cash Drawer`, `Shift Change`, `SMS Invoice`, `Due Ledger`, `Supplier`.
  - Avoid robotic archaic translations (Never say "বিজ্ঞাপনের বাজেট" or "ফেসবুকের নীল বাটন").

### Non-Negotiable Contact & CTA Rules
- **NEVER use dummy or placeholder phone numbers** (`+880 1700-000000` is strictly forbidden).
- **Standard CTAs**:
  - `💬 ফ্রি ডেমো দেখতে এখনই ইনবক্স করুন আমাদের পেইজে (Facebook & LinkedIn)`
  - `🌐 ভিজিট করুন: https://infoaidtech.net`

---

## 9. Changelog

- **v1.0.0 (2026-11-20)**: Initialized canonical Aidly PMS product marketing brief based on `/apps/aidlyPms` Angular source code.
