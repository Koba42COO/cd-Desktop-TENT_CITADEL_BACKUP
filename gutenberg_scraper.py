#!/usr/bin/env python3
"""TENT GUTENBERG SCRAPER - Ingesting the Public Domain (CC0)."""

import urllib.request
import re
from upg_store import UniversalPrimeGraph

# Targeted Classics (ID mapping)
# 3300 = Wealth of Nations (Smith)
# 132 = The Art of War (Sun Tzu)
# 1232 = The Prince (Machiavelli)
# 3207 = Leviathan (Hobbes)
# 1497 = The Republic (Plato)
# 11 = Alice in Wonderland (Carroll) - just for fun/testing logic
TARGETS = {
    "3300": "The Wealth of Nations",
    "132": "The Art of War",
    "1232": "The Prince",
    "3207": "Leviathan",
    "1497": "The Republic",
    "11": "Alice's Adventures in Wonderland"
}

GUTENBERG_BASE = "https://www.gutenberg.org/files"

class GutenbergScraper:
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        self.stats = {"fetched": 0, "seeded": 0}

    def fetch_text(self, book_id: str) -> str:
        """Fetch raw text from Project Gutenberg."""
        # Try common URL patterns (they vary by ID)
        urls = [
            f"{GUTENBERG_BASE}/{book_id}/{book_id}-0.txt",
            f"{GUTENBERG_BASE}/{book_id}/{book_id}.txt"
        ]
        
        for url in urls:
            try:
                with urllib.request.urlopen(url, timeout=10) as f:
                    return f.read().decode('utf-8')
            except:
                continue
        return ""

    def clean_text(self, text: str) -> str:
        """Extract the actual book content, removing Gutenberg headers/footers."""
        # This is a heuristic; Gutenberg texts usually have start/end markers
        start_marker = re.search(r"\*\*\* START OF (THE|THIS) PROJECT GUTENBERG EBOOK", text)
        end_marker = re.search(r"\*\*\* END OF (THE|THIS) PROJECT GUTENBERG EBOOK", text)
        
        start_idx = start_marker.end() if start_marker else 0
        end_idx = end_marker.start() if end_marker else len(text)
        
        content = text[start_idx:end_idx].strip()
        return content

    def seed_book(self, book_id: str, title: str):
        print(f"📖 Fetching: {title} (ID: {book_id})...")
        raw_text = self.fetch_text(book_id)
        
        if not raw_text:
            print(f"  ❌ Failed to fetch text.")
            return

        content = self.clean_text(raw_text)
        sample = content[:500] + "..." # Store preview in abstract
        
        # Estimate mass/length
        word_count = len(content.split())
        
        node_id = f"GUTENBERG_{book_id}_{title.upper().replace(' ', '_')[:30]}"
        
        self.upg.add_node(node_id, {
            "title": title,
            "type": "book",
            "source": "project_gutenberg",
            "gutenberg_id": book_id,
            "author": "Public Domain Classic", # Could parse author if needed
            "abstract": sample,
            "word_count": word_count,
            "url": f"https://www.gutenberg.org/ebooks/{book_id}",
            "mass": "SOLID"
        })
        self.stats["seeded"] += 1
        print(f"  ✅ Seeded ({word_count} words)")

    def scrape(self):
        print("=" * 60)
        print("PROJECT GUTENBERG SCRAPER")
        print("=" * 60)
        
        for bid, title in TARGETS.items():
            self.seed_book(bid, title)
            self.stats["fetched"] += 1
            
        self.upg.save_graph()
        print(f"\n✅ Fetched: {self.stats['fetched']}, Seeded: {self.stats['seeded']}")

if __name__ == "__main__":
    GUTENBERG_BASE = "https://www.gutenberg.org/files" # Re-define if needed for script scope
    GutenbergScraper().scrape()
