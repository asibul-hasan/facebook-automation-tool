#!/usr/bin/env python3
"""
Facebook Page Automated Posting Script (Professional Media Edition)
--------------------------------------------------------------------
Publishes high-converting, spicy posts directly to the Facebook Page Timeline
Feed with full-width, eye-catching visual banners and Unicode bold formatting.

Features:
1. Two-Step Attached Media Upload:
   - Uploads high-res image to POST /{page_id}/photos as published=false
   - Attaches media to POST /{page_id}/feed with attached_media
   - Result: 100% full-width, edge-to-edge timeline photo post on the public wall!
2. Facebook Markdown Engine:
   - Automatically converts **bold text** into genuine Unicode Sans-Serif Bold
     characters so headlines and power words appear BOLD directly in the FB feed!
3. Fallback to standard feed post if no image URL is provided.

Uses strictly Python standard libraries (no third-party dependencies):
- urllib.request / urllib.parse / urllib.error
- json, re, os, sys, logging, datetime
"""

import json
import logging
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Configuration & Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("fb_scheduler")

API_VERSION = "v21.0"
GRAPH_API_BASE = f"https://graph.facebook.com/{API_VERSION}"
DEFAULT_POSTS_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "posts.json"
)


def get_required_env(var_name: str) -> str:
    """Retrieve an environment variable or abort execution."""
    value = os.getenv(var_name)
    if not value or not value.strip():
        logger.error("Missing required environment variable: '%s'", var_name)
        sys.exit(1)
    return value.strip()


# ---------------------------------------------------------------------------
# Facebook Typography Engine (Unicode Bold Renderer)
# ---------------------------------------------------------------------------
def _to_unicode_bold(text: str) -> str:
    """Converts standard Latin alphanumeric text into Unicode Sans-Serif Bold."""
    chars = []
    for char in text:
        code = ord(char)
        if 65 <= code <= 90:  # A-Z
            chars.append(chr(0x1D5D4 + (code - 65)))
        elif 97 <= code <= 122:  # a-z
            chars.append(chr(0x1D5EE + (code - 97)))
        elif 48 <= code <= 57:  # 0-9
            chars.append(chr(0x1D7EC + (code - 48)))
        else:
            chars.append(char)
    return "".join(chars)


def render_facebook_markdown(text: str) -> str:
    """Converts **bold markers** into real bold typography for Facebook."""
    return re.sub(r"\*\*(.+?)\*\*", lambda m: _to_unicode_bold(m.group(1)), text)


# ---------------------------------------------------------------------------
# Storage Layer
# ---------------------------------------------------------------------------
def load_posts(filepath: str) -> list[dict]:
    """Load the JSON queue file and validate format."""
    if not os.path.exists(filepath):
        logger.error("Posts file not found at: %s", filepath)
        sys.exit(1)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                logger.error("Invalid posts format: root element must be a list of post objects.")
                sys.exit(1)
            return data
    except json.JSONDecodeError as err:
        logger.error("Failed to parse JSON file '%s': %s", filepath, err)
        sys.exit(1)
    except OSError as err:
        logger.error("I/O error reading '%s': %s", filepath, err)
        sys.exit(1)


def save_posts(filepath: str, posts: list[dict]) -> None:
    """Write updated posts array back to JSON atomically."""
    temp_file = f"{filepath}.tmp"
    try:
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(temp_file, filepath)
        logger.info("Successfully updated '%s'.", filepath)
    except OSError as err:
        logger.error("Failed to write to '%s': %s", filepath, err)
        if os.path.exists(temp_file):
            os.remove(temp_file)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Meta Graph API Integration (Two-Step Full Banner Publishing)
# ---------------------------------------------------------------------------
def publish_timeline_photo_post(
    page_id: str,
    page_token: str,
    message: str,
    image_url: str,
) -> dict:
    """
    Publishes a full-width high-res banner directly onto the Page Timeline Feed.
    Supports both local image files (uploaded via multipart/form-data) and remote HTTP URLs.
    Step 1: Upload image as unpublished media (POST /{page_id}/photos)
    Step 2: Create public timeline story with attached_media (POST /{page_id}/feed)
    """
    photo_endpoint = f"{GRAPH_API_BASE}/{page_id}/photos"
    
    # Check if image_url points to a local file
    resolved_path = None
    if not (image_url.startswith("http://") or image_url.startswith("https://")):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        cand1 = os.path.join(base_dir, image_url)
        cand2 = os.path.abspath(image_url)
        if os.path.exists(cand1):
            resolved_path = cand1
        elif os.path.exists(cand2):
            resolved_path = cand2
        else:
            logger.warning("Local banner file '%s' not found, falling back to URL mode.", image_url)

    if resolved_path and os.path.isfile(resolved_path):
        logger.info("Step 1: Uploading local high-res banner '%s' via multipart to Meta...", resolved_path)
        boundary = "----WebKitFormBoundary" + os.urandom(16).hex()
        body = bytearray()
        
        for name, val in [("access_token", page_token), ("published", "false")]:
            body.extend(f"--{boundary}\r\n".encode())
            body.extend(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
            body.extend(f"{val}\r\n".encode())
            
        filename = os.path.basename(resolved_path)
        mime_type = "image/jpeg" if filename.lower().endswith((".jpg", ".jpeg")) else "image/png"
        body.extend(f"--{boundary}\r\n".encode())
        body.extend(f'Content-Disposition: form-data; name="source"; filename="{filename}"\r\n'.encode())
        body.extend(f"Content-Type: {mime_type}\r\n\r\n".encode())
        with open(resolved_path, "rb") as f:
            body.extend(f.read())
        body.extend(b"\r\n")
        body.extend(f"--{boundary}--\r\n".encode())
        
        req1 = urllib.request.Request(
            url=photo_endpoint,
            data=body,
            headers={
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "User-Agent": "AutomatedFBScheduler/4.0",
            },
            method="POST",
        )
    else:
        logger.info("Step 1: Uploading remote banner URL to Meta servers: %s", image_url)
        photo_payload = urllib.parse.urlencode({
            "url": image_url.strip(),
            "published": "false",
            "access_token": page_token,
        }).encode("utf-8")

        req1 = urllib.request.Request(
            url=photo_endpoint,
            data=photo_payload,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "AutomatedFBScheduler/4.0",
            },
            method="POST",
        )

    try:
        with urllib.request.urlopen(req1, timeout=60) as resp1:
            photo_result = json.loads(resp1.read().decode("utf-8"))
            media_fbid = photo_result.get("id")
            logger.info("Banner uploaded successfully (Media FBID: %s).", media_fbid)
    except urllib.error.HTTPError as http_err:
        err_body = http_err.read().decode("utf-8", errors="replace")
        logger.error("Failed to upload banner photo (HTTP %d): %s", http_err.code, err_body)
        sys.exit(1)

    # Step 2: Publish public timeline feed post with attached banner
    logger.info("Step 2: Creating full-width timeline post on Page wall...")
    feed_endpoint = f"{GRAPH_API_BASE}/{page_id}/feed"
    feed_payload = urllib.parse.urlencode({
        "message": message,
        "attached_media": json.dumps([{"media_fbid": media_fbid}]),
        "access_token": page_token,
        "published": "true",
    }).encode("utf-8")

    req2 = urllib.request.Request(
        url=feed_endpoint,
        data=feed_payload,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "AutomatedFBScheduler/4.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req2, timeout=45) as resp2:
            feed_result = json.loads(resp2.read().decode("utf-8"))
            logger.info("Facebook Timeline Post Published: %s", feed_result)
            return feed_result
    except urllib.error.HTTPError as http_err:
        err_body = http_err.read().decode("utf-8", errors="replace")
        logger.error("Failed to publish timeline feed post (HTTP %d): %s", http_err.code, err_body)
        sys.exit(1)


def publish_timeline_video_post(
    page_id: str,
    page_token: str,
    description: str,
    video_path: str,
    title: str = "Aidly PMS · Smart Pharmacy ERP & POS",
) -> dict:
    """
    Publishes an MP4 video directly to the Facebook Page Timeline.
    Uses POST /{page_id}/videos with multipart/form-data.
    """
    video_endpoint = f"{GRAPH_API_BASE}/{page_id}/videos"
    logger.info("Uploading video file '%s' to Facebook Page %s...", video_path, page_id)

    boundary = "----WebKitFormBoundary" + os.urandom(16).hex()
    body = bytearray()

    fields = [
        ("access_token", page_token),
        ("description", description),
        ("title", title),
    ]
    for name, val in fields:
        body.extend(f"--{boundary}\r\n".encode())
        body.extend(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
        body.extend(f"{val}\r\n".encode())

    filename = os.path.basename(video_path)
    body.extend(f"--{boundary}\r\n".encode())
    body.extend(f'Content-Disposition: form-data; name="source"; filename="{filename}"\r\n'.encode())
    body.extend(b"Content-Type: video/mp4\r\n\r\n")
    with open(video_path, "rb") as f:
        body.extend(f.read())
    body.extend(b"\r\n")
    body.extend(f"--{boundary}--\r\n".encode())

    req = urllib.request.Request(
        url=video_endpoint,
        data=body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "User-Agent": "AutomatedFBScheduler/4.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            video_result = json.loads(resp.read().decode("utf-8"))
            logger.info("Facebook Timeline Video Published successfully: %s", video_result)
            return video_result
    except urllib.error.HTTPError as http_err:
        err_body = http_err.read().decode("utf-8", errors="replace")
        logger.error("Failed to upload video to Facebook (HTTP %d): %s", http_err.code, err_body)
        sys.exit(1)


def publish_timeline_feed_post(
    page_id: str,
    page_token: str,
    message: str,
    link: str | None = None,
) -> dict:
    """Standard feed post fallback when no banner image is provided."""
    url = f"{GRAPH_API_BASE}/{page_id}/feed"
    payload = {
        "message": message,
        "access_token": page_token,
        "published": "true",
    }
    if link and link.strip():
        payload["link"] = link.strip()

    encoded_data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(
        url=url,
        data=encoded_data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "AutomatedFBScheduler/4.0",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode("utf-8"))


# ---------------------------------------------------------------------------
# LinkedIn Integration (Community Management & Share API)
# ---------------------------------------------------------------------------
LINKEDIN_API_BASE = "https://api.linkedin.com/v2"


def get_linkedin_author_urn(linkedin_token: str) -> str:
    """Discover member URN if not manually provided via LINKEDIN_AUTHOR_URN."""
    # Attempt 1: OpenID userinfo
    try:
        url = "https://api.linkedin.com/v2/userinfo"
        req = urllib.request.Request(
            url=url,
            headers={
                "Authorization": f"Bearer {linkedin_token}",
                "User-Agent": "CrossPlatformScheduler/4.0",
            },
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            sub = data.get("sub")
            if sub:
                return f"urn:li:person:{sub}"
    except Exception as e:
        logger.warning("Could not fetch userinfo via OpenID: %s. Trying /v2/me...", e)

    # Attempt 2: Legacy /v2/me
    try:
        req2 = urllib.request.Request(
            url=f"{LINKEDIN_API_BASE}/me",
            headers={
                "Authorization": f"Bearer {linkedin_token}",
                "User-Agent": "CrossPlatformScheduler/4.0",
            },
            method="GET",
        )
        with urllib.request.urlopen(req2, timeout=20) as resp2:
            data2 = json.loads(resp2.read().decode("utf-8"))
            person_id = data2.get("id")
            if person_id:
                return f"urn:li:person:{person_id}"
    except Exception as e2:
        logger.error("Failed to determine LinkedIn author URN: %s", e2)

    return ""


def upload_linkedin_image(linkedin_token: str, author_urn: str, image_path: str) -> str:
    """Registers and uploads an image to LinkedIn Assets API, returning asset URN."""
    register_url = f"{LINKEDIN_API_BASE}/assets?action=registerUpload"
    payload = {
        "registerUploadRequest": {
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
            "owner": author_urn,
            "serviceRelationships": [
                {
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent",
                }
            ],
        }
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url=register_url,
        data=data,
        headers={
            "Authorization": f"Bearer {linkedin_token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
            "User-Agent": "CrossPlatformScheduler/4.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        res = json.loads(resp.read().decode("utf-8"))

    upload_mechanism = res["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]
    upload_url = upload_mechanism["uploadUrl"]
    asset_urn = res["value"]["asset"]

    with open(image_path, "rb") as f:
        img_bytes = f.read()

    mime_type = "image/jpeg" if image_path.lower().endswith((".jpg", ".jpeg")) else "image/png"
    upload_req = urllib.request.Request(
        url=upload_url,
        data=img_bytes,
        headers={
            "Authorization": f"Bearer {linkedin_token}",
            "Content-Type": mime_type,
        },
        method="PUT",
    )
    with urllib.request.urlopen(upload_req, timeout=60) as resp:
        pass

    return asset_urn


def publish_linkedin_post(
    linkedin_token: str,
    message: str,
    image_path: str | None = None,
    author_urn: str | None = None,
) -> dict | None:
    """Publishes a text or image post directly to LinkedIn."""
    try:
        if not author_urn:
            author_urn = os.getenv("LINKEDIN_AUTHOR_URN")
        if not author_urn:
            author_urn = get_linkedin_author_urn(linkedin_token)

        if not author_urn:
            logger.warning("No LinkedIn author URN found. Skipping LinkedIn publishing.")
            return None

        logger.info("Publishing to LinkedIn as %s...", author_urn)

        asset_urn = None
        if image_path and os.path.exists(image_path) and not image_path.lower().endswith(".mp4"):
            try:
                asset_urn = upload_linkedin_image(linkedin_token, author_urn, image_path)
            except Exception as e:
                logger.warning("Failed to upload image to LinkedIn, falling back to text: %s", e)

        if asset_urn:
            media_block = [{
                "status": "READY",
                "description": {"text": "Info AidTech & Aidly PMS Update"},
                "media": asset_urn,
                "title": {"text": "Info AidTech"},
            }]
            share_media_category = "IMAGE"
        else:
            media_block = []
            share_media_category = "NONE"

        ugc_payload = {
            "author": author_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": message},
                    "shareMediaCategory": share_media_category,
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        }
        if media_block:
            ugc_payload["specificContent"]["com.linkedin.ugc.ShareContent"]["media"] = media_block

        ugc_url = f"{LINKEDIN_API_BASE}/ugcPosts"
        req = urllib.request.Request(
            url=ugc_url,
            data=json.dumps(ugc_payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {linkedin_token}",
                "Content-Type": "application/json",
                "X-Restli-Protocol-Version": "2.0.0",
                "User-Agent": "CrossPlatformScheduler/4.0",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=45) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            post_urn = res.get("id")
            logger.info("LinkedIn Post Published successfully: %s", post_urn)
            return res
    except Exception as err:
        logger.error("Error publishing to LinkedIn: %s", err)
        return None


# ---------------------------------------------------------------------------
# Instagram Integration (via Meta Graph API)
# ---------------------------------------------------------------------------
def get_instagram_account_id(page_id: str, page_token: str) -> str | None:
    """Fetch the connected Instagram Business/Creator Account ID for the Facebook Page."""
    # 1. Environment variable override
    env_ig_id = os.getenv("IG_ACCOUNT_ID") or os.getenv("INSTAGRAM_ACCOUNT_ID")
    if env_ig_id and env_ig_id.strip():
        logger.info("Using configured IG_ACCOUNT_ID from environment: %s", env_ig_id.strip())
        return env_ig_id.strip()

    # 2. Query Meta Graph API for connected Instagram accounts
    fields = "instagram_business_account,page_backed_instagram_accounts,connected_instagram_account"
    url = f"{GRAPH_API_BASE}/{page_id}?fields={fields}&access_token={page_token}"
    req = urllib.request.Request(url=url, headers={"User-Agent": "CrossPlatformScheduler/4.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))

            # Check standard Instagram Business/Creator Account
            ig_biz = data.get("instagram_business_account")
            if ig_biz and ig_biz.get("id"):
                logger.info("Found connected Instagram Business Account: %s", ig_biz.get("id"))
                return ig_biz.get("id")

            # Check Page-backed Instagram accounts
            pbia = data.get("page_backed_instagram_accounts", {}).get("data", [])
            if pbia and pbia[0].get("id"):
                logger.info("Found Page-Backed Instagram Account: %s", pbia[0].get("id"))
                return pbia[0].get("id")

            # Check connected instagram account
            cia = data.get("connected_instagram_account")
            if cia and cia.get("id"):
                logger.info("Found connected Instagram Account: %s", cia.get("id"))
                return cia.get("id")

            logger.warning("No linked Instagram account found on Facebook Page %s.", page_id)
    except Exception as e:
        logger.warning("Could not query Instagram account fields from Meta Graph API: %s", e)
    return None


def publish_instagram_post(
    ig_user_id: str,
    page_token: str,
    caption: str,
    media_relative_path: str,
) -> dict | None:
    """Publishes an image or Reel to Instagram Business Account via Meta Graph API."""
    try:
        import time
        repo = os.getenv("GITHUB_REPOSITORY", "asibul-hasan/facebook-automation-tool")
        public_url = f"https://raw.githubusercontent.com/{repo}/main/{media_relative_path}"

        is_video = media_relative_path.lower().endswith(".mp4")
        media_url = f"{GRAPH_API_BASE}/{ig_user_id}/media"

        if is_video:
            logger.info("Creating Instagram Reel container for: %s (URL: %s)", media_relative_path, public_url)
            payload = {
                "media_type": "REELS",
                "video_url": public_url,
                "caption": caption,
                "access_token": page_token,
            }
        else:
            logger.info("Creating Instagram Photo container for: %s (URL: %s)", media_relative_path, public_url)
            payload = {
                "image_url": public_url,
                "caption": caption,
                "access_token": page_token,
            }

        encoded = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(
            url=media_url,
            data=encoded,
            headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "CrossPlatformScheduler/4.0"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                creation_res = json.loads(resp.read().decode("utf-8"))
                creation_id = creation_res.get("id")
        except urllib.error.HTTPError as err:
            err_body = err.read().decode("utf-8", errors="replace")
            logger.error("Failed to create Instagram media container (HTTP %d): %s", err.code, err_body)
            return None

        if not creation_id:
            logger.warning("No creation_id received from Instagram for %s.", media_relative_path)
            return None

        if is_video:
            logger.info("Polling Instagram Reel transcoding status for container %s...", creation_id)
            status_url = f"{GRAPH_API_BASE}/{creation_id}?fields=status_code,status&access_token={page_token}"
            poll_req = urllib.request.Request(url=status_url, headers={"User-Agent": "CrossPlatformScheduler/4.0"})
            for attempt in range(1, 19):
                time.sleep(5)
                try:
                    with urllib.request.urlopen(poll_req, timeout=20) as status_resp:
                        status_data = json.loads(status_resp.read().decode("utf-8"))
                        status_code = status_data.get("status_code")
                        logger.info("Instagram Reel status [Attempt %d/18]: %s", attempt, status_code)
                        if status_code == "FINISHED":
                            break
                        elif status_code in ("ERROR", "EXPIRED"):
                            logger.error("Instagram Reel processing failed: %s", status_data)
                            return None
                except Exception as pe:
                    logger.warning("Could not check container status on attempt %d: %s", attempt, pe)

        publish_url = f"{GRAPH_API_BASE}/{ig_user_id}/media_publish"
        pub_payload = urllib.parse.urlencode({
            "creation_id": creation_id,
            "access_token": page_token,
        }).encode("utf-8")
        pub_req = urllib.request.Request(
            url=publish_url,
            data=pub_payload,
            headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "CrossPlatformScheduler/4.0"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(pub_req, timeout=45) as pub_resp:
                pub_res = json.loads(pub_resp.read().decode("utf-8"))
                logger.info("Instagram Post Published successfully: %s", pub_res)
                return pub_res
        except urllib.error.HTTPError as err:
            err_body = err.read().decode("utf-8", errors="replace")
            logger.error("Failed to publish Instagram media container (HTTP %d): %s", err.code, err_body)
            return None
    except Exception as e:
        logger.warning("Could not publish to Instagram: %s", e)
        return None


# ---------------------------------------------------------------------------
# Main Orchestration Loop
# ---------------------------------------------------------------------------
def main():
    posts_filepath = os.getenv("POSTS_FILE_PATH", DEFAULT_POSTS_FILE)
    page_id = get_required_env("FB_PAGE_ID")
    page_token = get_required_env("FB_PAGE_TOKEN")

    logger.info("Starting Facebook post publisher run.")
    posts = load_posts(posts_filepath)

    target_index = None
    target_post = None

    for idx, post in enumerate(posts):
        if not post.get("published", False):
            target_index = idx
            target_post = post
            break

    if target_post is None:
        logger.info("Queue clean: No unpublished posts found in '%s'. Exiting.", posts_filepath)
        sys.exit(0)

    post_id = target_post.get("id", f"index_{target_index}")
    category = target_post.get("category", "General")
    raw_message = target_post.get("message", "")
    link = target_post.get("link")
    image_url = target_post.get("image_url")

    if not raw_message.strip():
        logger.error("Post (ID: %s) has no 'message' field or message is empty.", post_id)
        sys.exit(1)

    # Render genuine Unicode Bold characters from markdown **bold**
    formatted_message = render_facebook_markdown(raw_message.strip())

    logger.info(
        "Publishing [ID: %s | Category: %s] as Full-Width Banner Timeline Post to Page %s...",
        post_id,
        category,
        page_id,
    )

    if image_url and image_url.strip().lower().endswith(".mp4"):
        resolved_video = image_url.strip()
        if not os.path.isabs(resolved_video):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            cand = os.path.join(base_dir, resolved_video)
            if os.path.exists(cand):
                resolved_video = cand
        api_result = publish_timeline_video_post(
            page_id=page_id,
            page_token=page_token,
            description=formatted_message,
            video_path=resolved_video,
            title=f"Aidly PMS · {category}",
        )
    elif image_url and image_url.strip():
        api_result = publish_timeline_photo_post(
            page_id=page_id,
            page_token=page_token,
            message=formatted_message,
            image_url=image_url.strip(),
        )
    else:
        api_result = publish_timeline_feed_post(
            page_id=page_id,
            page_token=page_token,
            message=formatted_message,
            link=link,
        )

    published_id = api_result.get("id", "unknown_id")
    target_post["published"] = True
    target_post["facebook_post_id"] = published_id
    target_post["published_at"] = datetime.now(timezone.utc).isoformat()

    # -----------------------------------------------------------------------
    # Step 3: Multi-Platform Cross-Posting (LinkedIn)
    # -----------------------------------------------------------------------
    linkedin_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    if linkedin_token and linkedin_token.strip():
        resolved_image = None
        if image_url and not image_url.strip().lower().endswith(".mp4"):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            cand1 = os.path.join(base_dir, image_url.strip())
            if os.path.exists(cand1):
                resolved_image = cand1
            elif os.path.exists(image_url.strip()):
                resolved_image = os.path.abspath(image_url.strip())

        logger.info("Triggering LinkedIn cross-post for post ID: %s...", post_id)
        li_result = publish_linkedin_post(
            linkedin_token=linkedin_token.strip(),
            message=formatted_message,
            image_path=resolved_image,
        )
        if li_result:
            target_post["linkedin_post_id"] = li_result.get("id")
    else:
        logger.info("LinkedIn cross-posting skipped (LINKEDIN_ACCESS_TOKEN not set).")

    # -----------------------------------------------------------------------
    # Step 4: Multi-Platform Cross-Posting (Instagram)
    # -----------------------------------------------------------------------
    ig_account_id = get_instagram_account_id(page_id=page_id, page_token=page_token)
    if ig_account_id and image_url and image_url.strip():
        logger.info("Triggering Instagram cross-post for IG Account %s...", ig_account_id)
        ig_result = publish_instagram_post(
            ig_user_id=ig_account_id,
            page_token=page_token,
            caption=formatted_message,
            media_relative_path=image_url.strip(),
        )
        if ig_result:
            target_post["instagram_post_id"] = ig_result.get("id")
    else:
        logger.info("Instagram cross-posting skipped (No connected Instagram business account or no media).")

    posts[target_index] = target_post
    save_posts(posts_filepath, posts)
    logger.info("Successfully finished multi-platform publishing cycle for post ID: %s", post_id)


if __name__ == "__main__":
    main()
