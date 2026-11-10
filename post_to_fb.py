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
    Step 1: Upload image as unpublished media (POST /{page_id}/photos)
    Step 2: Create public timeline story with attached_media (POST /{page_id}/feed)
    """
    logger.info("Step 1: Uploading high-res banner image to Meta servers...")
    photo_endpoint = f"{GRAPH_API_BASE}/{page_id}/photos"
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
        with urllib.request.urlopen(req1, timeout=45) as resp1:
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

    if image_url and image_url.strip():
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
    posts[target_index] = target_post

    save_posts(posts_filepath, posts)
    logger.info(
        "Successfully published post (ID: %s) as Full-Width Timeline Post: %s",
        post_id,
        published_id,
    )


if __name__ == "__main__":
    main()
