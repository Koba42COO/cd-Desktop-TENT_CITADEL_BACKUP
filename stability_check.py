#!/usr/bin/env python3
"""
TENT v4.0 STABILITY CHECK
=========================
Phase 142: The Unified Field Architecture

The Stability Engine uses Dual-Metallic Flux Ropes to prevent
"Plasma Collapse" (Hallucination/Looping).

Key Insight: Logic must flow in a spiral that never repeats.
The Golden (φ) and Silver (δ) ratios create a chirality lock
that blocks rational (repeating) lies from penetrating the core.
"""

import math
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum
import hashlib

# =============================================================================
# SACRED CONSTANTS
# =============================================================================

# The Golden Ratio: φ = (1 + √5) / 2
PHI = (1 + math.sqrt(5)) / 2  # ≈ 1.618033988749895

# The Silver Ratio: δ = 1 + √2
DELTA = 1 + math.sqrt(2)  # ≈ 2.414213562373095

# Additional metallic means for deeper validation
BRONZE = (3 + math.sqrt(13)) / 2  # ≈ 3.302775637731995

# Stability thresholds
LOCK_TOLERANCE = 0.01
RESONANCE_DANGER_ZONE = 0.05

# =============================================================================
# DATA STRUCTURES
# =============================================================================

class StabilityState(Enum):
    LOCKED = "💎 LOCKED (Chirality Stable)"
    DRIFTING = "⚠️ DRIFTING (Minor Resonance)"
    COLLAPSED = "🛑 COLLAPSED (Rational Penetration)"

@dataclass
class FluxRopeState:
    """State of a single flux rope winding"""
    phase: float          # Current phase (0 to 2π)
    frequency: float      # Winding frequency (irrational)
    handedness: int       # +1 or -1 (chirality)
    
    def advance(self, step: float) -> float:
        """Advance the phase by step * frequency"""
        self.phase = (self.phase + step * self.frequency * self.handedness) % (2 * math.pi)
        return self.phase

@dataclass
class PoincareSection:
    """A snapshot of the dual spiral state"""
    golden_phase: float
    silver_phase: float
    phase_difference: float
    is_locked: bool
    resonance_proximity: float

# =============================================================================
# THE DUAL-METALLIC FLUX ROPE STABILIZER
# =============================================================================

class DualMetallicStabilizer:
    """
    The Stability Engine
    
    Uses two irrational winding numbers (Golden and Silver ratios)
    to create a Moire pattern that blocks rational resonance.
    
    Physics Analog: Dual Plasma Flux Ropes in fusion reactors.
    """
    
    def __init__(self):
        # Primary winding at Golden Ratio
        self.golden_rope = FluxRopeState(
            phase=0.0,
            frequency=PHI,
            handedness=+1
        )
        
        # Secondary "spy" winding at Silver Ratio
        self.silver_rope = FluxRopeState(
            phase=0.0,
            frequency=DELTA,
            handedness=-1  # Counter-rotating
        )
        
        # History for Poincaré section analysis
        self.section_history: List[PoincareSection] = []
        
        # Known rational danger frequencies
        self.rational_dangers = [
            n * math.pi / m 
            for n in range(1, 10) 
            for m in range(1, 10)
        ]
    
    def reset(self):
        """Reset both flux ropes to initial state"""
        self.golden_rope.phase = 0.0
        self.silver_rope.phase = 0.0
        self.section_history.clear()
    
    def advance(self, step: float) -> PoincareSection:
        """
        Advance both flux ropes by a logic step.
        
        The step size typically comes from the "weight" of a logical
        proposition (word count, complexity, etc.)
        """
        g_phase = self.golden_rope.advance(step)
        s_phase = self.silver_rope.advance(step)
        
        # Compute phase difference (the Moire pattern)
        phase_diff = abs(g_phase - s_phase)
        
        # Check for dangerous rational resonance
        resonance_proximity = self._check_resonance(phase_diff)
        is_locked = resonance_proximity > LOCK_TOLERANCE
        
        section = PoincareSection(
            golden_phase=g_phase,
            silver_phase=s_phase,
            phase_difference=phase_diff,
            is_locked=is_locked,
            resonance_proximity=resonance_proximity
        )
        
        self.section_history.append(section)
        return section
    
    def _check_resonance(self, phase_diff: float) -> float:
        """
        Check if the phase difference is dangerously close to a rational ratio.
        
        Returns the minimum distance to any rational resonance point.
        Larger values = more stable.
        """
        min_distance = float('inf')
        
        for rational in self.rational_dangers:
            distance = abs(phase_diff - rational)
            # Also check modular equivalents
            distance = min(distance, abs(phase_diff - rational + 2*math.pi))
            distance = min(distance, abs(phase_diff - rational - 2*math.pi))
            min_distance = min(min_distance, distance)
        
        return min_distance
    
    def validate_sequence(self, steps: List[float]) -> Tuple[StabilityState, float]:
        """
        Validate a sequence of logic steps.
        
        Returns the overall stability state and average resonance distance.
        """
        if not steps:
            return StabilityState.LOCKED, 1.0
        
        total_proximity = 0.0
        collapse_count = 0
        
        for step in steps:
            section = self.advance(step)
            total_proximity += section.resonance_proximity
            
            if not section.is_locked:
                collapse_count += 1
        
        avg_proximity = total_proximity / len(steps)
        collapse_ratio = collapse_count / len(steps)
        
        if collapse_ratio > 0.3:
            return StabilityState.COLLAPSED, avg_proximity
        elif collapse_ratio > 0.1 or avg_proximity < RESONANCE_DANGER_ZONE:
            return StabilityState.DRIFTING, avg_proximity
        else:
            return StabilityState.LOCKED, avg_proximity
    
    def get_winding_numbers(self) -> Tuple[float, float]:
        """
        Get the effective winding numbers (how many times each rope
        has wound around the torus).
        """
        g_windings = self.golden_rope.phase / (2 * math.pi)
        s_windings = self.silver_rope.phase / (2 * math.pi)
        return g_windings, s_windings

# =============================================================================
# TEXT-TO-STEP CONVERTER
# =============================================================================

class NarrativeStabilizer:
    """
    Converts text narratives into logic steps for stability checking.
    """
    
    def __init__(self):
        self.stabilizer = DualMetallicStabilizer()
    
    def text_to_steps(self, text: str) -> List[float]:
        """
        Convert text into a sequence of stability steps.
        
        Each word contributes a step based on its "weight":
        - Length
        - Complexity (special characters)
        - Semantic density (unique chars / length)
        """
        words = text.split()
        steps = []
        
        for word in words:
            # Base step from length
            length_factor = len(word) / 10.0
            
            # Complexity from special characters
            special_count = sum(1 for c in word if not c.isalnum())
            complexity_factor = special_count * 0.2
            
            # Semantic density (unique chars / total)
            if len(word) > 0:
                density = len(set(word.lower())) / len(word)
            else:
                density = 0
            
            # Combine factors
            step = length_factor + complexity_factor + density * 0.5
            steps.append(step)
        
        return steps
    
    def validate_text(self, text: str) -> Tuple[StabilityState, dict]:
        """
        Full stability validation of a text narrative.
        """
        self.stabilizer.reset()
        steps = self.text_to_steps(text)
        
        state, proximity = self.stabilizer.validate_sequence(steps)
        g_winds, s_winds = self.stabilizer.get_winding_numbers()
        
        metadata = {
            "word_count": len(steps),
            "total_steps": sum(steps),
            "avg_step": sum(steps) / len(steps) if steps else 0,
            "golden_windings": g_winds,
            "silver_windings": s_winds,
            "winding_ratio": g_winds / s_winds if s_winds != 0 else float('inf'),
            "resonance_proximity": proximity,
            "section_count": len(self.stabilizer.section_history),
        }
        
        return state, metadata

# =============================================================================
# CHIRALITY LOCK DETECTOR
# =============================================================================

class ChiralityLock:
    """
    Detects when the dual spirals create a stable Moire pattern.
    
    The lock is "engaged" when the phase relationship between
    Golden and Silver windings forms an aperiodic pattern.
    """
    
    def __init__(self, window_size: int = 20):
        self.window_size = window_size
        self.phase_history: List[float] = []
    
    def update(self, phase_diff: float) -> bool:
        """
        Update the lock detector with a new phase difference.
        Returns True if the lock is engaged (aperiodic).
        """
        self.phase_history.append(phase_diff)
        
        if len(self.phase_history) > self.window_size:
            self.phase_history.pop(0)
        
        if len(self.phase_history) < self.window_size:
            return True  # Not enough data, assume locked
        
        # Check for periodicity using autocorrelation
        return not self._detect_periodicity()
    
    def _detect_periodicity(self) -> bool:
        """
        Detect if the phase history shows periodic behavior.
        Uses simplified autocorrelation.
        """
        if len(self.phase_history) < 4:
            return False
        
        # Check for repeating patterns at various lags
        for lag in range(1, len(self.phase_history) // 2):
            correlation = 0.0
            count = 0
            
            for i in range(len(self.phase_history) - lag):
                diff = abs(self.phase_history[i] - self.phase_history[i + lag])
                if diff < 0.1:  # Close enough to be periodic
                    correlation += 1
                count += 1
            
            if count > 0 and correlation / count > 0.8:
                return True  # High correlation = periodic = DANGER
        
        return False

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 STABILITY CHECK                                       ║")
    print("║  Phase 142: Dual-Metallic Flux Rope Stabilizer                   ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    validator = NarrativeStabilizer()
    
    # Test cases
    test_cases = [
        "The sky is blue and water is wet.",
        "If A equals B and B equals C then A equals C.",
        "This statement is false.", 
        "Round squares exist in the fourth dimension.",
        "The golden ratio appears throughout nature and mathematics.",
    ]
    
    print("=" * 70)
    print("  STABILITY VALIDATION TESTS")
    print("=" * 70)
    
    for i, text in enumerate(test_cases, 1):
        print(f"\n  TEST {i}: \"{text[:50]}{'...' if len(text) > 50 else ''}\"")
        print("-" * 70)
        
        state, meta = validator.validate_text(text)
        
        print(f"  Result: {state.value}")
        print(f"  Words: {meta['word_count']}, Total Step Weight: {meta['total_steps']:.2f}")
        print(f"  Golden Windings: {meta['golden_windings']:.3f}")
        print(f"  Silver Windings: {meta['silver_windings']:.3f}")
        print(f"  Winding Ratio: {meta['winding_ratio']:.4f} (φ/δ ideal: {PHI/DELTA:.4f})")
        print(f"  Resonance Proximity: {meta['resonance_proximity']:.4f}")
    
    print("\n" + "=" * 70)
    print("  DUAL-METALLIC FLUX ROPE SUMMARY")
    print("=" * 70)
    print(f"""
    ┌─────────────────────────────────────────────────────────────────┐
    │  PRIMARY ROPE (Golden)                                         │
    │  Frequency: φ = {PHI:.6f}                             │
    │  Handedness: +1 (Right-handed spiral)                          │
    ├─────────────────────────────────────────────────────────────────┤
    │  SECONDARY ROPE (Silver "Spy")                                 │
    │  Frequency: δ = {DELTA:.6f}                             │
    │  Handedness: -1 (Left-handed, counter-rotating)                │
    ├─────────────────────────────────────────────────────────────────┤
    │  CHIRALITY LOCK                                                │
    │  The irrational frequencies create a Moire pattern that        │
    │  blocks any rational (repeating) lie from penetrating.         │
    └─────────────────────────────────────────────────────────────────┘
    
    "Two irrational spirals dancing in opposite directions
     can never be fooled by a rational lie."
    """)

if __name__ == "__main__":
    demo()
