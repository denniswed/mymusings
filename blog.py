#!/usr/bin/env python3
"""
CLI tool for managing My Musings blog.
"""

import sys
from pathlib import Path
from datetime import datetime
import argparse


def create_new_post(title, author=None, tags=None):
    """Create a new blog post with frontmatter template."""
    # Create slug from title
    slug = title.lower()
    slug = ''.join(c if c.isalnum() or c in ' -' else '' for c in slug)
    slug = '-'.join(slug.split())
    
    # Create filename with date
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = f"{date_str}-{slug}.md"
    
    # Prepare frontmatter
    post_date = datetime.now().strftime('%Y-%m-%d')
    tags_str = str(tags) if tags else '[]'
    author_str = author if author else 'Your Name'
    
    # Post template
    template = f"""---
title: "{title}"
date: {post_date}
author: {author_str}
tags: {tags_str}
---

# {title}

Write your post content here using Markdown...

## Section Example

You can use:
- Lists
- **Bold** and *italic* text
- [Links](https://example.com)
- Code blocks
- And more!

```python
# Code example
def hello():
    print("Hello, world!")
```
"""
    
    # Write to posts directory
    posts_dir = Path(__file__).parent / 'posts'
    posts_dir.mkdir(exist_ok=True)
    
    post_path = posts_dir / filename
    
    if post_path.exists():
        print(f"Error: Post already exists at {post_path}")
        return False
    
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"✓ Created new post: {post_path}")
    print(f"\nNext steps:")
    print(f"1. Edit {post_path} to write your content")
    print(f"2. Run 'python build.py' to generate the site")
    return True


def list_posts():
    """List all existing posts."""
    posts_dir = Path(__file__).parent / 'posts'
    
    if not posts_dir.exists():
        print("No posts directory found.")
        return
    
    posts = list(posts_dir.glob('*.md'))
    
    if not posts:
        print("No posts found.")
        return
    
    print(f"\nFound {len(posts)} post(s):\n")
    for post_path in sorted(posts):
        print(f"  - {post_path.name}")


def kill_process_on_port(port):
    """Kill any process using the specified port."""
    import subprocess
    import signal
    
    try:
        # Find process using the port
        result = subprocess.run(
            ['lsof', '-ti', f':{port}'],
            capture_output=True,
            text=True
        )
        
        if result.stdout.strip():
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                try:
                    pid_int = int(pid)
                    print(f"Found orphaned process (PID {pid_int}) on port {port}. Killing it...")
                    import os
                    os.kill(pid_int, signal.SIGKILL)
                    print(f"✓ Killed process {pid_int}")
                except (ValueError, ProcessLookupError, PermissionError) as e:
                    print(f"Warning: Could not kill process {pid}: {e}")
    except FileNotFoundError:
        # lsof not available, try alternative method
        try:
            result = subprocess.run(
                ['ss', '-lptn', f'sport = :{port}'],
                capture_output=True,
                text=True
            )
            # This is a fallback but won't work well for killing processes
            print(f"Note: lsof not available, cannot automatically kill processes on port {port}")
        except FileNotFoundError:
            pass


def serve_blog(port=8000):
    """Start a simple HTTP server to preview the blog."""
    import http.server
    import socketserver
    import subprocess
    
    output_dir = Path(__file__).parent / 'output'
    
    # Rebuild site for local testing
    print("Rebuilding site for local testing...")
    result = subprocess.run([sys.executable, 'build.py', '--local'], cwd=Path(__file__).parent)
    if result.returncode != 0:
        print("Error: Build failed.")
        return
    
    if not output_dir.exists():
        print("Error: Output directory not found after build.")
        return
    
    # Kill any orphaned processes on the port
    kill_process_on_port(port)
    
    # Change to output directory
    import os
    os.chdir(output_dir)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"\n{'='*50}")
            print(f"✓ Serving blog at http://localhost:{port}")
            print(f"{'='*50}")
            print(f"\nPress Ctrl+C to stop the server.\n")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\nError: Port {port} is still in use. Please wait a moment and try again.")
        else:
            raise


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='My Musings - A simple blog management tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create a new post
  python blog.py new "My First Post" --author "John Doe" --tags "intro,personal"
  
  # List all posts
  python blog.py list
  
  # Build the site
  python build.py
  
  # Preview the blog
  python blog.py serve
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # New post command
    new_parser = subparsers.add_parser('new', help='Create a new blog post')
    new_parser.add_argument('title', help='Title of the post')
    new_parser.add_argument('--author', help='Author name', default=None)
    new_parser.add_argument('--tags', help='Comma-separated tags', default=None)
    
    # List posts command
    subparsers.add_parser('list', help='List all posts')
    
    # Serve command
    serve_parser = subparsers.add_parser('serve', help='Preview the blog locally')
    serve_parser.add_argument('--port', type=int, default=8000, help='Port to serve on (default: 8000)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == 'new':
        tags = [tag.strip() for tag in args.tags.split(',')] if args.tags else []
        create_new_post(args.title, args.author, tags)
    elif args.command == 'list':
        list_posts()
    elif args.command == 'serve':
        serve_blog(args.port)


if __name__ == '__main__':
    main()
