#!/usr/bin/env python3
"""
Aidly PMS & Info AidTech Commercial Marketing Banner Generator
--------------------------------------------------------------
Generates high-converting 1:1 square (1080x1080) and 1.91:1 landscape (1200x630)
commercial marketing banners adopting real competitor ad themes (AppNexaa, SK Soft, Pyora).
Embeds actual software screenshots from /home/asibul/app/features/aidly/screenshots
inside realistic MacBook and mobile mockups with floating metric cards.
"""

import os
import subprocess
import tempfile

BANNERS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "banners")
SCREENSHOTS_DIR = "/home/asibul/app/features/aidly/screenshots"
os.makedirs(BANNERS_DIR, exist_ok=True)

# Templates are maintained in HTML format and compiled via headless Google Chrome
TEMPLATES = [
    ("banner_marketing_aidly_pos.png", "render_banner_theme_green.html"),
    ("banner_marketing_aidly_red.png", "render_banner_theme_red.html"),
    ("banner_marketing_aidly_blue.png", "render_banner_theme_blue.html"),
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
        print(f"Generating commercial banner: {out_name}...")
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"  -> Generated {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    generate()
