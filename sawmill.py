#!/usr/bin/env python3
"""
TENT v4.0 SAWMILL
=================
Phase 158: Stripping the Bark

The Sawmill strips the "Green Light" (reflected fluff) from text,
leaving only the "Red/Blue" (absorbed mass).

Physics:
- High Albedo (1.0) = Mirror = Buzzword (all reflection, no mass)
- Low Albedo (0.1) = Iron = Anchor (all absorption, pure mass)

Process:
1. Calculate albedo per word
2. Cut anything > 0.7
3. Show what remains

"A Chrome Sphere is cold. A Molten Iron Sphere glows."
"""

import re
from dataclasses import dataclass
from typing import List, Tuple
from enum import Enum

# =============================================================================
# ALBEDO CLASSIFICATIONS
# =============================================================================

# MIRRORS (Albedo 1.0) - Pure reflection, no mass
MIRRORS = {
    'synergy', 'synergistic', 'leverage', 'leveraging', 'leveraged',
    'paradigm', 'paradigms', 'proactive', 'proactively',
    'holistic', 'holistically', 'stakeholder', 'stakeholders',
    'actionable', 'incentivize', 'incentivized', 'optimize', 'optimized',
    'revolutionary', 'game-changing', 'disruptive', 'disrupting',
    'innovative', 'innovate', 'ideate', 'ideation',
    'ecosystem', 'ecosystems', 'scalable', 'scalability',
    'best-in-class', 'world-class', 'cutting-edge', 'bleeding-edge',
    'thought-leader', 'thought-leadership', 'value-add', 'value-added',
    'synergize', 'synergizing', 'impactful', 'impacting',
    'empower', 'empowering', 'empowered', 'enablement',
    'bandwidth', 'deliverables', 'low-hanging', 'pushback',
    'circle-back', 'pivot', 'pivoting', 'agile', 'lean',
}

# HIGH REFLECTION (Albedo 0.9) - Almost all reflection
HIGH_REFLECTION = {
    'guaranteed', 'guarantee', 'guarantees', 'guaranteeing',
    'infinite', 'infinitely', 'unlimited', 'limitless',
    'passive', 'passively', 'effortless', 'effortlessly',
    'instant', 'instantly', 'immediate', 'immediately',
    'amazing', 'incredible', 'unbelievable', 'fantastic',
    'revolutionary', 'breakthrough', 'miracle', 'miraculous',
    'secret', 'secrets', 'exclusive', 'exclusively',
    'free', 'risk-free', 'foolproof', 'fail-proof',
}

# IRON (Albedo 0.1) - Pure absorption, heavy mass
IRON = {
    'prime', 'primes', 'theorem', 'theorems', 'proof', 'proofs',
    'derivative', 'integral', 'calculus', 'differential',
    'thermodynamic', 'thermodynamics', 'entropy', 'enthalpy',
    'quantum', 'wave', 'particle', 'photon', 'electron',
    'algorithm', 'function', 'equation', 'equations',
    'hypothesis', 'axiom', 'axioms', 'lemma', 'corollary',
    'riemann', 'zeta', 'zeros', 'fourier', 'laplace',
    'euler', 'gauss', 'gaussian', 'manifold', 'topology',
    'tensor', 'vector', 'matrix', 'eigenvalue', 'eigenvector',
    'conservation', 'symmetry', 'invariant', 'invariance',
    'causation', 'causal', 'falsifiable', 'empirical',
    'measurement', 'observation', 'experiment', 'experimental',
    'mass', 'energy', 'force', 'momentum', 'velocity',
    'curvature', 'surface', 'minimal', 'geodesic',
}

# GLASS (Albedo 0.5) - Neutral connectors
GLASS = {
    'the', 'a', 'an', 'of', 'to', 'in', 'for', 'on', 'with',
    'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'and', 'or', 'but', 'if', 'then', 'that', 'which',
    'this', 'these', 'those', 'it', 'its', 'their', 'our',
    'we', 'you', 'they', 'he', 'she', 'i', 'me', 'us',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
    'can', 'could', 'should', 'may', 'might', 'must',
    'all', 'any', 'some', 'no', 'not', 'very', 'just',
}

# =============================================================================
# DATA STRUCTURES
# =============================================================================

class WoodType(Enum):
    HEARTWOOD = "🪵 HEARTWOOD (Albedo < 0.3) - Dense core"
    SAPWOOD = "🌲 SAPWOOD (Albedo 0.3-0.5) - Solid content"
    BARK = "🍂 BARK (Albedo 0.5-0.7) - Neutral filler"
    LICHEN = "🦠 LICHEN (Albedo 0.7-0.9) - Surface growth"
    MIRROR = "🪞 MIRROR (Albedo > 0.9) - Pure reflection"

@dataclass
class WordAnalysis:
    word: str
    albedo: float
    wood_type: WoodType
    keep: bool

@dataclass
class SawmillReport:
    original: str
    original_word_count: int
    lumber: str
    lumber_word_count: int
    compression_ratio: float
    word_analyses: List[WordAnalysis]

# =============================================================================
# THE SAWMILL
# =============================================================================

class Sawmill:
    """
    The Digital Saw.
    
    Strips the bark (high-albedo words) from text,
    leaving only the lumber (low-albedo words).
    """
    
    def __init__(self, cut_threshold: float = 0.7):
        self.cut_threshold = cut_threshold
    
    def calculate_albedo(self, word: str) -> float:
        """Calculate the albedo of a single word."""
        w = word.lower().strip('.,!?;:\'\"()[]{}')
        
        if w in MIRRORS:
            return 1.0
        elif w in HIGH_REFLECTION:
            return 0.9
        elif w in IRON:
            return 0.1
        elif w in GLASS:
            return 0.5
        elif len(w) <= 2:
            return 0.6  # Short words are often connectors
        else:
            # Default: estimate based on length and patterns
            # Longer words with more syllables tend to be fluffier
            syllables = self._count_syllables(w)
            if syllables >= 4:
                return 0.7  # Long words often fluffy
            elif syllables >= 3:
                return 0.6
            else:
                return 0.4  # Short content words
    
    def _count_syllables(self, word: str) -> int:
        """Estimate syllable count."""
        word = word.lower()
        vowels = 'aeiouy'
        count = 0
        prev_vowel = False
        
        for char in word:
            is_vowel = char in vowels
            if is_vowel and not prev_vowel:
                count += 1
            prev_vowel = is_vowel
        
        if word.endswith('e') and count > 1:
            count -= 1
        
        return max(1, count)
    
    def _classify_wood(self, albedo: float) -> WoodType:
        """Classify word based on albedo."""
        if albedo > 0.9:
            return WoodType.MIRROR
        elif albedo > 0.7:
            return WoodType.LICHEN
        elif albedo > 0.5:
            return WoodType.BARK
        elif albedo > 0.3:
            return WoodType.SAPWOOD
        else:
            return WoodType.HEARTWOOD
    
    def mill(self, text: str) -> SawmillReport:
        """
        Run the sawmill on a piece of text.
        
        Returns a report showing what was cut and what remains.
        """
        # Extract words while preserving punctuation positions
        words = text.split()
        original_count = len(words)
        
        analyses = []
        lumber_words = []
        
        for word in words:
            albedo = self.calculate_albedo(word)
            wood_type = self._classify_wood(albedo)
            keep = albedo <= self.cut_threshold
            
            analyses.append(WordAnalysis(
                word=word,
                albedo=albedo,
                wood_type=wood_type,
                keep=keep,
            ))
            
            if keep:
                lumber_words.append(word)
        
        lumber = ' '.join(lumber_words)
        lumber_count = len(lumber_words)
        
        compression = 1 - (lumber_count / original_count) if original_count > 0 else 0
        
        return SawmillReport(
            original=text,
            original_word_count=original_count,
            lumber=lumber,
            lumber_word_count=lumber_count,
            compression_ratio=compression,
            word_analyses=analyses,
        )
    
    def display_report(self, report: SawmillReport):
        """Display a visual sawmill report."""
        print()
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║  TENT v4.0 SAWMILL - Stripping the Bark                              ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
        print()
        print(f"INPUT ({report.original_word_count} words):")
        print(f'  "{report.original[:70]}{"..." if len(report.original) > 70 else ""}"')
        print()
        print("┌─────────────────────────────────────────────────────────────────────┐")
        print("│  WORD-BY-WORD ANALYSIS                                              │")
        print("├─────────────────────────────────────────────────────────────────────┤")
        
        for wa in report.word_analyses:
            status = "KEEP" if wa.keep else "CUT "
            icon = "✓" if wa.keep else "✗"
            w = wa.word[:15].ljust(15)
            print(f"│  {icon} {w} Albedo: {wa.albedo:.1f} → {status}")
        
        print("└─────────────────────────────────────────────────────────────────────┘")
        print()
        print(f"OUTPUT (The Lumber) - {report.lumber_word_count} words:")
        
        if report.lumber_word_count == 0:
            print('  "...(nothing remains)..."')
            print()
            print("  ⚠️ WARNING: This text was 100% BARK. No wood inside.")
        else:
            print(f'  "{report.lumber}"')
        
        print()
        print(f"COMPRESSION: {report.compression_ratio:.0%} of text was reflection (cut)")
        print()
        
        # Wood composition
        heartwood = sum(1 for wa in report.word_analyses if wa.wood_type == WoodType.HEARTWOOD)
        sapwood = sum(1 for wa in report.word_analyses if wa.wood_type == WoodType.SAPWOOD)
        bark = sum(1 for wa in report.word_analyses if wa.wood_type == WoodType.BARK)
        lichen = sum(1 for wa in report.word_analyses if wa.wood_type == WoodType.LICHEN)
        mirror = sum(1 for wa in report.word_analyses if wa.wood_type == WoodType.MIRROR)
        
        print("COMPOSITION:")
        print(f"  🪵 Heartwood: {heartwood} ({heartwood/len(report.word_analyses)*100:.0f}%)")
        print(f"  🌲 Sapwood:   {sapwood} ({sapwood/len(report.word_analyses)*100:.0f}%)")
        print(f"  🍂 Bark:      {bark} ({bark/len(report.word_analyses)*100:.0f}%)")
        print(f"  🦠 Lichen:    {lichen} ({lichen/len(report.word_analyses)*100:.0f}%)")
        print(f"  🪞 Mirror:    {mirror} ({mirror/len(report.word_analyses)*100:.0f}%)")
        print()

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 SAWMILL DEMONSTRATION                                 ║")
    print("║  \"Stripping the Green Light to reveal the Red/Blue\"              ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    sawmill = Sawmill(cut_threshold=0.7)
    
    test_cases = [
        # Pure fluff
        ("We are proactively leveraging our synergistic paradigm to guarantee "
         "infinite passive income for all stakeholders.",
         "Marketing scam"),
        
        # Technical truth
        ("The Riemann Hypothesis states that all non-trivial zeros of the "
         "Zeta function have real part equal to one half.",
         "Mathematical truth"),
        
        # Mixed content
        ("Our innovative quantum algorithm leverages cutting-edge machine learning "
         "to compute eigenvalues of the Hamiltonian matrix.",
         "Mixed tech/marketing"),
        
        # Physics
        ("Energy equals mass times the speed of light squared.",
         "Physics (E=mc²)"),
    ]
    
    for text, label in test_cases:
        print(f"\n{'='*72}")
        print(f"  TEST: {label}")
        print(f"{'='*72}")
        
        report = sawmill.mill(text)
        sawmill.display_report(report)

if __name__ == "__main__":
    demo()
