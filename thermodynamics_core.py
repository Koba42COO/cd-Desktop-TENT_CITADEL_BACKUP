#!/usr/bin/env python3
import math
import random
from dataclasses import dataclass, field
from typing import List

# Physical Constants
K_BOLTZMANN = 1.380649e-23  # Boltzmann Constant (J/K)
STEFAN_BOLTZMANN = 5.670374419e-8  # Stefan-Boltzmann Constant (W/m²K⁴)
R_GAS = 8.314  # Ideal Gas Constant (J/mol·K)

@dataclass
class ThermoState:
    """Thermodynamic State of a Prime Node."""
    internal_energy: float  # U (Joules)
    temperature: float  # T (Kelvin)
    entropy: float  # S (J/K)
    volume: float  # V (m³)
    pressure: float  # P (Pa)
    heat_capacity: float = 1.0  # Cv (J/K)

class ThermodynamicsEngine:
    """
    TENT v4.0 Thermodynamics Engine.
    
    Treats Prime Nodes as closed thermodynamic systems.
    - Internal Energy (U): The "true value" of the asset.
    - Temperature (T): The "activity level" or "market heat".
    - Entropy (S): The "disorder" or "uncertainty" of the asset.
    """

    # ==========================================
    # LAWS OF THERMODYNAMICS
    # ==========================================

    def first_law(self, state: ThermoState, heat_in: float, work_done: float) -> ThermoState:
        """
        1st Law: ΔU = Q - W
        Conservation of Energy.
        """
        delta_u = heat_in - work_done
        new_u = state.internal_energy + delta_u
        new_t = state.temperature + (delta_u / state.heat_capacity)  # Simplified
        return ThermoState(
            internal_energy=new_u,
            temperature=max(0.01, new_t),  # Avoid absolute zero
            entropy=state.entropy,
            volume=state.volume,
            pressure=state.pressure,
            heat_capacity=state.heat_capacity
        )

    def second_law_entropy_change(self, heat: float, temperature: float) -> float:
        """
        2nd Law: ΔS = Q / T
        Entropy always increases in an isolated system.
        """
        if temperature <= 0: return float('inf')
        return heat / temperature

    def third_law_check(self, state: ThermoState) -> bool:
        """
        3rd Law: As T → 0, S → 0.
        Returns True if the system is approaching absolute zero.
        """
        return state.temperature < 1.0  # Near absolute zero

    # ==========================================
    # HEAT TRANSFER
    # ==========================================

    def conduction(self, k: float, area: float, temp_diff: float, thickness: float) -> float:
        """Fourier's Law: Q = -kA(dT/dx)"""
        if thickness <= 0: return 0.0
        return k * area * temp_diff / thickness

    def convection(self, h: float, area: float, temp_diff: float) -> float:
        """Newton's Law of Cooling: Q = hA(T_s - T_∞)"""
        return h * area * temp_diff

    def radiation(self, emissivity: float, area: float, temperature: float) -> float:
        """Stefan-Boltzmann Law: Q = εσAT⁴"""
        return emissivity * STEFAN_BOLTZMANN * area * (temperature ** 4)

    # ==========================================
    # STATISTICAL MECHANICS
    # ==========================================

    def boltzmann_distribution(self, energy_levels: List[float], temperature: float) -> List[float]:
        """
        P(Eᵢ) = exp(-Eᵢ / kT) / Z
        Returns probability distribution over energy states.
        """
        if temperature <= 0: return [0.0] * len(energy_levels)
        
        boltzmann_factors = [math.exp(-e / (K_BOLTZMANN * temperature)) for e in energy_levels]
        z = sum(boltzmann_factors)  # Partition function
        
        return [bf / z for bf in boltzmann_factors]

    def calculate_entropy_statistical(self, probabilities: List[float]) -> float:
        """S = -k Σ pᵢ ln(pᵢ)  (Gibbs Entropy)"""
        entropy = 0.0
        for p in probabilities:
            if p > 0:
                entropy -= K_BOLTZMANN * p * math.log(p)
        return entropy

    def ideal_gas_equation(self, n_moles: float, temperature: float, volume: float) -> float:
        """PV = nRT -> P = nRT/V"""
        if volume <= 0: return float('inf')
        return n_moles * R_GAS * temperature / volume

# ==========================================
# SIMULATION
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("   ⛺  TENT v4.0  |  THERMODYNAMICS ENGINE")
    print("   PHASE 194: ENERGY, ENTROPY, HEAT")
    print("="*60 + "\n")
    
    engine = ThermodynamicsEngine()
    
    # 1. FIRST LAW
    print("--- FIRST LAW (Energy Conservation) ---")
    state = ThermoState(internal_energy=1000, temperature=300, entropy=10, volume=1, pressure=101325)
    new_state = engine.first_law(state, heat_in=500, work_done=200)
    print(f"   Initial U: {state.internal_energy} J, T: {state.temperature} K")
    print(f"   After +500J heat, -200J work:")
    print(f"   New U: {new_state.internal_energy} J, T: {new_state.temperature:.1f} K")
    
    # 2. SECOND LAW
    print("\n--- SECOND LAW (Entropy Increase) ---")
    delta_s = engine.second_law_entropy_change(heat=500, temperature=300)
    print(f"   ΔS for 500J heat at 300K: {delta_s:.4f} J/K")
    
    # 3. HEAT TRANSFER
    print("\n--- HEAT TRANSFER ---")
    q_cond = engine.conduction(k=200, area=0.1, temp_diff=50, thickness=0.01)
    q_conv = engine.convection(h=25, area=0.1, temp_diff=50)
    q_rad = engine.radiation(emissivity=0.9, area=0.1, temperature=500)
    print(f"   Conduction (Copper):  {q_cond:.2f} W")
    print(f"   Convection (Air):     {q_conv:.2f} W")
    print(f"   Radiation (500K):     {q_rad:.2f} W")
    
    # 4. STATISTICAL MECHANICS
    print("\n--- BOLTZMANN DISTRIBUTION ---")
    energies = [0, 1e-21, 2e-21, 3e-21]
    probs = engine.boltzmann_distribution(energies, temperature=300)
    for i, (e, p) in enumerate(zip(energies, probs)):
        print(f"   E{i} = {e:.2e} J: P = {p:.4f}")
    
    gibbs_s = engine.calculate_entropy_statistical(probs)
    print(f"   Gibbs Entropy: {gibbs_s:.4e} J/K")
    
    # 5. IDEAL GAS
    print("\n--- IDEAL GAS LAW ---")
    pressure = engine.ideal_gas_equation(n_moles=1, temperature=300, volume=0.0224)
    print(f"   1 mol at STP: P = {pressure:.0f} Pa")
    
    print("\n>> THERMODYNAMICS ENGINE OPERATIONAL.")
