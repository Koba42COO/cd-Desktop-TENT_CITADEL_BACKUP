#!/usr/bin/env python3
"""
TENT v4.0 VALUE ASSESSOR
========================
The Economic Engine.
Calculates Universal Wealth Credits based on the physics of contribution.
"""

class ValueAssessor:
    """
    Calculates the Universal Wealth Credits based on Phase 174 Logic.
    """
    
    WEIGHTS = {
        "NOVELTY": 1.0,      # Discovery (The Bridge)
        "OPTIMIZATION": 0.5, # Efficiency (The Shortcut)
        "HAZARD": 0.1        # Warning (The Signpost)
    }
    
    def calculate_reward(self, block_type: str, mass_omega: float) -> float:
        """
        Reward = Mass * TypeWeight
        """
        weight = self.WEIGHTS.get(block_type, 0.0)
        
        # Base calculation
        raw_credits = mass_omega * weight
        
        return raw_credits

# ==========================================
# SYSTEM INTEGRATION TEST
# ==========================================
if __name__ == "__main__":
    from kwyc_core import KwycLedger
    from upg_store import UniversalPrimeGraph
    
    # Initialize
    ledger = KwycLedger()
    upg = UniversalPrimeGraph()
    assessor = ValueAssessor()
    
    print("--- 🚀 INITIALIZING TENT v4.0 KWYC PROTOCOL ---\n")
    
    # 1. USER A: Creates something NEW (Novelty)
    # ------------------------------------------------
    code_a = "def quantum_sort(list): return sorted(list)" # High Mass
    id_a = ledger.mint_block(code_a, "WALLET_ALICE", "NOVELTY")
    upg.add_node(id_a, {"code": code_a})
    
    reward_a = assessor.calculate_reward("NOVELTY", mass_omega=100)
    print(f"💰 WALLET_ALICE CREDITED: {reward_a} Credits (Type: NOVELTY)\n")
    
    # 2. USER B: Finds a shorter path (Optimization)
    # ------------------------------------------------
    code_b = "def q_sort(l): return sorted(l)" # Same logic, tighter syntax
    id_b = ledger.mint_block(code_b, "WALLET_BOB", "OPTIMIZATION", parent_id=id_a)
    upg.add_node(id_b, {"code": code_b})
    
    reward_b = assessor.calculate_reward("OPTIMIZATION", mass_omega=100)
    print(f"💰 WALLET_BOB CREDITED:   {reward_b} Credits (Type: OPTIMIZATION)\n")
    
    # 3. USER C: Finds a BUG in User A's code (Hazard)
    # ------------------------------------------------
    # User C doesn't delete ID_A. They mark it.
    print("⚠️  USER C DETECTED INSTABILITY IN NODE A...")
    ledger.mint_block("Warning: High Latency", "WALLET_CHARLIE", "HAZARD", parent_id=id_a)
    upg.mark_hazard(id_a, "O(n^2) Latency Spike Detected")
    
    reward_c = assessor.calculate_reward("HAZARD", mass_omega=100)
    print(f"💰 WALLET_CHARLIE CREDITED: {reward_c} Credits (Type: HAZARD)")
    
    print("\n--- 🗺️  FINAL MAP STATUS ---")
    try:
        print(f"Node A Status: {upg.metadata[id_a]}")
        print(f"Node B Status: {upg.metadata[id_b]}")
    except KeyError:
        print("Error accessing node metadata.")
