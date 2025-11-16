# Quick Start Guide

Get your blog up and running in 5 minutes!

## 1. Setup

```bash

# setup environment

source venv/bin/activate

# Install dependencies
pip install -r requirements.txt



# Customize your blog
# Edit config.yaml with your name and blog details
```

## 2. Create Posts

```bash
# Create a new post
python blog.py new "My First Real Post" --author "Your Name" --tags "personal,thoughts"

# Edit the generated .md file in the posts/ directory
```

## 3. Build & Preview

```bash
# Preview locally (automatically rebuilds with correct paths)
python blog.py serve
# Visit http://localhost:8000

# Or manually build for local testing
python build.py --local

# Build for deployment to GitHub Pages
python build.py
```

## 4. Deploy to GitHub Pages (Free!)

### Important: Update config.yaml first!

```yaml
base_url: "/your-repo-name/"  # e.g., "/mymusings/"
```

### Option A: Automatic (Recommended)

1. Push your code to GitHub
2. Go to Settings → Pages
3. Enable Pages with source: GitHub Actions
4. Push to main/master branch - site deploys automatically!

### Option B: Manual

```bash
# Run the deployment script
./deploy.sh
```

**Note**: Local testing uses `python blog.py serve` which automatically uses `/` as base_url. Deployment uses the `base_url` from config.yaml.

## 5. Start Writing!

That's it! Your blog is live and free forever.

### Tips:
- Posts are in `posts/*.md` format
- Use `python blog.py serve` for local testing (auto-rebuilds)
- Use `python build.py` for deployment builds
- Use Markdown for formatting
- Add images: `![alt](url)` or host in static/
- Optional comments: Enable in `config.yaml`
- Stuck server? `python blog.py serve` automatically kills orphaned processes on port 8000

### Costs:
- Hosting: **$0** (GitHub Pages/Netlify/Vercel)
- Domain: **$0** (use GitHub domain) or ~$10/year (custom)
- Total: **FREE** 🎉

Happy blogging!
