#!/usr/bin/env python3
"""
Meta Permanent Page Access Token Generator Helper
-------------------------------------------------
Automates the token exchange process to get a permanent (never-expiring)
Page Access Token and your Facebook Page ID.

Usage:
    python3 get_page_token.py
"""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API_VERSION = "v21.0"
GRAPH_BASE = f"https://graph.facebook.com/{API_VERSION}"


def make_get_request(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "FBTokenHelper/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        try:
            err_json = json.loads(error_body)
            msg = err_json.get("error", {}).get("message", error_body)
        except Exception:
            msg = error_body
        print(f"\n[!] Meta API Error (HTTP {e.code}): {msg}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] Network error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    print("=" * 65)
    print("   Meta Permanent Page Access Token Helper")
    print("=" * 65)
    print("\nPlease enter the details from your Meta Developer Portal:\n")

    app_id = input("1. Enter App ID: ").strip()
    if not app_id:
        print("[!] App ID cannot be empty.")
        sys.exit(1)

    app_secret = input("2. Enter App Secret: ").strip()
    if not app_secret:
        print("[!] App Secret cannot be empty.")
        sys.exit(1)

    short_token = input("3. Enter Short-Lived User Token (from Graph API Explorer): ").strip()
    if not short_token:
        print("[!] Token cannot be empty.")
        sys.exit(1)

    print("\n[*] Exchanging short-lived token for long-lived user token...")
    params = urllib.parse.urlencode({
        "grant_type": "fb_exchange_token",
        "client_id": app_id,
        "client_secret": app_secret,
        "fb_exchange_token": short_token,
    })
    exchange_url = f"{GRAPH_BASE}/oauth/access_token?{params}"
    token_resp = make_get_request(exchange_url)

    long_lived_token = token_resp.get("access_token")
    if not long_lived_token:
        print("[!] Failed to obtain long-lived token from Meta response.", file=sys.stderr)
        sys.exit(1)

    print("[+] Long-lived user token obtained successfully.")

    print("[*] Retrieving Pages, Permanent Page Access Tokens, and Connected Instagram Accounts...")
    accounts_url = f"{GRAPH_BASE}/me/accounts?{urllib.parse.urlencode({'access_token': long_lived_token, 'fields': 'id,name,access_token,instagram_business_account,page_backed_instagram_accounts,connected_instagram_account'})}"
    accounts_resp = make_get_request(accounts_url)

    pages = accounts_resp.get("data", [])
    if not pages:
        print("\n[!] No pages found for this user account.")
        print("    Ensure your user is an Admin of the Page and you approved:")
        print("    'pages_show_list', 'pages_read_engagement', 'pages_manage_posts',")
        print("    'instagram_basic', and 'instagram_content_publish'.")
        sys.exit(1)

    print("\n" + "=" * 65)
    print("                 YOUR GITHUB SECRETS")
    print("=" * 65)

    for idx, page in enumerate(pages, 1):
        name = page.get("name")
        page_id = page.get("id")
        page_token = page.get("access_token")

        # Discover Instagram Account ID
        ig_id = None
        ig_biz = page.get("instagram_business_account")
        if ig_biz and ig_biz.get("id"):
            ig_id = ig_biz.get("id")
        elif page.get("page_backed_instagram_accounts", {}).get("data"):
            ig_id = page["page_backed_instagram_accounts"]["data"][0].get("id")
        elif page.get("connected_instagram_account", {}).get("id"):
            ig_id = page["connected_instagram_account"]["id"]

        print(f"\n--- Page {idx}: {name} ---")
        print(f"Secret Name : FB_PAGE_ID")
        print(f"Secret Value: {page_id}\n")
        print(f"Secret Name : FB_PAGE_TOKEN")
        print(f"Secret Value: {page_token}\n")

        if ig_id:
            print(f"Secret Name : IG_ACCOUNT_ID")
            print(f"Secret Value: {ig_id}\n")
            print(f"[+] Connected Instagram Account ID: {ig_id}")
        else:
            print("[!] Note: No linked Instagram business/creator account detected.")

    print("\n" + "=" * 65)
    print("These Page Access Tokens DO NOT EXPIRE.")
    print("Add/Update FB_PAGE_ID, FB_PAGE_TOKEN, and IG_ACCOUNT_ID in your GitHub Secrets.")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    main()
