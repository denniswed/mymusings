# Quick Start Guide

Get your blog up and running in 5 minutes!

## 1. Setup (One-time)

```bash
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
# Generate the static site
python build.py

# Preview locally
python blog.py serve
# Visit http://localhost:8000
```

## 4. Deploy to GitHub Pages (Free!)

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

## 5. Start Writing!

That's it! Your blog is live and free forever.

### Tips:
- Posts are in `posts/*.md` format
- Rebuild after changes: `python build.py`
- Use Markdown for formatting
- Add images: `![alt](url)` or host in static/
- Optional comments: Enable in `config.yaml`

### Costs:
- Hosting: **$0** (GitHub Pages/Netlify/Vercel)
- Domain: **$0** (use GitHub domain) or ~$10/year (custom)
- Total: **FREE** 🎉

Happy blogging!
