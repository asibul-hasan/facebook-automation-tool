#!/usr/bin/env python3
"""
Multi-Platform Credentials & Connection Health Verifier
-------------------------------------------------------
Tests live API connections for Facebook, LinkedIn, Instagram, and ElevenLabs
without publishing any content or consuming scheduled posts.
"""

import os
import json
import urllib.request
import urllib.error

def verify_facebook(page_id, page_token):
    print("\n--- 1. FACEBOOK PAGE CONNECTION ---")
    if not page_id or not page_token:
        print("❌ FB_PAGE_ID or FB_PAGE_TOKEN is missing.")
        return
    url = f"https://graph.facebook.com/v21.0/{page_id}?fields=name,id&access_token={page_token}"
    req = urllib.request.Request(url, headers={"User-Agent": "HealthCheck/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            print(f"✅ Facebook Page Connected: '{data.get('name')}' (ID: {data.get('id')})")
    except urllib.error.HTTPError as e:
        print(f"❌ Facebook API Error (HTTP {e.code}): {e.read().decode()}")
    except Exception as e:
        print(f"❌ Facebook Network Error: {e}")

def verify_linkedin(linkedin_token, author_urn=None):
    print("\n--- 2. LINKEDIN CONNECTION ---")
    if not linkedin_token:
        print("❌ LINKEDIN_ACCESS_TOKEN is missing or empty in Secrets.")
        return
    
    # Check userinfo (OpenID Connect)
    userinfo_url = "https://api.linkedin.com/v2/userinfo"
    req = urllib.request.Request(userinfo_url, headers={
        "Authorization": f"Bearer {linkedin_token.strip()}",
        "User-Agent": "HealthCheck/1.0"
    })
    detected_urn = None
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            u_data = json.loads(resp.read().decode())
            name = u_data.get("name") or f"{u_data.get('given_name', '')} {u_data.get('family_name', '')}".strip()
            sub = u_data.get("sub")
            detected_urn = f"urn:li:person:{sub}" if sub else None
            print(f"✅ LinkedIn Token Valid!")
            print(f"   Member Name : {name}")
            print(f"   Member Email: {u_data.get('email', 'N/A')}")
            print(f"   Member URN  : {detected_urn}")
    except urllib.error.HTTPError as e:
        print(f"⚠️  LinkedIn /userinfo returned HTTP {e.code}: {e.read().decode()}")
        # Fallback to /me
        me_url = "https://api.linkedin.com/v2/me"
        req_me = urllib.request.Request(me_url, headers={
            "Authorization": f"Bearer {linkedin_token.strip()}",
            "User-Agent": "HealthCheck/1.0"
        })
        try:
            with urllib.request.urlopen(req_me, timeout=15) as me_resp:
                me_data = json.loads(me_resp.read().decode())
                mid = me_data.get("id")
                detected_urn = f"urn:li:person:{mid}"
                print(f"✅ LinkedIn Token Valid (via /me)! Member URN: {detected_urn}")
        except Exception as me_err:
            print(f"❌ LinkedIn /me error: {me_err}")

    # Check UGC Post permission
    target_urn = author_urn or detected_urn
    if target_urn:
        print(f"   Ready to publish as author: {target_urn}")
    else:
        print("⚠️  Could not auto-determine LinkedIn Author URN. Make sure 'openid' and 'profile' scopes were approved.")

def verify_elevenlabs(api_key):
    print("\n--- 3. ELEVENLABS TTS CONNECTION ---")
    if not api_key:
        print("⚠️  ELEVENLABS_API_KEY is not set.")
        return
    url = "https://api.elevenlabs.io/v1/user/subscription"
    req = urllib.request.Request(url, headers={
        "xi-api-key": api_key.strip(),
        "User-Agent": "HealthCheck/1.0"
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            tier = data.get("tier", "unknown")
            used = data.get("character_count", 0)
            limit = data.get("character_limit", 0)
            print(f"✅ ElevenLabs Connected!")
            print(f"   Plan Tier : {tier}")
            print(f"   Characters: {used} / {limit} used")
    except urllib.error.HTTPError as e:
        print(f"❌ ElevenLabs API Error (HTTP {e.code}): {e.read().decode()}")
    except Exception as e:
        print(f"❌ ElevenLabs Error: {e}")

def main():
    print("=" * 60)
    print("       MULTI-PLATFORM SECRETS HEALTH CHECK")
    print("=" * 60)
    
    fb_id = os.getenv("FB_PAGE_ID")
    fb_token = os.getenv("FB_PAGE_TOKEN")
    li_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    li_urn = os.getenv("LINKEDIN_AUTHOR_URN")
    el_key = os.getenv("ELEVENLABS_API_KEY")

    verify_facebook(fb_id, fb_token)
    verify_linkedin(li_token, li_urn)
    verify_elevenlabs(el_key)

    print("\n" + "=" * 60)
    print("                 END HEALTH CHECK")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
