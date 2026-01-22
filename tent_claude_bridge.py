#!/usr/bin/env python3
"""
TENT v4.1: THE CLAUDE API BRIDGE
================================
Phase 241: The Translation Layer

Objective:
Provide a REST API that translates natural language queries
into deterministic Prime Lattice coordinates.

Input:  English sentence ("What is truth?")
Output: Mathematical coordinates (Base-21, Prime, FHT Signature)

This allows High-Level LLMs to interface with the Low-Level Physics Engine.
"""

from flask import Flask, request, jsonify
import hashlib
import time
import json
import os

# --- PRIME CONSTANTS ---
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
PHI = 1.618033988749895

app = Flask(__name__)

# --- CORE FUNCTIONS ---

def hash_to_base21(text: str):
    """Converts text to a sequence of Base-21 digits via SHA256 hash."""
    h = hashlib.sha256(text.encode()).hexdigest()
    digits = []
    for i in range(0, 16, 2):  # Take 8 pairs of hex digits
        val = int(h[i:i+2], 16)
        digits.append(val % 21)  # Map to Base-21
    return digits

def base21_to_primes(base21_digits: list):
    """Maps Base-21 digits to their corresponding Prime coordinates."""
    return [PRIMES[d % len(PRIMES)] for d in base21_digits]

def compute_fht_signature(prime_coords: list):
    """Computes a Fractal Harmonic Topology signature (resonance score)."""
    if not prime_coords:
        return 0.0
    # Simulate harmonic resonance based on prime ratios
    resonance = 0.0
    for i in range(len(prime_coords) - 1):
        ratio = prime_coords[i] / prime_coords[i+1] if prime_coords[i+1] else 1.0
        resonance += abs(ratio - PHI) / PHI  # Deviation from Golden Ratio
    raw_score = 1.0 - (resonance / len(prime_coords))
    return round(max(0.0, min(1.0, raw_score)), 4)

def compute_lattice_position(prime_coords: list):
    """Computes a unique lattice position hash from prime coordinates."""
    return sum(prime_coords) % 1000  # Simple modular hash

def load_upg_stats():
    """Loads stats from the Universal Prime Graph."""
    upg_path = "universal_prime_graph.json"
    if os.path.exists(upg_path):
        try:
            with open(upg_path, 'r') as f:
                data = json.load(f)
                return {
                    "nodes": len(data.get("nodes", {})),
                    "ledger": len(data.get("ledger", []))
                }
        except:
            pass
    return {"nodes": 0, "ledger": 0}

# --- API ENDPOINTS ---

@app.route('/query', methods=['POST'])
def query():
    """Main endpoint: Translates natural language to Prime Coordinates."""
    start = time.time()
    
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"success": False, "error": "Missing 'query' field."}), 400
    
    text = data['query']
    
    # 1. Hash to Base-21
    base21 = hash_to_base21(text)
    
    # 2. Map to Primes
    prime_coords = base21_to_primes(base21)
    
    # 3. Compute Resonance
    fht_sig = compute_fht_signature(prime_coords)
    
    # 4. Compute Lattice Position
    lattice_pos = compute_lattice_position(prime_coords)
    
    latency = round((time.time() - start) * 1000, 2)
    
    return jsonify({
        "success": True,
        "result": {
            "query": text,
            "coordinates": {
                "base21": base21,
                "prime_coords": prime_coords,
                "fht_signature": fht_sig,
                "lattice_position": lattice_pos
            },
            "solution": {
                "type": "coordinate_mapping",
                "confidence": fht_sig,
                "resonance": fht_sig,
                "operations": 1,
                "cached": False
            },
            "source": "TENT_PHYSICS_ENGINE",
            "latency_ms": latency
        }
    })

@app.route('/status', methods=['GET'])
def status():
    """Returns Bridge health and UPG statistics."""
    upg = load_upg_stats()
    return jsonify({
        "bridge": "ONLINE",
        "version": "4.1.241",
        "upg_nodes": upg['nodes'],
        "upg_ledger": upg['ledger'],
        "physics_mode": "PRIME_LATTICE"
    })

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "TENT Claude Bridge Active. POST to /query or GET /status."})

if __name__ == "__main__":
    print(">> [BRIDGE] INITIALIZING TENT-CLAUDE TRANSLATION LAYER...")
    print(">> [BRIDGE] LISTENING ON http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=False)
