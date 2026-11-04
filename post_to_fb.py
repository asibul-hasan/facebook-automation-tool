#!/usr/bin/env python3
"""
Facebook Page Automated Posting Script
--------------------------------------
Publishes queued content from a local JSON file to a Meta Facebook Page
using the Meta Graph API v21.0.

Uses only Python standard libraries:
- urllib.request / urllib.parse / urllib.error
- json
- os
- sys
- logging
- datetime
"""

import json
import logging
import os
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
# Meta Graph API Integration
# ---------------------------------------------------------------------------
def publish_to_facebook(page_id: str, page_token: str, message: str, link: str | None = None) -> dict:
    """
    Publish a post to the Facebook Page feed via Graph API v21.0.
    
    Endpoint: POST https://graph.facebook.com/v21.0/{page_id}/feed
    """
    url = f"{GRAPH_API_BASE}/{page_id}/feed"

    form_payload = {
        "message": message,
        "access_token": page_token,
    }
    if link and link.strip():
        form_payload["link"] = link.strip()

    encoded_data = urllib.parse.urlencode(form_payload).encode("utf-8")

    request = urllib.request.Request(
        url=url,
        data=encoded_data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "AutomatedFBScheduler/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status_code = response.getcode()
            raw_body = response.read().decode("utf-8")
            response_json = json.loads(raw_body)
            logger.info("Facebook API responded with HTTP %d: %s", status_code, response_json)
            return response_json
    except urllib.error.HTTPError as http_err:
        error_detail = http_err.read().decode("utf-8", errors="replace")
        try:
            parsed_error = json.loads(error_detail)
            error_msg = parsed_error.get("error", {}).get("message", error_detail)
            error_code = parsed_error.get("error", {}).get("code", "unknown")
            error_subcode = parsed_error.get("error", {}).get("error_subcode", "none")
            logger.error(
                "Facebook Graph API Error (HTTP %d, Code: %s, Subcode: %s): %s",
                http_err.code,
                error_code,
                error_subcode,
                error_msg,
            )
        except json.JSONDecodeError:
            logger.error("Facebook API Error HTTP %d: %s", http_err.code, error_detail)
        sys.exit(1)
    except urllib.error.URLError as url_err:
        logger.error("Network connection error reaching Facebook API: %s", url_err.reason)
        sys.exit(1)
    except TimeoutError:
        logger.error("Request to Facebook Graph API timed out after 30 seconds.")
        sys.exit(1)


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
    message = target_post.get("message")
    link = target_post.get("link")

    if not message:
        logger.error("Post (ID: %s) has no 'message' field or message is empty.", post_id)
        sys.exit(1)

    logger.info("Found unpublished post (ID: %s). Publishing to Page %s...", post_id, page_id)
    api_result = publish_to_facebook(
        page_id=page_id,
        page_token=page_token,
        message=message,
        link=link,
    )

    published_id = api_result.get("id", "unknown_id")
    target_post["published"] = True
    target_post["facebook_post_id"] = published_id
    target_post["published_at"] = datetime.now(timezone.utc).isoformat()
    posts[target_index] = target_post

    save_posts(posts_filepath, posts)
    logger.info(
        "Successfully published post (ID: %s) as Facebook post ID: %s",
        post_id,
        published_id,
    )


if __name__ == "__main__":
    main()
