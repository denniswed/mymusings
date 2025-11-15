#!/usr/bin/env python3
"""
Simple static site generator for My Musings blog.
Converts Markdown posts to HTML pages.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import frontmatter
import markdown
import yaml
from jinja2 import Environment, FileSystemLoader


class BlogGenerator:
    """Generates static blog site from Markdown posts."""
    
    def __init__(self, config_path='config.yaml'):
        """Initialize the blog generator."""
        self.base_dir = Path(__file__).parent
        self.posts_dir = self.base_dir / 'posts'
        self.templates_dir = self.base_dir / 'templates'
        self.output_dir = self.base_dir / 'output'
        self.static_dir = self.base_dir / 'static'
        
        # Load configuration
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        # Setup Jinja2 environment
        self.jinja_env = Environment(loader=FileSystemLoader(str(self.templates_dir)))
        
        # Setup Markdown processor
        self.md = markdown.Markdown(extensions=['fenced_code', 'tables', 'codehilite'])
    
    def clean_output(self):
        """Remove existing output directory."""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def copy_static_files(self):
        """Copy static files to output directory."""
        if self.static_dir.exists():
            output_static = self.output_dir / 'static'
            shutil.copytree(self.static_dir, output_static)
            print(f"✓ Copied static files to {output_static}")
    
    def parse_post(self, post_path):
        """Parse a Markdown post with frontmatter."""
        with open(post_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        # Convert Markdown content to HTML
        html_content = self.md.convert(post.content)
        self.md.reset()  # Reset for next post
        
        # Get slug from filename
        slug = post_path.stem
        
        # Parse metadata
        metadata = {
            'title': post.get('title', 'Untitled'),
            'date': post.get('date', datetime.now().strftime('%Y-%m-%d')),
            'author': post.get('author', self.config.get('author', 'Unknown')),
            'tags': post.get('tags', []),
            'content': html_content,
            'slug': slug
        }
        
        return metadata
    
    def get_all_posts(self):
        """Get all posts sorted by date (newest first)."""
        posts = []
        
        if not self.posts_dir.exists():
            print(f"Warning: Posts directory not found at {self.posts_dir}")
            return posts
        
        for post_file in self.posts_dir.glob('*.md'):
            try:
                post_data = self.parse_post(post_file)
                posts.append(post_data)
                print(f"✓ Parsed post: {post_data['title']}")
            except Exception as e:
                print(f"✗ Error parsing {post_file}: {e}")
        
        # Sort by date (newest first)
        posts.sort(key=lambda x: x['date'], reverse=True)
        return posts
    
    def generate_post_page(self, post):
        """Generate individual post page."""
        template = self.jinja_env.get_template('post.html')
        html = template.render(post=post, config=self.config)
        
        # Create posts directory in output
        posts_output_dir = self.output_dir / 'posts'
        posts_output_dir.mkdir(exist_ok=True)
        
        # Write post HTML file
        output_path = posts_output_dir / f"{post['slug']}.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✓ Generated post page: {output_path}")
    
    def generate_index_page(self, posts):
        """Generate index page with list of all posts."""
        template = self.jinja_env.get_template('index.html')
        html = template.render(posts=posts, config=self.config)
        
        output_path = self.output_dir / 'index.html'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✓ Generated index page: {output_path}")
    
    def build(self):
        """Build the entire site."""
        print("Starting blog generation...\n")
        
        # Clean and prepare output directory
        self.clean_output()
        print(f"✓ Cleaned output directory: {self.output_dir}\n")
        
        # Copy static files
        self.copy_static_files()
        print()
        
        # Get all posts
        posts = self.get_all_posts()
        print(f"\n✓ Found {len(posts)} post(s)\n")
        
        # Generate individual post pages
        for post in posts:
            self.generate_post_page(post)
        print()
        
        # Generate index page
        self.generate_index_page(posts)
        
        print(f"\n{'='*50}")
        print(f"✓ Site generated successfully!")
        print(f"{'='*50}")
        print(f"Output directory: {self.output_dir}")
        print(f"Open {self.output_dir}/index.html in your browser to view the site.")


def main():
    """Main entry point."""
    generator = BlogGenerator()
    generator.build()


if __name__ == '__main__':
    main()
