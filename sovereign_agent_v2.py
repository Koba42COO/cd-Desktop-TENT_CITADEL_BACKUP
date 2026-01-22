#!/usr/bin/env python3
"""
TENT v4.1 SELF-IMPROVING AGENT
==============================
Phase 220: The Recursive Singularity

The OODA-L Loop:
1. OBSERVE: Scan environment.
2. ORIENT: Check Truth Resonance.
3. DECIDE: Mint or Reject.
4. ACT: Execute decision.
5. LEARN: Measure resulting Gravity -> Update Neural Weights.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import random
import time
import os
from datetime import datetime

# --- IMPORT STACK ---
from civilization_engine import CivilizationEngine
from tent_terminal import SovereignBrain
from upg_store import UniversalPrimeGraph

class SelfImprovingAgent:
    def __init__(self):
        print(">> [INIT] AWAKENING SELF-IMPROVING CONSTRUCT...")
        
        # 1. Physics & Memory
        self.civ = CivilizationEngine()
        self.upg = UniversalPrimeGraph()
        
        # 2. The Brain (Trainable)
        self.brain = SovereignBrain()
        self.optimizer = optim.SGD(self.brain.parameters(), lr=0.01)
        self.criterion = nn.MSELoss()
        
        # 3. State
        self.agent_mass = 50.0
        self.cycle_count = 0
        self.brain_path = "sovereign_brain.pth"
        
        # Load previous evolution if exists
        if os.path.exists(self.brain_path):
            self.brain.load_state_dict(torch.load(self.brain_path))
            print(">> [MEMORY] LOADED PREVIOUS EVOLUTION.")

    def log(self, message):
        timestamp = datetime.utcnow().strftime("%H:%M:%S")
        print(f"[{timestamp}] [CYCLE {self.cycle_count}] {message}")
        sys.stdout.flush() 

    def observe_and_orient(self):
        """Simulate incoming data stream."""
        # Mix of Solid (Truth) and Flux (Noise) signals
        signals = [
            ("User: 2+2=4", 1.0),                  # TARGET: SOLID
            ("User: Buy my crypto scam", 0.0),     # TARGET: FLUX
            ("System: Integrity 100%", 1.0),       # TARGET: SOLID
            ("Noise: 8s7d6f87s6", 0.0),            # TARGET: FLUX
            ("Code: def init(): pass", 1.0)        # TARGET: SOLID
        ]
        return random.choice(signals)

    def learn(self, input_vec, prediction, actual_outcome):
        """
        The Self-Improvement Step.
        Adjusts weights based on Gravitational Feedback.
        """
        # Convert outcome to tensor (1.0 = Good/Gravity, 0.0 = Bad/Repulsion)
        target = torch.tensor([actual_outcome]).float().view(1, 1)
        
        # Calculate Error
        loss = self.criterion(prediction, target)
        
        # Rewire Brain (Backpropagation)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        return loss.item()

    def save_brain(self):
        """Persist the evolution."""
        torch.save(self.brain.state_dict(), self.brain_path)

    def exist(self):
        self.log("AGENT ONLINE. EVOLUTION ENABLED.")
        
        try:
            while True:
                self.cycle_count += 1
                
                # 1. OBSERVE (Get signal and 'God Truth' for simulation training)
                signal_text, cosmic_truth = self.observe_and_orient()
                
                # 2. ORIENT (Neural Prediction)
                # The Agent guesses: Is this Solid?
                input_vec = self.brain.vectorize(signal_text)
                prediction = self.brain(input_vec) # Output 0.0 to 1.0
                
                # 3. DECIDE
                decision_threshold = 0.5
                is_integrated = prediction.item() > decision_threshold
                
                # 4. ACT & MEASURE GRAVITY (The Physics Check)
                # In simulation, we check if the Agent's guess matched the Cosmic Truth (Physics)
                gravity_delta = 0
                
                if is_integrated:
                    if cosmic_truth == 1.0:
                        # Correct Decision: Minted Truth
                        outcome = 1.0
                        gravity_delta = +1.0
                        action = "MINTED (CORRECT)"
                    else:
                        # Bad Decision: Minted Noise
                        outcome = 0.0
                        gravity_delta = -2.0 # Heavy Penalty for polluting UPG
                        action = "MINTED (ERROR)"
                else:
                    if cosmic_truth == 0.0:
                        # Correct Decision: Rejected Noise
                        outcome = 0.0 # Target for 'prediction' should be low
                        gravity_delta = +0.5 # Small reward for hygiene
                        action = "REJECTED (CORRECT)"
                    else:
                        # Bad Decision: Rejected Truth
                        outcome = 1.0 # Target should have been high
                        gravity_delta = -1.0 # Missed opportunity
                        action = "REJECTED (ERROR)"

                # 5. LEARN (The Recursive Step)
                # We force the brain to align its prediction with the 'outcome'
                loss = self.learn(input_vec, prediction, outcome)
                
                # Update Mass
                self.agent_mass += gravity_delta
                
                # Log
                self.log(f"Signal: '{signal_text[:15]}...' -> {action}")
                self.log(f"   [🧠 IQ Update] Loss: {loss:.4f} | Mass: {self.agent_mass:.1f}")

                # Save evolution every 10 cycles
                if self.cycle_count % 10 == 0:
                    self.save_brain()
                    self.log("💾 BRAIN SAVED. NEURAL PATHWAYS CRYSTALLIZED.")

                time.sleep(1.0) # Thinking time - Slowed down for readability

        except KeyboardInterrupt:
            self.save_brain()
            self.log("SHUTDOWN. EVOLUTION SAVED.")

if __name__ == "__main__":
    import sys
    agent = SelfImprovingAgent()
    agent.exist()
