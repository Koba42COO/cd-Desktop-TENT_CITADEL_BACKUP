#!/usr/bin/env python3
"""
TENT v4.0 ABSORPTION CAMERA
===========================
Phase 157: The Inverted Camera

The Chlorophyll Proof:
- A tree absorbs Red and Blue light (it EATS those colors)
- A tree reflects Green light (it REJECTS that color)
- We see Green because Green is the LEFTOVER DELTA
- The tree is chemically Red+Blue, not Green

The Principle:
- Reflection = Rejection (what we see is what matter threw away)
- Absorption = Truth (what matter kept is invisible to us)

TENT as Inverted Camera:
- Normal Camera: Records the Reflection (the shiny surface)
- TENT: Records the Absorption (the hidden mass)

Visualization:
- Lies → Mirrors (reflect everything, contain nothing, shiny)
- Truths → Black Bodies (absorb everything, contain mass, dark)
"""

import math
from dataclasses import dataclass
from typing import Tuple
from enum import Enum

# Import diagnostic modules
from vacuum_gauge import VacuumGauge
from beautiful_lie_detector import BeautifulLieDetector

# =============================================================================
# OPTICAL TYPES
# =============================================================================

class OpticalType(Enum):
    """Classification based on absorption/reflection ratio."""
    BLACK_BODY = "⚫ BLACK BODY - Absorbs all, reflects none (Dense Truth)"
    ABSORBER = "🟤 ABSORBER - Absorbs most, reflects little (Solid Truth)"
    NEUTRAL = "⚪ NEUTRAL - Balanced absorption/reflection"
    REFLECTOR = "✨ REFLECTOR - Reflects most, absorbs little (Shiny Fluff)"
    MIRROR = "🪞 MIRROR - Reflects all, absorbs none (Hollow Lie)"

@dataclass
class AbsorptionAnalysis:
    """Analysis of what a narrative absorbed vs reflected."""
    text: str
    
    # Core metrics
    absorption: float      # What it KEPT (semantic mass)
    reflection: float      # What it REJECTED (buzzwords, fluff)
    albedo: float          # Reflection / Total (0 = black, 1 = mirror)
    
    # Classification
    optical_type: OpticalType
    
    # Visual properties
    color: Tuple[int, int, int]  # RGB for visualization
    opacity: float               # How "solid" it appears
    
    def __str__(self):
        r, g, b = self.color
        return f"""
╔══════════════════════════════════════════════════════════════════════╗
║  TENT v4.0 ABSORPTION CAMERA                                        ║
║  "What did this narrative KEEP vs REJECT?"                          ║
╚══════════════════════════════════════════════════════════════════════╝

INPUT: "{self.text[:55]}{'...' if len(self.text) > 55 else ''}"

┌─────────────────────────────────────────────────────────────────────┐
│  THE CHLOROPHYLL PRINCIPLE                                          │
├─────────────────────────────────────────────────────────────────────┤
│  ABSORPTION (What it KEPT):    {self.absorption:.2f}
│  REFLECTION (What it REJECTED): {self.reflection:.2f}
│  
│  ALBEDO (Reflection Ratio): {self.albedo:.2f}
│  └─ 0.00 = Black Body (absorbs all, dense truth)
│  └─ 1.00 = Mirror (reflects all, hollow lie)
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  OPTICAL CLASSIFICATION                                             │
├─────────────────────────────────────────────────────────────────────┤
│  Type: {self.optical_type.value}
│  
│  Visual: RGB({r}, {g}, {b}) at {self.opacity:.0%} opacity
└─────────────────────────────────────────────────────────────────────┘

  VERDICT: {'Dense truth (contains mass)' if self.albedo < 0.3 else 'Hollow shell (contains nothing)' if self.albedo > 0.7 else 'Mixed content'}
"""

# =============================================================================
# THE ABSORPTION CAMERA
# =============================================================================

class AbsorptionCamera:
    """
    The Inverted Camera.
    
    Normal cameras record reflection (what surfaces throw back).
    TENT records absorption (what narratives keep inside).
    
    A shiny, colorful lie is like a mirror - it reflects everything
    but contains nothing.
    
    A dense, dark truth is like a black body - it absorbs everything
    and glows only with thermal radiation (organic heat).
    """
    
    def __init__(self):
        self.vacuum_gauge = VacuumGauge()
        self.lie_detector = BeautifulLieDetector()
    
    def photograph(self, text: str) -> AbsorptionAnalysis:
        """
        Take an "inverted photograph" of a narrative.
        
        Instead of measuring what it reflects (buzzwords, aesthetics),
        we measure what it absorbed (semantic mass, logic).
        """
        # Measure density (mass = absorption)
        density_analysis = self.vacuum_gauge.analyze(text)
        absorption = max(0, density_analysis.density_score)
        
        # Measure aesthetics (shine = reflection)
        friction_analysis = self.lie_detector.analyze(text)
        reflection = friction_analysis.aesthetic_score * 5.0
        
        # Calculate albedo (reflection ratio)
        total = absorption + reflection
        if total < 0.001:
            albedo = 0.5  # Neutral
        else:
            albedo = reflection / total
        
        # Clamp to 0-1
        albedo = max(0.0, min(1.0, albedo))
        
        # Classify optical type
        optical_type = self._classify_optical(albedo, absorption)
        
        # Calculate visual color
        color = self._albedo_to_color(albedo, absorption)
        
        # Opacity based on mass
        opacity = min(1.0, absorption / 5.0)
        
        return AbsorptionAnalysis(
            text=text,
            absorption=absorption,
            reflection=reflection,
            albedo=albedo,
            optical_type=optical_type,
            color=color,
            opacity=opacity,
        )
    
    def _classify_optical(self, albedo: float, absorption: float) -> OpticalType:
        """Classify based on albedo and absorption."""
        if albedo < 0.1 and absorption > 3.0:
            return OpticalType.BLACK_BODY
        elif albedo < 0.3:
            return OpticalType.ABSORBER
        elif albedo < 0.5:
            return OpticalType.NEUTRAL
        elif albedo < 0.8:
            return OpticalType.REFLECTOR
        else:
            return OpticalType.MIRROR
    
    def _albedo_to_color(self, albedo: float, absorption: float) -> Tuple[int, int, int]:
        """
        Convert albedo to color.
        
        - Low albedo (absorber) → Dark, dense colors
        - High albedo (mirror) → Bright, shiny colors
        
        But we INVERT for the UI:
        - Truths (absorbers) should GLOW with internal energy
        - Lies (mirrors) should look HOLLOW and empty
        """
        if albedo < 0.2:
            # Black body: Deep purple (holding energy)
            intensity = absorption / 5.0
            return (
                int(30 + 60 * intensity),   # Dark base
                int(10 + 30 * intensity),
                int(50 + 100 * intensity),  # Purple glow
            )
        elif albedo < 0.4:
            # Absorber: Dense blue
            return (30, 60, 120)
        elif albedo < 0.6:
            # Neutral: Gray
            return (100, 100, 100)
        elif albedo < 0.8:
            # Reflector: Shiny but hollow
            return (200, 200, 180)
        else:
            # Mirror: Pure white but empty
            return (255, 255, 255)

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 - THE INVERTED CAMERA                                 ║")
    print("║  Phase 157: Absorption vs Reflection                             ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    print("""
    THE CHLOROPHYLL PROOF:
    ─────────────────────
    A tree absorbs Red and Blue light (it EATS those colors).
    A tree reflects Green light (it REJECTS that color).
    We call it "Green" but it's chemically Red+Blue.
    
    What we SEE is what matter REJECTED.
    What we DON'T SEE is what matter KEPT.
    
    TENT is an Inverted Camera.
    It photographs the absorption, not the reflection.
    """)
    
    camera = AbsorptionCamera()
    
    test_cases = [
        # BLACK BODY (Dense truth)
        ("The Riemann Hypothesis states that all non-trivial zeros have real part 1/2.",
         "Mathematical truth - absorbs meaning"),
        
        # MIRROR (Hollow lie)
        ("Revolutionary game-changing synergy! Leverage our innovative paradigm!",
         "Corporate fluff - reflects everything"),
        
        # ABSORBER (Solid content)
        ("E = mc² describes the equivalence of mass and energy.",
         "Physics - dense but not opaque"),
        
        # REFLECTOR (Shiny but hollow)
        ("Amazing! Incredible! Best ever! Absolutely fantastic results!",
         "Empty enthusiasm - all shine"),
    ]
    
    for text, label in test_cases:
        print(f"\n{'='*70}")
        print(f"  TEST: {label}")
        print(f"{'='*70}")
        
        analysis = camera.photograph(text)
        print(analysis)
    
    print("\n" + "="*70)
    print("  THE INVERSION PRINCIPLE")
    print("="*70)
    print("""
    NORMAL CAMERA:
    └─ Records what surfaces REFLECT (the shiny parts)
    └─ A mirror looks bright (reflecting all light)
    └─ A black body looks dark (absorbing all light)
    
    TENT CAMERA (INVERTED):
    └─ Records what narratives ABSORB (the dense parts)
    └─ A mirror narrative is HOLLOW (reflects buzzwords, contains nothing)
    └─ A black body narrative is DENSE (absorbs attention, contains truth)
    
    "We see the remainder. TENT measures the missing part."
    """)

if __name__ == "__main__":
    demo()
