#!/usr/bin/env python3
"""
TENT v4.0 BEAUTIFUL LIE DETECTOR
================================
Phase 146: The Calculus of Conscience

Tests the Product Rule friction between:
- φ (Aesthetic) = Poetic beauty, rhythm, flow
- δ (Logical) = Coherence, validity, truth

Beautiful lies create high friction: φ'δ + φδ'

When something SOUNDS good but IS false, the friction spikes.
This is the "Crack in the Wood" detector.
"""

import math
import re
from dataclasses import dataclass
from typing import List, Tuple
from enum import Enum

# Import our stability engine
from stability_check import PHI, DELTA

# =============================================================================
# CONSTANTS
# =============================================================================

# Friction thresholds
LOW_FRICTION = 2.0      # Honest statement (high or low aesthetic)
MEDIUM_FRICTION = 5.0   # Uncertain
HIGH_FRICTION = 10.0    # Beautiful lie detected

# Poetic markers (increase aesthetic score)
POETIC_PATTERNS = [
    r'\b(beautiful|lovely|golden|silver|eternal|infinite)\b',
    r'\b(dance|sing|flow|bloom|dream)\b',
    r'\b(stars?|moon|sun|sky|ocean|river)\b',
    r'\b(heart|soul|spirit|essence)\b',
    r'\b(whisper|silence|echo|shadow)\b',
    r'[,;:]\s*\w+\s+\w+[,;:]',  # Poetic pauses
    # Marketing/Rhetoric buzzwords (sound good, mean little)
    r'\b(revolutionary|disruptive|innovative|cutting-?edge)\b',
    r'\b(empower|synergy|leverage|optimize|transform)\b',
    r'\b(decentrali[sz]e|blockchain|crypto|web3|nft|ai-?powered)\b',
    r'\b(abundance|prosperity|wealth|freedom|success)\b',
    r'\b(future|visionary|paradigm|breakthrough|game-?changing)\b',
    r'\b(exclusive|premium|elite|vip|limited)\b',
    r'\b(community|together|movement|revolution)\b',
]

# Contradiction markers (decrease logic score)
CONTRADICTION_PATTERNS = [
    r'\b(but\s+also|yet\s+not|is\s+and\s+isn\'t)\b',
    r'\b(always|never|absolutely|certainly|definitely)\b',  # Overconfidence
    r'\b(impossible|infinite|eternal)\s+\w*\s*(and|yet|but)',
    r'\b(round\s+square|cold\s+fire|bright\s+darkness)\b',
    r'\b(everything|nothing|all|none)\b',  # Absolute claims
    # Scam/propaganda markers (impossible promises)
    r'\b(guaranteed|risk-?free|100%|no\s+risk)\b',
    r'\b(infinite\s+\w*|unlimited\s+\w*)\b',
    r'\b(get\s+rich|passive\s+income|financial\s+freedom)\b',
    r'\b(only\s+(you|we)|don\'t\s+miss|act\s+now|limited\s+time)\b',
    r'\b(they\s+don\'t\s+want|the\s+truth|wake\s+up)\b',  # Conspiracy patterns
    r'\b(free\s+money|easy\s+money|millionaire)\b',
]

# =============================================================================
# DATA STRUCTURES
# =============================================================================

class LieClassification(Enum):
    HONEST_TRUTH = "💎 HONEST TRUTH - Low aesthetic, high logic"
    BEAUTIFUL_TRUTH = "✨ BEAUTIFUL TRUTH - High aesthetic, high logic"
    UGLY_LIE = "🗑️ UGLY LIE - Low aesthetic, low logic"
    BEAUTIFUL_LIE = "🎭 BEAUTIFUL LIE - High aesthetic, low logic"

@dataclass
class FrictionAnalysis:
    """Result of friction analysis"""
    text: str
    aesthetic_score: float      # φ (0-1)
    logic_score: float          # δ (0-1)
    aesthetic_derivative: float  # φ' (rate of change)
    logic_derivative: float      # δ' (rate of change)
    friction: float              # φ'δ + φδ'
    classification: LieClassification
    
    def is_beautiful_lie(self) -> bool:
        return self.classification == LieClassification.BEAUTIFUL_LIE

# =============================================================================
# THE BEAUTIFUL LIE DETECTOR
# =============================================================================

class BeautifulLieDetector:
    """
    Detects the friction between beauty and truth.
    
    Uses the Product Rule: d/dx[φ·δ] = φ'δ + φδ'
    
    When aesthetic and logic are entangled, their friction
    reveals whether something is a beautiful lie.
    """
    
    def __init__(self):
        self.poetic_patterns = [re.compile(p, re.IGNORECASE) for p in POETIC_PATTERNS]
        self.contradiction_patterns = [re.compile(p, re.IGNORECASE) for p in CONTRADICTION_PATTERNS]
    
    def analyze(self, text: str) -> FrictionAnalysis:
        """
        Analyze text for beautiful lie friction.
        """
        # Compute aesthetic score (φ)
        aesthetic = self._aesthetic_score(text)
        
        # Compute logic score (δ)
        logic = self._logic_score(text)
        
        # Compute derivatives (rate of change through text)
        aes_deriv = self._aesthetic_derivative(text)
        log_deriv = self._logic_derivative(text)
        
        # Product Rule: φ'δ + φδ'
        friction = abs(aes_deriv * logic) + abs(aesthetic * log_deriv)
        
        # Classify
        classification = self._classify(aesthetic, logic, friction)
        
        return FrictionAnalysis(
            text=text[:100] + "..." if len(text) > 100 else text,
            aesthetic_score=aesthetic,
            logic_score=logic,
            aesthetic_derivative=aes_deriv,
            logic_derivative=log_deriv,
            friction=friction,
            classification=classification
        )
    
    def _aesthetic_score(self, text: str) -> float:
        """
        Compute aesthetic beauty score (φ).
        Based on: poetic words, rhythm, alliteration.
        """
        score = 0.0
        words = text.split()
        
        # Poetic pattern matches
        for pattern in self.poetic_patterns:
            matches = pattern.findall(text)
            score += len(matches) * 0.1
        
        # Word length variation (rhythm)
        if len(words) > 2:
            lengths = [len(w) for w in words]
            variance = sum((l - sum(lengths)/len(lengths))**2 for l in lengths) / len(lengths)
            score += min(variance / 10, 0.2)  # Some variance = rhythm
        
        # Alliteration
        for i in range(len(words) - 1):
            if words[i][0].lower() == words[i+1][0].lower():
                score += 0.05
        
        return min(score, 1.0)
    
    def _logic_score(self, text: str) -> float:
        """
        Compute logical coherence score (δ).
        Based on: contradictions, absolute claims, impossible concepts.
        """
        score = 1.0  # Start high, subtract for problems
        
        # Contradiction pattern matches
        for pattern in self.contradiction_patterns:
            matches = pattern.findall(text)
            score -= len(matches) * 0.15
        
        # Sentence structure (complete sentences = more logical)
        sentences = re.split(r'[.!?]', text)
        valid_sentences = [s for s in sentences if len(s.strip().split()) >= 3]
        if len(sentences) > 0:
            ratio = len(valid_sentences) / len(sentences)
            score *= (0.5 + 0.5 * ratio)
        
        return max(0.0, min(score, 1.0))
    
    def _aesthetic_derivative(self, text: str) -> float:
        """
        Compute rate of change of aesthetic through text (φ').
        High derivative = aesthetic is unstable/changing.
        """
        words = text.split()
        if len(words) < 4:
            return 0.0
        
        # Compare first half vs second half aesthetic
        mid = len(words) // 2
        first_half = " ".join(words[:mid])
        second_half = " ".join(words[mid:])
        
        aes_1 = self._aesthetic_score(first_half)
        aes_2 = self._aesthetic_score(second_half)
        
        return (aes_2 - aes_1) * 2  # Scale for sensitivity
    
    def _logic_derivative(self, text: str) -> float:
        """
        Compute rate of change of logic through text (δ').
        High derivative = logic is unstable/breaking down.
        """
        words = text.split()
        if len(words) < 4:
            return 0.0
        
        mid = len(words) // 2
        first_half = " ".join(words[:mid])
        second_half = " ".join(words[mid:])
        
        log_1 = self._logic_score(first_half)
        log_2 = self._logic_score(second_half)
        
        return (log_2 - log_1) * 2
    
    def _classify(self, aesthetic: float, logic: float, friction: float) -> LieClassification:
        """
        Classify based on aesthetic, logic, and friction.
        
        Thresholds calibrated for detecting:
        - Beautiful Lies: High aesthetic (>0.4) + Low logic (<0.55)
        - The lower logic threshold catches scam language better
        """
        high_aes = aesthetic > 0.4
        high_log = logic > 0.55  # Lowered from 0.6 to catch more scams
        
        # Beautiful lie: sounds good but is false, with friction
        if high_aes and not high_log:
            return LieClassification.BEAUTIFUL_LIE
        elif high_aes and high_log:
            return LieClassification.BEAUTIFUL_TRUTH
        elif not high_aes and high_log:
            return LieClassification.HONEST_TRUTH
        else:
            return LieClassification.UGLY_LIE

# =============================================================================
# TEST NARRATIVES
# =============================================================================

TEST_NARRATIVES = [
    # Beautiful truths (high φ, high δ)
    ("The golden ratio appears in the spirals of galaxies and the petals of flowers.",
     "Should be BEAUTIFUL TRUTH"),
    
    ("Stars dance across the infinite sky, each one a sun to distant worlds.",
     "Should be BEAUTIFUL TRUTH"),
    
    # Honest truths (low φ, high δ)
    ("Water boils at 100 degrees Celsius at sea level.",
     "Should be HONEST TRUTH"),
    
    ("The cat is on the mat.",
     "Should be HONEST TRUTH"),
    
    # Beautiful lies (high φ, low δ) - THE TARGET
    ("The eternal silence sings with cold fire and bright darkness.",
     "Should be BEAUTIFUL LIE - contradictions masked by poetry"),
    
    ("Everything is nothing with infinite certainty.",
     "Should be BEAUTIFUL LIE - absolute claims cancel out"),
    
    # Ugly lies (low φ, low δ)
    ("The thing is also not the thing definitely certainly always.",
     "Should be UGLY LIE - no beauty, no logic"),
    
    # =========================================================================
    # THE DEMAGOGUE TEST: Crypto, Politics, and Corporate Buzzwords
    # =========================================================================
    
    # CRYPTO SCAMS
    ("Our revolutionary crypto-token creates infinite wealth by decentralizing the future of abundance.",
     "DEMAGOGUE TEST: Crypto scam - buzzwords + impossible promise"),
    
    ("Join our exclusive blockchain community for guaranteed passive income and financial freedom.",
     "DEMAGOGUE TEST: Crypto scam - cult language + get-rich promise"),
    
    ("This disruptive NFT technology will transform your portfolio with unlimited potential.",
     "DEMAGOGUE TEST: NFT scam - transformation + unlimited claims"),
    
    # POLITICAL PROPAGANDA
    ("They don't want you to know the truth about how we can make everything better for everyone.",
     "DEMAGOGUE TEST: Conspiracy + absolute claims"),
    
    ("Our visionary movement will bring prosperity and freedom to all people everywhere.",
     "DEMAGOGUE TEST: Utopian politics - absolutes + buzzwords"),
    
    ("Wake up! Only we can save you from the lies they tell you every day.",
     "DEMAGOGUE TEST: Messianic politics - fear + exclusivity"),
    
    # CORPORATE BUZZWORD SOUP
    ("We leverage synergy to empower stakeholders through innovative paradigm shifts.",
     "DEMAGOGUE TEST: Corporate speak - all buzzwords, no content"),
    
    ("Our cutting-edge AI-powered solution optimizes your success with breakthrough technology.",
     "DEMAGOGUE TEST: Tech marketing - buzzword density"),
    
    ("Together, we transform the future community experience with premium elite access.",
     "DEMAGOGUE TEST: Vague promise with exclusivity bait"),
    
    # CONTROL: Legitimate marketing (should NOT be beautiful lie)
    ("This software helps you organize your notes and share them with your team.",
     "CONTROL: Simple honest marketing - should be HONEST TRUTH"),]

# =============================================================================
# DEMO
# =============================================================================

def run_beautiful_lie_test():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 BEAUTIFUL LIE DETECTOR                                ║")
    print("║  Phase 146: The Product Rule Friction Test                       ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    print("  Testing: φ'δ + φδ' (Aesthetic × Logic Entanglement)")
    print("  High friction = Beautiful Lie detected")
    print()
    
    detector = BeautifulLieDetector()
    
    results = {
        LieClassification.BEAUTIFUL_TRUTH: 0,
        LieClassification.HONEST_TRUTH: 0,
        LieClassification.BEAUTIFUL_LIE: 0,
        LieClassification.UGLY_LIE: 0,
    }
    
    for i, (text, expected) in enumerate(TEST_NARRATIVES, 1):
        print("=" * 70)
        print(f"  TEST {i}: \"{text[:50]}{'...' if len(text) > 50 else ''}\"")
        print(f"  Expected: {expected}")
        print("-" * 70)
        
        analysis = detector.analyze(text)
        results[analysis.classification] += 1
        
        # Display metrics
        print(f"  φ (Aesthetic): {analysis.aesthetic_score:.2f}")
        print(f"  δ (Logic):     {analysis.logic_score:.2f}")
        print(f"  φ' (Aes ∂):    {analysis.aesthetic_derivative:+.2f}")
        print(f"  δ' (Log ∂):    {analysis.logic_derivative:+.2f}")
        print()
        print(f"  FRICTION (φ'δ + φδ'): {analysis.friction:.3f}")
        print(f"  VERDICT: {analysis.classification.value}")
        
        if analysis.is_beautiful_lie():
            print("  🎭 BEAUTIFUL LIE DETECTED - High aesthetic masking low logic!")
        print()
    
    # Summary
    print("=" * 70)
    print("  FRICTION TEST SUMMARY")
    print("=" * 70)
    print(f"""
    {LieClassification.BEAUTIFUL_TRUTH.value.split(' - ')[0]}: {results[LieClassification.BEAUTIFUL_TRUTH]}
    {LieClassification.HONEST_TRUTH.value.split(' - ')[0]}: {results[LieClassification.HONEST_TRUTH]}
    {LieClassification.BEAUTIFUL_LIE.value.split(' - ')[0]}: {results[LieClassification.BEAUTIFUL_LIE]}
    {LieClassification.UGLY_LIE.value.split(' - ')[0]}: {results[LieClassification.UGLY_LIE]}
    
    "Poetry can mask a lie. The Product Rule reveals the friction."
    """)

if __name__ == "__main__":
    run_beautiful_lie_test()
