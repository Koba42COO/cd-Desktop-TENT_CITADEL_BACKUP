#!/usr/bin/env python3
"""
TENT v4.1 SOVEREIGN HUD
=======================
Phase 226: The Cockpit

Visualizes the heartbeat of the Sovereign Agent.
Reads the neural logs and renders an ASCII chart of Mass & Entropy.
"""

import time
import os
import sys
import math
import shutil

# --- CONFIGURATION ---
# The path you used in your tail command
LOG_PATH = "/Users/coo-koba42/.gemini/antigravity/brain/a342aeff-f029-42a7-ad5f-12028bd87db8/tent_sovereign.log"

class SovereignHUD:
    def __init__(self, log_file):
        self.log_file = log_file
        self.mass_history = []
        self.loss_history = []
        self.max_history = 60 # Width of the chart
        self.last_cycle = 0
        self.last_action = "INITIALIZING..."

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def parse_log(self):
        """Reads the entire log file and extracts the latest data points."""
        if not os.path.exists(self.log_file):
            return False

        try:
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
                
            # We only care about the last N lines to keep it snappy
            relevant_lines = lines[-200:] if len(lines) > 200 else lines
            
            new_mass = []
            new_loss = []
            
            for line in relevant_lines:
                # Parse Mass and Loss
                # Format: [CYCLE 120] ... Loss: 0.2362 | Mass: 39.5
                if "Mass:" in line and "Loss:" in line:
                    parts = line.split("|")
                    try:
                        # Extract Mass
                        m_part = parts[1].strip() # "Mass: 39.5"
                        mass_val = float(m_part.split(":")[1].strip())
                        new_mass.append(mass_val)
                        
                        # Extract Loss
                        l_part = parts[0].strip() # "... Loss: 0.2362"
                        loss_val = float(l_part.split("Loss:")[1].strip())
                        new_loss.append(loss_val)
                        
                        # Extract Cycle
                        c_part = line.split("]")[1].strip() # "[CYCLE 120"
                        self.last_cycle = int(c_part.replace("[CYCLE ", ""))
                        
                    except:
                        continue
                
                # Parse Action
                # Format: [CYCLE 120] Signal: '...' -> MINTED (CORRECT)
                if "Signal:" in line and "->" in line:
                    self.last_action = line.split("->")[1].strip()

            self.mass_history = new_mass[-self.max_history:]
            self.loss_history = new_loss[-self.max_history:]
            return True
            
        except Exception as e:
            return False

    def render_ascii_chart(self, data, height=10, label="MASS"):
        """Draws a beautiful ASCII graph."""
        if not data:
            return ["No Data"] * height

        min_val = min(data)
        max_val = max(data)
        if max_val == min_val: max_val += 1
        
        range_val = max_val - min_val
        step = range_val / height
        
        rows = []
        # Draw from top to bottom
        for h in range(height, -1, -1):
            row_str = ""
            cutoff = min_val + (step * h)
            
            # Y-Axis Label
            if h == height:
                row_str += f"{max_val:6.1f} ┤ "
            elif h == 0:
                row_str += f"{min_val:6.1f} ┤ "
            else:
                row_str += "       │ "
            
            # Plot points
            for val in data:
                if val >= cutoff:
                    if val >= cutoff + step: # Full block
                        row_str += "█"
                    else: # Partial block based on remainder
                        remainder = val - cutoff
                        if remainder > step * 0.75: row_str += "▇"
                        elif remainder > step * 0.5: row_str += "▆"
                        elif remainder > step * 0.25: row_str += "▃"
                        else: row_str += " "
                else:
                    row_str += " "
            rows.append(row_str)
        
        return rows

    def run(self):
        print(f">> LINKING TO NEURAL LOG: {self.log_file}")
        
        while True:
            if self.parse_log():
                self.clear_screen()
                
                # HEADER
                print("="*60)
                print("   ⛺  TENT v4.1 SOVEREIGN HUD")
                print(f"   STATUS: ONLINE  |  PID: DAEMON  |  CYCLE: {self.last_cycle}")
                print("="*60)
                
                # LATEST ACTION
                action_color = ""
                if "CORRECT" in self.last_action: status = "✅ OPTIMAL"
                elif "ERROR" in self.last_action: status = "⚠️  LEARNING"
                else: status = "WAITING"
                
                print(f"\n   LATEST SYNAPSE: {self.last_action}")
                print(f"   SYSTEM STATUS:  {status}")
                
                # MASS CHART
                print(f"\n   📈 SOVEREIGN MASS (Gravitational Pull)")
                print("   " + "-"*50)
                rows = self.render_ascii_chart(self.mass_history, height=8)
                for row in rows:
                    print(row)
                
                # LOSS CHART (Mini)
                current_loss = self.loss_history[-1] if self.loss_history else 0
                print(f"\n   🧠 NEURAL PLASTICITY (Loss: {current_loss:.4f})")
                
                # Footer
                print("\n" + "="*60)
                print("   [CTRL+C] to Exit HUD (Agent keeps running)")
            
            else:
                print("Waiting for log stream...")
            
            time.sleep(1)

if __name__ == "__main__":
    # Allow override via command line
    path = sys.argv[1] if len(sys.argv) > 1 else LOG_PATH
    hud = SovereignHUD(path)
    hud.run()
