#!/usr/bin/env python3
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Any

# ==========================================
# LESSON 1: DEFINING THE INGREDIENTS (The Map)
# ==========================================

class NodeType(Enum):
    MEDIA = "MEDIA" # Matter/Ingredients
    CODE = "CODE"   # Action/Process

@dataclass
class PrimeNode:
    id: int
    type: NodeType
    content: str
    mass: float

# 1. DEFINE THE RAW MATERIALS (The "Map")
# These are Public Domain. You don't own "Iron".
node_iron   = PrimeNode(id=26, type=NodeType.MEDIA, content="Element: Iron (Fe)", mass=55.8)
node_carbon = PrimeNode(id=6,  type=NodeType.MEDIA, content="Element: Carbon (C)", mass=12.0)
node_heat   = PrimeNode(id=200, type=NodeType.CODE,  content="Action: Thermal Induction", mass=0.0)

print(f"📍 MAP CHECK: Found {node_iron.content} and {node_carbon.content}")

# ==========================================
# LESSON 2: DEFINING THE VECTOR (The Secret Sauce)
# ==========================================

@dataclass
class RecipeVector:
    action_id: int
    params: Dict[str, Any]

# 2. DEFINE THE RECIPE VECTOR (The "Knowledge")
# This is the difference between a rusty bucket and a jet engine.
# YOU OWN THESE NUMBERS.
process_smelt = RecipeVector(
    action_id=node_heat.id,
    params={
        "temp_c": 1450,       # The Critical Temp
        "duration_m": 45,     # The Critical Time
        "atmosphere": "Vacuum", # The Environment
        "carbon_ratio": 0.02  # 2% Carbon (High Carbon Steel)
    }
)

# ==========================================
# LESSON 3: THE CHAIN (The Algorithm)
# ==========================================

class RecipeBlock:
    def __init__(self, name, author_wallet):
        self.name = name
        self.author = author_wallet
        self.steps = []

    def add_step(self, ingredients: List[PrimeNode], vector: RecipeVector, result_name: str):
        step = {
            "inputs": [i.content for i in ingredients],
            "process": vector.params,
            "output": result_name
        }
        self.steps.append(step)
        print(f"🍳 STEP ADDED: {ingredients[0].content} + ... -> {result_name}")

# 3. COMPILE THE RECIPE
my_recipe = RecipeBlock("Aerospace Steel v1", "WALLET_BRAD")

my_recipe.add_step(
    ingredients=[node_iron, node_carbon],
    vector=process_smelt,
    result_name="Steel_Grade_Aerospace"
)

# ==========================================
# LESSON 4: THE MINT (Printing the Currency)
# ==========================================

# Mocking KwycLedger for this standalone lesson script if kwyc_core isn't imported or to keep it self-contained as per lesson structure.
# But user environment has kwyc_core, so let's try to use it if creating a real file, 
# or use the provided simulated print format if we want to stick strictly to the lesson text.
# The user code imports KwycLedger. I will attempt to import it.

try:
    from kwyc_core import KwycLedger
    ledger = KwycLedger()
    
    # We convert the complex recipe object into a string for the ledger
    recipe_content = str(my_recipe.steps) 
    
    block_id = ledger.mint_block(
        content=recipe_content,
        wallet="WALLET_BRAD",
        block_type="RECIPE"  # Special Asset Class
    )
    
    print(f"\n💎 ASSET MINTED: {block_id}")
    print("   Status: Sovereign Wisdom")
    print("   Dividend: ACTIVE (0.05 Credits per Use)")

except ImportError:
    # Fallback if kwyc_core is generic or missing in this context
    print("\n[!] KwycLedger not found, simulating minting...")
    import hashlib
    import time
    block_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
    print(f"\n💎 ASSET MINTED: {block_id}")
    print("   Status: Sovereign Wisdom")
    print("   Dividend: ACTIVE (0.05 Credits per Use)")
