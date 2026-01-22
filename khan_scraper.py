#!/usr/bin/env python3
"""TENT KHAN ACADEMY SCRAPER - Free education knowledge."""

import json
import urllib.request
from upg_store import UniversalPrimeGraph

KA_API = "https://www.khanacademy.org/api/v1"

# Key subject areas
SUBJECTS = [
    "math", "science", "computing", "economics-finance-domain",
    "humanities", "ela", "test-prep"
]

class KhanAcademyScraper:
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        self.stats = {"fetched": 0, "seeded": 0}
    
    def fetch_topic(self, slug: str) -> dict:
        """Fetch topic tree for a subject."""
        url = f"{KA_API}/topic/{slug}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "TENT/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            print(f"  ❌ Error [{slug}]: {e}")
            return {}
    
    def seed_topic(self, data: dict, parent: str = "") -> int:
        """Recursively seed topics."""
        count = 0
        title = data.get("title", "")
        slug = data.get("slug", "")
        desc = data.get("description", "")
        
        if title and slug:
            node_id = f"KA_{slug.upper().replace('-', '_')[:40]}"
            self.upg.add_node(node_id, {
                "title": title,
                "type": "education",
                "source": "khan_academy",
                "parent": parent,
                "abstract": desc[:300] if desc else title,
                "url": f"https://www.khanacademy.org/{slug}",
                "mass": "SOLID"
            })
            count += 1
            self.stats["seeded"] += 1
        
        # Process children (limit depth)
        for child in data.get("children", [])[:5]:
            if isinstance(child, dict):
                count += self.seed_topic(child, title)
        
        return count
    
    def scrape(self):
        print("=" * 60)
        print("KHAN ACADEMY SCRAPER")
        print("=" * 60)
        print(f"Subjects: {len(SUBJECTS)}\n")
        
        for subject in SUBJECTS:
            print(f"📡 [{subject}]...")
            data = self.fetch_topic(subject)
            self.stats["fetched"] += 1
            
            if data:
                count = self.seed_topic(data)
                print(f"   ✅ Seeded {count} topics")
        
        self.upg.save_graph()
        print(f"\n✅ Total Seeded: {self.stats['seeded']}")
        return self.stats

if __name__ == "__main__":
    KhanAcademyScraper().scrape()
