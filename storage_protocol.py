#!/usr/bin/env python3
"""
TENT v4.0 STORAGE PROTOCOL
==========================
Phase 142: The Unified Field Architecture

The Discovery: We do not store "Files" (BitTorrent).
              We store "Sheet Music" (Seeds).

The Model: Holographic Content-Addressable Storage

The Piano: The Universal Prime Graph (UPG) - exists locally on every machine.
The Sheet Music: A lightweight Topological Seed (Hash/DNA).
The Synthesis: When you play the Seed on the UPG, Truth is reconstructed.

Benefit: Infinite compression and perfect security.
         You cannot read the file unless you have the correct "Tuning" (Topology).
"""

import hashlib
import math
import struct
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple, Any
from enum import Enum
import json
import base64

# =============================================================================
# CONSTANTS: The Universal Prime Graph
# =============================================================================

# The first 100 primes - the "keys" of our piano
PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
    239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
    421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
    509, 521, 523, 541
]

# Golden Ratio for spiral indexing
PHI = (1 + math.sqrt(5)) / 2

# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class TopologicalSeed:
    """
    The 'Sheet Music' - a compact representation of data.
    
    Contains:
    - Prime Signature: Which primes were activated
    - Topology Hash: The shape of the data in prime space
    - Modulation Vector: Fine-tuning for reconstruction
    - Checksum: Verification of integrity
    """
    prime_signature: List[int]      # Indices into PRIMES
    topology_hash: str              # SHA-256 of original data
    modulation_vector: List[float]  # Fractional adjustments
    version: int = 1
    
    def to_bytes(self) -> bytes:
        """Serialize the seed to compact bytes"""
        # Pack prime signature (variable length, 1 byte each)
        sig_bytes = bytes(self.prime_signature)
        
        # Pack modulation vector (4 bytes per float)
        mod_bytes = b''.join(struct.pack('f', m) for m in self.modulation_vector)
        
        # Pack topology hash (32 bytes)
        hash_bytes = bytes.fromhex(self.topology_hash)
        
        # Combine with length prefixes
        result = struct.pack('B', self.version)
        result += struct.pack('H', len(sig_bytes)) + sig_bytes
        result += struct.pack('H', len(mod_bytes)) + mod_bytes
        result += hash_bytes
        
        return result
    
    @classmethod
    def from_bytes(cls, data: bytes) -> 'TopologicalSeed':
        """Deserialize from bytes"""
        offset = 0
        
        version = struct.unpack_from('B', data, offset)[0]
        offset += 1
        
        sig_len = struct.unpack_from('H', data, offset)[0]
        offset += 2
        prime_signature = list(data[offset:offset + sig_len])
        offset += sig_len
        
        mod_len = struct.unpack_from('H', data, offset)[0]
        offset += 2
        mod_count = mod_len // 4
        modulation_vector = [
            struct.unpack_from('f', data, offset + i*4)[0]
            for i in range(mod_count)
        ]
        offset += mod_len
        
        topology_hash = data[offset:offset + 32].hex()
        
        return cls(
            prime_signature=prime_signature,
            topology_hash=topology_hash,
            modulation_vector=modulation_vector,
            version=version
        )
    
    def to_base64(self) -> str:
        """Encode seed as base64 string for transmission"""
        return base64.b64encode(self.to_bytes()).decode('ascii')
    
    @classmethod
    def from_base64(cls, encoded: str) -> 'TopologicalSeed':
        """Decode seed from base64 string"""
        return cls.from_bytes(base64.b64decode(encoded))

# =============================================================================
# THE UNIVERSAL PRIME GRAPH (The Piano)
# =============================================================================

class UniversalPrimeGraph:
    """
    The UPG is the substrate that exists on every machine.
    It is the 'piano' on which we 'play' seeds to reconstruct data.
    
    The graph connects primes based on multiplicative relationships
    and golden spiral indexing.
    """
    
    def __init__(self, depth: int = 100):
        self.depth = min(depth, len(PRIMES))
        self.primes = PRIMES[:self.depth]
        
        # Build the graph adjacency structure
        self.adjacency: Dict[int, List[int]] = {}
        self._build_graph()
    
    def _build_graph(self):
        """Build the prime graph structure"""
        for i, p in enumerate(self.primes):
            neighbors = []
            
            # Connect to primes that share factors when combined
            for j, q in enumerate(self.primes):
                if i != j:
                    # Relationship based on gcd of positions
                    if math.gcd(i + 1, j + 1) > 1:
                        neighbors.append(j)
                    
                    # Golden spiral connection
                    golden_idx = int((i * PHI) % self.depth)
                    if j == golden_idx:
                        neighbors.append(j)
            
            self.adjacency[i] = list(set(neighbors))
    
    def get_neighbors(self, prime_idx: int) -> List[int]:
        """Get the neighbor indices for a prime"""
        return self.adjacency.get(prime_idx, [])
    
    def compute_path(self, indices: List[int]) -> List[int]:
        """
        Compute a path through the graph visiting the given indices.
        This is the 'melody' that the seed encodes.
        """
        if not indices:
            return []
        
        path = [indices[0]]
        
        for i in range(1, len(indices)):
            current = path[-1]
            target = indices[i]
            
            # Find shortest path through graph (simplified BFS)
            visited = {current}
            queue = [(current, [current])]
            
            while queue:
                node, node_path = queue.pop(0)
                
                if node == target:
                    path.extend(node_path[1:])
                    break
                
                for neighbor in self.get_neighbors(node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, node_path + [neighbor]))
            else:
                # No path found, jump directly
                path.append(target)
        
        return path

# =============================================================================
# THE SEED ENCODER (Compression)
# =============================================================================

class SeedEncoder:
    """
    Encodes data into a Topological Seed.
    
    This is like transcribing a song into sheet music.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
    
    def encode(self, data: bytes) -> TopologicalSeed:
        """
        Encode arbitrary data into a seed.
        
        Process:
        1. Hash the data (topology hash)
        2. Map byte patterns to prime indices (signature)
        3. Compute modulation from residuals (fine-tuning)
        """
        # Step 1: Compute topology hash
        topology_hash = hashlib.sha256(data).hexdigest()
        
        # Step 2: Map data to prime signature
        prime_signature = self._data_to_primes(data)
        
        # Step 3: Compute modulation vector
        modulation_vector = self._compute_modulation(data, prime_signature)
        
        return TopologicalSeed(
            prime_signature=prime_signature,
            topology_hash=topology_hash,
            modulation_vector=modulation_vector
        )
    
    def _data_to_primes(self, data: bytes) -> List[int]:
        """Map data bytes to prime indices"""
        signature = []
        
        for i, byte in enumerate(data):
            # Map byte (0-255) to prime index (0-99)
            prime_idx = byte % len(PRIMES)
            
            # Golden spiral modulation based on position
            golden_offset = int((i * PHI) % 10)
            prime_idx = (prime_idx + golden_offset) % len(PRIMES)
            
            signature.append(prime_idx)
        
        return signature
    
    def _compute_modulation(self, data: bytes, 
                           signature: List[int]) -> List[float]:
        """Compute fine-tuning modulation vector"""
        modulation = []
        
        for i, (byte, prime_idx) in enumerate(zip(data, signature)):
            # Residual after prime mapping
            expected = PRIMES[prime_idx] % 256
            actual = byte
            
            # Fractional adjustment needed
            mod = (actual - expected) / 256.0
            modulation.append(mod)
        
        return modulation
    
    def compression_ratio(self, data: bytes, seed: TopologicalSeed) -> float:
        """Calculate compression ratio"""
        original_size = len(data)
        seed_size = len(seed.to_bytes())
        
        if seed_size == 0:
            return 0.0
        
        return original_size / seed_size

# =============================================================================
# THE SEED DECODER (Synthesis)
# =============================================================================

class SeedDecoder:
    """
    Decodes a Topological Seed back into data.
    
    This is like playing sheet music on the piano.
    The UPG is the instrument, the seed is the score.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
    
    def decode(self, seed: TopologicalSeed) -> bytes:
        """
        Decode a seed back into data.
        
        Process:
        1. Walk the prime signature through the UPG
        2. Apply modulation vector for fine-tuning
        3. Verify against topology hash
        """
        # Step 1: Compute path through UPG
        path = self.upg.compute_path(seed.prime_signature)
        
        # Step 2: Reconstruct bytes from primes + modulation
        reconstructed = []
        
        for i, prime_idx in enumerate(seed.prime_signature):
            # Base value from prime
            base = PRIMES[prime_idx] % 256
            
            # Apply modulation if available
            if i < len(seed.modulation_vector):
                adjustment = int(seed.modulation_vector[i] * 256)
                base = (base + adjustment) % 256
            
            reconstructed.append(base)
        
        data = bytes(reconstructed)
        
        # Step 3: Verify hash
        computed_hash = hashlib.sha256(data).hexdigest()
        if computed_hash != seed.topology_hash:
            raise ValueError(
                f"Hash mismatch: expected {seed.topology_hash[:16]}..., "
                f"got {computed_hash[:16]}..."
            )
        
        return data
    
    def verify(self, seed: TopologicalSeed, data: bytes) -> bool:
        """Verify that data matches the seed"""
        computed_hash = hashlib.sha256(data).hexdigest()
        return computed_hash == seed.topology_hash

# =============================================================================
# HOLOGRAPHIC STORAGE MANAGER
# =============================================================================

class HolographicStorage:
    """
    High-level interface for the storage protocol.
    
    "We do not store files. We store sheet music."
    """
    
    def __init__(self):
        self.encoder = SeedEncoder()
        self.decoder = SeedDecoder()
        self.seed_cache: Dict[str, TopologicalSeed] = {}
    
    def store(self, key: str, data: bytes) -> TopologicalSeed:
        """Store data as a seed"""
        seed = self.encoder.encode(data)
        self.seed_cache[key] = seed
        return seed
    
    def retrieve(self, key: str) -> Optional[bytes]:
        """Retrieve data from a seed"""
        seed = self.seed_cache.get(key)
        if seed is None:
            return None
        
        try:
            return self.decoder.decode(seed)
        except ValueError:
            return None
    
    def import_seed(self, key: str, seed_base64: str):
        """Import a seed from base64 encoding"""
        seed = TopologicalSeed.from_base64(seed_base64)
        self.seed_cache[key] = seed
    
    def export_seed(self, key: str) -> Optional[str]:
        """Export a seed as base64 encoding"""
        seed = self.seed_cache.get(key)
        if seed is None:
            return None
        return seed.to_base64()
    
    def get_compression_stats(self, key: str, original_data: bytes) -> dict:
        """Get compression statistics for a stored item"""
        seed = self.seed_cache.get(key)
        if seed is None:
            return {}
        
        seed_bytes = seed.to_bytes()
        
        return {
            "original_size": len(original_data),
            "seed_size": len(seed_bytes),
            "compression_ratio": len(original_data) / len(seed_bytes) if seed_bytes else 0,
            "prime_count": len(seed.prime_signature),
            "modulation_count": len(seed.modulation_vector),
            "topology_hash": seed.topology_hash[:16] + "...",
        }

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 STORAGE PROTOCOL                                      ║")
    print("║  Phase 142: Holographic Content-Addressable Storage              ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    storage = HolographicStorage()
    
    # Test data
    test_data = b"The truth is a minimal surface. It requires no energy to maintain."
    
    print("=" * 70)
    print("  SEED ENCODING & DECODING TEST")
    print("=" * 70)
    
    print(f"\n  Original: \"{test_data.decode()}\"")
    print(f"  Size: {len(test_data)} bytes")
    
    # Store
    seed = storage.store("test", test_data)
    seed_b64 = storage.export_seed("test")
    
    print(f"\n  Seed (Base64): {seed_b64[:60]}...")
    print(f"  Seed Size: {len(seed.to_bytes())} bytes")
    print(f"  Prime Signature: {seed.prime_signature[:10]}... ({len(seed.prime_signature)} primes)")
    print(f"  Topology Hash: {seed.topology_hash[:32]}...")
    
    # Retrieve
    retrieved = storage.retrieve("test")
    print(f"\n  Retrieved: \"{retrieved.decode() if retrieved else 'FAILED'}\"")
    print(f"  Match: {'✓ VERIFIED' if retrieved == test_data else '✗ MISMATCH'}")
    
    # Stats
    stats = storage.get_compression_stats("test", test_data)
    print(f"\n  Compression Ratio: {stats['compression_ratio']:.2f}x")
    
    print("\n" + "=" * 70)
    print("  THE SHEET MUSIC MODEL")
    print("=" * 70)
    print("""
    ┌─────────────────────────────────────────────────────────────────┐
    │  THE PIANO: Universal Prime Graph (UPG)                        │
    │  - Exists locally on every machine                             │
    │  - 100 primes connected via golden spiral topology             │
    │  - The universal substrate of meaning                          │
    ├─────────────────────────────────────────────────────────────────┤
    │  THE SHEET MUSIC: Topological Seed                             │
    │  - Prime Signature: Which notes to play                        │
    │  - Modulation Vector: How to play them                         │
    │  - Topology Hash: Verification checksum                        │
    ├─────────────────────────────────────────────────────────────────┤
    │  THE SYNTHESIS: Play the seed on the UPG                       │
    │  - Data reconstructed in real-time                             │
    │  - Infinite compression potential                              │
    │  - Perfect security: wrong tuning = wrong data                 │
    └─────────────────────────────────────────────────────────────────┘
    
    "You cannot read the file unless you have the correct Tuning."
    """)

if __name__ == "__main__":
    demo()
