#!/usr/bin/env python3
import hashlib
import json
import time
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict

# CRYPTO PRIMITIVES (Simulated for this build)
def sha256(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

@dataclass
class CodeBlock:
    """
    A single atom of code in the UPG.
    It is Content-Addressable (ID = Hash).
    """
    content: str            # The actual code or logic path
    author_wallet: str      # The Creator's Public Key
    prev_hash: str          # The 'Parent' node (for chains)
    timestamp: float
    block_type: str         # 'NOVELTY', 'OPTIMIZATION', 'HAZARD'
    signature: str          # Cryptographic signature of the Author
    
    @property
    def fingerprint(self) -> str:
        # The ID is derived from the content + context.
        payload = f"{self.content}|{self.author_wallet}|{self.prev_hash}|{self.block_type}"
        return sha256(payload)

class KwycLedger:
    def __init__(self):
        self.chain: Dict[str, CodeBlock] = {} # The Immutable History
    
    def mint_block(self, content: str, wallet: str, block_type: str, parent_id: str = "GENESIS") -> str:
        """
        Creates a new immutable record.
        """
        block = CodeBlock(
            content=content,
            author_wallet=wallet,
            prev_hash=parent_id,
            timestamp=time.time(),
            block_type=block_type,
            signature=f"SIG_{wallet[:6]}_{int(time.time())}" # Simulation
        )
        
        block_id = block.fingerprint
        self.chain[block_id] = block
        
        print(f"🔗 MINTED BLOCK: {block_id[:8]}... | Type: {block_type}")
        return block_id

    def verify_provenance(self, block_id: str) -> bool:
        """
        Walks the chain backwards to verify integrity.
        """
        current_id = block_id
        while current_id != "GENESIS":
            if current_id not in self.chain:
                return False
            block = self.chain[current_id]
            # Verify the math holds
            if block.fingerprint != current_id:
                return False
            current_id = block.prev_hash
        return True
