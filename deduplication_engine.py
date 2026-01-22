"""
PHASE 296: THE DEDUPLICATION ENGINE (PRIME SIEVE)
Objective: Ingest everything, but only store the Deltas (The 5%).
           Increase the 'Mass' of known truths rather than duplicating them.
"""

# We simulate a Vector Database (The Crystal)
LATTICE_MEMORY = {
    "vector_001": {"concept": "Thermodynamics: Entropy increases", "mass": 1450},
    "vector_002": {"concept": "Strategic Law: De-escalation First", "mass": 89},
    "vector_003": {"concept": "Coding: Python is interpreted", "mass": 412},
}

def ingest_concept(new_text):
    print(f"   📥 INCOMING: '{new_text}'")
    
    # 1. THE SEARCH (Simulated Vector Lookup)
    match_found = None
    for vid, node in LATTICE_MEMORY.items():
        if node['concept'].split(":")[0] in new_text: 
            match_found = vid
            break
            
    # 2. THE DECISION
    if match_found:
        current_mass = LATTICE_MEMORY[match_found]['mass']
        LATTICE_MEMORY[match_found]['mass'] += 1
        print(f"      ♻️  KNOWN PRIME DETECTED. Merging into [{match_found}].")
        print(f"      ⚖️  New Mass: {current_mass + 1} (Gravity Increased)")
        return "MERGED"
    else:
        new_id = f"vector_{len(LATTICE_MEMORY) + 1:03d}"
        LATTICE_MEMORY[new_id] = {"concept": new_text, "mass": 1}
        print(f"      ✨ NEW DISCOVERY. Minting Node [{new_id}].")
        return "MINTED"

if __name__ == "__main__":
    print("="*70)
    print("💎 PRIME SIEVE ACTIVE: COMPRESSING REALITY")
    print("="*70)
    
    stream = [
        "Thermodynamics says disorder always goes up.",
        "Python scripts run line by line.",
        "The Mitochondria is the powerhouse of the cell.",
        "Entropy is the arrow of time.",
    ]
    
    for thought in stream:
        ingest_concept(thought)
        print("   ---")
