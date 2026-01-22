#!/usr/bin/env python3
"""
TENT v4.1: THE SEMANTIC STABILIZER
==================================
Phase 240: PID Controller for Agent Mass

Concept (from ROADMAP_v4.md):
"If the saw blade gets hot, you are cutting wrong."

This module monitors the Agent's Mass over time and applies
feedback-loop corrections to prevent oscillation or runaway bias.

PID Components:
- P (Proportional): Correct current error (Mass vs Target).
- I (Integral): Correct accumulated historical drift.
- D (Derivative): Dampen sudden changes (prevent overshoot).
"""

import json
import os
from datetime import datetime

# --- CONFIG ---
HISTORY_FILE = "stabilizer_history.json"
TARGET_MASS = 400.0  # The "Ideal" sovereign mass target
Kp = 0.5  # Proportional gain
Ki = 0.1  # Integral gain
Kd = 0.05 # Derivative gain

class SemanticStabilizer:
    def __init__(self):
        self.history = []  # List of (timestamp, mass) tuples
        self.integral = 0.0
        self.last_error = 0.0
        self.load_history()
    
    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            try:
                with open(HISTORY_FILE, 'r') as f:
                    data = json.load(f)
                    self.history = data.get("history", [])
                    self.integral = data.get("integral", 0.0)
                    self.last_error = data.get("last_error", 0.0)
            except:
                pass
    
    def save_history(self):
        data = {
            "history": self.history[-100:],  # Keep last 100 readings
            "integral": self.integral,
            "last_error": self.last_error
        }
        with open(HISTORY_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    
    def record(self, current_mass: float):
        """Records a mass reading and returns the PID correction signal."""
        timestamp = datetime.utcnow().isoformat()
        self.history.append((timestamp, current_mass))
        
        # --- PID Calculation ---
        error = TARGET_MASS - current_mass
        
        # P: Proportional
        p_term = Kp * error
        
        # I: Integral (cumulative error)
        self.integral += error
        i_term = Ki * self.integral
        
        # D: Derivative (rate of change)
        derivative = error - self.last_error
        d_term = Kd * derivative
        
        self.last_error = error
        
        # Total Correction Signal
        correction = p_term + i_term + d_term
        
        self.save_history()
        
        return {
            "error": error,
            "p_term": p_term,
            "i_term": i_term,
            "d_term": d_term,
            "correction": correction,
            "recommendation": self._interpret(correction)
        }
    
    def _interpret(self, correction: float) -> str:
        """Translates the correction signal into an actionable recommendation."""
        if correction > 5.0:
            return "EXPAND FILTER: Accept more papers to increase Mass."
        elif correction < -5.0:
            return "CONTRACT FILTER: Reject more papers to stabilize."
        else:
            return "HOLD STEADY: Mass is within acceptable range."
    
    def status(self) -> str:
        """Returns a human-readable status."""
        if not self.history:
            return "No data recorded yet."
        
        _, last_mass = self.history[-1]
        result = self.record(last_mass)  # Get latest PID output
        
        return f"""
SEMANTIC STABILIZER STATUS
==========================
Target Mass:    {TARGET_MASS}
Current Mass:   {last_mass:.2f}
Error:          {result['error']:.2f}
Correction:     {result['correction']:.2f}
Recommendation: {result['recommendation']}
"""

# --- CLI Interface ---
if __name__ == "__main__":
    import sys
    stabilizer = SemanticStabilizer()
    
    if len(sys.argv) > 1:
        try:
            mass = float(sys.argv[1])
            result = stabilizer.record(mass)
            print(f">> [STABILIZER] Recorded Mass: {mass}")
            print(f"   Error: {result['error']:.2f}")
            print(f"   Correction: {result['correction']:.2f}")
            print(f"   >> {result['recommendation']}")
        except ValueError:
            print("Usage: python3 semantic_stabilizer.py <mass_value>")
    else:
        print(stabilizer.status())
