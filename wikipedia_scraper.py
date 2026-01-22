#!/usr/bin/env python3
"""TENT WIKIPEDIA SCRAPER - Encyclopedia knowledge integration."""

import json
import re
import urllib.request
import urllib.parse
from upg_store import UniversalPrimeGraph

WIKI_API = "https://en.wikipedia.org/api/rest_v1"

# Key topics to fetch
KEY_TOPICS = [
    "Artificial_intelligence", "Machine_learning", "Deep_learning", "Neural_network",
    "Computer_science", "Algorithm", "Data_structure", "Programming_language",
    "Mathematics", "Calculus", "Linear_algebra", "Probability_theory", "Statistics",
    "Physics", "Quantum_mechanics", "Relativity", "Thermodynamics", "Electromagnetism",
    "Philosophy", "Logic", "Ethics", "Epistemology", "Metaphysics",
    "Economics", "Game_theory", "Microeconomics", "Macroeconomics",
    "Biology", "Genetics", "Evolution", "Neuroscience", "Cell_biology",
    "Chemistry", "Organic_chemistry", "Biochemistry", "Molecular_biology",
    "History", "World_War_II", "Industrial_Revolution", "Renaissance",
    "Psychology", "Cognitive_science", "Behavioral_economics",
    "Linguistics", "Natural_language_processing", "Semantics",
    "Cryptography", "Information_theory", "Complexity_theory",
]

class WikipediaScraper:
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        self.stats = {"fetched": 0, "seeded": 0, "errors": 0}
    
    def fetch_summary(self, title: str) -> dict:
        """Fetch Wikipedia summary for a topic."""
        url = f"{WIKI_API}/page/summary/{urllib.parse.quote(title)}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "TENT-Scraper/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            self.stats["errors"] += 1
            return {}
    
    def seed_article(self, data: dict) -> bool:
        title = data.get("title", "")
        extract = data.get("extract", "")
        if not title or not extract:
            return False
        
        node_id = f"WIKI_{title.upper().replace(' ', '_')[:40]}"
        
        self.upg.add_node(node_id, {
            "title": title,
            "type": "encyclopedia",
            "source": "wikipedia",
            "abstract": extract[:500],
            "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
            "mass": "SOLID"
        })
        self.stats["seeded"] += 1
        return True
    
    def scrape(self):
        print("=" * 60)
        print("WIKIPEDIA SCRAPER")
        print("=" * 60)
        print(f"Topics: {len(KEY_TOPICS)}\n")
        
        for topic in KEY_TOPICS:
            data = self.fetch_summary(topic)
            self.stats["fetched"] += 1
            
            if self.seed_article(data):
                print(f"  ✅ {data.get('title', topic)}")
            else:
                print(f"  ❌ {topic}")
        
        self.upg.save_graph()
        print(f"\n✅ Fetched: {self.stats['fetched']}, Seeded: {self.stats['seeded']}, Errors: {self.stats['errors']}")
        return self.stats

if __name__ == "__main__":
    WikipediaScraper().scrape()
