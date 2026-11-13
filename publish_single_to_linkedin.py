#!/usr/bin/env python3
"""
Publish a Specific Post Directly to LinkedIn
---------------------------------------------
Publishes an existing post from posts.json (by ID or default to last published post)
directly to LinkedIn using LINKEDIN_ACCESS_TOKEN.
"""

import os
import sys
import json
import logging
from datetime import datetime, timezone
from post_to_fb import (
    load_posts,
    save_posts,
    publish_linkedin_post,
    publish_buffer_post,
    render_facebook_markdown,
    DEFAULT_POSTS_FILE,
    load_env_local
)

load_env_local()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("linkedin_publisher")

def main():
    target_id = sys.argv[1] if len(sys.argv) > 1 else "day1_slot1_agency_roi_funnel"
    buffer_token = os.getenv("BUFFER_ACCESS_TOKEN")
    linkedin_token = os.getenv("LINKEDIN_ACCESS_TOKEN")

    if not buffer_token and not linkedin_token:
        logger.error("Neither BUFFER_ACCESS_TOKEN nor LINKEDIN_ACCESS_TOKEN is set. Please set at least one in GitHub Secrets or environment.")
        sys.exit(1)

    posts_file = os.getenv("POSTS_FILE_PATH", DEFAULT_POSTS_FILE)
    posts = load_posts(posts_file)

    target_index = None
    target_post = None

    for idx, p in enumerate(posts):
        if p.get("id") == target_id:
            target_index = idx
            target_post = p
            break

    if target_post is None:
        logger.error("Post with ID '%s' not found in %s", target_id, posts_file)
        sys.exit(1)

    logger.info("Found target post: %s (Topic: %s)", target_id, target_post.get("topic"))

    raw_message = target_post.get("message", "")
    image_url = target_post.get("image_url")
    formatted_message = render_facebook_markdown(raw_message.strip())

    if buffer_token and buffer_token.strip():
        logger.info("Publishing '%s' to LinkedIn Company Page via Buffer...", target_id)
        res = publish_buffer_post(
            buffer_token=buffer_token.strip(),
            text=formatted_message,
            media_relative_path=image_url,
        )
        if not res:
            logger.error("Failed to publish post '%s' via Buffer.", target_id)
            sys.exit(1)
        post_urn = res.get("id") or (res.get("updates", [{}])[0].get("id")) or "buffer_success"
        target_post["buffer_update_id"] = post_urn
    else:
        resolved_image = None
        if image_url and not image_url.strip().lower().endswith(".mp4"):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            cand1 = os.path.join(base_dir, image_url.strip())
            if os.path.exists(cand1):
                resolved_image = cand1
            elif os.path.exists(image_url.strip()):
                resolved_image = os.path.abspath(image_url.strip())

        logger.info("Publishing '%s' to LinkedIn (Direct API, Image: %s)...", target_id, resolved_image)
        res = publish_linkedin_post(
            linkedin_token=linkedin_token.strip(),
            message=formatted_message,
            image_path=resolved_image,
        )
        if not res:
            logger.error("Failed to publish post '%s' to LinkedIn.", target_id)
            sys.exit(1)
        post_urn = res.get("id", "urn:li:share:unknown")

    target_post["linkedin_post_id"] = post_urn
    target_post["linkedin_published_at"] = datetime.now(timezone.utc).isoformat()
    posts[target_index] = target_post
    save_posts(posts_file, posts)

    logger.info("🎉 SUCCESS! Post '%s' published to LinkedIn with ID: %s", target_id, post_urn)

if __name__ == "__main__":
    main()
