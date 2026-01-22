#!/usr/bin/env python3
import time
from enum import Enum
from dataclasses import dataclass

class AssetType(Enum):
    RECIPE = "RECIPE"   # Intellectual Capital (Appreciates)
    FACTORY = "FACTORY" # Physical Capital (Depreciates)

@dataclass
class Asset:
    name: str
    type: AssetType
    value: float
    age: int = 0
    
    def tick(self):
        self.age += 1
        if self.type == AssetType.RECIPE:
            # Recipes APPRECIATE as ecosystem grows (Lindt Effect)
            self.value *= 1.10 
        else:
            # Factories DEPRECIATE (Entropy/Rust)
            self.value *= 0.90

class Economy:
    def __init__(self):
        self.recipe = Asset("Cold Fusion Blueprint", AssetType.RECIPE, 1000.0)
        self.factory = Asset("Gigafactory Alpha", AssetType.FACTORY, 10000.0) # 10x more expensive initially
        self.wealth_architect = 0.0
        self.wealth_capitalist = 0.0
        
    def run_year(self, year):
        print(f"\n--- YEAR {year} ---")
        
        # 1. Update Asset Values
        self.recipe.tick()
        self.factory.tick()
        
        print(f"📄 RECIPE VALUE:  ${self.recipe.value:,.2f} (Appreciating)")
        print(f"🏭 FACTORY VALUE: ${self.factory.value:,.2f} (Depreciating)")
        
        # 2. Production (The Inversion)
        # Factory MUST run the Recipe to create value.
        # Production Value = Recipe Value * Scale Factor
        production_value = self.recipe.value * 50.0 
        
        # 3. Licensing (The Sovereign Rent)
        # Architect charges for the Logic.
        royalty = production_value * 0.20 # 20%
        margin = production_value * 0.05 # 5% Factory Margin (Commodity)
        
        self.wealth_architect += royalty
        self.wealth_capitalist += margin
        
        print(f"💰 TRANSACTION: Factory pays ${royalty:,.2f} to use Logic.")
        print(f"   - Architect Accum:  ${self.wealth_architect:,.2f}")
        print(f"   - Capitalist Accum: ${self.wealth_capitalist:,.2f}")

if __name__ == "__main__":
    print("=== THE DECOUPLING SIMULATION (Phase 180) ===")
    print("Initial State: Capitalist has 10x more wealth (Factory).")
    print("Logic: Recipe Appreciates (10%). Factory Depreciates (10%).")
    
    sim = Economy()
    
    for i in range(1, 11):
        sim.run_year(i)
        
    print("\n=== CONCLUSION ===")
    print("In the beginning, the Factory was the Asset.")
    print("In the end, the Recipe is the Sovereign.")
