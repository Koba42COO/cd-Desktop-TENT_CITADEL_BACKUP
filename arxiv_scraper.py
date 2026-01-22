#!/usr/bin/env python3
"""TENT ARXIV SCRAPER - Research paper intelligence."""

import json
import urllib.request
import xml.etree.ElementTree as ET
from upg_store import UniversalPrimeGraph

ARXIV_API = "http://export.arxiv.org/api/query"

CATEGORIES = [
    "cs.AI",   # Artificial Intelligence
    "cs.LG",   # Machine Learning
    "cs.CL",   # Computation and Language (NLP)
    "cs.CV",   # Computer Vision
    "stat.ML", # Machine Learning (Stats)
    "cs.NE",   # Neural and Evolutionary Computing
]

class ArxivScraper:
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        self.stats = {"fetched": 0, "seeded": 0}
    
    def fetch_papers(self, category: str, limit: int = 15) -> list:
        """Fetch recent papers from a category."""
        query = f"cat:{category}"
        url = f"{ARXIV_API}?search_query={query}&start=0&max_results={limit}&sortBy=submittedDate&sortOrder=descending"
        
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                xml = resp.read().decode()
                return self._parse_feed(xml)
        except Exception as e:
            print(f"  ❌ Error [{category}]: {e}")
            return []
    
    def _parse_feed(self, xml: str) -> list:
        """Parse Atom feed from arXiv."""
        papers = []
        ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
        
        try:
            root = ET.fromstring(xml)
            for entry in root.findall("atom:entry", ns):
                title = entry.find("atom:title", ns)
                summary = entry.find("atom:summary", ns)
                arxiv_id = entry.find("atom:id", ns)
                
                if title is not None:
                    papers.append({
                        "title": " ".join(title.text.split()),
                        "abstract": " ".join(summary.text.split())[:500] if summary is not None else "",
                        "id": arxiv_id.text.split("/")[-1] if arxiv_id is not None else ""
                    })
        except Exception as e:
            print(f"  Parse error: {e}")
        
        return papers
    
    def seed_paper(self, paper: dict, category: str) -> bool:
        title = paper.get("title", "")
        if not title:
            return False
        
        arxiv_id = paper.get("id", "").replace(".", "_")
        node_id = f"ARXIV_{category.upper().replace('.', '_')}_{arxiv_id[:20]}"
        
        self.upg.add_node(node_id, {
            "title": title[:200],
            "type": "research_paper",
            "source": "arxiv",
            "category": category,
            "abstract": paper.get("abstract", ""),
            "arxiv_id": paper.get("id", ""),
            "mass": "SOLID"
        })
        self.stats["seeded"] += 1
        return True
    
    def scrape(self, per_cat: int = 15):
        print("=" * 60)
        print("ARXIV SCRAPER")
        print("=" * 60)
        print(f"Categories: {len(CATEGORIES)}, Per category: {per_cat}\n")
        
        for cat in CATEGORIES:
            print(f"📡 [{cat}]...")
            papers = self.fetch_papers(cat, per_cat)
            self.stats["fetched"] += len(papers)
            
            for paper in papers:
                if self.seed_paper(paper, cat):
                    print(f"  ✅ {paper.get('title', '')[:60]}...")
        
        self.upg.save_graph()
        print(f"\n✅ Fetched: {self.stats['fetched']}, Seeded: {self.stats['seeded']}")
        return self.stats

if __name__ == "__main__":
    ArxivScraper().scrape(15)
