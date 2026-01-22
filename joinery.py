#!/usr/bin/env python3
"""
TENT v4.0 JOINERY
=================
Phase 159: Logical Interlocking

The Sawmill stripped the bark. Now we test the joints.
A pile of good wood is not a house. A house is defined by how the wood connects.

Joint Types (Structural Ratings):
- Butt Joint (1):       Simple association ("Apples are red")
- Miter Joint (5):      Correlation ("Smoking causes cancer")
- Mortise & Tenon (10): Causation ("Force = Mass × Acceleration")
- Dovetail (100):       Definition/Identity ("π = C/d")

The difference between a Proverb and a Law:
- Proverb: "Hard work leads to success" (Correlation, exceptions exist)
- Law: "Friction generates heat" (Causation, no exceptions)
"""

import re
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum

from sawmill import Sawmill, WoodType

# =============================================================================
# JOINT TYPES
# =============================================================================

class JointType(Enum):
    """Classification of logical connections."""
    BUTT = "🔩 BUTT JOINT (1) - Simple association"
    MITER = "📐 MITER JOINT (5) - Correlation"
    MORTISE_TENON = "🔧 MORTISE & TENON (10) - Causation"
    DOVETAIL = "🔷 DOVETAIL (100) - Definition/Identity"
    BROKEN = "💔 BROKEN - No connection"

class StatementType(Enum):
    """Classification of statement nature."""
    OPINION = "💭 OPINION - Subjective, no joints"
    PROVERB = "📜 PROVERB - Correlation, exceptions exist"
    PRINCIPLE = "⚖️ PRINCIPLE - Strong causation"
    LAW = "🔬 LAW - Definition/Identity, no exceptions"

# =============================================================================
# CONNECTOR WORDS (The Glue)
# =============================================================================

# Identity connectors (Dovetail)
IDENTITY_CONNECTORS = {
    'equals', 'is', 'are', 'means', 'defined', 'definition',
    '=', '≡', '≜', 'identical', 'same', 'equivalent',
}

# Causation connectors (Mortise & Tenon)
CAUSATION_CONNECTORS = {
    'causes', 'generates', 'produces', 'creates', 'yields',
    'forces', 'requires', 'implies', 'results', 'leads',
    'determines', 'necessitates', 'entails', 'therefore',
    'thus', 'hence', 'because', 'since', 'given',
}

# Correlation connectors (Miter)
CORRELATION_CONNECTORS = {
    'correlates', 'associated', 'related', 'linked', 'connected',
    'tends', 'often', 'usually', 'sometimes', 'can',
    'may', 'might', 'could', 'suggests', 'indicates',
}

# Association connectors (Butt)
ASSOCIATION_CONNECTORS = {
    'and', 'with', 'or', 'like', 'similar', 'near', 'by',
}

# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class Joint:
    """A connection between two concepts."""
    word_a: str
    word_b: str
    connector: str
    joint_type: JointType
    strength: int

@dataclass
class JoineryReport:
    """Complete analysis of structural integrity."""
    text: str
    lumber_words: List[str]
    joints: List[Joint]
    total_strength: int
    average_strength: float
    weakest_joint: Optional[Joint]
    strongest_joint: Optional[Joint]
    statement_type: StatementType

# =============================================================================
# THE JOINERY
# =============================================================================

class Joinery:
    """
    The Structural Integrity Analyzer.
    
    Tests the connections between Heartwood words to determine
    if a sentence is a pile of wood or a load-bearing structure.
    """
    
    def __init__(self):
        self.sawmill = Sawmill()
    
    def analyze(self, text: str) -> JoineryReport:
        """
        Analyze the joinery of a sentence.
        
        1. Run through sawmill to get lumber
        2. Find connectors between lumber words
        3. Rate each joint
        4. Determine overall structural type
        """
        # Get lumber from sawmill
        sawmill_report = self.sawmill.mill(text)
        lumber_words = sawmill_report.lumber.split()
        
        # Find all joints
        joints = self._find_joints(text, lumber_words)
        
        # Calculate strengths
        total_strength = sum(j.strength for j in joints)
        avg_strength = total_strength / len(joints) if joints else 0
        
        weakest = min(joints, key=lambda j: j.strength) if joints else None
        strongest = max(joints, key=lambda j: j.strength) if joints else None
        
        # Classify statement type
        statement_type = self._classify_statement(joints, avg_strength)
        
        return JoineryReport(
            text=text,
            lumber_words=lumber_words,
            joints=joints,
            total_strength=total_strength,
            average_strength=avg_strength,
            weakest_joint=weakest,
            strongest_joint=strongest,
            statement_type=statement_type,
        )
    
    def _find_joints(self, text: str, lumber_words: List[str]) -> List[Joint]:
        """Find and classify all joints between lumber words."""
        joints = []
        text_lower = text.lower()
        
        if len(lumber_words) < 2:
            return joints
        
        # First, scan the ENTIRE text for key connector verbs
        detected_connectors = []
        
        for word in text_lower.split():
            w = word.strip('.,!?')
            if w in IDENTITY_CONNECTORS:
                detected_connectors.append(('identity', w))
            elif w in CAUSATION_CONNECTORS:
                detected_connectors.append(('causation', w))
            elif w in CORRELATION_CONNECTORS:
                detected_connectors.append(('correlation', w))
        
        # Determine the primary connector type for this sentence
        if detected_connectors:
            primary_type = detected_connectors[0][0]
            primary_connector = detected_connectors[0][1]
        else:
            primary_type = 'association'
            primary_connector = ''
        
        # Now create joints between heartwood words using the detected connector
        heartwood_words = [w.lower().strip('.,!?') for w in lumber_words 
                          if self.sawmill.calculate_albedo(w) <= 0.3]
        
        if len(heartwood_words) < 2:
            # Not enough heartwood, use all lumber
            heartwood_words = [w.lower().strip('.,!?') for w in lumber_words[:5]]
        
        # Create main structural joint based on sentence connector
        if len(heartwood_words) >= 2:
            joint_type, strength = self._type_to_joint(primary_type)
            
            joints.append(Joint(
                word_a=heartwood_words[0],
                word_b=heartwood_words[-1] if len(heartwood_words) > 1 else heartwood_words[0],
                connector=primary_connector,
                joint_type=joint_type,
                strength=strength,
            ))
        
        return joints
    
    def _type_to_joint(self, connector_type: str) -> Tuple[JointType, int]:
        """Convert connector type to joint type."""
        if connector_type == 'identity':
            return JointType.DOVETAIL, 100
        elif connector_type == 'causation':
            return JointType.MORTISE_TENON, 10
        elif connector_type == 'correlation':
            return JointType.MITER, 5
        else:
            return JointType.BUTT, 1
    
    def _classify_joint(self, connector: str, word_a: str, word_b: str) -> Tuple[JointType, int]:
        """Classify the joint type based on connector."""
        conn = connector.lower().strip('.,!?')
        
        # Check for identity (Dovetail)
        if conn in IDENTITY_CONNECTORS or '=' in connector:
            return JointType.DOVETAIL, 100
        
        # Check for causation (Mortise & Tenon)
        if conn in CAUSATION_CONNECTORS:
            return JointType.MORTISE_TENON, 10
        
        # Check for correlation (Miter)
        if conn in CORRELATION_CONNECTORS:
            return JointType.MITER, 5
        
        # Check for simple association (Butt)
        if conn in ASSOCIATION_CONNECTORS:
            return JointType.BUTT, 1
        
        # Check for mathematical operators
        if any(op in connector for op in ['×', '*', '+', '-', '/', '^']):
            return JointType.DOVETAIL, 100
        
        # Default: If words are adjacent or close, assume butt joint
        if connector == "" or len(connector.split()) <= 2:
            return JointType.BUTT, 1
        
        # Broken connection
        return JointType.BROKEN, 0
    
    def _classify_statement(self, joints: List[Joint], avg_strength: float) -> StatementType:
        """Classify the overall statement type."""
        if not joints:
            return StatementType.OPINION
        
        # Count joint types
        dovetails = sum(1 for j in joints if j.joint_type == JointType.DOVETAIL)
        mortise = sum(1 for j in joints if j.joint_type == JointType.MORTISE_TENON)
        miter = sum(1 for j in joints if j.joint_type == JointType.MITER)
        
        total_joints = len(joints)
        
        # Classification logic
        if dovetails > 0 and avg_strength >= 50:
            return StatementType.LAW  # Contains identity/definition
        elif mortise > 0 and avg_strength >= 8:
            return StatementType.PRINCIPLE  # Strong causation
        elif miter > 0 or avg_strength >= 3:
            return StatementType.PROVERB  # Correlation
        else:
            return StatementType.OPINION  # Weak associations
    
    def display_report(self, report: JoineryReport):
        """Display a visual joinery report."""
        print()
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║  TENT v4.0 JOINERY - Structural Integrity Analysis                   ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
        print()
        print(f"INPUT: \"{report.text[:65]}{'...' if len(report.text) > 65 else ''}\"")
        print()
        print(f"LUMBER (After Sawmill): {' — '.join(report.lumber_words[:8])}")
        print()
        
        if not report.joints:
            print("  ⚠️ NO JOINTS FOUND - Just a pile of wood.")
            return
        
        print("┌─────────────────────────────────────────────────────────────────────┐")
        print("│  JOINT ANALYSIS                                                     │")
        print("├─────────────────────────────────────────────────────────────────────┤")
        
        for j in report.joints:
            print(f"│  [{j.word_a}] —({j.connector})— [{j.word_b}]")
            print(f"│    └─ {j.joint_type.value}")
        
        print("└─────────────────────────────────────────────────────────────────────┘")
        print()
        print(f"STRUCTURAL METRICS:")
        print(f"  Total Strength:   {report.total_strength}")
        print(f"  Average Strength: {report.average_strength:.1f}")
        
        if report.weakest_joint:
            print(f"  Weakest Joint:    {report.weakest_joint.word_a} — {report.weakest_joint.word_b}")
        if report.strongest_joint:
            print(f"  Strongest Joint:  {report.strongest_joint.word_a} — {report.strongest_joint.word_b}")
        
        print()
        print(f"CLASSIFICATION: {report.statement_type.value}")
        print()

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 JOINERY DEMONSTRATION                                 ║")
    print("║  \"Proverb vs Law: Can TENT tell the difference?\"                 ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    joinery = Joinery()
    
    test_cases = [
        # Proverbs (Correlation - Miter Joints)
        ("Hard work leads to success.",
         "Proverb - Correlation"),
        
        # Laws (Causation - Mortise & Tenon)
        ("Friction generates heat.",
         "Law - Causation"),
        
        # Definition (Dovetail)
        ("Energy equals mass times the speed of light squared.",
         "Law - Definition (E=mc²)"),
        
        # Simple association (Butt Joint)
        ("Apples and oranges are fruits.",
         "Opinion - Association"),
        
        # Mathematical identity
        ("The circumference equals pi times diameter.",
         "Law - Identity (C=πd)"),
        
        # Weak correlation
        ("Money sometimes brings happiness.",
         "Proverb - Weak correlation"),
    ]
    
    for text, label in test_cases:
        print(f"\n{'='*72}")
        print(f"  STRESS TEST: {label}")
        print(f"{'='*72}")
        
        report = joinery.analyze(text)
        joinery.display_report(report)

if __name__ == "__main__":
    demo()
