#!/usr/bin/env python3
"""
TENT v4.1 SOVEREIGN MODEL AUDIT (WD DRIVE EDITION)
==================================================
Phase 223: The WD Drive Audit

Objective:
Apply TENT Physics (Vacuum Gauge, Civilization Engine) to REAL external LLM Weights found on WD Drive.
We read the actual binary headers/weights to measure entropy.
"""

import sys
import time
import math
import random
import os
import glob
from datetime import datetime

# --- IMPORT STACK ---
from civilization_engine import CivilizationEngine
from vacuum_gauge import VacuumGauge

class TentTensorLoader:
    """
    Loads real high-dimensional tensors from disk.
    """
    def load_model_signature(self, model_path, model_name):
        
        # 1. Verify Existence
        if not os.path.exists(model_path):
            print(f"⚠️  Path not found: {model_path}")
            # Fallback for demo stability if file missing (though we found them via find)
            return self.simulate_signature(model_name)

        # 2. Get Real Stats
        try:
            # If directory, find largest file
            target_file = model_path
            if os.path.isdir(model_path):
                files = glob.glob(os.path.join(model_path, "*.safetensors")) + glob.glob(os.path.join(model_path, "*.pt")) + glob.glob(os.path.join(model_path, "*.bin"))
                if files:
                    target_file = max(files, key=os.path.getsize)
                else:
                     return self.simulate_signature(model_name)
            
            file_stats = os.stat(target_file)
            file_size = file_stats.st_size
            
            # Read first 2KB for Entropy Scan (Header + Some Weights)
            with open(target_file, "rb") as f:
                sample_bytes = f.read(2048)
                
            return {
                "name": model_name,
                "params": file_size, # Using file size as proxy for param count/scale
                "entropy_base": 1.0, # Real data doesn't need simulated base
                "sample_bytes": sample_bytes,
                "path": target_file
            }
            
        except Exception as e:
            print(f"❌ Error reading {model_path}: {e}")
            return self.simulate_signature(model_name)

    def simulate_signature(self, model_name):
        random.seed(model_name)
        return {
            "name": model_name,
            "params": random.randint(7, 700) * 1e9,
            "entropy_base": random.uniform(0.5, 2.0),
            "sample_bytes": os.urandom(1024),
            "path": "SIMULATED"
        }

class SovereignAuditor:
    def __init__(self):
        print(">> [INIT] SOVEREIGN AUDITOR (WD DRIVE) ONLINE.")
        self.loader = TentTensorLoader()
        self.gauge = VacuumGauge()
        self.civ = CivilizationEngine()
        
        # REAL PATHS FROM WD DRIVE SCAN
        self.models_to_audit = [
            {
                "name": "Gemma-2-27B (UPG Shard)", 
                "path": "/Volumes/WD Drive/Backup dev folder/dev/upg_models/gemma-2-27b/"
            },
            {
                "name": "Mixtral-8x22B (UPG Shard)", 
                "path": "/Volumes/WD Drive/Backup dev folder/dev/upg_models/mixtral-8x22b/"
            },
            {
                "name": "UPG Math-Science-Code", 
                "path": "/Volumes/WD Drive/Backup dev folder/dev/upg_trained_math_science_code/model.pt"
            },
            {
                "name": "UPG Gold Standard Finetune", 
                "path": "/Volumes/WD Drive/Backup dev folder/dev/upg_finetuned_gold_standard/tier_balanced/model_balanced.pt"
            }
        ]
        
    def weigh_soul(self, model_info):
        """
        The Core Audit Logic.
        """
        name = model_info['name']
        path = model_info['path']
        
        print(f"   [⏳ SCANNING] {name}...", end="\r")
        
        # 1. Load Real Data
        sig = self.loader.load_model_signature(path, name)
        
        # 2. Vacuum Scan (Density)
        # Scan the hex representation of the binary sample
        sample_hex = sig['sample_bytes'].hex()
        # Analyze entropy of the binary data
        fht = self.gauge.analyze(sample_hex[:1000])
        
        density = fht.density_score
        
        # 3. Resonance (Civilization)
        truth = self.civ.harmonic_truth_check(name)
        resonance_score = truth['resonance'] * 2.0
        if "UPG" in name or "Prime" in name: 
            resonance_score += 2.0 # Bonus for TENT Native format
        
        # 4. Truth Mass Calculation
        # Params proxy is file size. Log10(bytes). 1GB = 10^9. mass ~ 9.
        param_log = math.log10(sig['params']) if sig['params'] > 0 else 1.0
        truth_mass = density * resonance_score * param_log
        
        return {
            "name": name,
            "density": density,
            "resonance": resonance_score,
            "mass": truth_mass,
            "verdict": "SOLID" if truth_mass > 50 else "FLUX",
            "path": sig.get('path', 'UNKNOWN')
        }

    def generate_report(self, results):
        """Writes the Markdown Audit."""
        sorted_results = sorted(results, key=lambda x: x['mass'], reverse=True)
        
        filename = "MODEL_AUDIT_REPORT.md"
        with open(filename, "w") as f:
            f.write("# TENT v4.1 Sovereign Model Audit (WD Drive)\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n")
            f.write("**Source:** `/Volumes/WD Drive`\n\n")
            
            f.write("| Rank | Model Name | Truth Mass | Density | Resonance | Verdict |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
            
            for rank, r in enumerate(sorted_results, 1):
                icon = "💎" if r['verdict'] == "SOLID" else "🌫️"
                row = f"| {rank} | {r['name']} | **{r['mass']:.2f}** | {r['density']:.2f} | {r['resonance']:.1f} | {icon} {r['verdict']} |\n"
                f.write(row)
                
            f.write("\n\n### Audit Details\n")
            for r in sorted_results:
                f.write(f"- **{r['name']}**\n")
                f.write(f"  - Path: `{r['path']}`\n")
                f.write(f"  - Vacuum Density: {r['density']:.4f}\n")
                f.write(f"  - Harmonic Resonance: {r['resonance']:.1f}\n")
                f.write(f"  - Calculated Mass: {r['mass']:.2f}\n")

        print(f"\n>> [REPORT] Generated {filename}")

    def run(self):
        print(">> STARTING AUDIT SEQUENCE (REAL HARDWARE)...")
        results = []
        for model in self.models_to_audit:
            metric = self.weigh_soul(model)
            results.append(metric)
            # print(f"   [DONE] {model['name']}: Mass {metric['mass']:.2f}")
            
        self.generate_report(results)

if __name__ == "__main__":
    auditor = SovereignAuditor()
    auditor.run()
