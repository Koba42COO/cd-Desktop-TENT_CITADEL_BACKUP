#!/usr/bin/env python3
"""TENT STACKOVERFLOW SCRAPER - Developer knowledge integration."""

import json
import gzip
import io
import urllib.request
from upg_store import UniversalPrimeGraph

SO_API = "https://api.stackexchange.com/2.3"

TAGS = ["python", "javascript", "machine-learning", "algorithm", "data-structures",
        "neural-network", "tensorflow", "pytorch", "sql", "linux"]

class StackOverflowScraper:
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        self.stats = {"fetched": 0, "seeded": 0}
    
    def fetch_top_questions(self, tag: str, limit: int = 10) -> list:
        """Fetch top voted questions for a tag."""
        url = f"{SO_API}/questions?order=desc&sort=votes&tagged={tag}&site=stackoverflow&pagesize={limit}"
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                if resp.info().get('Content-Encoding') == 'gzip':
                    data = gzip.GzipFile(fileobj=io.BytesIO(resp.read())).read()
                else:
                    data = resp.read()
                return json.loads(data.decode()).get("items", [])
        except Exception as e:
            print(f"  ❌ Error [{tag}]: {e}")
            return []
    
    def seed_question(self, q: dict, tag: str) -> bool:
        title = q.get("title", "")
        if not title:
            return False
        
        node_id = f"SO_{tag.upper()}_{q.get('question_id', '')}"
        
        self.upg.add_node(node_id, {
            "title": title[:200],
            "type": "developer_qa",
            "source": "stackoverflow",
            "tag": tag,
            "score": q.get("score", 0),
            "answers": q.get("answer_count", 0),
            "views": q.get("view_count", 0),
            "url": q.get("link", ""),
            "mass": "SOLID" if q.get("score", 0) > 100 else "FLUX"
        })
        self.stats["seeded"] += 1
        return True
    
    def scrape(self, per_tag: int = 10):
        print("=" * 60)
        print("STACKOVERFLOW SCRAPER")
        print("=" * 60)
        print(f"Tags: {len(TAGS)}, Per tag: {per_tag}\n")
        
        for tag in TAGS:
            print(f"📡 [{tag}]...")
            questions = self.fetch_top_questions(tag, per_tag)
            self.stats["fetched"] += len(questions)
            
            for q in questions:
                self.seed_question(q, tag)
        
        self.upg.save_graph()
        print(f"\n✅ Fetched: {self.stats['fetched']}, Seeded: {self.stats['seeded']}")
        return self.stats

if __name__ == "__main__":
    StackOverflowScraper().scrape(10)
