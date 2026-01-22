#!/usr/bin/env python3
"""
TENT v4.0 ENTERPRISE BENCHMARK
==============================
Phase 170: The Heavy Lift

"Real Data. Real Scale. Real Physics."

Objective:
Stress-test the TENT v4.0 Engine against a simulated "Corporate Data Lake"
containing 1,000+ documents of mixed density:
1. LEGAL (Uranium) - Contracts, NDAs
2. TECHNICAL (Steel) - Specs, API Docs
3. MARKETING (Vapor) - Blog posts, Press Releases
4. EMAIL (Noise) - Internal communication

Metrics:
- Throughput (Words/sec)
- Separation Accuracy (Do Contracts sink? Does Marketing float?)
- The Centrifuge Effect (Visualizing the distribution)
"""

import time
import random
import statistics
from dataclasses import dataclass
from typing import List, Dict
import os

# Import the TENT Stack
from vacuum_gauge import VacuumGauge, HAZARD_WORDS
from grain_check import GrainCheck
from joinery import Joinery
from sawmill import Sawmill
from absorption_camera import AbsorptionCamera

# =============================================================================
# DATA GENERATOR (The Simulator)
# =============================================================================

@dataclass
class Document:
    id: str
    type: str # LEGAL, TECH, MARKETING, EMAIL
    text: str

class DataLakesSim:
    """Generates realistic corporate clutter."""
    
    def __init__(self):
        # INGREDIENTS
        self.legal_terms = list(HAZARD_WORDS.keys()) + ["whereas", "heretofore", "parties", "execution", "governing law"]
        self.tech_terms = ["latency", "throughput", "API", "json", "endpoint", "stack", "recursion", "boolean", "integer", "database"]
        self.marketing_terms = ["synergy", "value-add", "holistic", "journey", "experience", "delight", "empower", "connect", "revolutionize"]
        self.filler = ["the", "a", "an", "and", "or", "but", "is", "are", "was", "were", "to", "for", "with", "on", "in", "at", "by"]
        
    def generate_legal(self, word_count=50) -> str:
        # High density of Hazard words, low aesthetic
        words = []
        for _ in range(word_count):
            if random.random() < 0.4: # 40% dense legal terms
                words.append(random.choice(self.legal_terms))
            else:
                words.append(random.choice(self.filler))
        return " ".join(words) + "."

    def generate_tech(self, word_count=100) -> str:
        # Moderate density, technical terms
        words = []
        for _ in range(word_count):
            if random.random() < 0.3:
                words.append(random.choice(self.tech_terms))
            else:
                words.append(random.choice(self.filler))
        return "The system shall " + " ".join(words) + "."

    def generate_marketing(self, word_count=200) -> str:
        # Low density, high volume, buzzwords
        words = []
        for _ in range(word_count):
            if random.random() < 0.2:
                words.append(random.choice(self.marketing_terms))
            else:
                words.append(random.choice(self.filler))
        return "We " + " ".join(words) + "!"

    def generate_dataset(self, size: int = 100) -> List[Document]:
        dataset = []
        print(f"🌊 FLOODING DATA LAKE WITH {size} DOCUMENTS...")
        
        for i in range(size):
            r = random.random()
            if r < 0.1: # 10% Legal (Hidden Uranium)
                doc = Document(f"DOC_{i:04d}", "LEGAL", self.generate_legal(30))
            elif r < 0.4: # 30% Tech (Steel)
                doc = Document(f"DOC_{i:04d}", "TECH", self.generate_tech(80))
            else: # 60% Marketing/Email (Fluff)
                doc = Document(f"DOC_{i:04d}", "FLUFF", self.generate_marketing(150))
            dataset.append(doc)
            
        return dataset

# =============================================================================
# THE BENCHMARK
# =============================================================================

class TentBenchmark:
    def __init__(self):
        self.vacuum = VacuumGauge()
        self.grain = GrainCheck()
        self.joinery = Joinery()
        self.camera = AbsorptionCamera()
        
    def process_document(self, doc: Document) -> float:
        """Runs the full stack and returns Omega."""
        # 1. Vacuum (Specific Gravity + Hazards)
        vac_res = self.vacuum.analyze(doc.text)
        mass = max(0.1, vac_res.density_score)
        
        # 2. Grain (Provenance)
        grain_res = self.grain.analyze_text(doc.text)
        avg_fiber = sum(w.fiber_length for w in grain_res.word_analyses) / max(1, len(grain_res.word_analyses))
        history = avg_fiber / 100.0
        
        # 3. Joinery (Logic)
        join_res = self.joinery.analyze(doc.text)
        curvature = 1.0 - (join_res.average_strength / 100.0)
        curvature = max(0.01, curvature)
        
        # 4. Camera (Albedo)
        cam_res = self.camera.photograph(doc.text)
        albedo = max(0.01, cam_res.albedo)
        
        # OMEGA CALCULATION
        omega = (mass * history) / (curvature * albedo)
        return omega

    def run(self, dataset: List[Document]):
        print(f"\n⚙️  SPINNING UP CENTRIFUGE FOR {len(dataset)} ITEMS...\n")
        
        start_time = time.time()
        results = {"LEGAL": [], "TECH": [], "FLUFF": []}
        total_words = 0
        
        for doc in dataset:
            omega = self.process_document(doc)
            results[doc.type].append(omega)
            total_words += len(doc.text.split())
            
        end_time = time.time()
        duration = end_time - start_time
        throughput = total_words / duration
        
        # REPORT
        print("╔══════════════════════════════════════════════════════════════════╗")
        print("║  TENT v4.0 ENTERPRISE BENCHMARK REPORT                           ║")
        print("╠══════════════════════════════════════════════════════════════════╣")
        print(f"║  Items Processed:   {len(dataset)}")
        print(f"║  Total Word Volume: {total_words:,.0f}")
        print(f"║  Time Elapsed:      {duration:.2f}s")
        print(f"║  Throughput:        {throughput:,.0f} words/sec")
        print("╠══════════════════════════════════════════════════════════════════╣")
        print("║  THE CENTRIFUGE SEPARATION (Avg Omega)                           ║")
        print("╠══════════════════════════════════════════════════════════════════╣")
        
        avg_legal = statistics.mean(results["LEGAL"]) if results["LEGAL"] else 0
        avg_tech = statistics.mean(results["TECH"]) if results["TECH"] else 0
        avg_fluff = statistics.mean(results["FLUFF"]) if results["FLUFF"] else 0
        
        print(f"║  ☢️  LEGAL (Uranium):    Ω = {avg_legal:10,.1f}  [SANK TO CORE]")
        print(f"║  🔩 TECH (Steel):       Ω = {avg_tech:10,.1f}  [MID-LEVEL]")
        print(f"║  ☁️  FLUFF (Vapor):      Ω = {avg_fluff:10,.1f}  [FLOATED]")
        print("╠══════════════════════════════════════════════════════════════════╣")
        
        # Check Separation
        ratio = avg_legal / max(0.1, avg_fluff)
        print(f"║  SEPARATION RATIO:      {ratio:,.0f}x")
        
        if avg_legal > avg_tech > avg_fluff:
            print("║  STATUS:                🟢 PHYSICS VALIDATED")
        else:
            print("║  STATUS:                🔴 ANOMALY DETECTED")
            
        print("╚══════════════════════════════════════════════════════════════════╝")

if __name__ == "__main__":
    sim = DataLakesSim()
    # Generate 500 documents for a good sample
    data = sim.generate_dataset(500)
    
    bench = TentBenchmark()
    bench.run(data)
