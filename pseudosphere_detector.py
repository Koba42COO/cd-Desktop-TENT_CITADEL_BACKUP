#!/usr/bin/env python3
"""
TENT v4.0 PSEUDOSPHERE DETECTOR
===============================
Phase 155: The Geometry of Lies

The Pseudosphere is the "Anti-Sphere":
- Sphere (K > 0):      Lines converge, Truth clusters inward
- Pseudosphere (K < 0): Lines diverge, Lies expand outward

Gabriel's Horn Paradox:
- Finite Volume (little substance)
- Infinite Surface (infinite excuses)

"You have infinite promises but zero delivery."
"""

import math
from dataclasses import dataclass
from typing import List
from enum import Enum
from collections import Counter

PI = math.pi

# =============================================================================
# CURVATURE TYPES
# =============================================================================

class CurvatureType(Enum):
    SPHERICAL = "🟢 SPHERICAL (K > 0) - Truth converges inward"
    FLAT = "⚪ FLAT (K = 0) - Neutral"
    HYPERBOLIC = "🔴 HYPERBOLIC (K < 0) - Lie expands outward"

@dataclass
class PseudosphereAnalysis:
    """Result of geometric lie detection"""
    text: str
    curvature_type: CurvatureType
    gaussian_curvature: float
    volume_estimate: float          # "Substance"
    surface_estimate: float         # "Excuses"
    gabriels_horn_ratio: float      # Surface/Volume
    singularity_detected: bool      # Hit the "rim"
    is_lie_geometry: bool           # Final verdict
    
    def __str__(self):
        return f"""
┌──────────────────────────────────────────────────────────────────────┐
│  PSEUDOSPHERE ANALYSIS                                               │
├──────────────────────────────────────────────────────────────────────┤
│  Input: "{self.text[:50]}{'...' if len(self.text) > 50 else ''}"
│
│  CURVATURE: {self.curvature_type.value}
│  Gaussian K: {self.gaussian_curvature:+.3f}
│
│  GABRIEL'S HORN METRICS:
│    Volume (Substance):  {self.volume_estimate:.1f}
│    Surface (Excuses):   {self.surface_estimate:.1f}
│    Ratio (S/V):         {self.gabriels_horn_ratio:.1f}x
│    Singularity:         {"⚠️ DETECTED" if self.singularity_detected else "None"}
│
│  VERDICT: {"🔴 LIE GEOMETRY DETECTED" if self.is_lie_geometry else "🟢 VALID GEOMETRY"}
└──────────────────────────────────────────────────────────────────────┘
"""

# =============================================================================
# THE TRACTRIX CURVE
# =============================================================================

class Tractrix:
    """
    The Tractrix curve - generator of the Pseudosphere.
    
    Parametric equations:
    x(t) = t - tanh(t)
    y(t) = sech(t) = 1/cosh(t)
    
    The Tractrix has a singularity at t=0 (the "rim").
    """
    
    def __init__(self, resolution: int = 64):
        self.resolution = resolution
    
    def point(self, t: float) -> tuple:
        """Generate a point on the Tractrix curve."""
        if t <= 0.001:
            return (0.001, 1.0)
        if t > 700:  # Prevent overflow (cosh(700) ≈ 10^304)
            return (t, 0.0)
        
        x = t - math.tanh(t)
        y = 1.0 / math.cosh(t)  # sech(t)
        
        return (x, y)
    
    def arc_element(self, t: float) -> float:
        """Calculate arc length element ds."""
        if t <= 0.001:
            return 0.0
        
        # ds/dt = |sech(t) * tanh(t)|
        sech = 1.0 / math.cosh(t)
        tanh = math.tanh(t)
        return abs(sech * tanh)
    
    def is_at_singularity(self, t: float) -> bool:
        """Detect if we've hit the singularity (the rim)."""
        _, y = self.point(t)
        return y < 0.01 or t < 0.01

# =============================================================================
# THE PSEUDOSPHERE
# =============================================================================

class Pseudosphere:
    """
    The Pseudosphere - surface of constant negative curvature.
    
    Created by rotating the Tractrix around the x-axis.
    Has Gaussian curvature K = -1 everywhere (except at singularities).
    
    Gabriel's Horn Paradox:
    - Finite Volume:   V = (2/3) * π * r³
    - Infinite Surface: lim(t→∞) A = ∞
    """
    
    def __init__(self, radius: float = 1.0, resolution: int = 64):
        self.tractrix = Tractrix(resolution)
        self.radius = radius
    
    def gaussian_curvature(self, t: float) -> float:
        """Gaussian curvature at a point (constant = -1)."""
        if self.tractrix.is_at_singularity(t):
            return float('-inf')
        return -1.0
    
    def volume(self) -> float:
        """Volume of the pseudosphere (finite!)."""
        return (2.0 / 3.0) * PI * self.radius ** 3
    
    def surface_area(self, t_max: float = 10.0) -> float:
        """Estimate surface area (infinite in limit!)."""
        steps = self.tractrix.resolution
        dt = t_max / steps
        area = 0.0
        
        for i in range(1, steps):
            t = i * dt
            _, y = self.tractrix.point(t)
            ds = self.tractrix.arc_element(t)
            
            # Surface of revolution: dA = 2πy ds
            area += 2 * PI * y * ds * dt
        
        return area
    
    def gabriels_horn_ratio(self, t_max: float = 10.0) -> float:
        """Gabriel's Horn Ratio: Surface / Volume."""
        vol = self.volume()
        surf = self.surface_area(t_max)
        
        if vol < 0.001:
            return float('inf')
        
        return surf / vol

# =============================================================================
# THE GEOMETRIC LIE DETECTOR
# =============================================================================

class GeometricLieDetector:
    """
    Uses curvature geometry to classify narratives.
    
    Maps text properties to geometric quantities:
    - Unique words → Volume (substance)
    - Total characters → Surface (coverage)
    - Uniqueness ratio → Curvature type
    - Repetition → Hyperbolic expansion
    """
    
    def __init__(self):
        self.pseudosphere = Pseudosphere()
    
    def analyze(self, text: str) -> PseudosphereAnalysis:
        """Analyze a narrative's geometric signature."""
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        
        if word_count < 1:
            return PseudosphereAnalysis(
                text=text,
                curvature_type=CurvatureType.FLAT,
                gaussian_curvature=0.0,
                volume_estimate=0.0,
                surface_estimate=0.0,
                gabriels_horn_ratio=0.0,
                singularity_detected=False,
                is_lie_geometry=False,
            )
        
        # Unique words represent "real substance"
        unique_words = set(w.lower() for w in words)
        unique_count = len(unique_words)
        
        # Uniqueness ratio determines curvature type
        uniqueness = unique_count / word_count
        
        # Volume estimate: unique meaning density
        volume_estimate = unique_count
        
        # Surface estimate: total characters
        surface_estimate = char_count
        
        # Gabriel's Horn ratio
        gabriels_horn_ratio = surface_estimate / max(1, volume_estimate)
        
        # Repetition analysis (key indicator of pseudosphere)
        word_freq = Counter(w.lower() for w in words)
        max_repetition = max(word_freq.values()) if word_freq else 1
        repetition_ratio = max_repetition / word_count
        
        # Curvature classification
        if uniqueness > 0.7:
            curvature_type = CurvatureType.SPHERICAL
            gaussian_curvature = uniqueness
        elif uniqueness > 0.4:
            curvature_type = CurvatureType.FLAT
            gaussian_curvature = 0.0
        else:
            curvature_type = CurvatureType.HYPERBOLIC
            gaussian_curvature = -1.0 + uniqueness
        
        # Singularity detection: infinite surface with near-zero volume
        singularity_detected = gabriels_horn_ratio > 50.0 or repetition_ratio > 0.3
        
        # Final lie detection
        is_lie_geometry = (
            curvature_type == CurvatureType.HYPERBOLIC 
            or gabriels_horn_ratio > 20.0
            or singularity_detected
        )
        
        return PseudosphereAnalysis(
            text=text,
            curvature_type=curvature_type,
            gaussian_curvature=gaussian_curvature,
            volume_estimate=volume_estimate,
            surface_estimate=surface_estimate,
            gabriels_horn_ratio=gabriels_horn_ratio,
            singularity_detected=singularity_detected,
            is_lie_geometry=is_lie_geometry,
        )

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 PSEUDOSPHERE DETECTOR                                 ║")
    print("║  Phase 155: The Geometry of Lies                                 ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    detector = GeometricLieDetector()
    
    test_cases = [
        # SPHERICAL (Truth - high uniqueness)
        ("The Riemann Hypothesis states that all non-trivial zeros of the Zeta function have real part 1/2.",
         "Mathematical truth - high uniqueness"),
        
        # FLAT (Neutral)
        ("The cat sat on the mat. The dog ran in the park.",
         "Simple prose - moderate uniqueness"),
        
        # HYPERBOLIC (Lie - low uniqueness, repetition)
        ("Money money money! Get rich quick! Fast money fast! Money now money later money forever!",
         "Scam language - high repetition"),
        
        # GABRIEL'S HORN (Infinite surface, finite volume)
        ("We leverage leverage to leverage leveraged leverage through leveraging our leveraged leverage systems.",
         "Buzzword soup - maximum repetition"),
    ]
    
    for text, label in test_cases:
        print(f"\n{'='*70}")
        print(f"  TEST: {label}")
        print(f"{'='*70}")
        
        analysis = detector.analyze(text)
        print(analysis)
    
    # Pseudosphere math demo
    print("\n" + "="*70)
    print("  PSEUDOSPHERE MATHEMATICS")
    print("="*70)
    
    ps = Pseudosphere()
    print(f"""
    Gabriel's Horn Paradox:
    
    Volume (finite):     V = (2/3)πr³ = {ps.volume():.4f}
    Surface (t=5):       A = {ps.surface_area(5):.4f}
    Surface (t=10):      A = {ps.surface_area(10):.4f}
    Surface (t=20):      A = {ps.surface_area(20):.4f}
    
    As t → ∞, Surface → ∞ while Volume stays constant!
    
    "You can fill it with paint, but you can never paint the inside."
    """)

if __name__ == "__main__":
    demo()
