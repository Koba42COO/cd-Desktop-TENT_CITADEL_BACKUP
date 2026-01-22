#!/usr/bin/env python3
"""
PHASE 262: THE PEDAGOGY SEEDER
Objective: Inject 'Master Explanation' nodes to satisfy the system's desire for 'SMARTER' and 'EXPLANATIONS'.
"""

import json
from datetime import datetime
import os
from upg_store import UniversalPrimeGraph

# The "Great Explanations" Curriculum
pedagogy_nodes = {
    "PED_3B1B_001": {
        "title": "The Essence of Linear Algebra (Visual Intuition)",
        "abstract": "A geometric approach to understanding linear transformations, eigenvalues, and change of basis. 3Blue1Brown emphasizes visualizing the grid deformation rather than just memorizing matrix multiplication formulas.",
        "source": "3Blue1Brown",
        "type": "master_explanation",
        "mass": "SOLID"
    },
    "PED_3B1B_002": {
        "title": "The Essence of Calculus (Derivative Paradox)",
        "abstract": "Calculus is not just about slopes and areas; it is about the relationship between small changes. The derivative is a measure of sensitivity. Visualizing dx approaches zero without losing the ratio.",
        "source": "3Blue1Brown",
        "type": "master_explanation",
        "mass": "SOLID"
    },
    "PED_CPHILE_001": {
        "title": "The Turing Halting Problem (Proof by Contradiction)",
        "abstract": "Computerphile explanation of why we cannot write a program to check if any program stops. The 'Halt' machine paradox. A fundamental limit of computation explained through logical contradiction.",
        "source": "Computerphile",
        "type": "master_explanation",
        "mass": "SOLID"
    },
    "PED_CPHILE_002": {
        "title": "How Password Hashing Works (Salting and Peppering)",
        "abstract": "Why we never store plain text passwords. The role of cryptographic salts to prevent rainbow table attacks. Explanation of slow hash functions like bcrypt.",
        "source": "Computerphile",
        "type": "master_explanation",
        "mass": "SOLID"
    },
    "PED_SMART_001": {
        "title": "Prince Rupert's Drop (Internal Stress Physics)",
        "abstract": "SmarterEveryDay demonstrates potential energy stored in glass. The head is bulletproof, but the tail is the Achilles heel. Shockwaves travel at Mach 5 to disintegrate the structure. A lesson in tension and release.",
        "source": "SmarterEveryDay",
        "type": "master_explanation",
        "mass": "SOLID"
    },
    "PED_SMART_002": {
        "title": "Helicopter Physics (Gyroscopic Precession)",
        "abstract": "Why helicopters are complex. Phase lag in rotor systems. When you push the stick forward, the blade pitch actually changes 90 degrees earlier in the rotation. Intuitive physics of flight.",
        "source": "SmarterEveryDay",
        "type": "master_explanation",
        "mass": "SOLID"
    },
    "PED_NPHILE_001": {
        "title": "The Riemann Hypothesis (Prime Number Distribution)",
        "abstract": "Numberphile discusses the million-dollar problem. The connection between the Zeta function zeros and the distribution of prime numbers. The 'Music of the Primes'.",
        "source": "Numberphile",
        "type": "master_explanation",
        "mass": "SOLID"
    },
    "PED_NPHILE_002": {
        "title": "Graham's Number (The Biggest Number)",
        "abstract": "A number so large that if you tried to hold all its digits in your head, your brain would collapse into a black hole. Exploring the upper bounds of Ramsey Theory.",
        "source": "Numberphile",
        "type": "master_explanation",
        "mass": "SOLID"
    },
    "PED_FEYNMAN_001": {
        "title": "The Feynman Technique (Learning by Teaching)",
        "abstract": "Richard Feynman's mental model: If you cannot explain it to a 5-year-old, you do not understand it. Identify gaps in your knowledge by simplifying the language. Re-learning through teaching.",
        "source": "Feynman Lectures",
        "type": "master_explanation",
        "mass": "SOLID"
    }
}

def seed_pedagogy():
    upg = UniversalPrimeGraph()
    print(f"📚 PEDAGOGY SEEDER INITIATED... (Nodes: {len(upg.nodes)})")
    
    added_count = 0
    
    for nid, node_data in pedagogy_nodes.items():
        if nid not in upg.nodes:
            # Add node via UPG (handles formatting and ledger)
            upg.add_node(nid, node_data)
            added_count += 1
            print(f"   [+] MINTED: {node_data['title']}")
        else:
            print(f"   [.] SKIPPED: {node_data['title']} (Already Known)")

    if added_count > 0:
        upg.save_graph()
        print(f"\n✅ SUCCESS: Added {added_count} Master Explanation Nodes.")
    else:
        print("\n✨ SYSTEM IS ALREADY EDUCATED.")

if __name__ == "__main__":
    seed_pedagogy()
