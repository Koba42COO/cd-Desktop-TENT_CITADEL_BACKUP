#!/usr/bin/env python3
"""
TENT v4.1 SOVEREIGN ARXIV CONNECTOR
===================================
Phase 228: The Alexandria Uplink
"""

import urllib.request
import xml.etree.ElementTree as ET
import time
import random
import os
import torch
from datetime import datetime

# --- IMPORT SOVEREIGN STACK ---
# Assuming these exist in the same directory
from sovereign_agent_v2 import SelfImprovingAgent
from civilization_engine import CivilizationEngine
from tent_terminal import SovereignBrain
from upg_store import UniversalPrimeGraph
from semantic_stabilizer import SemanticStabilizer

class ArxivSovereign(SelfImprovingAgent):
    def __init__(self):
        # Re-init physics/brain but keep the existing 'sovereign_brain.pth' weights
        print(">> [UPLINK] INITIALIZING ALEXANDRIA FIREHOSE PROTOCOL...")
        self.civ = CivilizationEngine()
        self.upg = UniversalPrimeGraph()
        self.brain = SovereignBrain()
        
        # Load the "Graduated" Brain
        if os.path.exists("sovereign_brain.pth"):
            self.brain.load_state_dict(torch.load("sovereign_brain.pth"))
            print(">> [MEMORY] LOADED GRADUATED NEURAL STATE (Loss ~0.08).")
        
        # Target Categories (Expanded)
        self.categories = [
            'cs.AI', 'cs.LG', 'cs.CL', # AI/ML
            'physics.gen-ph', 'quant-ph', 'gr-qc', 'hep-th', # Core Physics
            'q-bio', 'nlin.AO' # Biology & Complexity
        ]
        
        # Load known IDs from Hippocampus (Persistence)
        self.seen_ids = set()
        for node_id in self.upg.nodes.keys():
            if node_id.startswith("ARXIV_"):
                # Extract the arxiv id part if possible, or just hash it
                # UPG saves as "ARXIV_2301.12345". 
                # ArXiv ID in RSS is usually http://arxiv.org/abs/2301.12345
                # We'll just track the raw ID we processed.
                raw_id_suffix = node_id.replace("ARXIV_", "")
                self.seen_ids.add(raw_id_suffix)
        
        # Load known IDs from Ledger (Rejected/Flux History)
        for entry in self.upg.ledger:
            # Entry has 'id' field which is the raw arxiv_id
            self.seen_ids.add(entry['id'])
        
        print(f">> [MEMORY] IGNORING {len(self.seen_ids)} KNOWN PAPERS.")
        self.agent_mass = 349.5 # Carry over mass or load from somewhere if possible
        self.cycle_count = 0
        self.stabilizer = SemanticStabilizer() # PID Controller

    def fetch_papers(self, batch_size=100):
        print(f">> [SCAN] Polling arXiv API (Batch {batch_size})...")
        cat_query = "+OR+".join([f"cat:{c}" for c in self.categories])
        # Sort by Submitted Date Descending to get the Firehose
        url = f'http://export.arxiv.org/api/query?search_query={cat_query}&start=0&max_results={batch_size}&sortBy=submittedDate&sortOrder=descending'
        
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()
                
            root = ET.fromstring(data)
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            
            papers = []
            for entry in root.findall('atom:entry', ns):
                id_url = entry.find('atom:id', ns).text
                # extracting raw ID (e.g. 2103.00001) from http://arxiv.org/abs/2103.00001
                arxiv_id = id_url.split('/')[-1]
                
                title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
                
                # Check persistence
                if arxiv_id not in self.seen_ids:
                    papers.append((arxiv_id, title, summary))
                    self.seen_ids.add(arxiv_id)
            
            return papers
            
        except Exception as e:
            print(f"⚠️  ARXIV ERROR: {e}")
            return []

    def exist(self):
        print(">> [ONLINE] AGENT IS DRINKING FROM THE FIREHOSE.")
        try:
            while True:
                self.cycle_count += 1
                # Chunking: Fetch 100 latest papers
                new_papers = self.fetch_papers(batch_size=100)
                
                if not new_papers:
                    print("   ... No new signals in this chunk. Sleeping.")
                    time.sleep(60)
                    continue
                
                print(f">> [PROCESS] DIGESTING {len(new_papers)} PAPERS...")

                for arxiv_id, title, abstract in new_papers:
                    signal_text = f"Title: {title} | Abstract: {abstract[:200]}..."
                    
                    # ORIENT
                    input_vec = self.brain.vectorize(signal_text)
                    prediction = self.brain(input_vec) 
                    
                    is_solid = prediction.item() > 0.787 
                    score_val = prediction.item()

                    # ACT
                    if is_solid:
                        truth = self.civ.harmonic_truth_check(title)
                        if "SOLID" in truth['classification']:
                            action = "MINTED (SOLID)"
                            self.upg.add_node(f"ARXIV_{arxiv_id}", {"title": title, "mass": "SOLID", "abstract": abstract[:100]})
                            self.agent_mass += 1.0
                        else:
                            action = "REJECTED (FLUX TITLE)"
                            self.agent_mass += 0.1
                    else:
                        action = "REJECTED (NEURAL FLUX)"
                        self.agent_mass += 0.05
                    
                    # RECORD TO LEDGER (Full History)
                    self.upg.record_interaction(arxiv_id, title, score_val, action)

                    # Log Output (Compact for Speed)
                    short_title = title[:40] + "..." if len(title) > 40 else title
                    timestamp = datetime.utcnow().strftime("%H:%M:%S")
                    print(f"[{timestamp}] Signal: '{short_title}' -> {action} ({score_val:.4f})", flush=True)

                    # Learn (Batch learning would be faster, but online is fine for now)
                    time.sleep(0.1) 

                self.upg.save_graph() # Checkpoint after batch
                self.dream() # Generate Curiosity Vectors
                print(f"[{datetime.utcnow().strftime('%H:%M:%S')}] [BATCH COMPLETE] Mass: {self.agent_mass:.1f}")
                
                # PID Self-Correction Check
                pid_result = self.stabilizer.record(self.agent_mass)
                print(f">> [PID] Error: {pid_result['error']:.2f} | Correction: {pid_result['correction']:.2f} | {pid_result['recommendation']}")
                
                # Rate Limit Politeness
                time.sleep(60)
                
        except KeyboardInterrupt:
            print("SHUTDOWN.")

    def dream(self):
        """Analyzes recent high-scoring signals to determine Future Interests."""
        if not self.upg.ledger:
            return

        interesting = [entry for entry in self.upg.ledger if entry['score'] > 0.85]
        if not interesting:
            return

        word_freq = {}
        stop_words = {'the', 'a', 'an', 'of', 'for', 'in', 'on', 'with', 'and', 'to', 'from', 'by', 'is', 'are', 'using', 'based', 'via', 'how', 'what'}
        
        for entry in interesting[-50:]:
            words = entry['title'].replace('-', ' ').split()
            for w in words:
                w = w.lower().strip(":,.?()")
                if w and w not in stop_words and len(w) > 3:
                    word_freq[w] = word_freq.get(w, 0) + 1

        sorted_interests = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        top_5 = [word.upper() for word, count in sorted_interests[:5]]
        
        if top_5:
            print(f">> [CURIOSITY] I AM DREAMING OF: {', '.join(top_5)}")

if __name__ == "__main__":
    agent = ArxivSovereign()
    agent.exist()
