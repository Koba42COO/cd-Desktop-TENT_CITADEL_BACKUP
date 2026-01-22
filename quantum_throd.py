#!/usr/bin/env python3
import random
import math
from dataclasses import dataclass
from typing import Literal

# Reduced Planck Constant (for simulation, set to readable value)
HBAR_TENT = 1.0

@dataclass
class QuantumState:
    """
    Wraps a PrimeNode in a Quantum Superposition.
    Until measured, its values are probabilistic.
    """
    mass_true: float
    velocity_true: float
    position_true: float
    
    # Uncertainty (Δ)
    delta_mass: float = 0.0
    delta_velocity: float = 0.0

class QuantumThrodEngine:
    """
    TENT v4.0 Quantum Engine.
    Implements the Heisenberg Uncertainty Principle:
    Δx * Δp >= ħ/2
    
    Measuring Mass precisely -> introduces Velocity uncertainty.
    Measuring Velocity precisely -> introduces Mass uncertainty.
    """
    
    def measure_observable(self, state: QuantumState, observable: Literal['mass', 'velocity']) -> dict:
        """
        Collapses the wavefunction for the specified observable.
        The conjugate variable becomes uncertain.
        """
        result = {}
        
        if observable == 'mass':
            # Measure Mass precisely
            result['mass'] = state.mass_true
            result['mass_uncertainty'] = 0.0
            
            # Apply Uncertainty to Velocity (the conjugate)
            # ΔvΔm >= ħ/2 -> Δv >= ħ / (2 * m)
            # For simulation, add noise proportional to 1/mass
            noise_factor = HBAR_TENT / (2 * max(state.mass_true, 0.1))
            velocity_noise = random.uniform(-noise_factor * 10, noise_factor * 10)
            
            result['velocity'] = state.velocity_true + velocity_noise
            result['velocity_uncertainty'] = abs(velocity_noise)
            
            state.delta_velocity = abs(velocity_noise)
            state.delta_mass = 0.0
            
        elif observable == 'velocity':
            # Measure Velocity precisely
            result['velocity'] = state.velocity_true
            result['velocity_uncertainty'] = 0.0
            
            # Apply Uncertainty to Mass (Perceived Value Fluctuation)
            # Δm >= ħ / (2 * v) - but for near-zero v, cap the effect
            v_eff = max(abs(state.velocity_true), 0.5)
            noise_factor = HBAR_TENT / (2 * v_eff)
            mass_noise = random.uniform(-noise_factor * 10, noise_factor * 10)
            
            result['mass'] = state.mass_true + mass_noise
            result['mass_uncertainty'] = abs(mass_noise)
            
            state.delta_mass = abs(mass_noise)
            state.delta_velocity = 0.0
        
        return result

    def throd_operator(self, state: QuantumState) -> str:
        """
        The 'Throd' is the quantum of semantic disturbance.
        When applied, it flips the uncertainty relationship.
        
        Throd Up: Increases position precision, increases momentum blur.
        Throd Down: Increases momentum precision, increases position blur.
        """
        # Simulate a random throd interaction
        throd_val = random.choice(['up', 'down'])
        
        if throd_val == 'up':
            state.delta_velocity *= 2  # More momentum blur
        else:
            state.delta_mass *= 2  # More value blur
            
        return throd_val

# ==========================================
# SIMULATION
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("   ⛺  TENT v4.0  |  QUANTUM THROD ENGINE")
    print("   PHASE 192: THE UNCERTAINTY PRINCIPLE")
    print("="*60 + "\n")
    
    engine = QuantumThrodEngine()
    
    # Create a Schrödinger's Asset
    asset = QuantumState(mass_true=50.0, velocity_true=10.0, position_true=0.0)
    print(f"INITIAL STATE: Mass={asset.mass_true}, Vel={asset.velocity_true}")
    
    print("\n--- MEASURING MASS (5 times) ---")
    for i in range(5):
        result = engine.measure_observable(asset, 'mass')
        print(f"   M{i+1}: Mass={result['mass']:.2f} (Δ={result['mass_uncertainty']:.4f}), "
              f"Vel={result['velocity']:.2f} (Δ={result['velocity_uncertainty']:.4f})")
              
    print("\n--- MEASURING VELOCITY (5 times) ---")
    for i in range(5):
        result = engine.measure_observable(asset, 'velocity')
        print(f"   V{i+1}: Mass={result['mass']:.2f} (Δ={result['mass_uncertainty']:.4f}), "
              f"Vel={result['velocity']:.2f} (Δ={result['velocity_uncertainty']:.4f})")
              
    print("\n>> VERDICT: Observing one property destabilizes the other.")
