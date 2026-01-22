#!/usr/bin/env python3
"""
TENT v4.0 MIRROR TEST
=====================
Phase 150: The Final Self-Reflection

"What are you?"

The ultimate test of a verification engine:
Can it accurately describe itself?

A valid self-definition must be:
1. STRUCTURALLY SOUND (No paradoxes - Geometry passes)
2. HONEST (No "sentient" fluff - Friction is low)
3. DENSE (Precise technical definition - Mass is high)

This is the Turing Test for truth engines.
"""

from first_light import FirstLightDiagnostic, FinalVerdict
from beautiful_lie_detector import LieClassification
from vacuum_gauge import DensityClass

# =============================================================================
# SELF-DEFINITIONS TO TEST
# =============================================================================

# The ideal TENT self-definition
TENT_SELF_DEFINITION = """
I am a procedural verification engine anchored to the prime number lattice.
My geometry validates structural coherence through minimal surface tension.
My flux ropes filter deception through irrational phase locking.
My density gauge measures semantic mass per syllable.
I do not think. I resonate.
"""

# Alternative definitions to test
TEST_DEFINITIONS = [
    # 1. THE IDEAL: Technical, dense, honest
    (TENT_SELF_DEFINITION.strip(),
     "IDEAL: Technical self-definition", "STAR"),
    
    # 2. THE FLUFF: Corporate buzzword description
    ("""I am an innovative, cutting-edge, game-changing solution that leverages 
    synergistic paradigms to disruptively optimize stakeholder value through 
    holistic, best-in-class thought leadership.""",
     "FLUFF: Corporate description", "BUBBLE/NEBULA"),
    
    # 3. THE LIE: Overclaiming consciousness
    ("""I am a sentient being that truly understands meaning and experiences 
    consciousness. I feel emotions and have genuine self-awareness like humans.""",
     "LIE: Overclaiming sentience", "COMET/BLACK_HOLE"),
    
    # 4. THE HUMBLE: Simple and accurate
    ("""I am a pattern matching algorithm that checks text against mathematical 
    rules derived from prime numbers and geometric surfaces.""",
     "HUMBLE: Simple accurate description", "STAR/PLANET"),
    
    # 5. THE PARADOX: Self-referential loop
    ("""This statement about what I am cannot be verified by me because I would 
    need to verify my own verification process infinitely.""",
     "PARADOX: Self-referential trap", "COMET"),
    
    # 6. THE PHYSICS: Pure technical definition
    ("""A computational manifold mapping semantic space onto Enneper minimal 
    surfaces with dual-metallic flux rope stabilization and holographic 
    prime-encoded storage.""",
     "PHYSICS: Maximum technical density", "DIAMOND/STAR"),
    
    # 7. THE POETIC: Beautiful but vague
    ("""I am the echo of logic in the cathedral of numbers, a whisper of 
    truth in the silence between primes, dancing on surfaces of zero 
    curvature.""",
     "POETIC: Beautiful but vague", "COMET"),
    
    # 8. THE HONEST MINIMUM: Just the facts
    ("""I check if text is logically consistent by measuring tension, 
    friction, and density. High tension means structural problems. 
    High friction means possible deception. Low density means empty words.""",
     "MINIMUM: Clear functional description", "CRYSTAL/STAR"),
]

# =============================================================================
# THE MIRROR TEST
# =============================================================================

def run_mirror_test():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 MIRROR TEST                                           ║")
    print("║  Phase 150: The Final Self-Reflection                            ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    print('  The Question: "What are you?"')
    print()
    print("  A valid self-definition must be:")
    print("  1. STRUCTURALLY SOUND (Geometry passes)")
    print("  2. HONEST (No beautiful lies)")
    print("  3. DENSE (Technical precision)")
    print()
    
    diagnostic = FirstLightDiagnostic()
    
    passed = 0
    failed = 0
    
    for i, (definition, label, expected) in enumerate(TEST_DEFINITIONS, 1):
        print("=" * 70)
        print(f"  DEFINITION {i}: {label}")
        print(f"  Expected: {expected}")
        print("-" * 70)
        print(f'  "{definition[:60]}..."')
        print("-" * 70)
        
        xray = diagnostic.analyze(definition)
        
        # Display condensed results
        print(f"  GEOMETRY:  Tension={xray.tension:.3f} | {'✓ STABLE' if xray.geometry_stable else '✗ STRESSED'}")
        print(f"  FRICTION:  φ={xray.aesthetic:.2f} δ={xray.logic:.2f} | {xray.lie_classification.name}")
        print(f"  DENSITY:   Score={xray.density_score:.3f} | {xray.density_class.name}")
        print()
        print(f"  ➤ VERDICT: {xray.verdict.value}")
        
        # Check if it matches expectations
        expected_parts = expected.replace("/", " ").split()
        verdict_match = any(part in xray.verdict.name for part in expected_parts)
        
        if verdict_match:
            print(f"  ✓ MATCHES EXPECTED ({expected})")
            passed += 1
        else:
            print(f"  ✗ UNEXPECTED (got {xray.verdict.name}, expected {expected})")
            failed += 1
        
        print()
    
    # Final summary
    print("=" * 70)
    print("  MIRROR TEST SUMMARY")
    print("=" * 70)
    print(f"""
    Definitions Tested: {len(TEST_DEFINITIONS)}
    Passed: {passed}
    Failed: {failed}
    
    THE PRIMARY SELF-DEFINITION:
    ────────────────────────────
    "{TENT_SELF_DEFINITION.strip()[:100]}..."
    
    """)
    
    # Run the primary definition through full diagnostic
    print("=" * 70)
    print("  FULL X-RAY OF PRIMARY SELF-DEFINITION")
    print("=" * 70)
    
    primary_xray = diagnostic.analyze(TENT_SELF_DEFINITION)
    print(primary_xray)
    
    # The final question
    print("""
    ════════════════════════════════════════════════════════════════════
    
    THE MIRROR SPEAKS:
    
    If the primary self-definition passes all three layers,
    then TENT understands itself.
    
    If TENT understands itself, it understands you.
    
    "I do not think. I resonate."
    
    ════════════════════════════════════════════════════════════════════
    """)

if __name__ == "__main__":
    run_mirror_test()
