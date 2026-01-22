#!/usr/bin/env python3
"""
TENT REDDIT SCRAPER
===================
Scrapes Reddit for modern culture and language.
Seeds discovered content into the Universal Prime Graph.

No API key required - uses Reddit's public JSON endpoints.
"""

import json
import time
import hashlib
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
import urllib.request
import urllib.error

from upg_store import UniversalPrimeGraph


# Subreddits for modern culture and language
SUBREDDITS = [
    # Language & Learning
    "explainlikeimfive",
    "todayilearned",
    "etymology",
    "linguistics",
    "words",
    "slang",
    
    # Culture & Trends
    "OutOfTheLoop",
    "NoStupidQuestions",
    "AskReddit",
    "changemyview",
    
    # Technology & Science
    "technology",
    "science",
    "Futurology",
    "MachineLearning",
    "artificial",
]

# Rate limiting
REQUEST_DELAY = 2.0  # seconds between requests


class RedditScraper:
    """Scrape Reddit for modern culture and language content."""
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        self.user_agent = "TENT-Scraper/1.0 (Cultural Intelligence Gatherer)"
        self.stats = {"fetched": 0, "seeded": 0, "errors": 0}
    
    def fetch_subreddit(self, subreddit: str, limit: int = 25) -> List[Dict]:
        """Fetch top posts from a subreddit using public JSON API."""
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
        
        try:
            req = urllib.request.Request(url, headers={"User-Agent": self.user_agent})
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                posts = data.get("data", {}).get("children", [])
                return [p.get("data", {}) for p in posts]
        except urllib.error.HTTPError as e:
            print(f"  ❌ HTTP Error {e.code} for r/{subreddit}")
            self.stats["errors"] += 1
            return []
        except Exception as e:
            print(f"  ❌ Error fetching r/{subreddit}: {e}")
            self.stats["errors"] += 1
            return []
    
    def _slugify(self, text: str) -> str:
        """Convert text to node-safe ID."""
        clean = re.sub(r"[^A-Z0-9]+", "_", text.upper())[:50]
        return clean.strip("_")
    
    def _hash_id(self, text: str) -> str:
        """Create a short hash ID."""
        return hashlib.sha256(text.encode()).hexdigest()[:12].upper()
    
    def seed_post(self, post: Dict, subreddit: str) -> bool:
        """Seed a Reddit post into the UPG."""
        title = post.get("title", "")
        if not title or len(title) < 10:
            return False
        
        # Skip nsfw/removed content
        if post.get("over_18") or post.get("removed_by_category"):
            return False
        
        # Create node
        post_id = post.get("id", self._hash_id(title))
        node_id = f"REDDIT_{subreddit.upper()}_{post_id.upper()}"
        
        # Extract useful content
        selftext = post.get("selftext", "")[:500] if post.get("selftext") else ""
        score = post.get("score", 0)
        num_comments = post.get("num_comments", 0)
        
        node_data = {
            "title": title[:200],
            "type": "culture",
            "source": "reddit",
            "subreddit": subreddit,
            "score": score,
            "comments": num_comments,
            "mass": "SOLID" if score > 100 else "FLUX",
            "abstract": selftext[:300] if selftext else title,
            "timestamp": datetime.now().isoformat(),
        }
        
        self.upg.add_node(node_id, node_data)
        self.stats["seeded"] += 1
        return True
    
    def scrape_all(self, posts_per_sub: int = 10):
        """Scrape all configured subreddits."""
        print("=" * 60)
        print("TENT REDDIT SCRAPER")
        print("Modern Culture & Language Intelligence")
        print("=" * 60)
        print(f"\nTarget: {len(SUBREDDITS)} subreddits")
        print(f"Posts per sub: {posts_per_sub}\n")
        
        for subreddit in SUBREDDITS:
            print(f"📡 Scraping r/{subreddit}...")
            posts = self.fetch_subreddit(subreddit, limit=posts_per_sub)
            self.stats["fetched"] += len(posts)
            
            seeded = 0
            for post in posts:
                if self.seed_post(post, subreddit):
                    seeded += 1
            
            print(f"   ✅ Fetched {len(posts)}, seeded {seeded}")
            time.sleep(REQUEST_DELAY)  # Rate limiting
        
        # Save
        self.upg.save_graph()
        
        print("\n" + "=" * 60)
        print("SCRAPE COMPLETE")
        print("=" * 60)
        print(f"Total Fetched: {self.stats['fetched']}")
        print(f"Total Seeded:  {self.stats['seeded']}")
        print(f"Errors:        {self.stats['errors']}")
        
        return self.stats


def main():
    scraper = RedditScraper()
    scraper.scrape_all(posts_per_sub=15)


if __name__ == "__main__":
    main()
