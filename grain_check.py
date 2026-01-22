#!/usr/bin/env python3
"""
TENT v4.0 GRAIN CHECK
=====================
Phase 161: Provenance Analysis (Anisotropy)

The Master Carpenter's insight:
- LONG GRAIN:  Fibers run parallel. Strong surface. Good bond.
- SHORT GRAIN: End grain. Open straws. Glue wicks away. WEAK.

In TENT:
- LONG GRAIN:  Historical concept (100+ years). Thousands of citations.
- SHORT GRAIN: New assertion (< 1 year). No provenance.

The Rule:
"Never glue End Grain to Long Grain without a spline."
(A spline in logic = a formal proof)

The Glue-Starved Lie:
When scams try to bond their new token to "Thermodynamics",
the glue wicks into the end grain and the joint fails.
"""

import re
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum

from sawmill import Sawmill, IRON

# =============================================================================
# GRAIN TYPES
# =============================================================================

class GrainType(Enum):
    """Classification of word provenance."""
    LONG_GRAIN = "🌲 LONG GRAIN - Historical, 100+ years of fibers"
    MEDIUM_GRAIN = "🪵 MEDIUM GRAIN - Established, 10-100 years"
    SHORT_GRAIN = "🪓 SHORT GRAIN - Recent, < 10 years"
    END_GRAIN = "⚠️ END GRAIN - No history, pure assertion"

class JointQuality(Enum):
    """Quality of the grain alignment in a joint."""
    PERFECT = "✓ PERFECT MATCH - Long to Long or Short to Short"
    ACCEPTABLE = "△ ACCEPTABLE - Medium alignment"
    STARVED = "✗ STARVED JOINT - End Grain to Long Grain (FAILURE)"

# =============================================================================
# FIBER LENGTH DATABASE (Provenance Map)
# =============================================================================

# LONG GRAIN: 100+ years of history (Established Laws)
LONG_GRAIN_WORDS = {
    # Physics (300+ years)
    'gravity', 'mass', 'energy', 'force', 'momentum', 'velocity',
    'acceleration', 'thermodynamics', 'entropy', 'conservation',
    'light', 'wave', 'particle', 'heat', 'temperature', 'pressure',
    
    # Mathematics (1000+ years)
    'prime', 'primes', 'number', 'equation', 'theorem', 'proof',
    'geometry', 'algebra', 'calculus', 'derivative', 'integral',
    'pi', 'euler', 'gauss', 'riemann', 'zeta', 'infinity',
    'ratio', 'proportion', 'pythagorean', 'euclidean',
    
    # Logic (2000+ years)
    'logic', 'axiom', 'truth', 'false', 'premise', 'conclusion',
    'syllogism', 'deduction', 'induction', 'contradiction',
    
    # Chemistry (200+ years)
    'atom', 'molecule', 'element', 'compound', 'reaction',
    'oxygen', 'hydrogen', 'carbon', 'periodic',
    
    # Biology (150+ years)
    'evolution', 'natural', 'selection', 'species', 'gene',
    'cell', 'dna', 'organism', 'ecosystem',
}

# MEDIUM GRAIN: 10-100 years (Established but Modern)
MEDIUM_GRAIN_WORDS = {
    # Computing (50-80 years)
    'algorithm', 'computer', 'software', 'hardware', 'binary',
    'processor', 'memory', 'data', 'program', 'code',
    
    # Modern Physics (50-100 years)
    'quantum', 'relativity', 'spacetime', 'photon', 'electron',
    'neutron', 'proton', 'quark', 'higgs',
    
    # Information Theory (70+ years)
    'information', 'entropy', 'bit', 'byte', 'bandwidth',
    'signal', 'noise', 'channel', 'encoding',
    
    # Economics (100+ years)
    'market', 'economy', 'inflation', 'supply', 'demand',
    'capital', 'investment', 'currency', 'exchange',
}

# SHORT GRAIN: < 10 years (Recent inventions)
SHORT_GRAIN_WORDS = {
    # Crypto (< 15 years)
    'bitcoin', 'blockchain', 'crypto', 'cryptocurrency',
    'nft', 'token', 'defi', 'dao', 'web3', 'metaverse',
    'staking', 'yield', 'airdrop', 'hodl', 'fomo',
    
    # Recent Tech (< 10 years)
    'ai', 'gpt', 'llm', 'chatgpt', 'deepfake',
    'tiktok', 'influencer', 
    
    # Recent Buzzwords
    'disrupt', 'pivot', 'unicorn', 'moonshot',
}

# END GRAIN: Self-referential or brand names (No history)
END_GRAIN_PATTERNS = [
    r'\bour\s+\w+',       # "our token", "our platform"
    r'\bmy\s+\w+',        # "my coin", "my app"
    r'\bwe\s+',           # "we created", "we offer"
    r'\bi\s+',            # "I invented"
    r'[A-Z][a-z]+coin',   # SafeMoon, DogeCoin, etc.
    r'[A-Z][a-z]+fi',     # DeFi variants
    r'[A-Z][a-z]+swap',   # UniSwap variants
]

# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class GrainAnalysis:
    """Analysis of a word's grain/provenance."""
    word: str
    grain_type: GrainType
    fiber_length: int  # 0 = end grain, 100 = long grain

@dataclass
class JointGrainReport:
    """Analysis of grain alignment in a joint."""
    text: str
    word_analyses: List[GrainAnalysis]
    joints: List[Tuple[GrainAnalysis, GrainAnalysis, JointQuality]]
    has_starved_joint: bool
    overall_quality: JointQuality

# =============================================================================
# THE GRAIN CHECK
# =============================================================================

class GrainCheck:
    """
    The Provenance Analyzer.
    
    Examines the "fiber length" of concepts to detect when
    someone tries to glue End Grain to Long Grain.
    """
    
    def __init__(self):
        self.sawmill = Sawmill()
    
    def analyze_word(self, word: str) -> GrainAnalysis:
        """Analyze the grain of a single word."""
        w = word.lower().strip('.,!?;:\'\"')
        
        # Check for end grain patterns first
        for pattern in END_GRAIN_PATTERNS:
            if re.match(pattern, word.lower()):
                return GrainAnalysis(word, GrainType.END_GRAIN, 0)
        
        # Check dictionaries
        if w in LONG_GRAIN_WORDS or w in IRON:
            return GrainAnalysis(word, GrainType.LONG_GRAIN, 100)
        elif w in MEDIUM_GRAIN_WORDS:
            return GrainAnalysis(word, GrainType.MEDIUM_GRAIN, 50)
        elif w in SHORT_GRAIN_WORDS:
            return GrainAnalysis(word, GrainType.SHORT_GRAIN, 10)
        
        # Default: medium grain for unknown content words
        if len(w) > 3:
            return GrainAnalysis(word, GrainType.MEDIUM_GRAIN, 30)
        else:
            return GrainAnalysis(word, GrainType.SHORT_GRAIN, 10)
    
    def analyze_joint(self, grain_a: GrainAnalysis, grain_b: GrainAnalysis) -> JointQuality:
        """
        Analyze the quality of a joint between two grains.
        
        The worst case: End Grain to Long Grain.
        The glue wicks into the end grain, leaving a starved joint.
        """
        diff = abs(grain_a.fiber_length - grain_b.fiber_length)
        
        # Check for the fatal combination
        if (grain_a.grain_type == GrainType.END_GRAIN and 
            grain_b.grain_type == GrainType.LONG_GRAIN):
            return JointQuality.STARVED
        if (grain_b.grain_type == GrainType.END_GRAIN and 
            grain_a.grain_type == GrainType.LONG_GRAIN):
            return JointQuality.STARVED
        
        # Short to Long is also weak
        if (grain_a.grain_type == GrainType.SHORT_GRAIN and 
            grain_b.grain_type == GrainType.LONG_GRAIN):
            return JointQuality.STARVED
        if (grain_b.grain_type == GrainType.SHORT_GRAIN and 
            grain_a.grain_type == GrainType.LONG_GRAIN):
            return JointQuality.STARVED
        
        # Same grain type = perfect
        if grain_a.grain_type == grain_b.grain_type:
            return JointQuality.PERFECT
        
        # Adjacent types = acceptable
        if diff <= 50:
            return JointQuality.ACCEPTABLE
        
        return JointQuality.STARVED
    
    def analyze_text(self, text: str) -> JointGrainReport:
        """
        Analyze a full text for grain alignment issues.
        
        Finds all heartwood words and checks their grain compatibility.
        """
        # Get heartwood words
        sawmill_report = self.sawmill.mill(text)
        lumber_words = sawmill_report.lumber.split()
        
        # Analyze grain of each word
        word_analyses = []
        for word in lumber_words:
            analysis = self.analyze_word(word)
            # Only care about content words (not connectors)
            if analysis.grain_type != GrainType.SHORT_GRAIN or len(word) > 4:
                word_analyses.append(analysis)
        
        # Find joints between significant words
        joints = []
        has_starved = False
        
        # Find long grain and short/end grain words
        long_grains = [a for a in word_analyses if a.grain_type == GrainType.LONG_GRAIN]
        short_grains = [a for a in word_analyses 
                       if a.grain_type in (GrainType.SHORT_GRAIN, GrainType.END_GRAIN)]
        
        # Check for starved joints
        for long_g in long_grains:
            for short_g in short_grains:
                quality = self.analyze_joint(long_g, short_g)
                joints.append((long_g, short_g, quality))
                if quality == JointQuality.STARVED:
                    has_starved = True
        
        # Determine overall quality
        if has_starved:
            overall = JointQuality.STARVED
        elif joints and all(j[2] == JointQuality.PERFECT for j in joints):
            overall = JointQuality.PERFECT
        elif joints:
            overall = JointQuality.ACCEPTABLE
        else:
            overall = JointQuality.PERFECT
        
        return JointGrainReport(
            text=text,
            word_analyses=word_analyses,
            joints=joints,
            has_starved_joint=has_starved,
            overall_quality=overall,
        )
    
    def display_report(self, report: JointGrainReport):
        """Display a visual grain analysis report."""
        print()
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║  TENT v4.0 GRAIN CHECK - Provenance Analysis                         ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
        print()
        print(f"INPUT: \"{report.text[:65]}{'...' if len(report.text) > 65 else ''}\"")
        print()
        
        # Word grain analysis
        print("┌─────────────────────────────────────────────────────────────────────┐")
        print("│  FIBER ANALYSIS                                                     │")
        print("├─────────────────────────────────────────────────────────────────────┤")
        
        for wa in report.word_analyses[:10]:  # Limit display
            fiber_bar = "█" * (wa.fiber_length // 10) + "░" * (10 - wa.fiber_length // 10)
            print(f"│  {wa.word[:15].ljust(15)} [{fiber_bar}] {wa.grain_type.value}")
        
        print("└─────────────────────────────────────────────────────────────────────┘")
        
        # Joint analysis
        if report.joints:
            print()
            print("┌─────────────────────────────────────────────────────────────────────┐")
            print("│  JOINT GRAIN ALIGNMENT                                              │")
            print("├─────────────────────────────────────────────────────────────────────┤")
            
            for grain_a, grain_b, quality in report.joints[:5]:
                icon = "✓" if quality == JointQuality.PERFECT else "△" if quality == JointQuality.ACCEPTABLE else "✗"
                print(f"│  {icon} [{grain_a.word}] ⟷ [{grain_b.word}]")
                print(f"│      └─ {quality.value}")
            
            print("└─────────────────────────────────────────────────────────────────────┘")
        
        print()
        print(f"OVERALL: {report.overall_quality.value}")
        
        if report.has_starved_joint:
            print()
            print("  ⚠️  WARNING: GLUE-STARVED JOINT DETECTED!")
            print("  ⚠️  End Grain is trying to bond with Long Grain.")
            print("  ⚠️  The joint will fail under stress.")
            print("  ⚠️  Require a SPLINE (formal proof) to reinforce.")
        
        print()

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 GRAIN CHECK DEMONSTRATION                             ║")
    print("║  \"Never glue End Grain to Long Grain without a spline.\"          ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    checker = GrainCheck()
    
    test_cases = [
        # STARVED JOINT: New + Old without proof
        ("Our revolutionary crypto-token utilizes the Second Law of Thermodynamics to generate passive income.",
         "Scam: End Grain + Long Grain"),
        
        # PERFECT: Long Grain to Long Grain
        ("Energy equals mass times the speed of light squared.",
         "Physics: Long Grain to Long Grain"),
        
        # PERFECT: Short Grain to Short Grain (honest)
        ("Our new blockchain platform offers token staking rewards.",
         "Honest Crypto: Short Grain to Short Grain"),
        
        # STARVED: Recent borrowing credibility
        ("Bitcoin mining follows the laws of thermodynamics and entropy.",
         "Mixed: Short Grain + Long Grain"),
        
        # PERFECT: Pure established science
        ("The derivative of position with respect to time equals velocity.",
         "Pure Physics: All Long Grain"),
    ]
    
    for text, label in test_cases:
        print(f"\n{'='*72}")
        print(f"  TEST: {label}")
        print(f"{'='*72}")
        
        report = checker.analyze_text(text)
        checker.display_report(report)

if __name__ == "__main__":
    demo()
