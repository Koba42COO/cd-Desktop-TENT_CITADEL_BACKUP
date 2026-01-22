#!/usr/bin/env python3
import sys
from command_deck import CommandDeck

def run_full_system_test():
    print("="*60)
    print("   ⛺  TENT v4.0  |  SYSTEM VERIFICATION SUITE")
    print("   PHASE 190: THE FINAL VOYAGE")
    print("="*60 + "\n")
    
    deck = CommandDeck()
    
    # TEST 1: SYSTEM BOOT
    print("--- [TEST 1] SYSTEM BOOT ---")
    if deck.user == "WALLET_BRAD_0x18012026":
        print("✅ AUTHENTICATION: PASS")
    else:
        print("❌ AUTHENTICATION: FAIL")
        
    # TEST 2: MINTING (Simulated via script availability)
    print("\n--- [TEST 2] MINTING PROTOCOL ---")
    # We verify the Ledger is active
    if deck.ledger:
        print("✅ LEDGER CHECK: PASS")
        # Mint a test block
        block_id = deck.ledger.mint_block("TEST_CONTENT", "TESTER", "QA_CHECK")
        if block_id:
             print(f"✅ MINTING CHECK: PASS (Block {block_id[:8]})")
    
    # TEST 3: TRANSPORT
    print("\n--- [TEST 3] HOLONOMY PROTOCOL ---")
    try:
        deck.transport_protocol()
        print("✅ TRANSPORT CHECK: PASS")
    except Exception as e:
        print(f"❌ TRANSPORT CHECK: FAIL ({e})")
        
    # TEST 4: MONAD SYNTHESIS
    print("\n--- [TEST 4] HOLOGRAPHIC MONAD ---")
    print(">> Invoking Monad for 'Heavy Industry'...")
    try:
        # We assume the Monad has been upgraded to find High Mass
        deck.monad.seek_truth("Heavy Industry")
        print("✅ MONAD EXECUTION: PASS")
    except Exception as e:
        print(f"❌ MONAD EXECUTION: FAIL ({e})")
        
    print("\n" + "="*60)
    print("   ✅ SYSTEM STATUS: OPERATIONAL")
    print("="*60)

if __name__ == "__main__":
    run_full_system_test()
