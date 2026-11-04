# Automated Facebook Page Posting Pipeline

A 100% free, serverless, automated social media pipeline that publishes scheduled content to a Meta Facebook Page using **Python** (standard library only) and **GitHub Actions**.

---

## 🚀 Features

- **Zero Third-Party Dependencies:** Uses purely Python standard libraries (`urllib.request`, `json`, `os`, `sys`). No `pip install` required.
- **Serverless & 100% Free:** Orchestrated via GitHub Actions cron schedules.
- **Automated Queue Management:** Sequentially reads posts from `posts.json`, publishes the next unpublished post, updates `published: true` with Facebook post ID and timestamp, and commits the state back to the repository.
- **Loop-Safe & Atomic:** Uses atomic file writes, fast-forward checks (`git pull --rebase`), and `[skip ci]` to prevent recursive workflow runs.
- **Meta Graph API v21.0:** Fully compatible with latest Meta endpoints and permanent Page Access Tokens.

---

## 📁 Repository Structure

```text
├── .github/
│   └── workflows/
│       └── scheduler.yml    # GitHub Actions workflow (runs at 04:00 & 14:00 UTC)
├── post_to_fb.py            # Publisher engine using Python standard library
├── posts.json               # Content queue file
├── get_page_token.py        # Token exchange utility (exchanges short-lived token for permanent token)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Configuration

### 1. Configure GitHub Actions Workflow Permissions
1. Go to repository **Settings** > **Actions** > **General**.
2. Under **Workflow permissions**, select **"Read and write permissions"**.
3. Click **Save**.

### 2. Configure Repository Secrets
Go to **Settings** > **Secrets and variables** > **Actions** > **New repository secret**:

| Secret Name | Description |
|---|---|
| `FB_PAGE_ID` | Your Facebook Page ID |
| `FB_PAGE_TOKEN` | Permanent (never-expiring) Page Access Token |

---

## 📝 Managing the Queue (`posts.json`)

To schedule new posts, simply edit `posts.json`:

```json
[
  {
    "id": "post_001",
    "message": "🚀 Excited to announce our new open-source automation toolkit!",
    "link": "https://example.com/blog/automation-toolkit",
    "published": false
  },
  {
    "id": "post_002",
    "message": "💡 DevOps Tip: Always treat infrastructure as code.",
    "link": "https://example.com/devops-tips",
    "published": false
  }
]
```

When a post is published, the bot automatically appends `facebook_post_id`, `published_at`, and flips `"published": true`.

---

## ⏰ Schedule

The GitHub Action is scheduled to run twice daily at **04:00 UTC** and **14:00 UTC**:
```yaml
schedule:
  - cron: '0 4,14 * * *'
```
You can also trigger a manual run anytime from the **Actions** tab using the **Run workflow** button.
