#!/usr/bin/env python3
"""
TENT v4.0 MASS VALIDATION SUITE
===============================
Phase 206: 10,000+ TESTS

Parametric testing across all modules:
- DNA Mapping: 2,000 random sequences
- Truth Resonance: 2,000 random strings
- Gravity: 2,000 random mass/distance pairs
- Physics: 2,000 random physics inputs
- Edge Cases: 2,000 fuzzing scenarios
"""

import random
import string
import math
import time
import sys
from dataclasses import dataclass
from typing import List, Tuple, Callable

# Import all modules
from civilization_engine import CivilizationEngine
from vacuum_gauge import VacuumGauge
from mechanics_core import DynamicsEngine
from quantum_throd import QuantumThrodEngine, QuantumState
from electromagnetism_core import ElectromagnetismEngine
from thermodynamics_core import ThermodynamicsEngine, ThermoState
from relativity_core import RelativityEngine
from wallace_tree_assembler import WallaceTreeAssembler, PartialProduct
from upg_store import PrimeNode, NodeType

@dataclass
class TestBatch:
    name: str
    passed: int
    failed: int
    errors: List[str]
    duration: float

class MassValidationSuite:
    def __init__(self, tests_per_category: int = 2000):
        self.n = tests_per_category
        self.civ = CivilizationEngine()
        self.gauge = VacuumGauge()
        self.mechanics = DynamicsEngine()
        self.quantum = QuantumThrodEngine()
        self.em = ElectromagnetismEngine()
        self.thermo = ThermodynamicsEngine()
        self.relativity = RelativityEngine()
        self.wallace = WallaceTreeAssembler()
        self.batches: List[TestBatch] = []
        
    def run_batch(self, name: str, test_func: Callable) -> TestBatch:
        """Run a batch of tests and collect results."""
        start = time.time()
        passed = 0
        failed = 0
        errors = []
        
        for i in range(self.n):
            try:
                result = test_func(i)
                if result:
                    passed += 1
                else:
                    failed += 1
                    if len(errors) < 5:
                        errors.append(f"Test {i}: returned False")
            except Exception as e:
                failed += 1
                if len(errors) < 5:
                    errors.append(f"Test {i}: {str(e)[:50]}")
        
        duration = time.time() - start
        batch = TestBatch(name, passed, failed, errors, duration)
        self.batches.append(batch)
        return batch

    # ==========================================
    # TEST GENERATORS
    # ==========================================
    
    def test_dna_mapping(self, i: int) -> bool:
        """Test DNA → Coordinate mapping with random sequences."""
        length = random.randint(3, 100)
        bases = ''.join(random.choices('ATCG', k=length))
        coord = self.civ.dna_to_coordinate(bases)
        # Coordinate should be positive and finite
        return coord > 0 and math.isfinite(coord)
    
    def test_truth_resonance(self, i: int) -> bool:
        """Test truth resonance with random strings."""
        length = random.randint(5, 200)
        text = ''.join(random.choices(string.ascii_letters + ' ', k=length))
        result = self.civ.harmonic_truth_check(text)
        # Should return valid classification
        return result['resonance'] in range(1, 10) and result['classification'] in ["SOLID (Fact)", "FLUX (Opinion)"]
    
    def test_gravity(self, i: int) -> bool:
        """Test gravity with random mass/distance combinations."""
        m1 = random.uniform(0.1, 1e30)
        m2 = random.uniform(0.1, 1e30)
        d = random.uniform(0.001, 1e10)
        force = self.civ.calculate_gravity(m1, m2, d)
        # Force should be positive and finite
        return force > 0 and math.isfinite(force)
    
    def test_fht_density(self, i: int) -> bool:
        """Test FHT density calculation with random text."""
        length = random.randint(10, 500)
        text = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))
        result = self.gauge.analyze(text)
        # Density should be non-negative
        return result.density_score >= 0
    
    def test_mechanics(self, i: int) -> bool:
        """Test mechanics with random mass/force."""
        mass = random.uniform(0.1, 1e6)
        force = random.uniform(0.1, 1e6)
        node = PrimeNode(i, NodeType.MEDIA, f"TEST_{i}", mass=mass)
        traj = self.mechanics.simulate_trajectory(node, force, steps=3)
        return len(traj) == 4  # Initial + 3 steps
    
    def test_quantum(self, i: int) -> bool:
        """Test quantum uncertainty with random states."""
        mass = random.uniform(1, 100)
        vel = random.uniform(0.1, 100)
        state = QuantumState(mass_true=mass, velocity_true=vel, position_true=0.0)
        result = self.quantum.measure_observable(state, random.choice(['mass', 'velocity']))
        return 'mass' in result and 'velocity' in result
    
    def test_electromagnetism(self, i: int) -> bool:
        """Test EM with random charges/distances."""
        charge = random.uniform(1e-9, 1e-3)
        distance = random.uniform(0.001, 100)
        e_field = self.em.calculate_e_field(charge, distance)
        return e_field > 0 and math.isfinite(e_field)
    
    def test_thermodynamics(self, i: int) -> bool:
        """Test thermodynamics with random states."""
        state = ThermoState(
            internal_energy=random.uniform(100, 10000),
            temperature=random.uniform(100, 1000),
            entropy=random.uniform(1, 100),
            volume=random.uniform(0.1, 10),
            pressure=random.uniform(1e4, 1e6)
        )
        new_state = self.thermo.first_law(state, heat_in=random.uniform(0, 1000), work_done=random.uniform(0, 500))
        return new_state.temperature > 0
    
    def test_relativity(self, i: int) -> bool:
        """Test relativity with random velocities."""
        C = 299792458
        v = random.uniform(0, 0.99 * C)
        gamma = self.relativity.lorentz_factor(v)
        return gamma >= 1 and math.isfinite(gamma)
    
    def test_wallace_tree(self, i: int) -> bool:
        """Test Wallace tree with random product counts."""
        n_products = random.randint(3, 50)
        products = [PartialProduct(f"P{j}", random.randint(0, 1), 0.1) for j in range(n_products)]
        reduced, depth = self.wallace.wallace_tree_reduction(products)
        return len(reduced) <= 2 and depth >= 0
    
    def test_edge_cases(self, i: int) -> bool:
        """Fuzz with edge cases."""
        edge_cases = [
            lambda: self.civ.harmonic_truth_check(""),
            lambda: self.civ.harmonic_truth_check(" " * 100),
            lambda: self.civ.dna_to_coordinate("XXXX"),
            lambda: self.civ.calculate_gravity(0.001, 0.001, 0.001),
            lambda: self.gauge.analyze("a" * 1000),
        ]
        try:
            func = random.choice(edge_cases)
            func()
            return True
        except:
            return False
    
    def run_all(self):
        """Execute all test batches."""
        print("="*70)
        print("   ⛺  TENT v4.0  |  MASS VALIDATION SUITE")
        print(f"   PHASE 206: {self.n * 11:,} TESTS")
        print("="*70 + "\n")
        
        test_configs = [
            ("DNA Mapping", self.test_dna_mapping),
            ("Truth Resonance", self.test_truth_resonance),
            ("Gravity", self.test_gravity),
            ("FHT Density", self.test_fht_density),
            ("Mechanics", self.test_mechanics),
            ("Quantum", self.test_quantum),
            ("Electromagnetism", self.test_electromagnetism),
            ("Thermodynamics", self.test_thermodynamics),
            ("Relativity", self.test_relativity),
            ("Wallace Tree", self.test_wallace_tree),
            ("Edge Cases", self.test_edge_cases),
        ]
        
        for name, func in test_configs:
            print(f"Running {name}...", end=" ", flush=True)
            batch = self.run_batch(name, func)
            status = "✅" if batch.failed == 0 else "⚠️"
            print(f"{status} {batch.passed}/{self.n} passed ({batch.duration:.2f}s)")
            if batch.errors:
                for err in batch.errors[:3]:
                    print(f"      └─ {err}")
        
        # Summary
        total_passed = sum(b.passed for b in self.batches)
        total_failed = sum(b.failed for b in self.batches)
        total_tests = total_passed + total_failed
        total_time = sum(b.duration for b in self.batches)
        
        print("\n" + "="*70)
        print("   MASS VALIDATION SUMMARY")
        print("="*70)
        print(f"\n   Total Tests:  {total_tests:,}")
        print(f"   Passed:       {total_passed:,}")
        print(f"   Failed:       {total_failed:,}")
        print(f"   Success Rate: {total_passed/total_tests*100:.2f}%")
        print(f"   Total Time:   {total_time:.2f}s")
        print(f"   Tests/Second: {total_tests/total_time:,.0f}")
        
        if total_failed == 0:
            print("\n   >> ALL TESTS PASSED.")
            print("   >> TENT v4.0 IS BATTLE-TESTED.")
        else:
            print(f"\n   >> {total_failed} TESTS FAILED.")
            
        print("="*70)
        
        return total_failed == 0

# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    # Default 1000 per category = 11,000 total
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    suite = MassValidationSuite(tests_per_category=n)
    success = suite.run_all()
    sys.exit(0 if success else 1)
