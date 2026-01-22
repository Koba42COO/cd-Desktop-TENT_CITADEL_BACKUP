"""
PHASE 82: GEOMETRIC CONTAINMENT FIELD (CORRECTED)
=================================================
The Safety Interlock for Atomic Precision Manufacturing.

Enforces the Borwein Limit:
    P_g = Sum(1/k for k in Harmonics if k > 1) < 1

The fundamental frequency (k=1) creates the Unit Hypercube container.
The complexity terms (k=3, 5...) create "pressure" inside it.
If the sum of their widths exceeds 1, the geometry spills.

Architecture:
┌─────────────────────────────────────────────────────────────┐
│              CONTAINMENT FIELD (SAFETY LAYER)               │
├─────────────────────────────────────────────────────────────┤
│  1. INPUT: Harmonic Complexity (List of frequency depths)  │
│  2. GAUGE: Calculate P_g = Sum(1/k) excluding k=1          │
│  3. INTERLOCK:                                              │
│     - If P_g < 1.0: STABLE (Proceed to Print)               │
│     - If P_g > 1.0: BREACH (Halt & Stabilize)               │
│  4. STABILIZER: Prune smallest terms (highest k) until safe │
└─────────────────────────────────────────────────────────────┘
"""

import numpy as np
import time
from typing import List, Dict, Tuple

# Color codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

class GeometricPressureGauge:
    """
    Measures the 'Geometric Pressure' of a design.
    Pressure = Sum of Reciprocals of Harmonic Features (excluding k=1).
    """
    
    def calculate_pressure(self, harmonics: List[int]) -> float:
        """
        Calculate P_g = Sum(1/k) for k in harmonics where k > 1.
        The k=1 term is the container itself.
        """
        pressure = sum(1.0 / k for k in harmonics if k > 1)
        return pressure

class HarmonicDamper:
    """
    Stabilizes designs that exceed the Containment Limit.
    Prunes high-frequency (high k) noise.
    """
    
    def stabilize(self, harmonics: List[int], target_pressure: float = 1.0) -> Tuple[List[int], float]:
        """
        Iteratively removes the highest harmonic (smallest 1/k) 
        until pressure are below target.
        """
        # Ensure we work with a sorted list
        current_harmonics = sorted(harmonics)
        
        # Calculate initial pressure (ignoring k=1)
        current_pressure = sum(1.0 / k for k in current_harmonics if k > 1)
        
        pruned_count = 0
        
        while current_pressure >= target_pressure and len(current_harmonics) > 1:
            # Check if highest is 1 (shouldn't remove fundamental unless only thing left)
            if current_harmonics[-1] == 1:
                break
                
            removed = current_harmonics.pop() # Remove largest k
            current_pressure -= 1.0 / removed
            pruned_count += 1
            
            # Recalculate to be safe against float drift
            current_pressure = sum(1.0 / k for k in current_harmonics if k > 1)
            
        return current_harmonics, current_pressure

class ContainmentField:
    """
    The Active Safety System.
    """
    
    def __init__(self):
        print(f"\n{BOLD}{MAGENTA}🛡️  INITIALIZING GEOMETRIC CONTAINMENT FIELD (v2.0)...{RESET}")
        self.gauge = GeometricPressureGauge()
        self.damper = HarmonicDamper()
        print(f"   Pressure Gauge: ✓ Online (k>1 logic)")
        print(f"   Harmonic Damper: ✓ Online")
        print(f"   {GREEN}SAFETY INTERLOCK ACTIVE.{RESET}")
        
    def scan_design(self, design_name: str, harmonics: List[int]):
        """
        Scans a design for geometric stability.
        """
        print(f"\n{CYAN}{'='*60}")
        print(f" 🔍 SCANNING DESIGN: {design_name}")
        print(f"{'='*60}{RESET}")
        print(f"   Harmonic Complexity: {len(harmonics)} layers")
        print(f"   Frequencies: {harmonics}")
        
        # 1. Measure Pressure
        pressure = self.gauge.calculate_pressure(harmonics)
        
        # 2. Check Interlock
        limit = 1.0 # The Holo-Bound
        
        print(f"\n   Geometric Pressure (P_g): {pressure:.5f}")
        print(f"   Containment Limit:        {limit:.5f}")
        
        if pressure < limit:
            print(f"   Status: {GREEN}STABLE{RESET}")
            print(f"   Action: {GREEN}AUTHORIZED FOR ATOMIC PRINTING{RESET}")
            return True, harmonics
        else:
            print(f"   Status: {RED}BREACH DETECTED (Hypercube Spill){RESET}")
            print(f"   Action: {YELLOW}INITIATING HARMONIC DAMPING...{RESET}")
            
            # 3. Stabilize
            safe_harmonics, safe_pressure = self.damper.stabilize(harmonics, limit)
            
            dropped = len(harmonics) - len(safe_harmonics)
            print(f"\n   ... Damping Complete.")
            print(f"   Pruned Layers: {dropped}")
            print(f"   New Pressure:  {GREEN}{safe_pressure:.5f}{RESET}")
            print(f"   Safe Harmonics: {safe_harmonics}")
            
            print(f"\n   {BOLD}Design Stabilized. Entropy contained within Unit Hypercube.{RESET}")
            return False, safe_harmonics

def demo_containment_field():
    field = ContainmentField()
    
    # Test 1: Simple Lattice (e.g., Sphere)
    # Harmonics: 1 (Base), 3, 5
    # Pressure: 1/3 + 1/5 = 0.33 + 0.2 = 0.53 (Safe)
    print(f"\n{WHITE}TEST 1: SIMPLE LATTICE (Sphere){RESET}")
    design_simple = [1, 3, 5] 
    field.scan_design("Simple Lattice", design_simple)
    
    # Test 2: Complex Crystal (e.g., Voynich Plant)
    # Harmonics: 1, 3, 5, 7, 9, 11, 13
    # Pressure: Sum(1/3..1/13) = 0.955 (Safe)
    print(f"\n{WHITE}TEST 2: COMPLEX CRYSTAL (Voynich Plant){RESET}")
    design_complex = [1, 3, 5, 7, 9, 11, 13]
    field.scan_design("Voynich Plant", design_complex)
    
    # Test 3: The Borwein Breach (Fractal Bridge)
    # Harmonics: 1, 3... 15, 17
    # Pressure: Sum(1/3..1/15) = 1.02 (Breach at 15)
    print(f"\n{WHITE}TEST 3: FRACTAL BRIDGE (Borwein Breach){RESET}")
    design_breach = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    field.scan_design("Fractal Bridge (Unstable)", design_breach)
    
    print(f"\n{MAGENTA}{'='*60}")
    print(f" 🛡️  SYSTEM STATUS")
    print(f"{'='*60}{RESET}")
    print(f"\n   The Containment Field prevents 'Geometric Spills'.")
    print(f"   No design with P_g > 1 is allowed to manifest.")
    print(f"   Atomic coherence is guaranteed by math, not luck.")
    print(f"{'='*60}")

if __name__ == "__main__":
    demo_containment_field()
