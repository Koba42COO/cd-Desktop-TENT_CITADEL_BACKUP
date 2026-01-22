#!/usr/bin/env python3
"""
TENT SYNTHESIZER v2
===================
Query the Universal Prime Graph using natural language.
Performs deterministic lattice lookups without LLM dependency.
"""

import json
import re
import hashlib
from pathlib import Path
from typing import List, Dict, Any


class TentSynthesizer:
    """Synthesize knowledge from the Universal Prime Graph."""
    
    def __init__(self, graph_path: str = "universal_prime_graph.json"):
        self.graph_path = Path(graph_path)
        self.graph = self.load_graph()
        
    def load_graph(self) -> Dict[str, Any]:
        """Load the UPG."""
        if not self.graph_path.exists():
            return {"nodes": {}, "ledger": []}
        with open(self.graph_path) as f:
            return json.load(f)
    
    def search_nodes(self, query: str) -> List[Dict[str, Any]]:
        """Search nodes by keyword matching in title/abstract."""
        query_lower = query.lower()
        keywords = query_lower.split()
        results = []
        
        for node_id, node_data in self.graph.get("nodes", {}).items():
            title = node_data.get("title", "").lower()
            abstract = node_data.get("abstract", "").lower()
            node_type = node_data.get("type", "")
            
            # Score based on keyword matches
            score = 0
            for kw in keywords:
                if kw in title:
                    score += 3
                if kw in abstract:
                    score += 1
                if kw in node_id.lower():
                    score += 2
            
            if score > 0:
                results.append({
                    "id": node_id,
                    "title": node_data.get("title", node_id),
                    "type": node_type,
                    "category": node_data.get("category", "unknown"),
                    "score": score
                })
        
        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:20]  # Top 20
    
    def get_curriculum_by_category(self, category_keyword: str) -> List[Dict]:
        """Get curriculum items by category."""
        results = []
        category_kw = category_keyword.lower()
        
        for node_id, node_data in self.graph.get("nodes", {}).items():
            if not node_id.startswith("CURR_"):
                continue
            
            title = node_data.get("title", "").lower()
            category = node_data.get("category", "").lower()
            node_type = node_data.get("type", "")
            
            if category_kw in title or category_kw in category or category_kw in node_id.lower():
                results.append({
                    "id": node_id,
                    "title": node_data.get("title", node_id),
                    "type": node_type,
                    "category": category
                })
        
        # Group by type
        courses = [r for r in results if r["type"] == "course"]
        modules = [r for r in results if r["type"] == "module"]
        categories = [r for r in results if r["type"] == "category"]
        
        return {"categories": categories, "courses": courses[:15], "modules": modules[:25]}
    
    def query(self, question: str) -> str:
        """Answer a question about the UPG content."""
        q_lower = question.lower()
        
        # Curriculum queries
        if "machine learning" in q_lower or "ml" in q_lower:
            data = self.get_curriculum_by_category("machine learning")
            return self._format_curriculum_response("Machine Learning and AI", data)
        
        if "physics" in q_lower:
            data = self.get_curriculum_by_category("physics")
            return self._format_curriculum_response("Physics", data)
        
        if "computer science" in q_lower or "cs" in q_lower:
            data = self.get_curriculum_by_category("computer science")
            return self._format_curriculum_response("Computer Science", data)
        
        if "mathematics" in q_lower or "math" in q_lower:
            data = self.get_curriculum_by_category("mathematics")
            return self._format_curriculum_response("Mathematics", data)
        
        if "chemistry" in q_lower:
            data = self.get_curriculum_by_category("chemistry")
            return self._format_curriculum_response("Chemistry", data)
        
        if "biology" in q_lower:
            data = self.get_curriculum_by_category("biology")
            return self._format_curriculum_response("Biology", data)
        
        if "engineering" in q_lower:
            data = self.get_curriculum_by_category("engineering")
            return self._format_curriculum_response("Engineering", data)
        
        # General search
        results = self.search_nodes(question)
        if results:
            return self._format_search_response(results)
        
        return "No matching nodes found in the Universal Prime Graph."
    
    def _format_curriculum_response(self, category: str, data: Dict) -> str:
        """Format curriculum data as readable text."""
        lines = [f"\n📚 {category.upper()} CURRICULUM", "=" * 50]
        
        if data["courses"]:
            lines.append(f"\n📗 COURSES ({len(data['courses'])} found):")
            for c in data["courses"]:
                lines.append(f"   • {c['title']}")
        
        if data["modules"]:
            lines.append(f"\n📘 MODULES ({len(data['modules'])} shown):")
            for m in data["modules"][:15]:
                lines.append(f"   • {m['title']}")
        
        lines.append(f"\n✅ Source: Universal Prime Graph ({len(self.graph.get('nodes', {}))} total nodes)")
        return "\n".join(lines)
    
    def _format_search_response(self, results: List[Dict]) -> str:
        """Format search results."""
        lines = [f"\n🔍 SEARCH RESULTS ({len(results)} matches)", "=" * 50]
        for r in results[:10]:
            type_emoji = {"course": "📗", "module": "📘", "category": "📚"}.get(r["type"], "📄")
            lines.append(f"   {type_emoji} [{r['score']}] {r['title']}")
        return "\n".join(lines)
    
    def stats(self) -> Dict:
        """Get graph statistics."""
        nodes = self.graph.get("nodes", {})
        ledger = self.graph.get("ledger", [])
        
        # Count by type
        types = {}
        for n in nodes.values():
            t = n.get("type", "unknown")
            types[t] = types.get(t, 0) + 1
        
        return {
            "total_nodes": len(nodes),
            "ledger_entries": len(ledger),
            "by_type": types
        }


def main():
    print("=" * 60)
    print("TENT SYNTHESIZER v2")
    print("Governance Layer: Deterministic UPG Query")
    print("=" * 60)
    
    synth = TentSynthesizer()
    stats = synth.stats()
    
    print(f"\n📊 Graph Stats:")
    print(f"   Total Nodes: {stats['total_nodes']}")
    print(f"   Ledger Entries: {stats['ledger_entries']}")
    print(f"   By Type: {stats['by_type']}")
    
    # Test queries
    queries = [
        "What is in the Machine Learning curriculum?",
        "Show me the Physics modules."
    ]
    
    for q in queries:
        print(f"\n❓ QUERY: {q}")
        print("-" * 50)
        response = synth.query(q)
        print(response)
    
    print("\n" + "=" * 60)
    print("SYNTHESIZER OPERATIONAL")
    print("=" * 60)


if __name__ == "__main__":
    main()
