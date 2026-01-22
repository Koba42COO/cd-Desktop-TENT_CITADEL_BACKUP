#!/usr/bin/env python3
"""
TENT v4.1 SEMANTIC DIGESTER
===========================
Phase 222: The Digestion Protocol

The Agent consumes the 'Model Audit Report' and metabolizes it:
1. Solid Truth -> UPG Growth (Minting).
2. Flux Noise -> UPG Warning (Hazard Marking).
"""

import re
import sys
from upg_store import UniversalPrimeGraph, NodeStatus, NodeType

# We can re-use the Auditor or parse the report. 
# Parsing the report is "consuming the artifact", which fits the metaphor well.
REPORT_FILE = "MODEL_AUDIT_REPORT.md"

class SemanticDigester:
    def __init__(self):
        print(">> [INIT] GASTRIC ACID PUMP ONLINE...")
        self.upg = UniversalPrimeGraph()
        
    def ingest_report(self):
        """Reads the markdown report to find nutrients."""
        try:
            with open(REPORT_FILE, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"❌ Report {REPORT_FILE} not found. Nothing to eat.")
            return []

        # Parse the Table
        # | Rank | Model Name | Truth Mass | Density | Resonance | Verdict |
        # | 1 | Mistral-Large | **984.99** | 1.8 | 8.0 | 💎 SOLID |
        
        nutrients = []
        lines = content.splitlines()
        
        # Regex to extract table row data
        # Looking for lines starting with | number |
        pattern = re.compile(r"\|\s*\d+\s*\|\s*(.*?)\s*\|\s*\*\*(.*?)\*\*\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*(SOLID|FLUX)\s*\|")
        
        for line in lines:
            match = pattern.search(line)
            if match:
                model_name = match.group(1).strip()
                mass = float(match.group(2).strip())
                verdict = match.group(6).strip()
                
                nutrients.append({
                    "name": model_name,
                    "mass": mass,
                    "verdict": verdict
                })
                
        return nutrients

    def metabolize(self, nutrients):
        """
        Converts Nutrients into UPG Nodes.
        """
        print(f">> [DIGESTION] Found {len(nutrients)} items to process.")
        
        for item in nutrients:
            node_id = f"MODEL_{item['name'].upper().replace(' ', '_')}"
            
            if item['verdict'] == "SOLID":
                # MINT
                data = {
                    "id": node_id,
                    "type": NodeType.CODE.value, # It's a 'structure'
                    "content": f"Architecture: {item['name']}, Mass: {item['mass']}",
                    "mass": item['mass'],
                    "status": NodeStatus.ACTIVE.value
                }
                self.upg.add_node(node_id, data)
                print(f"   💎 ABSORBED: {item['name']} (+{item['mass']} Mass)")
                
            elif item['verdict'] == "FLUX":
                # REJECT / MARK HAZARD
                # We create the node first so we can mark it as hazard
                data = {
                    "id": node_id,
                    "type": NodeType.HAZARD.value,
                    "content": f"Architecture: {item['name']}, Mass: {item['mass']}",
                    "mass": item['mass'],
                    "status": NodeStatus.HAZARD.value
                }
                self.upg.add_node(node_id, data) # Add it to map
                self.upg.mark_hazard(node_id, f"Low Truth Mass ({item['mass']}). High Entropy Flux.")
                print(f"   🤢 EXPELLED: {item['name']} (Marked as Hazard)")

    def run(self):
        nutrients = self.ingest_report()
        if nutrients:
            self.metabolize(nutrients)
            print("\n>> [METABOLISM] Cycle Complete. UPG Updated.")
        else:
            print(">> [HUNGER] No nutrients found.")

if __name__ == "__main__":
    digester = SemanticDigester()
    digester.run()
