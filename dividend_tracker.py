#!/usr/bin/env python3
from typing import Dict, List

class DividendEngine:
    """
    The Automated Royalties System.
    Tracks usage patterns and distributes Universal Wealth upstream.
    """
    
    ROYALTY_RATE = 0.05 # 5% of new value flows to the parent
    
    def __init__(self, ledger, assessor):
        self.ledger = ledger
        self.assessor = assessor
        self.wealth_map: Dict[str, float] = {} # Wallet -> Balance
        
    def process_upstream_dividends(self, new_block_id: str):
        """
        When a new block is born, it pays tribute to its parents.
        """
        if new_block_id not in self.ledger.chain:
            print(f"❌ Error: Block {new_block_id} not found in ledger.")
            return

        current_block = self.ledger.chain[new_block_id]
        parent_id = current_block.prev_hash
        
        # Calculate the Total Value of the new contribution
        mass = 100.0 # Simplified Mass
        new_value = self.assessor.calculate_reward(current_block.block_type, mass)
        
        print(f"💰 NEW VALUE CREATED: {new_value} Credits (Block: {new_block_id[:8]})")
        
        # Trace the Lineage (The "Pattern")
        depth = 0
        while parent_id != "GENESIS" and depth < 10: # Pay up to 10 generations back
            parent_block = self.ledger.chain.get(parent_id)
            if not parent_block:
                break
                
            # Calculate Dividend (Decays with distance)
            # The direct parent gets the most. The grandparent gets less.
            dividend = new_value * (self.ROYALTY_RATE / (depth + 1))
            
            # Pay the Ancestor
            ancestor_wallet = parent_block.author_wallet
            self._transfer(ancestor_wallet, dividend)
            
            print(f"   ⬆️  UPSTREAM FLOW: Paying {dividend:.2f} to {ancestor_wallet} (Gen -{depth+1})")
            
            # Move back one generation
            parent_id = parent_block.prev_hash
            depth += 1

    def _transfer(self, wallet: str, amount: float):
        current = self.wealth_map.get(wallet, 0.0)
        self.wealth_map[wallet] = current + amount

# ==========================================
# SIMULATION: THE "NEBRASKA GUY" SCENARIO
# ==========================================
if __name__ == "__main__":
    from kwyc_core import KwycLedger
    from value_assessor import ValueAssessor
    
    # Setup
    ledger = KwycLedger()
    assessor = ValueAssessor()
    engine = DividendEngine(ledger, assessor)
    
    print("--- 🌊 STARTING DIVIDEND FLOW SIMULATION ---\n")
    
    # 1. THE ANCESTOR (The Nebraska Guy)
    # He wrote a core library 5 years ago.
    print("1. MINTING CORE LIB (Nebraska Guy)...")
    root_id = ledger.mint_block("import core_lib", "WALLET_NEBRASKA", "NOVELTY")
    
    # 2. THE GIANT (The Tech Corp)
    # They build a massive app ON TOP of the core library.
    # They mint a block with MASSIVE Mass.
    print("\n2. MINTING SUPER APP (Tech Corp)...")
    app_id = ledger.mint_block("class SuperApp(core_lib): ...", "WALLET_CORP", "NOVELTY", parent_id=root_id)
    
    # 3. THE PAYOUT
    # The Corp creates value, but the Engine detects the PATTERN (Dependency).
    print("\n3. PROCESSING DIVIDENDS...")
    engine.process_upstream_dividends(app_id)
    
    print("\n--- 🏦 FINAL WALLET BALANCES ---")
    for wallet, balance in engine.wealth_map.items():
        print(f"{wallet}: {balance:.2f} Credits")
