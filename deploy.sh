#!/bin/bash
# Deploy script for GitHub Pages
# This script builds the site and deploys it to GitHub Pages

set -e  # Exit on error

echo "=================================================="
echo "Deploying My Musings to GitHub Pages"
echo "=================================================="
echo ""

# Build the site
echo "Step 1: Building the site..."
python build.py
echo ""

# Check if output directory exists
if [ ! -d "output" ]; then
    echo "Error: Output directory not found. Build failed?"
    exit 1
fi

# Deploy to gh-pages branch
echo "Step 2: Deploying to gh-pages branch..."
cd output

# Initialize git if not already done
if [ ! -d ".git" ]; then
    git init
    echo "✓ Initialized git repository in output/"
fi

# Add all files
git add -A
echo "✓ Added all files"

# Commit
git commit -m "Deploy blog - $(date +"%Y-%m-%d %H:%M:%S")" || echo "No changes to commit"

# Set branch to gh-pages
git branch -M gh-pages

# Get remote URL from parent repo
cd ..
REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")

if [ -z "$REMOTE_URL" ]; then
    echo ""
    echo "⚠️  No git remote found!"
    echo "Please add a remote manually:"
    echo "  cd output"
    echo "  git remote add origin https://github.com/username/repo.git"
    echo "  git push -f origin gh-pages"
    exit 1
fi

cd output

# Add or update remote
git remote remove origin 2>/dev/null || true
git remote add origin "$REMOTE_URL"
echo "✓ Set remote to: $REMOTE_URL"

# Push to gh-pages
echo ""
echo "Pushing to GitHub Pages..."
git push -f origin gh-pages

echo ""
echo "=================================================="
echo "✓ Deployment complete!"
echo "=================================================="
echo ""
echo "Your blog should be available at:"
echo "https://username.github.io/repo-name/"
echo ""
echo "Note: It may take a few minutes for GitHub Pages to update."
echo "Enable GitHub Pages in your repository settings if not already done:"
echo "  Settings → Pages → Source: gh-pages branch"
