#!/usr/bin/env python3
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Any

# ==========================================
# LESSON 1: THE INGREDIENTS (Logic Nodes)
# ==========================================

class NodeType(Enum):
    MEDIA = "MEDIA" # Raw Input/Model
    CODE = "CODE"   # Logic/Process

@dataclass
class PrimeNode:
    id: int
    type: NodeType
    content: str
    mass: float

# 1. DEFINE THE INGREDIENTS
# The LLM is just a tool (like a Hammer).
node_llm = PrimeNode(id=500, type=NodeType.MEDIA, content="Model: GPT-4-Turbo", mass=0.0)

# The Contract is the raw material.
node_contract = PrimeNode(id=501, type=NodeType.MEDIA, content="Input: PDF_Lease_Agreement", mass=10.0)

print(f"📍 MAP CHECK: Loaded {node_llm.content} and {node_contract.content}")

# ==========================================
# LESSON 2: THE VECTOR (The Tuning)
# ==========================================

@dataclass
class LogicVector:
    action_id: int
    params: Dict[str, Any]

# 2. DEFINE THE TUNING (The "Secret Sauce")
# If you run this at Temp 1.0, it lies.
# If you run this at Temp 0.1 with this specific System Prompt, it tells the Truth.
process_analyze = LogicVector(
    action_id=node_llm.id,
    params={
        "temperature": 0.1,        # Cold = Truth (No hallucinations)
        "max_tokens": 2000,        # Enough for depth, not for rambling
        "system_prompt": "You are a TENT-Verified Legal Sentinel. Ignore fluff. Flag liabilities.",
        "output_format": "JSON_RISK_REPORT" # Structured Data Only
    }
)

# ==========================================
# LESSON 3: THE EXECUTION (The Logic Block)
# ==========================================

class LogicBlock:
    def __init__(self, name, author_wallet):
        self.name = name
        self.author = author_wallet
        self.steps = []

    def add_logic_step(self, inputs: List[PrimeNode], vector: LogicVector, expected_output: str):
        step = {
            "input_nodes": [i.content for i in inputs],
            "configuration": vector.params,
            "expected_result": expected_output
        }
        self.steps.append(step)
        print(f"🧠 LOGIC MAPPED: {inputs[0].content} -> [Temp: {vector.params['temperature']}] -> {expected_output}")

# 3. COMPILE THE AI RECIPE
my_ai_recipe = LogicBlock("Sentinel_Legal_Analyst_v1", "WALLET_BRAD")

my_ai_recipe.add_logic_step(
    inputs=[node_contract],
    vector=process_analyze,
    expected_output="Verified_Risk_Score"
)

# ==========================================
# LESSON 4: MINTING THE "PROMPT" AS CAPITAL
# ==========================================

try:
    from kwyc_core import KwycLedger
    ledger = KwycLedger()
    
    logic_content = str(my_ai_recipe.steps)
    
    block_id = ledger.mint_block(
        content=logic_content,
        wallet="WALLET_BRAD",
        block_type="RECIPE" # It's a Recipe, not just Code
    )
    
    print(f"\n💎 ASSET MINTED: {block_id}")
    print("   Status: Sovereign Logic")
    print("   Utility: Legal Risk Analysis Standard")

except ImportError:
    # Fallback simulation
    import hashlib
    import time
    print("\n[!] KwycLedger not found, simulating minting...")
    block_id = hashlib.sha256("LogicRecipe".encode()).hexdigest()[:16]
    print(f"\n💎 ASSET MINTED: {block_id}")
    print("   Status: Sovereign Logic")
    print("   Utility: Legal Risk Analysis Standard")
