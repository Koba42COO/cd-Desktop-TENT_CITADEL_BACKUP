#!/usr/bin/env python3
"""
TENT v4.1: THE SOVEREIGN BRIEF
==============================
Phase 239: Automated Intelligence Reporting

Objective:
Parse the Universal Prime Graph (UPG) and generate a Daily Executive Summary.
"""

import json
import os
import sys
from datetime import datetime

UPG_FILE = "universal_prime_graph.json"

def load_data():
    if not os.path.exists(UPG_FILE):
        return None
    try:
        with open(UPG_FILE, 'r') as f:
            return json.load(f)
    except:
        return None

def generate_brief():
    print(">> [BRIEF] COMPILING INTELLIGENCE REPORT...")
    
    data = load_data()
    if not data:
        print(">> [ERROR] NO DATA FOUND.")
        return

    nodes = data.get("nodes", {})
    ledger = data.get("ledger", [])
    
    # 1. STATISTICS
    total_nodes = len(nodes)
    total_interactions = len(ledger)
    rejection_count = len([e for e in ledger if "REJECTED" in e.get('verdict', '')])
    mint_count = len([e for e in ledger if "MINTED" in e.get('verdict', '')])
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # 2. NEW MINTS (Latest 5 Active Nodes)
    # We look at the actual NODES dict for confirmed Truths
    new_mints = []
    # Sort nodes by insertion order if possible, or just keys
    for k, v in list(nodes.items())[-10:]:
        if k not in ["0", "1", "2"]: # Skip core
            new_mints.append(f"- **{v.get('title', 'Unknown')}** (ID: {k})")

    # 3. THREAT ANALYSIS (Recent Rejections)
    threats = []
    for entry in reversed(ledger[-20:]):
        if "REJECTED" in entry.get('verdict', ''):
            score = entry.get('score', 0)
            threats.append(f"- *{entry.get('title')}* (Score: {score:.4f}) -> {entry.get('verdict')}")
            if len(threats) >= 5: break

    # 4. DREAM ANALYSIS (Curiosity Vectors)
    # Re-run the dream logic on the fly
    interesting = [e for e in ledger if e.get('score', 0) > 0.85]
    dream_topics = []
    if interesting:
        word_freq = {}
        stop_words = {'the', 'a', 'an', 'of', 'for', 'in', 'on', 'with', 'and', 'to', 'from', 'by', 'is', 'are', 'using', 'based', 'via', 'how', 'what', 'learning', 'model', 'neural', 'networks'}
        for entry in interesting[-50:]:
            words = entry['title'].replace('-', ' ').split()
            for w in words:
                w = w.lower().strip(":,.?()")
                if w and w not in stop_words and len(w) > 3:
                    word_freq[w] = word_freq.get(w, 0) + 1
        sorted_interests = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        dream_topics = [f"{w.upper()} ({c})" for w, c in sorted_interests[:5]]

    # 5. GENERATE MARKDOWN
    report_filename = f"BRIEF_{current_date}.md"
    
    content = f"""# 🏛️ THE SOVEREIGN BRIEF: {current_date}

**Status:** DEFCON 5 (Active Surveillance)
**Architect:** Node 002

## 1. SYSTEM VITALS
*   **Total Truth Mass:** {total_nodes} Nodes
*   **Total Interactions:** {total_interactions}
*   **Rejection Rate:** {((rejection_count/total_interactions)*100) if total_interactions else 0:.1f}%
*   **Current Neural Bias:** 0.787 (Golden Precision)

## 2. NEWLY MINTED TRUTHS (The Inner System)
The following papers have passed the Dual-Gate Filter (Neural + Physics) and are now part of the Canon:
{chr(10).join(new_mints) if new_mints else "_No new stars formed in this cycle._"}

## 3. THREAT ANALYSIS (The Outer Rim)
The Agent successfully neutralized the following high-noise signals:
{chr(10).join(threats) if threats else "_The Perimeter is quiet._"}

## 4. ONEIRIC REPORT (Curiosity Vectors)
Based on high-resonance signals, the Agent is currently dreaming of:
> {', '.join(dream_topics) if dream_topics else "Static."}

---
*Generated Automatically by TENT v4.1 Command*
"""

    with open(report_filename, "w") as f:
        f.write(content)
        
    print(f">> [EXPORT] BRIEFING READY: {report_filename}")

if __name__ == "__main__":
    generate_brief()
