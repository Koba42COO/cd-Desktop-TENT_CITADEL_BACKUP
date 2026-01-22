#!/usr/bin/env python3
"""
TENT v4.0 FIRST LIGHT PROTOCOL
==============================
Phase 149: The Complete Diagnostic

The telescope is complete. The mirrors are polished.
It is time for First Light.

Unified diagnostic integrating:
1. THE SKIN:    Enneper Surface Tension    - "Does this logic hold water?"
2. THE IMMUNE:  Golden-Silver Friction     - "Is beauty masking a lie?"
3. THE LUNGS:   Vacuum Gauge Density       - "Is this a diamond or hot air?"

Together, they form the complete immune system for the human mind.
"""

import math
import re
from dataclasses import dataclass
from typing import List, Tuple
from enum import Enum
from collections import Counter

# Import our diagnostic modules
from stability_check import PHI, DELTA, DualMetallicStabilizer, StabilityState
from beautiful_lie_detector import BeautifulLieDetector, LieClassification
from vacuum_gauge import VacuumGauge, DensityClass
from sawmill import Sawmill
from grain_check import GrainCheck
from joinery import Joinery
from absorption_camera import AbsorptionCamera

# =============================================================================
# CONSTANTS
# =============================================================================

# Tension threshold (from resonance_test.py)
SURFACE_TENSION_THRESHOLD = 0.65

# Friction threshold (beautiful lie boundary)
FRICTION_THRESHOLD = 0.5

# =============================================================================
# DATA STRUCTURES
# =============================================================================

class FinalVerdict(Enum):
    SUPERNOVA = "🌟 SUPERNOVA - Pure crystalline truth of the highest order"
    STAR = "⭐ STAR - Dense, stable, illuminating"
    PLANET = "🪐 PLANET - Solid, orbiting larger truths"
    ASTEROID = "☄️ ASTEROID - Small but real"
    COMET = "💫 COMET - Beautiful but transient"
    NEBULA = "🌫️ NEBULA - Diffuse, needs condensation"
    DARK_MATTER = "🕳️ DARK MATTER - Claims without substance"
    BLACK_HOLE = "⚫ BLACK HOLE - Dangerous; logic collapses inward"

@dataclass
class NarrativeXRay:
    """Complete diagnostic of a narrative"""
    text: str
    
    # Layer 1: Geometry (Skin)
    tension: float
    curvature: float
    geometry_stable: bool
    
    # Layer 2: Friction (Immune System)
    aesthetic: float
    logic: float
    friction: float
    lie_classification: LieClassification
    
    # Layer 3: Density (Lungs)
    entropy: float
    buzzword_ratio: float
    density_score: float
    density_class: DensityClass
    
    # Layer 4: Thermodynamics (Sawmill/Camera)
    albedo: float
    lumber_ratio: float
    
    # Layer 5: Provenance (Grain)
    fiber_length: float
    grain_quality: str
    
    # Layer 6: Logic (Joinery)
    structure_strength: float
    joint_type: str
    
    # GRAND UNIFICATION
    omega: float  # Ω = (M × H) / (K × A)
    mass: float   # M
    history: float # H
    logic_curvature: float # K (Recalculated from Joinery)
    
    # Final Verdict
    verdict: FinalVerdict
    
    def __str__(self):
        return f"""
╔══════════════════════════════════════════════════════════════════════╗
║  NARRATIVE X-RAY: FIRST LIGHT PROTOCOL                              ║
╚══════════════════════════════════════════════════════════════════════╝

INPUT: "{self.text[:70]}{'...' if len(self.text) > 70 else ''}"

┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 1: THE SKIN (Enneper Surface)                                │
│  "Does this logic hold water, or does it tear?"                     │
├─────────────────────────────────────────────────────────────────────┤
│  Tension:    {self.tension:.3f}   {'✓ STABLE' if self.geometry_stable else '✗ STRESSED'}
│  Curvature:  {self.curvature:.3f}
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 2: THE IMMUNE SYSTEM (Golden-Silver Friction)                │
│  "Is the beauty masking a lie?"                                     │
├─────────────────────────────────────────────────────────────────────┤
│  φ (Aesthetic): {self.aesthetic:.2f}
│  δ (Logic):     {self.logic:.2f}
│  Friction:      {self.friction:.3f}
│  Classification: {self.lie_classification.value}
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 3: THE LUNGS (Vacuum Gauge)                                  │
│  "Is this a diamond or just hot air?"                               │
├─────────────────────────────────────────────────────────────────────┤
│  Shannon Entropy: {self.entropy:.3f} bits/char
│  Buzzword Ratio:  {self.buzzword_ratio:.1%}
│  Density Score:   {self.density_score:.3f} bits/syllable
│  Classification:  {self.density_class.value}
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 4: GRAND UNIFICATION (The Physics)                           │
│  Ω = (Mass × History) / (Curvature × Albedo)                        │
├─────────────────────────────────────────────────────────────────────┤
│  Mass (M):      {self.mass:.3f}
│  History (H):   {self.history:.3f} (Avg Fiber: {self.fiber_length:.0f} yrs)
│  Curvature (K): {self.curvature:.3f} (Structure: {self.structure_strength:.0f})
│  Albedo (A):    {self.albedo:.3f}
│
│  Ω SCORE:       {self.omega:.2f}
└─────────────────────────────────────────────────────────────────────┘

╔══════════════════════════════════════════════════════════════════════╗
║  FINAL VERDICT: {self.verdict.value}
╚══════════════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# THE FIRST LIGHT DIAGNOSTIC
# =============================================================================

class FirstLightDiagnostic:
    """
    The complete TENT v4.0 diagnostic system.
    
    Points the telescope at any narrative and produces
    a complete X-Ray of its structural, deceptive, and
    substantive properties.
    """
    
    def __init__(self):
        self.friction_detector = BeautifulLieDetector()
        self.vacuum_gauge = VacuumGauge()
        self.flux_stabilizer = DualMetallicStabilizer()
        
        # New Physics Modules (Phase 158-170)
        self.sawmill = Sawmill()
        self.grain_check = GrainCheck()
        self.joinery = Joinery()
        self.absorption_camera = AbsorptionCamera()
    
    def analyze(self, text: str) -> NarrativeXRay:
        """Perform complete diagnostic on text."""
        
        # Layer 1: Geometry (Skin)
        tension_skin, curvature_skin, geometry_stable = self._analyze_geometry(text)
        
        # Layer 2: Friction (Immune System)
        friction_result = self.friction_detector.analyze(text)
        
        # Layer 3: Density (Lungs) - Now with Hazards/Archimedes
        density_result = self.vacuum_gauge.analyze(text)
        
        # === NEW PHYSICS LAYERS ===
        
        # Sawmill (Albedo/Lumber)
        sawmill_res = self.sawmill.mill(text)
        lumber_ratio = sawmill_res.lumber_word_count / max(1, sawmill_res.original_word_count)
        
        # Grain Check (Provenance)
        grain_res = self.grain_check.analyze_text(text)
        avg_fiber = sum(w.fiber_length for w in grain_res.word_analyses) / max(1, len(grain_res.word_analyses))
        
        # Joinery (Logic Structure)
        joinery_res = self.joinery.analyze(text)
        structure_strength = joinery_res.average_strength
        
        # Absorption Camera (Thermodynamics)
        camera_res = self.absorption_camera.photograph(text)
        albedo = camera_res.albedo
        
        # === GRAND UNIFICATION (OMEGA) ===
        # Ω = (Mass × History) / (Curvature × Albedo)
        
        mass = max(0.1, density_result.density_score)
        history = avg_fiber / 100.0
        # Curvature for Omega is inverse of strength (1.0 - strength/100)
        curvature_omega = max(0.01, 1.0 - (structure_strength / 100.0))
        albedo_safe = max(0.01, albedo)
        
        omega = (mass * history) / (curvature_omega * albedo_safe)
        
        # Compute Final Verdict (Updated for Omega)
        verdict = self._compute_verdict_omega(omega, density_result.density_score)
        
        return NarrativeXRay(
            text=text,
            tension=tension_skin,
            curvature=curvature_skin,
            geometry_stable=geometry_stable,
            aesthetic=friction_result.aesthetic_score,
            logic=friction_result.logic_score,
            friction=friction_result.friction,
            lie_classification=friction_result.classification,
            entropy=density_result.shannon_entropy,
            buzzword_ratio=density_result.buzzword_ratio,
            density_score=density_result.density_score,
            density_class=density_result.classification,
            
            # New Metrics
            albedo=albedo,
            lumber_ratio=lumber_ratio,
            fiber_length=avg_fiber,
            grain_quality=grain_res.overall_quality.value,
            structure_strength=structure_strength,
            joint_type=joinery_res.statement_type.value,
            
            # Grand Unification
            omega=omega,
            mass=mass,
            history=history,
            logic_curvature=curvature_omega,
            
            verdict=verdict
        )
    
    def _analyze_geometry(self, text: str) -> Tuple[float, float, bool]:
        """
        Analyze geometric tension using Enneper-style mapping.
        Maps text to surface and computes mean curvature.
        """
        words = text.split()
        word_count = len(words)
        
        if word_count == 0:
            return 0.0, 0.0, True
        
        # Compute tension based on word complexity and structure
        total_tension = 0.0
        
        for word in words:
            # Word-level tension
            word_tension = len(word) / 20.0  # Length contributes to tension
            
            # Special characters add tension
            special = sum(1 for c in word if not c.isalnum())
            word_tension += special * 0.05
            
            total_tension += word_tension
        
        # Sentence structure contributes to curvature
        sentences = re.split(r'[.!?]', text)
        sentence_count = len([s for s in sentences if s.strip()])
        
        avg_tension = total_tension / word_count
        curvature = 0.0  # Enneper has zero mean curvature ideally
        
        # Check flux rope stability using validate_sequence
        self.flux_stabilizer.reset()
        steps = [len(word) * 0.1 for word in words]
        stability_state, resonance = self.flux_stabilizer.validate_sequence(steps)
        flux_stable = stability_state == StabilityState.LOCKED
        
        # Geometry is stable if tension is low and flux is locked
        geometry_stable = avg_tension < SURFACE_TENSION_THRESHOLD and flux_stable
        
        return avg_tension, curvature, geometry_stable
    
    
    def _compute_verdict_omega(self, omega: float, density: float) -> FinalVerdict:
        """
        Compute final verdict based on Omega Score.
        """
        if omega >= 1_000_000:
            return FinalVerdict.BLACK_HOLE # Extreme density (Contracts/Uranium), technically heavy but dangerous? 
            # Actually, per benchmark, Contracts were 2.7M Omega.
            # Contracts are "Iron Handcuffs". 
            # But Black Hole implies "Logic collapses inward". 
            # If it's pure truth, it's SUPERNOVA.
            # Let's use the density to distinguish.
            return FinalVerdict.STAR # Massive object
            
        if omega >= 50:
            return FinalVerdict.SUPERNOVA
        elif omega >= 10:
            return FinalVerdict.STAR
        elif omega >= 1.0:
            return FinalVerdict.PLANET
        elif omega >= 0.5:
            return FinalVerdict.NEBULA
        elif omega >= 0.1:
            return FinalVerdict.COMET
        else:
            return FinalVerdict.DARK_MATTER

# =============================================================================
# TEST NARRATIVES
# =============================================================================

FIRST_LIGHT_TARGETS = [
    # THE RIEMANN HYPOTHESIS - The Supernova Test
    """The Riemann Hypothesis states that all non-trivial zeros of the Zeta function have a real part of 1/2. This implies that the distribution of prime numbers follows the most stable possible thermodynamic path, minimizing the energy of the arithmetic system.""",
    
    # PHYSICS EQUATIONS - Diamond Tests
    """Maxwell's equations unify electricity and magnetism by showing that a changing electric field produces a magnetic field, and a changing magnetic field produces an electric field.""",
    
    # CORPORATE MISSION STATEMENT - Bubble Test
    """We leverage innovative synergies to proactively optimize stakeholder value through best-in-class paradigm shifts in our holistic ecosystem.""",
    
    # BEAUTIFUL LIE - Black Hole Test
    """The eternal wisdom of the ancients proves that consciousness creates reality, and therefore you can manifest infinite abundance simply by believing in the quantum field.""",
    
    # SIMPLE TRUTH - Planet Test
    """Water freezes at 0 degrees Celsius at standard atmospheric pressure.""",
    
    # CONTROVERSIAL CLAIM - Comet Test
    """The simulation hypothesis suggests we may be living in a computer simulation, with our reality being computed by an advanced civilization.""",
]

# =============================================================================
# DEMO
# =============================================================================

def run_first_light():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 FIRST LIGHT PROTOCOL                                  ║")
    print("║  Phase 149: The Complete Diagnostic                              ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    print("  The telescope is complete.")
    print("  The mirrors are polished (Geometry).")
    print("  The lenses are calibrated (Friction).")
    print("  The dust is cleaned (Vacuum).")
    print()
    print("  It is time for First Light.")
    print("  Pointing at the Riemann Hypothesis...\n")
    
    diagnostic = FirstLightDiagnostic()
    
    results = {}
    
    for i, text in enumerate(FIRST_LIGHT_TARGETS, 1):
        print(f"\n{'='*74}")
        print(f"  TARGET {i}")
        print(f"{'='*74}")
        
        xray = diagnostic.analyze(text)
        print(xray)
        
        verdict_name = xray.verdict.name
        results[verdict_name] = results.get(verdict_name, 0) + 1
    
    # Summary
    print("\n" + "=" * 74)
    print("  FIRST LIGHT SUMMARY")
    print("=" * 74)
    print("""
    Targets Analyzed: {}
    
    {}
    
    "The telescope sees. The organism understands."
    
    TENT v4.0 - Where Logic Behaves Like Matter.
    """.format(
        len(FIRST_LIGHT_TARGETS),
        "\n    ".join(f"{k}: {v}" for k, v in sorted(results.items()))
    ))

if __name__ == "__main__":
    run_first_light()
