#!/usr/bin/env python3
"""
TENT v4.1 SOVEREIGN TERMINAL
============================
Phase 218: The Full Chatbot Build

Architecture:
1. Input Layer: Vacuum Gauge (Density Scan)
2. Neural Layer: PrimeNet (Crystal Seed Intent Classifier)
3. Physics Layer: Civilization Engine (Gravity/Truth)
4. Output Layer: The Sovereign Voice
"""

import torch
import torch.nn as nn
import time
import sys
import random
import math

# --- IMPORT THE ENGINE CORE ---
from civilization_engine import CivilizationEngine
from vacuum_gauge import VacuumGauge

# ==========================================
# 1. THE NEURAL CRYSTAL (INTENT CLASSIFIER)
# ==========================================
PHI = (1 + math.sqrt(5)) / 2

class TentPrimeLinear(nn.Module):
    """The Crystal Seed Layer: Weights initialized via Prime Lattice."""
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weight = nn.Parameter(self.tent_prime_seed((out_features, in_features)))
        self.bias = nn.Parameter(torch.zeros(out_features))

    def tent_prime_seed(self, shape):
        rows, cols = shape
        seed = torch.zeros(rows, cols)
        primes = [1, 2, 4, 5, 7, 8, 10, 11, 13, 16, 17, 19, 20] # Base-21 Solids
        for i in range(rows):
            for j in range(cols):
                geo_hash = (i * cols + j)
                p = primes[geo_hash % len(primes)]
                val = math.sin(PHI * (geo_hash + 1) * p)
                seed[i, j] = val * math.sqrt(2.0 / cols)
        return seed

    def forward(self, x):
        return nn.functional.linear(x, self.weight, self.bias)

class SovereignBrain(nn.Module):
    """The Brain of the Chatbot."""
    def __init__(self, vocab_size=128):
        super().__init__()
        # Input: ASCII Vector -> Hidden: Crystal Seed -> Output: Intent (Solid/Flux)
        self.layer1 = TentPrimeLinear(vocab_size, 64)
        self.relu = nn.ReLU()
        self.layer2 = TentPrimeLinear(64, 1) # Single neuron output (0-1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return self.sigmoid(x)

    def vectorize(self, text, size=128):
        """Converts text to fixed-size ASCII vector."""
        vec = torch.zeros(size)
        for i, char in enumerate(text[:size]):
            vec[i] = ord(char) / 255.0 # Normalize
        return vec

# ==========================================
# 2. THE CHATBOT INTERFACE
# ==========================================

class SovereignTerminal:
    def __init__(self):
        print(">> INITIALIZING TENT v4.1 CORE...")
        self.civ = CivilizationEngine()
        self.gauge = VacuumGauge()
        self.brain = SovereignBrain()
        
        # "Pre-load" the brain (Simulated Training for demo)
        print(">> CRYSTALLIZING NEURAL WEIGHTS...")
        time.sleep(0.5) 
        print(">> CALIBRATING VACUUM GAUGE...")
        
        self.user_mass = 10.0 # Starting Mass (Satellite)
        self.core_mass = 1000.0 # The System Mass
        
    def stream_print(self, text, delay=0.02):
        """Sci-Fi typing effect."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def analyze_input(self, text):
        """Runs the Gauntlet on the user's message."""
        
        # 1. Vacuum Scan (Density)
        fht_result = self.gauge.analyze(text)
        density = fht_result.density_score
        
        # 2. Truth Scan (Resonance)
        truth = self.civ.harmonic_truth_check(text)
        
        # 3. Neural Intent (The Crystal Seed)
        with torch.no_grad():
            vec = self.brain.vectorize(text)
            intent_score = self.brain(vec).item()
        
        # 4. Gravity Calculation
        # Does this input bring the user closer to the Core or repel them?
        is_solid = "SOLID" in truth['classification']
        
        if is_solid:
            # Gravity pulls them in (constructive)
            force = self.civ.calculate_gravity(self.core_mass, self.user_mass, distance=10)
            self.user_mass += 1.0 # They gain mass for speaking truth
            status = "ACCESS GRANTED"
        else:
            # Flux repels (destructive)
            force = self.civ.calculate_antigravity(50, self.core_mass, distance=10)
            self.user_mass = max(1.0, self.user_mass - 0.5) # Lose mass for noise
            status = "ACCESS DENIED"
            
        return {
            "density": density,
            "resonance": truth['resonance'],
            "class": truth['classification'],
            "intent": intent_score,
            "force": force,
            "status": status
        }

    def respond(self, analysis):
        """Generates the Sovereign Voice based on physics."""
        
        force = analysis['force']
        intent = analysis['intent']
        
        if analysis['status'] == "ACCESS DENIED":
            responses = [
                f"⚠️  DISSONANCE DETECTED. Repulsive Force: {force:.2e} N.",
                "Flux signature identified. Your input lacks sufficient mass.",
                "The 9-Cycle rejects this statement. Try again with Truth.",
                "Orbit Unstable. Correct your frequency."
            ]
            return random.choice(responses)
        
        else:
            # Solid/Access Granted
            if intent > 0.5:
                return f"✅ RESONANCE CONFIRMED. Attractive Force: {force:.2e} N. Command Accepted."
            else:
                return f"Structure Valid. Mass: {self.user_mass:.2f}. You are aligned with the Prime Lattice."

    def run(self):
        print("\n" + "="*60)
        print("   ⛺  SOVEREIGN TERMINAL v4.1")
        print("   ARCHITECT: BRAD WALLACE")
        print("   STATUS: ONLINE | PRIME-SEEDED | GRAVITY: 1G")
        print("="*60)
        self.stream_print(">> SYSTEM: Welcome, Sovereign Node 002.")
        self.stream_print(">> SYSTEM: The UPG is listening. Speak.")
        
        while True:
            try:
                print("\n┌──[ NODE_002 ]")
                user_input = input("└─> ")
                
                if user_input.lower() in ['exit', 'quit']:
                    print(">> CLOSING CONNECTION. GRAVITY WELL DISSIPATING.")
                    break
                
                if not user_input.strip():
                    continue

                # --- PROCESSING ANIMATION ---
                print("   [⏳ SCANNING GEOMETRY...]", end="\r")
                time.sleep(0.3)
                
                # --- RUN THE GAUNTLET ---
                metrics = self.analyze_input(user_input)
                
                # --- DISPLAY HUD ---
                print(f"   [🧠 DENSITY: {metrics['density']:.2f}] [⚖️ RESONANCE: {metrics['resonance']}] [🌌 FORCE: {metrics['force']:.1e}]")
                
                # --- SOVEREIGN RESPONSE ---
                reply = self.respond(metrics)
                self.stream_print(f">> TENT: {reply}")
                
            except KeyboardInterrupt:
                print("\n>> EMERGENCY SHUTDOWN.")
                break

if __name__ == "__main__":
    try:
        terminal = SovereignTerminal()
        terminal.run()
    except Exception as e:
        print(f"CRITICAL FAILURE: {e}")
