#!/usr/bin/env python3
"""TENT MIT OCW SEEDER - Ingest MIT OpenCourseWare into UPG."""

import json
import sys
from upg_store import UniversalPrimeGraph


def seed_ocw_from_json(json_data: dict) -> dict:
    """Seed OCW courses from JSON data."""
    upg = UniversalPrimeGraph()
    stats = {"courses": 0, "skipped": 0}
    
    nodes = json_data.get("nodes", {})
    
    for node_id, node_data in nodes.items():
        if not node_id.startswith("OCW_"):
            continue
        
        # Skip index nodes
        if node_id == "OCW_COURSES":
            continue
        
        title = node_data.get("title", "")
        abstract = node_data.get("abstract", "")[:500]
        url = node_data.get("url", "")
        
        upg.add_node(node_id, {
            "title": title,
            "abstract": abstract,
            "type": "ocw_course",
            "provider": "MIT OpenCourseWare",
            "url": url,
            "license": node_data.get("license", "CC BY-NC-SA 4.0"),
            "mass": "SOLID"
        })
        stats["courses"] += 1
    
    upg.save_graph()
    return stats


def main():
    if len(sys.argv) > 1:
        # Load from file
        with open(sys.argv[1]) as f:
            data = json.load(f)
    else:
        # Read from stdin
        data = json.load(sys.stdin)
    
    print("=" * 60)
    print("MIT OCW SEEDER")
    print("=" * 60)
    
    stats = seed_ocw_from_json(data)
    
    print(f"\n✅ Seeded: {stats['courses']} MIT OCW courses")
    print(f"   Skipped: {stats['skipped']}")


if __name__ == "__main__":
    main()
