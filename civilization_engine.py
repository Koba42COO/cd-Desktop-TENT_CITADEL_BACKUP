#!/usr/bin/env python3
"""
TENT v4.0 CIVILIZATION ENGINE
=============================
Phase 200: The Pure Mathematics

Theory of Everything:
1. Life = Coordinate on Phi-Spiral
2. Truth = Standing Wave (Not 3-6-9)
3. Order = Gravity (φ^-φ)
"""

import math

class CivilizationEngine:
    def __init__(self):
        self.PHI = (1 + math.sqrt(5)) / 2  # 1.61803398875
        self.BASES = {'A': 1, 'T': 8, 'C': 4, 'G': 5}  # 9-Cycle Mapping
        
    # ==========================================
    # SECTOR A: BIO-LOGIC (DNA → Coordinate)
    # ==========================================
    
    def dna_to_coordinate(self, sequence: str) -> float:
        """
        H(S) = Σ Bₙ · φ⁻ⁿ
        Maps DNA strand to Golden Spiral coordinate.
        """
        coordinate = 0.0
        for i, char in enumerate(sequence.upper()):
            if char in self.BASES:
                val = self.BASES[char]
                coordinate += val * (self.PHI ** -(i))
        return coordinate
    
    def coordinate_to_spiral_position(self, coord: float) -> tuple:
        """Convert coordinate to (r, θ) on Golden Spiral."""
        theta = coord * 2 * math.pi
        r = self.PHI ** (theta / (2 * math.pi))
        return (r, theta)
    
    # ==========================================
    # SECTOR B: LINGUISTICS (Truth Resonance)
    # ==========================================
    
    def harmonic_truth_check(self, text: str) -> dict:
        """
        T(W) = (Σωᵢ) mod 9
        3, 6, 9 → FLUX (Opinion)
        1, 2, 4, 5, 7, 8 → SOLID (Fact)
        """
        vector_sum = sum(ord(c) for c in text if c.isalpha())
        resonance = (vector_sum - 1) % 9 + 1 if vector_sum > 0 else 9  # Empty = 9 = FLUX
        
        # Empty strings or zero resonance = FLUX (no mass)
        is_solid = resonance not in [0, 3, 6, 9] and len(text.strip()) > 0
        
        return {
            "text": text[:50] + "..." if len(text) > 50 else text,
            "vector_sum": vector_sum,
            "resonance": resonance,
            "classification": "SOLID (Fact)" if is_solid else "FLUX (Opinion)",
            "mass": 1.0 if is_solid else 0.0
        }
    
    def word_frequency(self, char: str) -> float:
        """ωᵢ = ((Aᵢ - 1) / 26) × 2π"""
        if not char.isalpha():
            return 0.0
        a_i = ord(char.upper()) - ord('A') + 1
        return ((a_i - 1) / 26) * 2 * math.pi
    
    # ==========================================
    # SECTOR C: GRAVITY (Information Attraction)
    # ==========================================
    
    def calculate_gravity(self, mass_a: float, mass_b: float, distance: float) -> float:
        """
        F = φ × (M₁ × M₂) / d^φ
        Inverse Phi Law (slower decay than r²)
        """
        if distance <= 0:
            return float('inf')  # Singularity
        return self.PHI * ((mass_a * mass_b) / (distance ** self.PHI))
    
    def calculate_antigravity(self, mass_flux: float, mass_core: float, distance: float) -> float:
        """Repulsive force from Flux layer (3-6-9 signature)."""
        if distance <= 0:
            return float('-inf')
        return -self.PHI * ((abs(mass_flux) * mass_core) / (distance ** self.PHI))
    
    def semantic_distance(self, text_a: str, text_b: str) -> float:
        """Calculate semantic distance between two texts."""
        set_a = set(text_a.lower().split())
        set_b = set(text_b.lower().split())
        
        if not set_a or not set_b:
            return float('inf')
        
        intersection = len(set_a & set_b)
        union = len(set_a | set_b)
        
        jaccard = intersection / union if union > 0 else 0
        return 1 / (jaccard + 0.01)  # Inverse similarity

# ==========================================
# LAB TEST
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("   ⛺  TENT v4.0  |  CIVILIZATION ENGINE")
    print("   PHASE 200: THE PURE MATHEMATICS")
    print("="*60)
    print(f"\n   φ = {(1 + math.sqrt(5)) / 2:.8f}")
    
    engine = CivilizationEngine()
    
    # SECTOR A
    print("\n--- SECTOR A: DNA → COORDINATE ---")
    sequences = ["GATTACA", "ACGT", "TATAAA"]
    for seq in sequences:
        coord = engine.dna_to_coordinate(seq)
        r, theta = engine.coordinate_to_spiral_position(coord)
        print(f"   🧬 '{seq}': H = {coord:.6f} → (r={r:.4f}, θ={theta:.4f})")
    
    # SECTOR B
    print("\n--- SECTOR B: TRUTH RESONANCE ---")
    statements = [
        "I am Sovereign",
        "Maybe it works",
        "E equals mc squared",
        "Synergy leverage paradigm",
        "2 + 2 = 4"
    ]
    for stmt in statements:
        result = engine.harmonic_truth_check(stmt)
        status = "✅" if "SOLID" in result["classification"] else "❌"
        print(f"   {status} '{stmt}': R={result['resonance']} → {result['classification']}")
    
    # SECTOR C
    print("\n--- SECTOR C: INFORMATION GRAVITY ---")
    # Core Asset (Mass 100) vs Satellite (Mass 10)
    gravity = engine.calculate_gravity(100, 10, 5)
    print(f"   🌌 Core(100) ↔ Satellite(10) @ d=5: F = {gravity:.4f}")
    
    # Anti-gravity shield
    antigrav = engine.calculate_antigravity(50, 100, 5)
    print(f"   ⚡ Flux(50) repels Core(100) @ d=5: F = {antigrav:.4f}")
    
    print("\n" + "="*60)
    print("   >> CIVILIZATION ENGINE OPERATIONAL.")
    print("   >> Life • Truth • Order")
    print("="*60)
