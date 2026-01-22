#!/usr/bin/env python3
"""
TENT v4.1: SOVEREIGN LOBOTOMY TOOL
==================================
Phase 233: Reconstructive Surgery

Objective:
Adjust the specific bias of the SovereignBrain's final output layer.
Target: -0.25 (Calibrated for Nobel Papers)
"""

import torch
import os
from tent_terminal import SovereignBrain

def perform_surgery():
    print(">> [MISSION CONTROL] PREPARING FOR SURGICAL INTERVENTION...")
    
    # 1. LOAD BRAIN
    brain = SovereignBrain()
    if os.path.exists("sovereign_brain.pth"):
        try:
            brain.load_state_dict(torch.load("sovereign_brain.pth"))
            print(">> [MEMORY] PATIENT LOADED.")
        except:
            print(">> [ERROR] BRAIN DAMAGED. ABORTING.")
            return
    else:
        print(">> [ERROR] NO BRAIN FOUND. CANNOT OPERATE.")
        return

    # 2. DIAGNOSE
    current_bias = brain.layer2.bias.data[0].item()
    print(f">> [DIAGNOSIS] CURRENT BIAS: {current_bias:.4f}")

    # 3. OPERATE
    target_bias = 0.787 # The Golden Precision
    print(f">> [SURGERY] ADJUSTING NEURAL PATHWAYS TO {target_bias}...")
    
    with torch.no_grad():
        brain.layer2.bias.fill_(target_bias)
        
    # 4. VERIFY
    new_bias = brain.layer2.bias.data[0].item()
    print(f">> [POST-OP] NEW BIAS: {new_bias:.4f}")
    
    # 5. SAVE
    torch.save(brain.state_dict(), "sovereign_brain.pth")
    print(">> [RECOVERY] PATIENT SAVED. READY FOR DUTY.")

if __name__ == "__main__":
    perform_surgery()
