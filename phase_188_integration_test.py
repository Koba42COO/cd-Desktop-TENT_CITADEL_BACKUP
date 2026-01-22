#!/usr/bin/env python3
from command_deck import CommandDeck

def test_integration():
    print("TESTING: Command Deck Integration of Holonomy Protocol")
    deck = CommandDeck()
    
    # Directly call the method to avoid input() blocking
    print(">> Invoking deck.transport_protocol()...")
    deck.transport_protocol()
    
    print("\n>> Integration Test Complete.")

if __name__ == "__main__":
    test_integration()
