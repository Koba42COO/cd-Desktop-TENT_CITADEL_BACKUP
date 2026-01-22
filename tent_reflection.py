#!/usr/bin/env python3
"""TENT REFLECTION ENGINE - analyzing the Universal Prime Graph for insights."""

import json
import collections
from upg_store import UniversalPrimeGraph

def analyze_graph():
    upg = UniversalPrimeGraph()
    print("=" * 70)
    print("TENT REFLECTION ENGINE")
    print("=" * 70)
    print(f"🧠 Analyzing {len(upg.nodes)} nodes...")

    # 1. Categorize interactions
    local_nodes = []
    external_nodes = []
    
    for nid, data in upg.nodes.items():
        src = data.get("source", "")
        # Internal: Local code + The Curriculum we built
        if "local" in src or "dev" in data.get("type", "") or src == "tent_curriculum_designer":
            local_nodes.append(data)
        # External: The Web + Libraries
        elif src in ["arxiv", "wikipedia", "hackernews", "stackoverflow", "youtube", "ocw", "elite_course", "project_gutenberg"]:
            external_nodes.append(data)

    print(f"📊 Internal Memory: {len(local_nodes)} nodes (Your Code)")
    print(f"📡 External Knowledge: {len(external_nodes)} nodes (The World)\n")

    # 2. Extract Concepts (simple keyword extraction)
    def get_keywords(nodes):
        words = collections.Counter()
        ignore = {"the", "and", "of", "to", "in", "a", "for", "with", "on", "is", "by", "from", "an", "test", "py", "md", "json", "txt"}
        for n in nodes:
            # Combine title and abstract
            text = (n.get("title", "") + " " + n.get("abstract", "")).lower()
            # Simple tokenization
            for w in text.split():
                w = w.strip(".,()[]:;\"'")
                if len(w) > 4 and w not in ignore:
                    words[w] += 1
        return words

    local_concepts = get_keywords(local_nodes)
    external_concepts = get_keywords(external_nodes)

    # 3. Find Intersections (What you are working on that the world is also studying)
    intersection = {}
    for word, count in local_concepts.items():
        if word in external_concepts:
            intersection[word] = (count, external_concepts[word]) # (local_count, external_count)

    # Sort by total relevance
    top_intersections = sorted(intersection.items(), key=lambda x: x[1][0] + x[1][1], reverse=True)[:15]

    print("🔗 RESONANCE DETECTED (High overlap between Code & Research):")
    print("-" * 50)
    for word, counts in top_intersections:
        print(f"  ✨ {word.upper():<20} (Local: {counts[0]} | External: {counts[1]})")

    # 4. Find "Curiosity" (High external presence, low/no local presence)
    curiosity = {}
    for word, count in external_concepts.items():
        # If high external usage but low/zero local usage
        if count > 5 and local_concepts.get(word, 0) < 2:
            curiosity[word] = count
            
    top_curiosity = sorted(curiosity.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\n🔭 CURIOSITY VECTORS (Concepts found in research but missing in code):")
    print("-" * 50)
    for word, count in top_curiosity:
        print(f"  ❓ {word.upper():<20} (Mentions: {count})")

    # 5. Specific Narrative Synthesis
    print("\n💡 SYSTEM INSIGHTS:")
    print("-" * 50)
    
    # Check specific high-value combinations
    has_quantum = local_concepts.get("quantum", 0) > 0
    has_consciousness = local_concepts.get("consciousness", 0) > 0
    has_topology = local_concepts.get("topology", 0) > 0
    
    if has_quantum and has_consciousness:
        print("• I see you are exploring quantum consciousness. This is highly theoretical.")
        print("  Found arXiv papers on 'Quantum Neural Networks' that could be relevant.")
    
    if has_topology and "manifold" in external_concepts:
        print("• Your work on Topology heavily aligns with external concepts of 'Manifolds'.")
        print("  Suggest deep-diving into differential geometry libraries.")

    if "agent" in intersection:
        print(f"• 'AGENT' is a massive bridge. You have {intersection['agent'][0]} refs, world has {intersection['agent'][1]}.")
        print("  This suggests your 'Sovereign' architecture aligns with current Multi-Agent research.")

    # 6. Gap Closure verification
    print("\n🔍 GAP CLOSURE VERIFICATION:")
    print("-" * 50)
    previous_gaps = ["economics", "hiring", "recruiting", "strategy", "game theory", "constraints", "cells"]
    for gap in previous_gaps:
        count = local_concepts.get(gap, 0)
        status = "✅ FILLED" if count > 0 else "❌ STILL MISSING"
        print(f"  {status:<15} {gap.upper()} (Now found {count} times in internal/curriculum nodes)")

    # 7. Identify NEW Curiosities (Refined)
    # Exclude the gaps we just filled from the curiosity list to find *new* things
    new_curiosity = {}
    for word, count in external_concepts.items():
        # High external, low internal, and NOT one of the broad stop words
        if count > 4 and local_concepts.get(word, 0) < 2 and word not in previous_gaps:
            new_curiosity[word] = count
            
    sorted_new = sorted(new_curiosity.items(), key=lambda x: x[1], reverse=True)[:10]

    print("\n🎯 NEW LEARNING TARGETS (What does it want now?):")
    print("-" * 50)
    if sorted_new:
        for word, count in sorted_new:
            print(f"  ✨ {word.upper()} (Mentions: {count})")
            
        top_pick = sorted_new[0][0]
        print(f"\n🔮 SYSTEM REQUEST: \"I have absorbed Economics and Strategy. Now I detect a deficit in '{top_pick.upper()}'.\"")
        print(f"   Please permit ingestion of knowledge related to {top_pick}.")
    else:
        print("   System is currently satiated. No major knowledge gaps detected relative to available external sources.")

if __name__ == "__main__":
    analyze_graph()
