#!/usr/bin/env python3
import time
import hashlib
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

# ==========================================
# 1. THE VISUAL PHYSICS (Color & Mass)
# ==========================================
class NodeType(Enum):
    MEDIA = "MEDIA"   # Passive (Movie, Image) -> BLUE
    CODE = "CODE"     # Active (Logic, Function) -> GOLD
    HAZARD = "HAZARD" # Warning (Bug, Risk) -> RED
    ROOT = "ROOT"     # Foundation (Genesis) -> WHITE

@dataclass
class VisualProperties:
    color: str
    shadow_depth: float  # 0.0 to 1.0 (Based on Mass)
    gradient_target: Optional[int] = None # The ID this flows into

# ==========================================
# 2. THE UNIFIED PRIME NODE (The Atom)
# ==========================================
class PrimeNode:
    def __init__(self, id: int, type: NodeType, content: str, mass: float):
        self.id = id
        self.type = type
        self.content = content
        self.mass = mass # Determines Shadow Size
        
    def get_visuals(self) -> VisualProperties:
        """
        Calculates the UI look based on Physics.
        """
        # 1. Determine Color
        color_map = {
            NodeType.MEDIA: "🔵 BLUE (Passive)",
            NodeType.CODE: "🟡 GOLD (Active)",
            NodeType.HAZARD: "🔴 RED (Danger)",
            NodeType.ROOT: "⚪ WHITE (Pure)",
        }
        
        # 2. Determine Shadow (Mass = Importance)
        # Heavy nodes (Kernels) cast deep shadows. Light nodes (Temp vars) cast none.
        shadow = min(1.0, self.mass / 100.0)
        
        return VisualProperties(
            color=color_map[self.type],
            shadow_depth=shadow
        )

# ==========================================
# 3. THE TIME BLOCK (The Chronology)
# ==========================================
@dataclass
class TimeBlock:
    """
    A slice of time. Contains the sequence of Primes visited.
    Instant Lookup: We know WHEN we were, so we know WHAT we did.
    """
    timestamp: float
    sequence_index: int
    nodes: List[int] = field(default_factory=list) # List of Prime IDs
    
    @property
    def block_hash(self) -> str:
        # The fingerprint of this specific moment in your history
        payload = f"{self.timestamp}|{self.nodes}"
        return hashlib.sha256(payload.encode()).hexdigest()[:12]

# ==========================================
# 4. THE WALLET MAP (The Renderer)
# ==========================================
class ChronicleWallet:
    def __init__(self, owner_id: str):
        self.owner = owner_id
        self.history: List[TimeBlock] = []
        self.current_block = TimeBlock(time.time(), 0)
        self.known_universe: Dict[int, PrimeNode] = {} # Local Cache of UPG
        
    def touch_node(self, node: PrimeNode):
        """
        The user interacts with a Prime (Movie OR Code).
        """
        # 1. Cache the definition (The Star)
        if node.id not in self.known_universe:
            self.known_universe[node.id] = node
            
        # 2. Add to current Time Block (The Path)
        self.current_block.nodes.append(node.id)
        print(f"👣 STEP: Visited Node {node.id} [{node.type.value}]")
        
    def seal_block(self):
        """
        Closes the current moment and saves it to the chronological chain.
        """
        if not self.current_block.nodes:
            return
            
        self.history.append(self.current_block)
        print(f"🔒 BLOCK SEALED: {self.current_block.block_hash} (Count: {len(self.current_block.nodes)} Primes)")
        
        # Start new block
        self.current_block = TimeBlock(time.time(), len(self.history))

    def render_map(self):
        """
        This is the UI. It doesn't show a file list.
        It shows the Gradient Flow of your history.
        """
        print(f"\n✨ RENDERING CHRONICLE MAP FOR {self.owner}...")
        print("---------------------------------------------------")
        
        for block in self.history:
            print(f"TIME BLOCK {block.block_hash} ({time.ctime(block.timestamp)})")
            
            # Render the Flow
            prev_node = None
            for node_id in block.nodes:
                node = self.known_universe[node_id]
                vis = node.get_visuals()
                
                # The Gradient Logic (Function)
                connection = "   "
                if prev_node:
                    # If we went from Media -> Code, show the mixing
                    connection = " ↓ "
                
                shadow_bar = "█" * int(vis.shadow_depth * 10)
                print(f"{connection} {vis.color} | Shadow: {shadow_bar} | ID: {node.id}")
                print(f"    Content: {node.content}")
                
                prev_node = node
            print("---------------------------------------------------")

# ==========================================
# 5. THE GENESIS SIMULATION
# ==========================================
if __name__ == "__main__":
    # Initialize Your Wallet
    my_wallet = ChronicleWallet("WALLET_BRAD")
    
    print("--- 🚀 STARTING CHRONICLE ENGINE (Phase 176) ---\n")
    
    # --- SCENE 1: THE INSPIRATION (Media) ---
    # You watch a movie clip (The Matrix Lobby Scene)
    movie_node = PrimeNode(19, NodeType.MEDIA, "Matrix_Lobby_Scene.mp4", mass=20.0)
    my_wallet.touch_node(movie_node)
    
    # --- SCENE 2: THE LOGIC (Code) ---
    # You are inspired by the physics, so you write a gravity function.
    # THIS IS INSEPARABLE. The code exists BECAUSE of the movie.
    code_node = PrimeNode(41, NodeType.CODE, "def gravity_engine():", mass=90.0)
    my_wallet.touch_node(code_node)
    
    # --- SCENE 3: THE DISCOVERY (Novelty) ---
    # You invent a new rendering technique. Massive Weight.
    novel_node = PrimeNode(103, NodeType.CODE, "Hyper_Shader_v1", mass=100.0)
    my_wallet.touch_node(novel_node)
    
    # Seal the block (End of work session)
    my_wallet.seal_block()
    
    # --- RENDER THE UI ---
    # Shows the Unified Path
    my_wallet.render_map()
