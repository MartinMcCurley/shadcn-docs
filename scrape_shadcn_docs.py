#!/usr/bin/env python3
"""
Scrape shadcn/ui documentation to local .md files.
Usage: python scrape_shadcn_docs.py
"""

import os
import time
import json
import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from markdownify import markdownify as md  # pip install markdownify
from pathlib import Path

# Configuration
BASE = "https://ui.shadcn.com/docs"
OUTDIR = "shadcn_docs"
PROGRESS_FILE = "scraper_progress.json"
LOG_FILE = "scraper.log"

# Scraping parameters
HEADERS = {"User-Agent": "ShadcnDocsScraper/1.0 (Educational/Personal Use)"}
DELAY = 0.5           # seconds between requests (increased for politeness)
DEPTH_LIMIT = 2       # allow deeper nesting: /docs/<section>/<subsection>/<slug>
TIMEOUT = 15          # request timeout in seconds

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ShadcnScraper:
    def __init__(self):
        self.visited = set()
        self.queue = [BASE]
        self.failed_urls = []
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        
        # Load previous progress if exists
        self.load_progress()
        
        # Create output directory
        Path(OUTDIR).mkdir(exist_ok=True)
    
    def load_progress(self):
        """Load previous scraping progress to resume if interrupted."""
        if os.path.exists(PROGRESS_FILE):
            try:
                with open(PROGRESS_FILE, 'r') as f:
                    data = json.load(f)
                    self.visited = set(data.get('visited', []))
                    self.queue = data.get('queue', [BASE])
                    logger.info(f"Resumed: {len(self.visited)} visited, {len(self.queue)} queued")
            except Exception as e:
                logger.warning(f"Could not load progress: {e}")
    
    def save_progress(self):
        """Save current progress to file."""
        try:
            with open(PROGRESS_FILE, 'w') as f:
                json.dump({
                    'visited': list(self.visited),
                    'queue': self.queue,
                    'failed_urls': self.failed_urls
                }, f, indent=2)
        except Exception as e:
            logger.error(f"Could not save progress: {e}")
    
    def relative_path(self, url: str) -> str:
        """Return path fragment relative to /docs/ – used for folder structure."""
        path = urlparse(url).path.replace("/docs/", "", 1).strip("/")
        return path or "index"
    
    def clean_content(self, soup: BeautifulSoup) -> BeautifulSoup:
        """Remove unwanted elements from the page content."""
        # Remove navigation, headers, footers, etc.
        unwanted_selectors = [
            'nav', 'header', 'footer', 
            '.sidebar', '.navigation', '.nav',
            '.header', '.footer', '.breadcrumb',
            'script', 'style', '.ad', '.advertisement'
        ]
        
        for selector in unwanted_selectors:
            for element in soup.select(selector):
                element.decompose()
        
        return soup
    
    def save_markdown(self, url: str, html: str) -> bool:
        """Save HTML content as markdown file."""
        try:
            rel = self.relative_path(url)
            
            # Create directory structure
            file_path = Path(OUTDIR) / f"{rel}.md"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            soup = BeautifulSoup(html, "html.parser")
            
            # Extract title
            title = "Documentation"
            if soup.title:
                title = soup.title.string.strip()
            elif soup.find('h1'):
                title = soup.find('h1').get_text().strip()
            
            # Get main content, fallback to body, then whole page
            main = (soup.select_one("main") or 
                   soup.select_one("article") or 
                   soup.select_one(".content") or
                   soup.select_one("body") or 
                   soup)
            
            # Clean unwanted elements
            main = self.clean_content(main)
            
            # Convert to markdown
            content_md = md(str(main), heading_style="ATX")
            
            # Clean up markdown (remove excessive whitespace)
            lines = content_md.split('\n')
            cleaned_lines = []
            prev_empty = False
            
            for line in lines:
                line = line.rstrip()
                if line == '':
                    if not prev_empty:
                        cleaned_lines.append('')
                    prev_empty = True
                else:
                    cleaned_lines.append(line)
                    prev_empty = False
            
            content_md = '\n'.join(cleaned_lines).strip()
            
            # Write file
            with open(file_path, "w", encoding="utf-8") as fp:
                fp.write(f"# {title}\n\n")
                fp.write(f"Source: {url}\n\n")
                fp.write(content_md)
            
            logger.info(f"Saved: {rel}.md")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save {url}: {e}")
            return False
    
    def discover_links(self, base_url: str, soup: BeautifulSoup):
        """Yield internal doc links that are within the allowed depth."""
        links_found = 0
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("#"):
                continue  # same-page anchor
            
            full = urljoin(base_url, href)
            if not full.startswith(BASE):
                continue   # external link
            
            # Remove query parameters and fragments for consistency
            full = full.split('?')[0].split('#')[0]
            
            depth = self.relative_path(full).count("/")
            if depth <= DEPTH_LIMIT and full not in self.visited and full not in self.queue:
                self.queue.append(full)
                links_found += 1
                yield full
        
        if links_found > 0:
            logger.debug(f"Found {links_found} new links on {base_url}")
    
    def scrape(self):
        """Main scraping loop."""
        logger.info("Starting shadcn/ui documentation scrape")
        logger.info(f"Base URL: {BASE}")
        logger.info(f"Output directory: {OUTDIR}")
        logger.info(f"Depth limit: {DEPTH_LIMIT}")
        
        total_processed = 0
        
        try:
            while self.queue:
                url = self.queue.pop(0)
                
                if url in self.visited:
                    continue
                
                self.visited.add(url)
                total_processed += 1
                
                logger.info(f"[{total_processed}] Processing: {url}")
                logger.info(f"Queue remaining: {len(self.queue)}")
                
                try:
                    response = self.session.get(url, timeout=TIMEOUT)
                    response.raise_for_status()
                    
                    # Save content
                    if self.save_markdown(url, response.text):
                        # Discover new links
                        soup = BeautifulSoup(response.text, "html.parser")
                        list(self.discover_links(url, soup))  # Convert generator to list to execute
                    
                except requests.RequestException as e:
                    logger.error(f"Request failed for {url}: {e}")
                    self.failed_urls.append(url)
                except Exception as e:
                    logger.error(f"Unexpected error processing {url}: {e}")
                    self.failed_urls.append(url)
                
                # Save progress periodically
                if total_processed % 10 == 0:
                    self.save_progress()
                
                # Be polite
                time.sleep(DELAY)
        
        except KeyboardInterrupt:
            logger.info("Scraping interrupted by user")
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {e}")
        finally:
            self.save_progress()
            self.print_summary()
    
    def print_summary(self):
        """Print scraping summary."""
        logger.info("=" * 50)
        logger.info("SCRAPING SUMMARY")
        logger.info("=" * 50)
        logger.info(f"✅ Successfully processed: {len(self.visited)} pages")
        logger.info(f"📁 Saved to: ./{OUTDIR}")
        
        if self.failed_urls:
            logger.warning(f"❌ Failed URLs ({len(self.failed_urls)}):")
            for url in self.failed_urls:
                logger.warning(f"   - {url}")
        
        if self.queue:
            logger.info(f"⏸️  Remaining in queue: {len(self.queue)} URLs")
            logger.info("   (Run script again to continue)")
        
        # Clean up progress file if complete
        if not self.queue and os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)
            logger.info("🧹 Cleaned up progress file")

if __name__ == "__main__":
    scraper = ShadcnScraper()
    scraper.scrape()
