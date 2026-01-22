#!/usr/bin/env python3
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum
import hashlib

# ==========================================
# 1. THE STATIC MAP (The Periodic Table)
# ==========================================
# These are Public Domain. Connection to "Iron" is free.
class ElementType(Enum):
    MATTER = "MATTER" # Ingredients
    ENERGY = "ENERGY" # Processes

@dataclass
class PrimeNode:
    id: int
    name: str
    type: ElementType
    
    def __repr__(self):
        return f"[{self.id}: {self.name}]"

# The Global Public Map (The Pantry)
UPG_MAP = {
    26: PrimeNode(26, "Iron", ElementType.MATTER),
    6:  PrimeNode(6,  "Carbon", ElementType.MATTER),
    74: PrimeNode(74, "Tungsten", ElementType.MATTER),
    200: PrimeNode(200, "Heat", ElementType.ENERGY),
    300: PrimeNode(300, "Pressure", ElementType.ENERGY)
}

# ==========================================
# 2. THE DYNAMIC RECIPE (The Sovereign Asset)
# ==========================================
# This is the Instruction Set. The Value is in the PARAMETERS.

@dataclass
class RecipeStep:
    input_prime: int      # The Ingredient (Iron)
    action_prime: int     # The Process (Heat)
    
    # THE SECRET SAUCE (The "How")
    # This is what you license.
    parameters: dict 
    
    output_name: str      # What this step creates (Intermediate State)

@dataclass
class Recipe:
    name: str
    author_wallet: str
    steps: List[RecipeStep] = field(default_factory=list)
    
    @property
    def fingerprint(self) -> str:
        # The Hash proves you knew the EXACT parameters.
        payload = f"{self.name}|{self.author_wallet}"
        for step in self.steps:
            payload += f"|{step.input_prime}->{step.action_prime}:{step.parameters}"
        return hashlib.sha256(payload.encode()).hexdigest()[:16]

# ==========================================
# 3. THE FACTORY (The Renderer)
# ==========================================
class IndustrialForge:
    """
    The Factory is dumb. It just executes parameters.
    """
    def execute(self, recipe: Recipe):
        print(f"\n🏭 FACTORY ONLINE. Loading Recipe: {recipe.name} (Hash: {recipe.fingerprint})")
        print(f"   Authorized by: {recipe.author_wallet}")
        print("   ------------------------------------------------")
        
        for i, step in enumerate(recipe.steps):
            ingredient = UPG_MAP[step.input_prime]
            process = UPG_MAP[step.action_prime]
            
            print(f"   STEP {i+1}: Applying {process.name} to {ingredient.name}...")
            print(f"      -> CONFIGURING: {step.parameters}")
            
            # SIMULATION: Quality Check
            # In TENT, the physics engine checks if these params work.
            if step.parameters.get("temperature") == "1450C":
                print(f"      ✅ SUCCESS: Transformation valid. Created {step.output_name}.")
            elif step.parameters.get("temperature") == "1400C":
                print(f"      ❌ FAILURE: {ingredient.name} did not fuse correctly. Product Cracked.")
            else:
                print(f"      ⚠️  WARNING: Unknown parameters. Outcome unstable.")
        
        print("   ------------------------------------------------")
        print("   🏁 PROCESS COMPLETE.\n")

# ==========================================
# SIMULATION
# ==========================================
if __name__ == "__main__":
    print("--- ⚔️  THE RECIPE PROTOCOL (Phase 181) ---")
    
    # 1. THE ARCHITECT DEFINES THE "HOW"
    # This is the Sovereign Asset.
    damascus_steel = Recipe("Damascus Steel Pattern #402", "WALLET_ARCHITECT")
    
    # Step 1: Fuse Iron and Carbon with Heat (Precise Temp)
    step1 = RecipeStep(
        input_prime=26, # Iron
        action_prime=200, # Heat
        parameters={"temperature": "1450C", "duration": "4h"},
        output_name="High-Carbon Matrix"
    )
    damascus_steel.steps.append(step1)
    
    # Step 2: Forge with Pressure
    step2 = RecipeStep(
        input_prime=74, # Tungsten (Additive) - Just illustrating structure
        action_prime=300, # Pressure
        parameters={"pressure": "500atm", "method": "Fold 10x"},
        output_name="Folded Billet"
    )
    damascus_steel.steps.append(step2)
    
    # 2. THE FACTORY EXECUTES (Success)
    forge = IndustrialForge()
    forge.execute(damascus_steel)
    
    # 3. THE COUNTERFEIT (Failure)
    # Competitor tries to save energy (1400C instead of 1450C).
    print("--- 🕵️  DETECTING COUNTERFEIT ATTEMPT ---")
    cheap_knockoff = Recipe("Cheap Steel", "WALLET_COMPETITOR")
    cheap_step = RecipeStep(
        input_prime=26,
        action_prime=200,
        parameters={"temperature": "1400C", "duration": "3h"}, # WRONG TEMP
        output_name="Weak Steel"
    )
    cheap_knockoff.steps.append(cheap_step)
    
    forge.execute(cheap_knockoff)
