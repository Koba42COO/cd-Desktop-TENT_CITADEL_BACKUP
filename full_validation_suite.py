#!/usr/bin/env python3
"""
TENT v4.0 FULL SYSTEM VALIDATION SUITE
======================================
Phase 204: Train, Validate, Test

Tests all modules:
- Physics Stack (8 modules)
- Core Engines (FHT, UPG, KWYC)
- Civilization Engine (Sectors A, B, C)
- Wallace Tree Assembler
- Genesis Block
"""

import sys
import time
import traceback
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class TestResult:
    module: str
    test_name: str
    passed: bool
    details: str
    duration_ms: float

class FullValidationSuite:
    def __init__(self):
        self.results: List[TestResult] = []
        self.start_time = time.time()
        
    def run_test(self, module: str, test_name: str, test_func) -> TestResult:
        """Execute a single test and capture result."""
        start = time.time()
        try:
            result = test_func()
            passed = result[0] if isinstance(result, tuple) else bool(result)
            details = result[1] if isinstance(result, tuple) and len(result) > 1 else "OK"
            return TestResult(module, test_name, passed, str(details), (time.time() - start) * 1000)
        except Exception as e:
            return TestResult(module, test_name, False, f"ERROR: {str(e)}", (time.time() - start) * 1000)
    
    def add_result(self, result: TestResult):
        self.results.append(result)
    
    # ==========================================
    # PHYSICS TESTS
    # ==========================================
    
    def test_mechanics(self) -> Tuple[bool, str]:
        from mechanics_core import DynamicsEngine
        from upg_store import PrimeNode, NodeType
        engine = DynamicsEngine()
        node = PrimeNode(1, NodeType.MEDIA, "TEST", mass=10.0)
        traj = engine.simulate_trajectory(node, force=50.0, steps=3)
        return len(traj) == 4, f"{len(traj)} trajectory points"
    
    def test_quantum(self) -> Tuple[bool, str]:
        from quantum_throd import QuantumThrodEngine, QuantumState
        engine = QuantumThrodEngine()
        state = QuantumState(mass_true=50.0, velocity_true=10.0, position_true=0.0)
        result = engine.measure_observable(state, 'mass')
        return result['mass'] == 50.0 and result['velocity_uncertainty'] > 0, f"Δv={result['velocity_uncertainty']:.4f}"
    
    def test_electromagnetism(self) -> Tuple[bool, str]:
        from electromagnetism_core import ElectromagnetismEngine, SpinState
        engine = ElectromagnetismEngine()
        e_field = engine.calculate_e_field(charge=1e-6, distance=0.1)
        return e_field > 0, f"E={e_field:.2e} V/m"
    
    def test_thermodynamics(self) -> Tuple[bool, str]:
        from thermodynamics_core import ThermodynamicsEngine, ThermoState
        engine = ThermodynamicsEngine()
        state = ThermoState(1000, 300, 10, 1, 101325)
        new_state = engine.first_law(state, heat_in=500, work_done=200)
        return new_state.internal_energy == 1300, f"U={new_state.internal_energy} J"
    
    def test_relativity(self) -> Tuple[bool, str]:
        from relativity_core import RelativityEngine
        engine = RelativityEngine()
        C = 299792458
        gamma = engine.lorentz_factor(0.9 * C)
        return gamma > 2, f"γ={gamma:.4f}"
    
    def test_qft(self) -> Tuple[bool, str]:
        from qft_core import QFTEngine
        engine = QFTEngine()
        electron = engine.particles['electron']
        return electron.spin == 0.5, f"spin={electron.spin}"
    
    def test_beyond_sm(self) -> Tuple[bool, str]:
        from beyond_sm_core import (SupersymmetryEngine, DarkSectorEngine, 
                                     BlackHoleEngine, QuantumGravityEngine, L_PLANCK)
        susy = SupersymmetryEngine()
        bh = BlackHoleEngine()
        t_h = bh.hawking_temperature(1.989e30)
        return t_h > 0 and L_PLANCK > 0, f"T_H={t_h:.2e} K"
    
    def test_wallace_tree(self) -> Tuple[bool, str]:
        from wallace_tree_assembler import WallaceTreeAssembler, PartialProduct
        assembler = WallaceTreeAssembler()
        products = [PartialProduct(f"P{i}", i % 2, 0.1) for i in range(16)]
        reduced, depth = assembler.wallace_tree_reduction(products)
        return len(reduced) <= 2 and depth > 0, f"depth={depth}, final={len(reduced)}"
    
    # ==========================================
    # CORE ENGINE TESTS
    # ==========================================
    
    def test_fht(self) -> Tuple[bool, str]:
        from vacuum_gauge import VacuumGauge
        gauge = VacuumGauge()
        result = gauge.analyze("def hello(): return 'world'")
        return result.density_score > 0, f"density={result.density_score:.4f}"
    
    def test_upg(self) -> Tuple[bool, str]:
        from upg_store import UniversalPrimeGraph, PrimeNode, NodeType
        upg = UniversalPrimeGraph()
        node = PrimeNode(42, NodeType.CODE, "TEST_NODE", mass=10.0)
        upg.add_node("TEST_BLOCK_ID", {'data': node})
        return len(upg.nodes) == 1, f"nodes={len(upg.nodes)}"
    
    def test_kwyc(self) -> Tuple[bool, str]:
        from kwyc_core import KwycLedger
        ledger = KwycLedger()
        block_id = ledger.mint_block("TEST_CONTENT", "TEST_WALLET", "NOVELTY")
        return block_id is not None, f"block={block_id[:8]}"
    
    def test_dividends(self) -> Tuple[bool, str]:
        from dividend_tracker import DividendEngine
        from kwyc_core import KwycLedger
        from value_assessor import ValueAssessor
        ledger = KwycLedger()
        assessor = ValueAssessor()
        engine = DividendEngine(ledger, assessor)
        return engine is not None, "DividendEngine initialized"
    
    # ==========================================
    # CIVILIZATION ENGINE TESTS
    # ==========================================
    
    def test_sector_a_dna(self) -> Tuple[bool, str]:
        from civilization_engine import CivilizationEngine
        engine = CivilizationEngine()
        coord = engine.dna_to_coordinate("GATTACA")
        return coord > 0, f"H(GATTACA)={coord:.6f}"
    
    def test_sector_b_truth(self) -> Tuple[bool, str]:
        from civilization_engine import CivilizationEngine
        engine = CivilizationEngine()
        solid = engine.harmonic_truth_check("I am Sovereign")
        flux = engine.harmonic_truth_check("Maybe it works")
        return "SOLID" in solid["classification"] and "FLUX" in flux["classification"], "Truth resonance verified"
    
    def test_sector_c_gravity(self) -> Tuple[bool, str]:
        from civilization_engine import CivilizationEngine
        engine = CivilizationEngine()
        gravity = engine.calculate_gravity(100, 10, 5)
        return gravity > 0, f"F={gravity:.4f}"
    
    def test_genesis(self) -> Tuple[bool, str]:
        from genesis_launch import GenesisEngine
        engine = GenesisEngine()
        nodes = engine.launch()
        architect_node = [n for n in nodes if n.node_id == 2]
        return len(architect_node) == 1 and architect_node[0].resonance == 1, f"Node 2 resonance={architect_node[0].resonance}"
    
    # ==========================================
    # RUN ALL TESTS
    # ==========================================
    
    def run_all(self):
        print("="*70)
        print("   ⛺  TENT v4.0  |  FULL SYSTEM VALIDATION SUITE")
        print("   PHASE 204: TRAIN • VALIDATE • TEST")
        print("="*70 + "\n")
        
        # Physics Tests
        physics_tests = [
            ("Mechanics", "F=ma Trajectory", self.test_mechanics),
            ("Quantum", "Heisenberg Uncertainty", self.test_quantum),
            ("EM", "Coulomb E-Field", self.test_electromagnetism),
            ("Thermo", "First Law", self.test_thermodynamics),
            ("Relativity", "Lorentz Factor", self.test_relativity),
            ("QFT", "Electron Spin", self.test_qft),
            ("BSM", "Hawking Temperature", self.test_beyond_sm),
            ("Wallace", "Tree Reduction", self.test_wallace_tree),
        ]
        
        # Core Tests
        core_tests = [
            ("FHT", "Density Score", self.test_fht),
            ("UPG", "Node Storage", self.test_upg),
            ("KWYC", "Block Recording", self.test_kwyc),
            ("Dividends", "Engine Init", self.test_dividends),
        ]
        
        # Civilization Tests
        civ_tests = [
            ("Sector A", "DNA Coordinate", self.test_sector_a_dna),
            ("Sector B", "Truth Resonance", self.test_sector_b_truth),
            ("Sector C", "Gravity Force", self.test_sector_c_gravity),
            ("Genesis", "Block Validation", self.test_genesis),
        ]
        
        all_tests = [
            ("PHYSICS STACK", physics_tests),
            ("CORE ENGINES", core_tests),
            ("CIVILIZATION ENGINE", civ_tests),
        ]
        
        for section_name, tests in all_tests:
            print(f"--- {section_name} ---")
            for module, test_name, test_func in tests:
                result = self.run_test(module, test_name, test_func)
                self.add_result(result)
                status = "✅" if result.passed else "❌"
                print(f"   {status} [{module}] {test_name}: {result.details} ({result.duration_ms:.1f}ms)")
            print()
        
        # Summary
        passed = sum(1 for r in self.results if r.passed)
        total = len(self.results)
        duration = time.time() - self.start_time
        
        print("="*70)
        print("   VALIDATION SUMMARY")
        print("="*70)
        print(f"\n   Tests Passed: {passed}/{total}")
        print(f"   Success Rate: {passed/total*100:.1f}%")
        print(f"   Total Time:   {duration:.2f}s")
        
        if passed == total:
            print("\n   >> ALL TESTS PASSED.")
            print("   >> TENT v4.0 IS FULLY VALIDATED.")
        else:
            print(f"\n   >> {total - passed} TEST(S) FAILED.")
            for r in self.results:
                if not r.passed:
                    print(f"      ❌ [{r.module}] {r.test_name}: {r.details}")
        
        print("="*70)
        
        return passed == total

# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    suite = FullValidationSuite()
    success = suite.run_all()
    sys.exit(0 if success else 1)
