#!/usr/bin/env python3
"""
TENT v4.0 PIGMENT ENGINE
========================
Phase 152: Semantic Pointillism (Python Implementation)

The Holographic Reality Layer.
- Micro View (Machine): Each dot is a Seed containing Truth
- Macro View (Human): Arranged dots form a smooth Gradient

"The user sees the beauty. The machine reads the truth."

This Python version can be used immediately while the Rust/WASM version is compiled.
"""

import hashlib
import math
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum

# Import our diagnostic modules
from vacuum_gauge import VacuumGauge
from beautiful_lie_detector import BeautifulLieDetector

# =============================================================================
# CONSTANTS
# =============================================================================

PHI = 1.618033988749895  # Golden Ratio
DELTA = 2.414213562373095  # Silver Ratio
PI = math.pi

# =============================================================================
# THE PIGMENT - The Holographic Data Dot
# =============================================================================

class PigmentClass(Enum):
    DIAMOND = "💎 DIAMOND - Pure crystalline truth"
    CRYSTAL = "✨ CRYSTAL - High resonance"
    VAPOR = "☁️ VAPOR - Low density, high friction"
    BUBBLE = "🫧 BUBBLE - Empty noise"

@dataclass
class Pigment:
    """
    A Pigment is a "pixel" that contains both visual and semantic information.
    
    - color_value: What the Human sees (RGBA)
    - seed_hash: What the Machine reads (256-bit hash)
    - prime_coordinate: Where it sits in the Prime Universe
    - resonance: How "true" this pigment is (0.0 - 1.0)
    """
    color_value: int          # RGBA as 32-bit integer
    seed_hash: bytes          # 256-bit hash
    prime_coordinate: int     # Prime number position
    resonance: float          # 0.0 - 1.0
    density: float            # Semantic mass
    friction: float           # Aesthetic vs logic tension
    classification: PigmentClass
    
    @classmethod
    def from_text(cls, text: str, prime: int = 2) -> 'Pigment':
        """Create a Pigment from text."""
        # Compute hash
        seed_hash = hashlib.sha256(text.encode()).digest()
        
        # Compute color from hash
        r, g, b = seed_hash[0], seed_hash[1], seed_hash[2]
        color_value = (r << 24) | (g << 16) | (b << 8) | 0xFF
        
        # Compute resonance (phase alignment with prime)
        hash_int = int.from_bytes(seed_hash[:8], 'little')
        hash_phase = (hash_int * PHI) % (2 * PI)
        prime_phase = (prime * DELTA) % (2 * PI)
        phase_diff = abs(hash_phase - prime_phase)
        resonance = max(0.0, min(1.0, 1.0 - phase_diff / PI))
        
        # Use vacuum gauge for density
        gauge = VacuumGauge()
        analysis = gauge.analyze(text)
        density = analysis.density_score
        
        # Use friction detector
        detector = BeautifulLieDetector()
        friction_analysis = detector.analyze(text)
        friction = friction_analysis.friction
        
        # Classify
        classification = cls._classify(resonance, density, friction)
        
        return cls(
            color_value=color_value,
            seed_hash=seed_hash,
            prime_coordinate=prime,
            resonance=resonance,
            density=density,
            friction=friction,
            classification=classification
        )
    
    @staticmethod
    def _classify(resonance: float, density: float, friction: float) -> PigmentClass:
        """Classify the pigment based on its properties."""
        if resonance > 0.7 and density > 2.0 and friction < 0.3:
            return PigmentClass.DIAMOND
        elif resonance > 0.5 and density > 1.0:
            return PigmentClass.CRYSTAL
        elif density > 0.5:
            return PigmentClass.VAPOR
        else:
            return PigmentClass.BUBBLE
    
    def rgb(self) -> Tuple[int, int, int]:
        """Get RGB components."""
        r = (self.color_value >> 24) & 0xFF
        g = (self.color_value >> 16) & 0xFF
        b = (self.color_value >> 8) & 0xFF
        return (r, g, b)
    
    def resonance_color(self) -> Tuple[int, int, int]:
        """Get color adjusted by resonance (greener = more true)."""
        r, g, b = self.rgb()
        
        # Blend toward green for high resonance, red for low
        truth_r = int(r * (1.0 - self.resonance))
        truth_g = int(min(255, g * self.resonance + 128 * self.resonance))
        truth_b = int(b * 0.5)
        
        return (truth_r, truth_g, truth_b)
    
    def hex_color(self) -> str:
        """Get hex color string."""
        r, g, b = self.resonance_color()
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def is_diamond(self) -> bool:
        """Check if this is a Diamond (high truth density)."""
        return self.classification == PigmentClass.DIAMOND
    
    def is_bubble(self) -> bool:
        """Check if this is a Bubble (empty noise)."""
        return self.classification == PigmentClass.BUBBLE

# =============================================================================
# THE CANVAS - A Grid of Pigments
# =============================================================================

class Canvas:
    """A 2D grid of Pigments forming the 'Gradient'."""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pigments: List[List[Optional[Pigment]]] = [
            [None for _ in range(width)] for _ in range(height)
        ]
    
    def set(self, x: int, y: int, pigment: Pigment):
        """Set a pigment at position."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pigments[y][x] = pigment
    
    def get(self, x: int, y: int) -> Optional[Pigment]:
        """Get a pigment at position."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.pigments[y][x]
        return None
    
    def average_resonance(self) -> float:
        """Calculate average resonance of the canvas."""
        total = 0.0
        count = 0
        for row in self.pigments:
            for p in row:
                if p is not None:
                    total += p.resonance
                    count += 1
        return total / count if count > 0 else 0.0
    
    def diamond_count(self) -> int:
        """Count diamonds in the canvas."""
        return sum(
            1 for row in self.pigments 
            for p in row 
            if p is not None and p.is_diamond()
        )
    
    def bubble_count(self) -> int:
        """Count bubbles in the canvas."""
        return sum(
            1 for row in self.pigments 
            for p in row 
            if p is not None and p.is_bubble()
        )
    
    def to_html(self) -> str:
        """Generate an HTML table visualization."""
        html = ['<table style="border-collapse:collapse;">']
        
        for row in self.pigments:
            html.append('<tr>')
            for p in row:
                if p is not None:
                    color = p.hex_color()
                    title = f"R:{p.resonance:.2f} D:{p.density:.2f} F:{p.friction:.2f}"
                    html.append(
                        f'<td style="width:10px;height:10px;background:{color};" '
                        f'title="{title}"></td>'
                    )
                else:
                    html.append('<td style="width:10px;height:10px;background:#000;"></td>')
            html.append('</tr>')
        
        html.append('</table>')
        return '\n'.join(html)

# =============================================================================
# THE POINTILLIST ENGINE
# =============================================================================

class PointillistEngine:
    """
    The Semantic Pointillism Engine.
    Converts text into a grid of holographic pigments.
    """
    
    def __init__(self, primes: Optional[List[int]] = None):
        """Initialize with a list of primes for the Prime Graph."""
        self.primes = primes or self._generate_primes(1000)
    
    def _generate_primes(self, limit: int) -> List[int]:
        """Generate primes up to limit."""
        sieve = [True] * limit
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i*i, limit, i):
                    sieve[j] = False
        
        return [i for i, is_prime in enumerate(sieve) if is_prime]
    
    def text_to_canvas(self, text: str, width: int = 10) -> Canvas:
        """Convert text to a canvas of pigments."""
        words = text.split()
        height = (len(words) + width - 1) // width
        
        canvas = Canvas(width, height)
        
        for i, word in enumerate(words):
            x = i % width
            y = i // width
            prime = self.primes[i % len(self.primes)]
            pigment = Pigment.from_text(word, prime)
            canvas.set(x, y, pigment)
        
        return canvas
    
    def analyze_document(self, text: str) -> dict:
        """Analyze a document and return statistics."""
        canvas = self.text_to_canvas(text)
        
        return {
            "dimensions": f"{canvas.width}x{canvas.height}",
            "total_pigments": canvas.width * canvas.height,
            "average_resonance": canvas.average_resonance(),
            "diamonds": canvas.diamond_count(),
            "bubbles": canvas.bubble_count(),
            "verdict": self._get_verdict(canvas)
        }
    
    def _get_verdict(self, canvas: Canvas) -> str:
        """Get overall verdict for canvas."""
        avg = canvas.average_resonance()
        diamonds = canvas.diamond_count()
        bubbles = canvas.bubble_count()
        total = max(1, canvas.width * canvas.height)
        
        diamond_ratio = diamonds / total
        bubble_ratio = bubbles / total
        
        if avg > 0.7 and diamond_ratio > 0.3:
            return "🌟 SUPERNOVA - High truth density"
        elif avg > 0.5 and bubble_ratio < 0.2:
            return "⭐ STAR - Solid foundation"
        elif bubble_ratio > 0.5:
            return "🫧 VAPOR CLOUD - Mostly fluff"
        else:
            return "🪐 PLANET - Mixed content"

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 PIGMENT ENGINE                                        ║")
    print("║  Phase 152: Semantic Pointillism                                 ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    engine = PointillistEngine()
    
    # Test cases
    texts = [
        ("E = mc²", "Physics equation"),
        ("The Riemann Hypothesis states that all non-trivial zeros have real part 1/2.", "Mathematical truth"),
        ("We leverage synergy to proactively optimize stakeholder value.", "Corporate fluff"),
    ]
    
    for text, label in texts:
        print(f"{'='*60}")
        print(f"  {label}")
        print(f"  \"{text[:50]}{'...' if len(text) > 50 else ''}\"")
        print(f"-{'-'*58}")
        
        pigment = Pigment.from_text(text, 17)
        
        print(f"  Color:      {pigment.hex_color()}")
        print(f"  Resonance:  {pigment.resonance:.3f}")
        print(f"  Density:    {pigment.density:.3f}")
        print(f"  Friction:   {pigment.friction:.3f}")
        print(f"  Class:      {pigment.classification.value}")
        print()
    
    # Document analysis
    print("=" * 60)
    print("  DOCUMENT ANALYSIS")
    print("-" * 60)
    
    document = """
    The fundamental theorem of calculus establishes the relationship 
    between differentiation and integration. This theorem provides 
    a practical method for evaluating definite integrals and shows 
    that antidifferentiation is the reverse of differentiation.
    """
    
    analysis = engine.analyze_document(document)
    for key, value in analysis.items():
        print(f"  {key}: {value}")
    
    print()
    print("  'The user sees the beauty. The machine reads the truth.'")

if __name__ == "__main__":
    demo()
