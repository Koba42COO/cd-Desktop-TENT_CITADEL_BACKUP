import json
import os
from enum import Enum
from dataclasses import dataclass, asdict
from datetime import datetime

class NodeStatus(Enum):
    UNEXPLORED = "UNEXPLORED"
    ACTIVE = "ACTIVE"       # Safe, usable code
    DEPRECATED = "DEPRECATED" # Old way, but safe
    HAZARD = "HAZARD"       # DANGER: Do not use (The Skull Icon)

class NodeType(Enum):
    MEDIA = "MEDIA"   # Passive (Movie, Image, Text)
    CODE = "CODE"     # Active (Logic, Function, Recipe)
    HAZARD = "HAZARD" # Warning
    ROOT = "ROOT"     # Foundation

@dataclass
class PrimeNode:
    id: int
    type: NodeType
    content: str
    mass: float = 0.0
    velocity: float = 0.0
    position: float = 0.0

class UniversalPrimeGraph:
    DB_FILE = "universal_prime_graph.json"

    def __init__(self):
        self.nodes = {} # Map[ID, Data] (Only Solid)
        self.metadata = {} # Map[ID, Status]
        self.ledger = [] # List[Dict] (Full History: Pass + Fail)
        self.load_graph()
    
    def load_graph(self):
        """Loads the 'Truth' from the singular JSON file."""
        if os.path.exists(self.DB_FILE):
            try:
                with open(self.DB_FILE, 'r') as f:
                    data = json.load(f)
                    self.nodes = data.get("nodes", {})
                    self.metadata = data.get("metadata", {})
                    self.ledger = data.get("ledger", [])
                print(f">> [MEMORY] HIPPOCAMPUS LOADED: {len(self.nodes)} Nodes | {len(self.ledger)} Records.")
            except Exception as e:
                print(f"⚠️  MEMORY CORRUPTION: {e}")
        else:
            print(">> [MEMORY] NO PREVIOUS EXISTENCE FOUND. STARTING FRESH.")

    def save_graph(self):
        """Persists the 'Truth' to disk."""
        data = {
            "nodes": self.nodes,
            "metadata": {k: str(v) for k, v in self.metadata.items()},
            "ledger": self.ledger # Save the full history
        }
        try:
            with open(self.DB_FILE, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"❌ MEMORY FAILURE: {e}")

    def add_node(self, block_id: str, data: dict):
        if block_id in self.nodes:
            pass # Idempotent
        
        self.nodes[block_id] = data
        self.metadata[block_id] = str(NodeStatus.ACTIVE)
        print(f"Map Updated: {block_id}")
        self.save_graph()

    def record_interaction(self, arxiv_id, title, score, verdict):
        """Records a PASS or FAIL event into the immutable ledger."""
        entry = {
            "id": arxiv_id,
            "title": title,
            "score": float(score),
            "verdict": verdict,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.ledger.append(entry)
        # We don't save immediately on every rejection to save IO, rely on batch save
        # But for now, safety first:
        # self.save_graph() 

    def mark_hazard(self, block_id: str, reason: str):
        self.metadata[block_id] = str(NodeStatus.HAZARD)
        print(f"☠️  HAZARD MARKED: {block_id} | Reason: {reason}")
        self.save_graph()

    def get_safe_path(self, block_id: str):
        if self.metadata.get(block_id) == str(NodeStatus.HAZARD):
            return "⛔ ACCESS DENIED: This path is marked as hazardous."
        return self.nodes.get(block_id, None)
