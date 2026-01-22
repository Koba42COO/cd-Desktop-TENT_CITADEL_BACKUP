#!/usr/bin/env python3
import math
import random
from dataclasses import dataclass
from typing import Literal, Tuple
from enum import Enum

# Physical Constants (Simulation Scale)
EPSILON_0 = 8.854e-12  # Permittivity of Free Space
MU_0 = 4 * math.pi * 1e-7  # Permeability of Free Space
C_LIGHT = 1 / math.sqrt(EPSILON_0 * MU_0)  # Speed of Light

class SpinState(Enum):
    UP = "↑"
    DOWN = "↓"
    SUPERPOSITION = "↑↓"

class MagneticPolarity(Enum):
    NORTH = "N"
    SOUTH = "S"
    MONOPOLE_N = "M+"  # Hypothetical North Monopole
    MONOPOLE_S = "M-"  # Hypothetical South Monopole

@dataclass
class EMField:
    """Electromagnetic Field State for a Prime Node."""
    e_field: float  # Electric Field Strength (V/m) - "Influence"
    b_field: float  # Magnetic Field Strength (T) - "Persistence"
    spin: SpinState
    polarity: MagneticPolarity
    frequency: float  # Oscillation Frequency (Hz)

class ElectromagnetismEngine:
    """
    TENT v4.0 Electromagnetism Engine.
    Treats Prime Nodes as charged particles with EM properties.
    
    - E-Field: The "Influence" an asset has on its neighbors.
    - B-Field: The "Persistence" of an asset's trajectory.
    - Spin: The "Handedness" or chirality of the asset's logic.
    - Altermagnetism: Spin-split without net magnetization.
    - Monopoles: Isolated magnetic poles (theoretical).
    """

    def calculate_e_field(self, charge: float, distance: float) -> float:
        """Coulomb's Law: E = kQ / r^2"""
        if distance <= 0: return float('inf')
        k = 1 / (4 * math.pi * EPSILON_0)
        return k * charge / (distance ** 2)

    def calculate_b_field(self, current: float, distance: float) -> float:
        """Biot-Savart Law (simplified): B = μ₀I / (2πr)"""
        if distance <= 0: return float('inf')
        return MU_0 * current / (2 * math.pi * distance)

    def lorentz_force(self, charge: float, velocity: float, e_field: float, b_field: float) -> float:
        """F = q(E + v × B)"""
        return charge * (e_field + velocity * b_field)

    def em_wave_propagation(self, amplitude: float, frequency: float, time: float, position: float) -> float:
        """E(x,t) = E₀ * sin(kx - ωt)"""
        omega = 2 * math.pi * frequency
        k = omega / C_LIGHT
        return amplitude * math.sin(k * position - omega * time)

    def apply_spin_flip(self, state: EMField) -> EMField:
        """Simulates a spin-flip operation (e.g., via RF pulse)."""
        new_spin = SpinState.DOWN if state.spin == SpinState.UP else SpinState.UP
        return EMField(
            e_field=state.e_field,
            b_field=state.b_field,
            spin=new_spin,
            polarity=state.polarity,
            frequency=state.frequency
        )

    def altermagnetic_split(self, state: EMField) -> Tuple[EMField, EMField]:
        """
        Altermagnetism: Spin-dependent band splitting WITHOUT net magnetization.
        Creates two states with opposite spin but different energy levels.
        """
        spin_up = EMField(state.e_field * 1.1, state.b_field, SpinState.UP, state.polarity, state.frequency)
        spin_down = EMField(state.e_field * 0.9, state.b_field, SpinState.DOWN, state.polarity, state.frequency)
        return spin_up, spin_down

    def create_monopole(self, polarity: Literal['north', 'south']) -> EMField:
        """
        Hypothetical: Creates an isolated magnetic monopole.
        In reality, monopoles always come in dipole pairs.
        """
        pole = MagneticPolarity.MONOPOLE_N if polarity == 'north' else MagneticPolarity.MONOPOLE_S
        return EMField(
            e_field=0.0,  # Monopoles have no electric field
            b_field=1.0,  # Strong magnetic field
            spin=SpinState.SUPERPOSITION,
            polarity=pole,
            frequency=0.0
        )

    def spintronic_gate(self, input_spin: SpinState, gate_type: Literal['NOT', 'PASS']) -> SpinState:
        """Spintronic Logic Gate."""
        if gate_type == 'NOT':
            return SpinState.DOWN if input_spin == SpinState.UP else SpinState.UP
        return input_spin

# ==========================================
# SIMULATION
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("   ⛺  TENT v4.0  |  ELECTROMAGNETISM ENGINE")
    print("   PHASE 193: FIELDS, SPIN, ALTERMAGNETISM")
    print("="*60 + "\n")
    
    engine = ElectromagnetismEngine()
    
    # 1. FIELD CALCULATIONS
    print("--- FIELD CALCULATIONS ---")
    e = engine.calculate_e_field(charge=1e-6, distance=0.1)
    b = engine.calculate_b_field(current=10, distance=0.05)
    print(f"   E-Field (1μC at 10cm): {e:.2e} V/m")
    print(f"   B-Field (10A at 5cm):  {b:.2e} T")
    
    # 2. LORENTZ FORCE
    print("\n--- LORENTZ FORCE ---")
    f = engine.lorentz_force(charge=1e-6, velocity=1000, e_field=e, b_field=b)
    print(f"   Force on charged particle: {f:.4e} N")
    
    # 3. SPIN OPERATIONS
    print("\n--- SPIN OPERATIONS ---")
    state = EMField(e_field=100, b_field=0.5, spin=SpinState.UP, polarity=MagneticPolarity.NORTH, frequency=1e9)
    print(f"   Initial Spin: {state.spin.value}")
    flipped = engine.apply_spin_flip(state)
    print(f"   After Flip:   {flipped.spin.value}")
    
    # 4. ALTERMAGNETISM
    print("\n--- ALTERMAGNETISM (Spin-Split Bands) ---")
    up, down = engine.altermagnetic_split(state)
    print(f"   Spin-Up Band E-Field:   {up.e_field:.2f} V/m")
    print(f"   Spin-Down Band E-Field: {down.e_field:.2f} V/m")
    print(f"   (No net magnetization, but energy split!)")
    
    # 5. MONOPOLE
    print("\n--- MAGNETIC MONOPOLE (Theoretical) ---")
    mono = engine.create_monopole('north')
    print(f"   Monopole Polarity: {mono.polarity.value}")
    print(f"   B-Field: {mono.b_field} T (Isolated!)")
    
    # 6. SPINTRONIC GATE
    print("\n--- SPINTRONIC LOGIC GATE ---")
    input_spin = SpinState.UP
    output_spin = engine.spintronic_gate(input_spin, 'NOT')
    print(f"   Input:  {input_spin.value}")
    print(f"   Output: {output_spin.value} (via NOT gate)")
    
    print("\n>> ELECTROMAGNETISM ENGINE OPERATIONAL.")
