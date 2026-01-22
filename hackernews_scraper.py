#!/usr/bin/env python3
"""TENT HACKERNEWS SCRAPER - Tech culture intelligence."""

import json
import time
import urllib.request
from upg_store import UniversalPrimeGraph

HN_API = "https://hacker-news.firebaseio.com/v0"
ALGOLIA_API = "https://hn.algolia.com/api/v1"

class HackerNewsScraper:
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        self.stats = {"fetched": 0, "seeded": 0}
    
    def fetch_top_stories(self, limit: int = 50) -> list:
        """Fetch top stories using Algolia search API."""
        url = f"{ALGOLIA_API}/search?tags=front_page&hitsPerPage={limit}"
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                return data.get("hits", [])
        except Exception as e:
            print(f"❌ Error: {e}")
            return []
    
    def seed_story(self, story: dict) -> bool:
        title = story.get("title", "")
        if not title or len(title) < 5:
            return False
        
        story_id = story.get("objectID", str(hash(title))[:10])
        node_id = f"HN_{story_id}"
        
        self.upg.add_node(node_id, {
            "title": title[:200],
            "type": "tech_news",
            "source": "hackernews",
            "url": story.get("url", ""),
            "points": story.get("points", 0),
            "comments": story.get("num_comments", 0),
            "author": story.get("author", ""),
            "mass": "SOLID" if story.get("points", 0) > 100 else "FLUX"
        })
        self.stats["seeded"] += 1
        return True
    
    def scrape(self, limit: int = 50):
        print("=" * 60)
        print("HACKERNEWS SCRAPER")
        print("=" * 60)
        
        stories = self.fetch_top_stories(limit)
        self.stats["fetched"] = len(stories)
        
        for story in stories:
            if self.seed_story(story):
                print(f"  ✅ {story.get('title', '')[:60]}...")
        
        self.upg.save_graph()
        print(f"\n✅ Fetched: {self.stats['fetched']}, Seeded: {self.stats['seeded']}")
        return self.stats

if __name__ == "__main__":
    HackerNewsScraper().scrape(50)
