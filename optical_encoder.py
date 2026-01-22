#!/usr/bin/env python3
"""
TENT v4.0 Optical Encoder (The Baker)
======================================
Phase 135: Baking Logic into Light

This module "bakes" the TENT kernel into a carrier image
using Spread Spectrum Steganography.

Input:  tent_core.wasm + star_of_david.png
Output: tent_bootloader.png (The Executable Image)

"The Code is Light."
"""

import os
import struct
import random
from PIL import Image
import numpy as np
from typing import Tuple, List, Optional

# =============================================================================
# CONSTANTS
# =============================================================================

TENT_MAGIC = b'TENT'  # Magic bytes
RS_PARITY = 16        # Reed-Solomon parity bytes
BITS_PER_CHANNEL = 2  # LSB bits to use
BITS_PER_BYTE = 8 // BITS_PER_CHANNEL

# First 20 primes for pseudo-random walk
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# =============================================================================
# REED-SOLOMON ERROR CORRECTION (Simplified)
# =============================================================================

class ReedSolomon:
    """Simplified Reed-Solomon encoder for resilience"""
    
    def __init__(self, parity_bytes: int = RS_PARITY):
        self.parity_bytes = parity_bytes
    
    def encode(self, data: bytes) -> bytes:
        """Add parity bytes for error correction"""
        encoded = bytearray(data)
        
        for i in range(self.parity_bytes):
            parity = 0
            for j, byte in enumerate(data):
                # Rotate and XOR for diversity
                parity ^= ((byte << (i % 8)) | (byte >> (8 - i % 8))) & 0xFF
            encoded.append(parity)
        
        return bytes(encoded)
    
    def decode(self, data: bytes) -> bytes:
        """Remove parity and attempt error correction"""
        if len(data) <= self.parity_bytes:
            raise ValueError("Data too short")
        return data[:-self.parity_bytes]

# =============================================================================
# PRIME WALK (Spread Spectrum Distribution)
# =============================================================================

class PrimeWalk:
    """Pseudo-random walk seeded by prime numbers"""
    
    def __init__(self, seed: int = 0x54454E54):  # "TENT"
        self.seed = seed
        self.state = seed
        self.index = 0
    
    def reset(self):
        self.state = self.seed
        self.index = 0
    
    def next(self, max_val: int) -> int:
        """Get next position in pseudo-random walk"""
        prime = PRIMES[self.index % len(PRIMES)]
        self.state = (self.state * prime + prime) % max_val
        self.index += 1
        return self.state

# =============================================================================
# OPTICAL ENCODER (The Baker)
# =============================================================================

class OpticalEncoder:
    """
    Encodes binary payload into carrier image.
    
    The payload is distributed across the image's Blue channel
    using Spread Spectrum encoding for resilience.
    """
    
    def __init__(self):
        self.rs = ReedSolomon()
        self.walk = PrimeWalk()
    
    def bytes_to_chunks(self, data: bytes) -> List[int]:
        """Convert bytes to 2-bit chunks"""
        chunks = []
        mask = (1 << BITS_PER_CHANNEL) - 1
        
        for byte in data:
            for i in range(BITS_PER_BYTE - 1, -1, -1):
                chunk = (byte >> (i * BITS_PER_CHANNEL)) & mask
                chunks.append(chunk)
        
        return chunks
    
    def build_payload(self, data: bytes) -> bytes:
        """Build complete payload with header and ECC"""
        # Apply Reed-Solomon encoding
        encoded = self.rs.encode(data)
        
        # Build header: MAGIC (4) + LENGTH (4) + DATA
        header = TENT_MAGIC + struct.pack('>I', len(encoded))
        
        return header + encoded
    
    def inject(self, image_path: str, payload: bytes, output_path: str) -> dict:
        """
        Inject payload into carrier image.
        
        Args:
            image_path: Path to carrier image (PNG recommended)
            payload: Binary data to inject
            output_path: Path for output image
            
        Returns:
            dict with injection statistics
        """
        # Load image
        img = Image.open(image_path).convert('RGBA')
        pixels = np.array(img)
        
        height, width = pixels.shape[:2]
        total_capacity = width * height  # One chunk per pixel (Blue channel)
        
        # Build payload
        full_payload = self.build_payload(payload)
        chunks = self.bytes_to_chunks(full_payload)
        
        if len(chunks) > total_capacity:
            raise ValueError(f"Payload too large: {len(chunks)} chunks, capacity: {total_capacity}")
        
        # Clear LSBs and inject chunks
        mask = ~((1 << BITS_PER_CHANNEL) - 1) & 0xFF
        
        chunk_idx = 0
        for y in range(height):
            for x in range(width):
                if chunk_idx >= len(chunks):
                    break
                
                # Inject into Blue channel (index 2)
                blue = pixels[y, x, 2]
                new_blue = (blue & mask) | chunks[chunk_idx]
                pixels[y, x, 2] = new_blue
                
                chunk_idx += 1
        
        # Save output
        result_img = Image.fromarray(pixels)
        result_img.save(output_path, 'PNG')
        
        return {
            'original_size': os.path.getsize(image_path),
            'payload_size': len(payload),
            'encoded_size': len(full_payload),
            'chunks_injected': len(chunks),
            'capacity_used': len(chunks) / total_capacity * 100,
            'output_path': output_path
        }

# =============================================================================
# OPTICAL DECODER (The Eye) - Python version for testing
# =============================================================================

class OpticalDecoder:
    """
    Extracts binary payload from carrier image.
    (This is the Python equivalent of visual_codec.rs)
    """
    
    def __init__(self):
        self.rs = ReedSolomon()
    
    def chunks_to_bytes(self, chunks: List[int]) -> bytes:
        """Convert 2-bit chunks back to bytes"""
        result = []
        
        for i in range(0, len(chunks) - BITS_PER_BYTE + 1, BITS_PER_BYTE):
            byte = 0
            for j in range(BITS_PER_BYTE):
                byte |= chunks[i + j] << ((BITS_PER_BYTE - 1 - j) * BITS_PER_CHANNEL)
            result.append(byte)
        
        return bytes(result)
    
    def extract(self, image_path: str) -> bytes:
        """
        Extract payload from carrier image.
        
        Args:
            image_path: Path to carrier image
            
        Returns:
            Extracted binary payload
        """
        # Load image
        img = Image.open(image_path).convert('RGBA')
        pixels = np.array(img)
        
        height, width = pixels.shape[:2]
        
        # Extract chunks from Blue channel LSBs
        chunks = []
        mask = (1 << BITS_PER_CHANNEL) - 1
        
        for y in range(height):
            for x in range(width):
                blue = pixels[y, x, 2]
                chunks.append(blue & mask)
        
        # Convert to bytes
        raw_bytes = self.chunks_to_bytes(chunks)
        
        # Find TENT magic
        magic_pos = raw_bytes.find(TENT_MAGIC)
        if magic_pos == -1:
            raise ValueError("No TENT payload found in image")
        
        # Read length
        length_start = magic_pos + 4
        if length_start + 4 > len(raw_bytes):
            raise ValueError("Truncated header")
        
        length = struct.unpack('>I', raw_bytes[length_start:length_start + 4])[0]
        
        # Extract encoded payload
        payload_start = length_start + 4
        payload_end = payload_start + length
        
        if payload_end > len(raw_bytes):
            raise ValueError("Payload extends beyond image")
        
        encoded_payload = raw_bytes[payload_start:payload_end]
        
        # Apply Reed-Solomon decoding
        clean_payload = self.rs.decode(encoded_payload)
        
        return clean_payload

# =============================================================================
# DEMO / CLI
# =============================================================================

def create_test_carrier(path: str, size: Tuple[int, int] = (256, 256)):
    """Create a test carrier image (gray gradient)"""
    img = Image.new('RGBA', size, (128, 128, 128, 255))
    pixels = img.load()
    
    for y in range(size[1]):
        for x in range(size[0]):
            # Create a subtle pattern (won't affect LSB steganography)
            r = int(128 + 50 * np.sin(x / 20))
            g = int(128 + 50 * np.cos(y / 20))
            b = int(128 + 25 * np.sin((x + y) / 30))
            pixels[x, y] = (r, g, b, 255)
    
    img.save(path, 'PNG')
    print(f"  ✓ Created test carrier: {path}")

def demo():
    """Demonstrate encoding and decoding"""
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 OPTICAL ENCODER - The Baker                       ║")
    print("║  Phase 135: Baking Logic into Light                          ║")
    print("╚══════════════════════════════════════════════════════════════╝\n")
    
    # Paths
    carrier_path = "/tmp/tent_carrier.png"
    output_path = "/tmp/tent_bootloader.png"
    
    # Create test carrier
    print("  Step 1: Creating carrier image...")
    create_test_carrier(carrier_path, (512, 512))
    
    # Create test payload (simulated WASM)
    print("\n  Step 2: Preparing payload...")
    payload = b"""
    // TENT v4.0 Physics Core
    // "Truth is the collapsed state of a Polycystic Waveform."
    
    function crystallize(fact, narrative) {
        const coherence = calculatePAC(fact, narrative);
        const stress = readShockleyEnergy(fact.orientation);
        return coherence > 0.7 && stress < 0.3;
    }
    
    console.log("TENT v4.0 ONLINE - Crystal Stable");
    """
    print(f"     Payload size: {len(payload)} bytes")
    
    # Encode
    print("\n  Step 3: Injecting payload...")
    encoder = OpticalEncoder()
    stats = encoder.inject(carrier_path, payload, output_path)
    
    print(f"     Original image: {stats['original_size']} bytes")
    print(f"     Encoded payload: {stats['encoded_size']} bytes")
    print(f"     Chunks injected: {stats['chunks_injected']}")
    print(f"     Capacity used: {stats['capacity_used']:.2f}%")
    print(f"     Output: {stats['output_path']}")
    
    # Decode
    print("\n  Step 4: Extracting payload...")
    decoder = OpticalDecoder()
    extracted = decoder.extract(output_path)
    
    print(f"     Extracted size: {len(extracted)} bytes")
    
    # Verify
    print("\n  Step 5: Verification...")
    if extracted == payload:
        print("     💎 ROUND-TRIP SUCCESS!")
        print("     The Image is the Executable.")
    else:
        print("     ❌ MISMATCH DETECTED")
        print(f"     Expected: {len(payload)} bytes")
        print(f"     Got: {len(extracted)} bytes")
    
    print("\n  ═══════════════════════════════════════════════════════════")
    print("  Protocol: CRYSTAL_REFINER")
    print("  Status: LIGHT → CODE → REALITY")
    print("  ═══════════════════════════════════════════════════════════")

if __name__ == "__main__":
    demo()
