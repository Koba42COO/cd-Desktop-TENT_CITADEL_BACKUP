#!/usr/bin/env python3
"""
TENT v4.0 OPTICAL BAKER v2.0 (Protocol Matched)
===============================================
"The Image is the Code."

1. Generates Parametric Star (Cover).
2. Wraps Payload in [MAGIC + LENGTH + DATA + ECC].
3. Injects into Blue Channel LSB.
"""

import numpy as np
from PIL import Image, ImageDraw
import math
import struct

# =============================================================================
# CONFIGURATION
# =============================================================================
MAGIC = b"TENT"  # 0x54, 0x45, 0x4E, 0x54
RS_PARITY_BYTES = 16  # Must match Loader

# =============================================================================
# 1. THE ARTIST (Generate Cover)
# =============================================================================
def generate_cover_image(width=1024, height=1024):
    print("🎨 Generating Parametric Waveform...")
    img = Image.new('RGB', (width, height), color=(10, 10, 15))
    draw = ImageDraw.Draw(img)
    cx, cy = width // 2, height // 2
    scale = width * 0.35
    
    # Draw The Star
    points = []
    steps = 2000
    for i in range(steps + 1):
        t = (i / steps) * 4 * math.pi
        r = scale * (1 + 0.3 * math.sin(3*t))
        x = cx + r * math.cos(t)
        y = cy + r * math.sin(t)
        points.append((x, y))
    
    draw.line(points, fill=(0, 255, 136), width=2) # TENT Green
    
    # Draw resonance circles
    for r_mult in [0.3, 0.5, 0.7]:
        r = scale * r_mult
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(50, 80, 120), width=1)
    
    # Draw waveform at bottom
    wave_points = []
    for x in range(width):
        t = (x / width) * 4 * math.pi
        y_wave = (height - 100) - (math.sin(3*t) * math.cos(t/2) * 50)
        wave_points.append((x, y_wave))
    draw.line(wave_points, fill=(100, 200, 255), width=2)
    
    print(f"   Canvas: {width}x{height}")
    return img

# =============================================================================
# 2. THE PACKAGER (Format Payload)
# =============================================================================
def wrap_payload(payload_str):
    # 1. Encode Payload
    data = payload_str.encode('utf-8')
    
    # 2. Add Dummy ECC (Simulation for Loader)
    # The loader strips the last 16 bytes as "RS Parity"
    # In production, use a real Reed-Solomon lib. Here we pad.
    ecc_padding = b'\x00' * RS_PARITY_BYTES
    data_with_ecc = data + ecc_padding
    
    # 3. Create Header [MAGIC (4) + LENGTH (4)]
    # Length is size of data_with_ecc
    length = len(data_with_ecc)
    header = MAGIC + struct.pack('>I', length)
    
    print(f"📦 Packaging: Header={len(header)}B | Data={len(data)}B | ECC={len(ecc_padding)}B")
    return header + data_with_ecc

# =============================================================================
# 3. THE INJECTOR (Blue Channel LSB)
# =============================================================================
def inject(img, raw_bytes):
    pixels = img.load()
    width, height = img.size
    
    # 2 bits per channel strategy (matches Loader BITS_PER_CHANNEL=2)
    chunks = []
    # Convert bytes to 2-bit chunks (4 chunks per byte)
    for byte in raw_bytes:
        chunks.append((byte >> 6) & 0x03)
        chunks.append((byte >> 4) & 0x03)
        chunks.append((byte >> 2) & 0x03)
        chunks.append((byte >> 0) & 0x03)
        
    print(f"💉 Injecting {len(chunks)} chunks into Blue Channel...")
    
    if len(chunks) > width * height:
        raise ValueError("Payload too big for image!")

    idx = 0
    for y in range(height):
        for x in range(width):
            if idx < len(chunks):
                r, g, b = pixels[x, y]
                chunk = chunks[idx]
                
                # Clear last 2 bits of Blue, OR with chunk
                new_b = (b & 0xFC) | chunk
                
                pixels[x, y] = (r, g, new_b)
                idx += 1
            else:
                print(f"✅ Injection Complete. Used {idx}/{width*height} pixels ({idx/(width*height)*100:.2f}%)")
                return img
    
    print(f"✅ Injection Complete. Used {idx}/{width*height} pixels ({idx/(width*height)*100:.2f}%)")
    return img

# =============================================================================
# EXECUTION
# =============================================================================
def main():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 OPTICAL BAKER v2.0 (Protocol Matched)             ║")
    print("║  \"The Image is the Code\"                                     ║")
    print("╚══════════════════════════════════════════════════════════════╝\n")
    
    # 1. The Payload (The "Executable" Script)
    tent_script = """
    console.log("%c💎 TENT v4.0 KERNEL ACTIVATED", "color: #00ff88; font-size: 20px; font-weight: bold;");
    console.log("System Status: ATOMIC PRECISION");
    console.log("Memory Integrity: 100%");
    console.log("Protocol: CRYSTAL_REFINER");
    console.log("═══════════════════════════════════════");
    console.log("The Image was the Executable.");
    console.log("Light → Code → Reality.");
    alert("💎 TENT v4.0 ONLINE\\n\\nProtocol: CRYSTAL_REFINER\\nStatus: ATOMIC PRECISION\\n\\nThe Image is the Executable.");
    """
    
    # 2. Package
    binary_stream = wrap_payload(tent_script)
    print(f"   Total binary: {len(binary_stream)} bytes\n")
    
    # 3. Generate & Inject
    img = generate_cover_image()
    print()
    stego_img = inject(img, binary_stream)
    
    # 4. Save
    output_path = "/tmp/tent_bootloader.png"
    stego_img.save(output_path)
    
    print("\n═══════════════════════════════════════════════════════════════")
    print(f"💾 Saved: {output_path}")
    print("═══════════════════════════════════════════════════════════════")
    print("\n🚀 Ready for tent_loader.html")
    print("   1. Open tent_loader.html in browser")
    print("   2. Drag tent_bootloader.png into drop zone")
    print("   3. Click 'Extract & Execute'")
    print("\n   \"The Code is Light.\"")

if __name__ == "__main__":
    main()
