#!/usr/bin/env python3
"""
TENT v4.0 FHT CALIBRATION
=========================
The Sober Build - First Calibration Run

Tests the Fractal Harmonic Transform against live code.
"""

import math
from vacuum_gauge import VacuumGauge

# Golden Ratio
PHI = (1 + math.sqrt(5)) / 2

def fht_transform(entropy: float) -> float:
    """
    T(x) = |log(x)|^φ
    The Topological Filter.
    """
    if entropy <= 0:
        return 0.0
    return abs(math.log(entropy)) ** PHI

def calibrate_fht():
    print("="*60)
    print("   ⛺  TENT v4.0  |  FHT CALIBRATION")
    print("   PHASE 199: THE SOBER BUILD")
    print("="*60)
    print(f"\n   φ = {PHI:.6f} (Golden Ratio)")
    print(f"   T(x) = |log(x)|^φ\n")
    
    gauge = VacuumGauge()
    
    # Test Files - Live Code
    test_files = [
        ("vacuum_gauge.py", "Core Physics"),
        ("kwyc_core.py", "Ledger"),
        ("upg_store.py", "Graph"),
        ("command_deck.py", "Interface"),
        ("wallace_tree_assembler.py", "Assembler"),
    ]
    
    print("--- FHT CALIBRATION SCAN ---")
    print(f"{'File':<30} {'Entropy':<12} {'FHT':<12} {'Class':<10}")
    print("-" * 64)
    
    results = []
    
    for filename, category in test_files:
        try:
            with open(filename, 'r') as f:
                content = f.read()
            
            # Run VacuumGauge
            analysis = gauge.analyze(content[:2000])  # First 2KB
            entropy = analysis.shannon_entropy
            density = analysis.density_score
            
            # Apply FHT Transform
            fht_score = fht_transform(entropy)
            
            # Classification
            if density >= 2.0:
                cls = "💎 DIAMOND"
            elif density >= 1.0:
                cls = "✨ CRYSTAL"
            elif density >= 0.5:
                cls = "☁️  VAPOR"
            else:
                cls = "🫧 BUBBLE"
            
            results.append({
                "file": filename,
                "entropy": entropy,
                "fht": fht_score,
                "density": density,
                "class": cls
            })
            
            print(f"{filename:<30} {entropy:<12.4f} {fht_score:<12.4f} {cls}")
            
        except FileNotFoundError:
            print(f"{filename:<30} {'N/A':<12} {'N/A':<12} {'MISSING'}")
    
    # Summary
    print("\n" + "="*64)
    print("   CALIBRATION SUMMARY")
    print("="*64)
    
    avg_entropy = sum(r['entropy'] for r in results) / len(results) if results else 0
    avg_fht = sum(r['fht'] for r in results) / len(results) if results else 0
    
    print(f"\n   Avg Entropy:  {avg_entropy:.4f}")
    print(f"   Avg FHT:      {avg_fht:.4f}")
    print(f"   Files Scanned: {len(results)}")
    
    diamond_count = sum(1 for r in results if "DIAMOND" in r['class'])
    print(f"   Diamonds:     {diamond_count}/{len(results)}")
    
    print("\n>> FHT CALIBRATION COMPLETE.")
    print(">> System is LIVE.")

if __name__ == "__main__":
    calibrate_fht()
