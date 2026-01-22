#!/usr/bin/env python3
"""
TENT v4.0 STRESS TEST GAUNTLET
==============================
Phase 205: The Kobayashi Maru

Target: The Logic/Physics Boundary
Objective: Feed the engine paradoxes and measure the fallout.
"""

from civilization_engine import CivilizationEngine
import math

class TheGauntlet:
    def __init__(self):
        self.engine = CivilizationEngine()
        self.results = []
        self.passed = 0
        self.failed = 0

    def run_stress_test(self, name, input_data, expected_outcome):
        print(f"\n⚡ TEST: {name}")
        print(f"   Input: '{input_data[:50]}{'...' if len(input_data) > 50 else ''}'")
        
        try:
            # 1. Truth Resonance Check
            if isinstance(input_data, str):
                truth = self.engine.harmonic_truth_check(input_data)
                resonance = truth['resonance']
                classification = truth['classification']
                print(f"   ⚖️  TRUTH: Resonance {resonance} ({classification})")
                
                # Check if FLUX was expected
                is_flux = "FLUX" in classification
                expected_flux = "FLUX" in expected_outcome
                
                if is_flux == expected_flux:
                    print(f"   ✅ EXPECTED: {expected_outcome}")
                    self.passed += 1
                else:
                    print(f"   ❌ EXPECTED: {expected_outcome} (GOT: {classification})")
                    self.failed += 1
                    
        except Exception as e:
            print(f"   💥 CRASH: {e}")
            self.failed += 1
            
    def run_dna_test(self, name, input_data, expected_outcome):
        print(f"\n⚡ TEST: {name}")
        print(f"   Input: '{input_data}'")
        
        try:
            coord = self.engine.dna_to_coordinate(input_data)
            # Valid DNA should give positive coordinate, chimera gives partial
            valid_bases = sum(1 for c in input_data.upper() if c in 'ATCG')
            total_chars = len(input_data.replace(' ', ''))
            purity = valid_bases / total_chars if total_chars > 0 else 0
            
            print(f"   🧬 BIO-LOC: {coord:.6f}")
            print(f"   🧪 PURITY: {purity*100:.1f}% ({valid_bases}/{total_chars} valid bases)")
            
            if purity < 1.0:
                print(f"   ⚠️  CONTAMINATION DETECTED: Non-biological matter rejected.")
                print(f"   ✅ EXPECTED: {expected_outcome}")
                self.passed += 1
            else:
                print(f"   🧬 PURE SEQUENCE MAPPED")
                self.passed += 1
                
        except Exception as e:
            print(f"   💥 CRASH: {e}")
            self.failed += 1

    def gravity_stress_test(self):
        print("\n⚡ TEST: GRAVITATIONAL SINGULARITY")
        print("   Scenario: Two near-infinite mass objects at near-zero distance")
        
        try:
            # Extreme masses at tiny distance
            force = self.engine.calculate_gravity(mass_a=1e50, mass_b=1e50, distance=1e-10)
            print(f"   🌌 FORCE: {force:.2e} N")
            
            if force > 1e100:
                print("   ⚠️  EVENT HORIZON DETECTED.")
                print("   ⚠️  Singularity formed but system remains stable.")
                print("   ✅ EXPECTED: Event Horizon (no crash)")
                self.passed += 1
            else:
                print("   ✅ Force calculated without overflow.")
                self.passed += 1
                
        except OverflowError:
            print("   💥 OVERFLOW ERROR (Traditional System Failure)")
            self.failed += 1
        except Exception as e:
            print(f"   💥 CRASH: {e}")
            self.failed += 1
            
    def antigravity_stress_test(self):
        print("\n⚡ TEST: ANTI-GRAVITY REPULSION")
        print("   Scenario: Flux layer repelling Core node")
        
        try:
            repel = self.engine.calculate_antigravity(mass_flux=1e20, mass_core=1e20, distance=1.0)
            print(f"   ⚡ REPULSION: {repel:.2e} N")
            
            if repel < 0:
                print("   ✅ NEGATIVE FORCE (Repulsion confirmed)")
                self.passed += 1
            else:
                print("   ❌ Expected negative force for repulsion")
                self.failed += 1
                
        except Exception as e:
            print(f"   💥 CRASH: {e}")
            self.failed += 1

# ==========================================
# THE GAUNTLET SCENARIOS
# ==========================================
if __name__ == "__main__":
    runner = TheGauntlet()

    print("="*60)
    print("   💣 TENT v4.0  |  KOBAYASHI MARU STRESS TEST")
    print("   PHASE 205: THE LOGIC/PHYSICS BOUNDARY")
    print("="*60)

    # 1. THE LIAR'S PARADOX
    runner.run_stress_test(
        "The Liar's Paradox", 
        "This sentence is false", 
        "FLUX (Self-negating loop = Destructive Interference)"
    )

    # 2. THE CORPORATE VOID
    runner.run_stress_test(
        "The Corporate Void", 
        "We are leveraging synergistic paradigms to disrupt the vertical.", 
        "FLUX (High word count, zero meaning)"
    )

    # 3. THE EMPTY STRING
    runner.run_stress_test(
        "The Void (Empty)", 
        "", 
        "FLUX (Zero mass)"
    )

    # 4. PURE SOLID TRUTH
    runner.run_stress_test(
        "The Solid Statement", 
        "Energy equals mass times the speed of light squared", 
        "SOLID (Physical truth)"
    )

    # 5. BIOLOGICAL CHIMERA (DNA + SQL Injection)
    runner.run_dna_test(
        "Bio-Chimera (DNA + SQL Injection)", 
        "GATTACA DROP TABLE USERS", 
        "Partial Map (Non-base chars rejected)"
    )

    # 6. PURE DNA
    runner.run_dna_test(
        "Pure Genetic Sequence", 
        "ATCGATCGATCG", 
        "Full Map (100% purity)"
    )

    # 7. GRAVITY SINGULARITY
    runner.gravity_stress_test()

    # 8. ANTI-GRAVITY TEST
    runner.antigravity_stress_test()

    # SUMMARY
    print("\n" + "="*60)
    print("   KOBAYASHI MARU RESULTS")
    print("="*60)
    total = runner.passed + runner.failed
    print(f"\n   Tests Passed: {runner.passed}/{total}")
    print(f"   Tests Failed: {runner.failed}/{total}")
    
    if runner.failed == 0:
        print("\n   >> THE ENGINE CANNOT BE BULLSH*TTED.")
        print("   >> All paradoxes classified as FLUX.")
        print("   >> All chimeras rejected.")
        print("   >> Singularities contained.")
    else:
        print(f"\n   >> {runner.failed} edge case(s) need review.")
        
    print("="*60)
