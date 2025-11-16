# My Musings 📝

A simple, lightweight static blog generator for your thoughts and musings. Built with Python, designed for ease of use and free hosting.

## Features

- 🚀 **Simple**: Write posts in Markdown, generate static HTML
- 💰 **Free Hosting**: Deploy to GitHub Pages, Netlify, or Vercel for free
- 🎨 **Clean Design**: Responsive, readable layout
- 💬 **Optional Comments**: Integrate GitHub-based commenting (Utterances)
- 🐍 **Python-based**: Easy to customize and extend

## Quick Start

### 1. Installation

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Configuration

Edit `config.yaml` to customize your blog:

```yaml
blog_title: "My Musings"
blog_description: "A blog, a diary, a place to puke my thoughts"
author: "Your Name"
```

### 3. Create Your First Post

Use the CLI tool to create a new post:

```bash
python blog.py new "My First Post" --author "Your Name" --tags "intro,personal"
```

Or manually create a Markdown file in the `posts/` directory with this format:

```markdown
---
title: "Your Post Title"
date: 2024-01-15
author: Your Name
tags: [tag1, tag2]
---

# Your Post Title

Write your content here using Markdown...
```

### 4. Build Your Blog

Generate the static site:

```bash
# For local testing (uses base_url: "/")
python build.py --local

# For deployment to GitHub Pages (uses base_url: "/mymusings/")
python build.py
```

This creates the `output/` directory with your complete static site.

### 5. Preview Locally

Start a local server to preview your blog:

```bash
python blog.py serve
```

This automatically:
- Rebuilds the site with `--local` flag for correct paths
- Kills any orphaned processes on port 8000
- Starts the server at http://localhost:8000

Open http://localhost:8000 in your browser to see your blog.

## CLI Commands

```bash
# Create a new post
python blog.py new "Post Title" --author "Name" --tags "tag1,tag2"

# List all posts
python blog.py list

# Build for local testing
python build.py --local

# Build for deployment
python build.py

# Preview blog locally (auto-rebuilds with --local)
python blog.py serve --port 8000
```

## Deployment Options

Your blog is just static HTML files, making it **free and easy to deploy**:

### GitHub Pages (Recommended - FREE)

1. Create a new repository or use this one
2. Update `config.yaml` with your repository name:
   ```yaml
   base_url: "/repo-name/"  # e.g., "/mymusings/"
   ```
3. Add the included GitHub Actions workflow (`.github/workflows/deploy.yml`)
4. Push to main branch - site deploys automatically!
5. Enable GitHub Pages in repository settings (source: GitHub Actions)
6. Your blog will be live at `https://username.github.io/repo-name`

**Note**: The `base_url` in `config.yaml` should match your repository name for GitHub Pages. Use `--local` flag when building for local testing.

**Automated Deployment Script:**

```bash
# Build the site
python build.py

# Deploy to GitHub Pages
cd output
git init
git add .
git commit -m "Deploy blog"
git branch -M gh-pages
git remote add origin https://github.com/username/repo-name.git
git push -f origin gh-pages
```

### Netlify (FREE)

1. Sign up at [netlify.com](https://netlify.com)
2. Connect your repository
3. Set build command: `python build.py`
4. Set publish directory: `output`
5. Deploy!

### Vercel (FREE)

1. Sign up at [vercel.com](https://vercel.com)
2. Import your repository
3. Framework: Other
4. Build command: `python build.py`
5. Output directory: `output`
6. Deploy!

## Adding Comments

To enable GitHub-based comments using Utterances:

1. Install the [Utterances app](https://github.com/apps/utterances) on your repository
2. Edit `config.yaml`:

```yaml
comments:
  enabled: true
  repo: "username/repo-name"  # Your GitHub repo
```

3. Rebuild your site: `python build.py`

Comments will appear at the bottom of each post. They're stored as GitHub issues - free and no tracking!

## Project Structure

```
mymusings/
├── posts/              # Your blog posts (Markdown)
├── templates/          # HTML templates (Jinja2)
├── static/            # CSS and other static files
├── output/            # Generated site (created by build.py)
├── config.yaml        # Blog configuration
├── build.py           # Site generator
├── blog.py            # CLI tool
└── requirements.txt   # Python dependencies
```

## Writing Posts

Posts are written in Markdown with frontmatter:

### Frontmatter (Required)

```yaml
---
title: "Post Title"
date: 2024-01-15
author: Your Name
tags: [tag1, tag2]
---
```

### Markdown Features

- **Headers**: `# H1`, `## H2`, etc.
- **Bold/Italic**: `**bold**`, `*italic*`
- **Links**: `[text](url)`
- **Images**: `![alt](url)`
- **Lists**: `- item` or `1. item`
- **Code**: `` `inline` `` or ` ```language ` blocks
- **Quotes**: `> quote`

## Customization

### Styling

Edit `static/css/style.css` to customize the look and feel.

### Templates

Modify the Jinja2 templates in `templates/`:
- `base.html` - Base layout
- `index.html` - Homepage (list of posts)
- `post.html` - Individual post page

### Configuration

Edit `config.yaml` to change blog settings.

## Cost Breakdown

- **Hosting**: $0 (GitHub Pages, Netlify, or Vercel)
- **Domain** (optional): ~$10-15/year
- **Comments**: $0 (GitHub Utterances)
- **Total**: **FREE** (or ~$1/month with custom domain)

## Tips

- Write posts regularly to build your catalog
- Use descriptive titles and tags
- Keep posts in the `posts/` directory
- Rebuild after any changes: `python build.py`
- Test locally before deploying: `python blog.py serve`

## License

This is your personal blog - do whatever you want with it!

## Support

For issues or questions, open an issue in this repository.

Happy writing! 🎉
