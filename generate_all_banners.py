#!/usr/bin/env python3
"""
Aidly PMS & Info AidTech High-Converting Commercial Banner Generator
--------------------------------------------------------------------
Compiles 6 distinct 1:1 square (1080x1080) commercial banners:
3 for Aidly PMS (Pharma ERP/POS) and 3 for Info AidTech Marketing Agency.
"""

import os
import subprocess

BANNERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "banners")
os.makedirs(BANNERS_DIR, exist_ok=True)

TEMPLATES = [
    # 3 Distinct Aidly PMS Themes
    ("banner_marketing_aidly_pos.png", "render_banner_theme_green.html"),
    ("banner_marketing_aidly_red.png", "render_banner_theme_red.html"),
    ("banner_marketing_aidly_blue.png", "render_banner_theme_blue.html"),
    # 3 Distinct Agency Marketing Themes
    ("banner_marketing_agency_meta_ads.png", "render_agency_meta_ads.html"),
    ("banner_marketing_agency_google_ppc.png", "render_agency_google_ppc.html"),
    ("banner_marketing_agency_custom_software.png", "render_agency_custom_software.html"),
]

def generate():
    chrome_bin = "/usr/bin/google-chrome"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for out_name, html_file in TEMPLATES:
        html_path = os.path.join(base_dir, html_file)
        if not os.path.exists(html_path):
            continue
        out_path = os.path.join(BANNERS_DIR, out_name)
        cmd = [
            chrome_bin,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--allow-file-access-from-files",
            "--window-size=1080,1080",
            f"--screenshot={out_path}",
            f"file://{html_path}",
        ]
        print(f"Compiling: {out_name}...")
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"  -> Generated {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    generate()
