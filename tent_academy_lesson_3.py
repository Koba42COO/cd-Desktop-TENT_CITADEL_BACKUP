#!/usr/bin/env python3
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Any

# ==========================================
# LESSON 1: THE LIVE STREAM (The Nervous System)
# ==========================================

class NodeType(Enum):
    MEDIA = "MEDIA" # Stream/Sensor
    CODE = "CODE"   # Actuator/Logic

@dataclass
class PrimeNode:
    id: int
    type: NodeType
    content: str
    mass: float

# 1. DEFINE THE LIVE INGREDIENTS
# This node doesn't hold data; it holds a POINTER to a live stream.
node_sensor_temp = PrimeNode(id=800, type=NodeType.MEDIA, content="Stream: Thermocouple_A1", mass=0.0)
node_sensor_pres = PrimeNode(id=801, type=NodeType.MEDIA, content="Stream: Barometer_B2", mass=0.0)

# The Actuator is the muscle we control.
node_valve_gas = PrimeNode(id=850, type=NodeType.CODE, content="Actuator: Gas_Flow_Controller", mass=50.0)

print(f"📍 MAP CHECK: Connected to Sensors {node_sensor_temp.content} & {node_sensor_pres.content}")

# ==========================================
# LESSON 2: THE FEEDBACK LOOP (The Reflex)
# ==========================================

@dataclass
class ReflexVector:
    trigger_condition: str   # When to act
    response_action: Dict[str, Any]    # What to do

# 2. DEFINE THE REFLEX (The "Brain")
# This is the logic that saves the factory from exploding.
process_stabilize = ReflexVector(
    trigger_condition="Pressure < 4.8 atm AND Temp_Trend == 'RISING'",
    response_action={
        "target": "Gas_Flow_Controller",
        "adjustment": "-2.5%",      # Precise reduction
        "latency_max": "50ms"       # Must happen instantly
    }
)

# ==========================================
# LESSON 3: THE CYBER-PHYSICAL BLOCK
# ==========================================

class CyberPhysicalBlock:
    def __init__(self, name, author_wallet):
        self.name = name
        self.author = author_wallet
        self.loops = []

    def add_feedback_loop(self, sensors: List[PrimeNode], vector: ReflexVector, actuator: PrimeNode):
        loop = {
            "monitors": [s.content for s in sensors],
            "logic": f"IF {vector.trigger_condition} THEN {vector.response_action}",
            "control": actuator.content
        }
        self.loops.append(loop)
        print(f"⚡ REFLEX MAPPED: If {vector.trigger_condition} -> Adjust {actuator.content}")

# 3. COMPILE THE GUARDIAN
my_guardian = CyberPhysicalBlock("Smelter_Stabilizer_AI_v1", "WALLET_BRAD")

my_guardian.add_feedback_loop(
    sensors=[node_sensor_temp, node_sensor_pres],
    vector=process_stabilize,
    actuator=node_valve_gas
)

# ==========================================
# LESSON 4: MINTING THE "GHOST IN THE MACHINE"
# ==========================================

try:
    from kwyc_core import KwycLedger
    ledger = KwycLedger()
    
    guardian_content = str(my_guardian.loops)
    
    block_id = ledger.mint_block(
        content=guardian_content,
        wallet="WALLET_BRAD",
        block_type="RECIPE"
    )
    
    print(f"\n💎 ASSET MINTED: {block_id}")
    print("   Status: Sovereign Reflex")
    print("   Utility: Industrial Safety Protocol")

except ImportError:
    # Fallback simulation
    import hashlib
    print("\n[!] KwycLedger not found, simulating minting...")
    block_id = hashlib.sha256("ReflexRecipe".encode()).hexdigest()[:16]
    print(f"\n💎 ASSET MINTED: {block_id}")
    print("   Status: Sovereign Reflex")
    print("   Utility: Industrial Safety Protocol")
