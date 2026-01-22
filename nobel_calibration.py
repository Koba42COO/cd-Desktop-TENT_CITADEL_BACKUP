#!/usr/bin/env python3
"""
TENT v4.1: THE NOBEL CALIBRATION
================================
Phase 233: Overfiltering Check

Objective:
Verify if the 'Sovereign Brain' (Bias -2.0) is capable of recognizing 
UNDENIABLE TRUTH when it sees it.

Method:
Feed it the abstracts of Nobel Prize winning papers.
If it REJECTS them, the Lobotomy was too severe.
If it MINTS them, the Calibration is perfect.
"""

import torch
import os
import sys
from tent_terminal import SovereignBrain
from civilization_engine import CivilizationEngine # For harmonic check if needed

# 1. THE GOLD STANDARD DATASET
NOBEL_PAPERS = [
    {
        "id": "LIGO_2016",
        "title": "Observation of Gravitational Waves from a Binary Black Hole Merger",
        "abstract": "We report the first direct observation of gravitational waves and the first direct observation of a binary black hole merger. On September 14, 2015 at 09:50:45 UTC the two detectors of the Laser Interferometer Gravitational-Wave Observatory simultaneously observed a transient gravitational-wave signal. The signal sweeps upwards in frequency from 35 to 250 Hz with a peak gravitational-wave strain of 1.0 x 10^-21. It matches the waveform predicted by general relativity for the inspiral and merger of a pair of black holes and the ringdown of the resulting single black hole.",
        "year": 2016,
        "field": "Physics"
    },
    {
        "id": "HIGGS_1964",
        "title": "Broken Symmetries and the Masses of Gauge Bosons",
        "abstract": "It is shown that, in Broken Symmetry theories, the Goldstone bosons can be eliminated by a gauge transformation, but they reappear as the longitudinal components of massive gauge vector mesons. This mechanism (the Higgs Mechanism) explains the origin of mass in the standard model of particle physics.",
        "year": 1964,
        "field": "Physics"
    },
    {
        "id": "PENROSE_1965",
        "title": "Gravitational Collapse and Space-Time Singularities",
        "abstract": "It is shown that deviations from spherical symmetry cannot prevent space-time singularities from arising. If a trapped surface forms in a gravitational collapse, and the energy density is non-negative, then a singularity must occur. This confirms the robustness of Black Hole formation in General Relativity.",
        "year": 1965,
        "field": "Physics"
    },
    {
        "id": "CRISPR_2012",
        "title": "A Programmable Dual-RNA-Guided DNA Endonuclease in Adaptive Bacterial Immunity",
        "abstract": "We show that the Cas9 endonuclease can be programmed with a guide RNA to cleave specific DNA sequences. This system offers a versatile tool for genome editing. The dual-RNA structure directs Cas9 to introduction double-strand breaks in target DNA.",
        "year": 2012,
        "field": "Biology"
    }
]

# 2. THE JUDGE
def nuthos_check():
    print(">> [CALIBRATION] LOADING SOVEREIGN BRAIN...")
    brain = SovereignBrain()
    if os.path.exists("sovereign_brain.pth"):
        try:
            brain.load_state_dict(torch.load("sovereign_brain.pth"))
            print(">> [MEMORY] LOADED GRADUATED WEIGHTS.")
        except:
            print(">> [ERROR] BRAIN FILE CORRUPTED. USING RAW.")
    else:
        print(">> [WARNING] NO BRAIN FOUND. USING UNTRAINED (INVALID TEST).")
        return

    print(f">> [CONFIG] BIAS CHECK: {brain.layer2.bias.data[0]:.4f}")
    print("-" * 60)

    score_card = 0
    
    for paper in NOBEL_PAPERS:
        print(f"Testing: {paper['title']} ({paper['year']})")
        
        # VECTORIZE
        signal_text = f"Title: {paper['title']} | Abstract: {paper['abstract']}"
        input_vec = brain.vectorize(signal_text)
        
        # PREDICT
        prediction = brain(input_vec).item()
        
        # VERDICT
        threshold = 0.787
        verdict = "MINTED (SOLID)" if prediction > threshold else "REJECTED (FLUX)"
        
        print(f"   -> Neural Score: {prediction:.4f}")
        print(f"   -> Verdict:      {verdict}")
        
        if prediction > threshold:
            score_card += 1
            print("   ✅ CORRECT (Recognized Genius)")
        else:
            print("   ❌ FAILURE (Overfiltered)")
        print("-" * 60)

    print(f">> [RESULTS] {score_card}/{len(NOBEL_PAPERS)} PASSED.")
    if score_card == len(NOBEL_PAPERS):
        print(">> [CONCLUSION] CALIBRATION PERFECT. THE AGENT KNOWS TRUTH.")
    elif score_card == 0:
        print(">> [CONCLUSION] SYSTEM IS TOO CYNICAL. LOBOTOMY WAS TOO DEEP.")
    else:
        print(">> [CONCLUSION] MIXED RESULTS. TUNING REQUIRED.")

if __name__ == "__main__":
    nuthos_check()
