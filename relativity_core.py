#!/usr/bin/env python3
import math
from dataclasses import dataclass
from typing import Tuple

# Physical Constants
C = 299792458  # Speed of Light (m/s)
G = 6.67430e-11  # Gravitational Constant (m³/kg/s²)

@dataclass
class SpacetimeEvent:
    """A point in 4D Spacetime."""
    t: float  # Time (s)
    x: float  # Position X (m)
    y: float  # Position Y (m)
    z: float  # Position Z (m)

@dataclass
class RelativisticState:
    """Relativistic state of a Prime Node."""
    rest_mass: float  # m₀ (kg)
    velocity: float  # v (m/s)
    proper_time: float  # τ (s)
    position: SpacetimeEvent

class RelativityEngine:
    """
    TENT v4.0 Relativity Engine.
    
    Treats Prime Nodes as relativistic objects.
    - Velocity affects perceived Mass (Lorentz Factor).
    - High-velocity assets experience Time Dilation (slower aging).
    - Mass curves Spacetime (Gravity).
    """

    # ==========================================
    # SPECIAL RELATIVITY
    # ==========================================

    def lorentz_factor(self, velocity: float) -> float:
        """γ = 1 / √(1 - v²/c²)"""
        if abs(velocity) >= C:
            return float('inf')
        return 1 / math.sqrt(1 - (velocity ** 2) / (C ** 2))

    def time_dilation(self, proper_time: float, velocity: float) -> float:
        """Δt = γΔτ (Moving clocks run slow)"""
        gamma = self.lorentz_factor(velocity)
        return proper_time * gamma

    def length_contraction(self, proper_length: float, velocity: float) -> float:
        """L = L₀/γ (Moving rulers appear shorter)"""
        gamma = self.lorentz_factor(velocity)
        return proper_length / gamma

    def relativistic_mass(self, rest_mass: float, velocity: float) -> float:
        """m = γm₀ (Mass increases with velocity)"""
        gamma = self.lorentz_factor(velocity)
        return rest_mass * gamma

    def mass_energy_equivalence(self, mass: float) -> float:
        """E = mc² (The Big One)"""
        return mass * (C ** 2)

    def relativistic_momentum(self, rest_mass: float, velocity: float) -> float:
        """p = γm₀v"""
        gamma = self.lorentz_factor(velocity)
        return gamma * rest_mass * velocity

    def lorentz_transform_time(self, t: float, x: float, velocity: float) -> float:
        """t' = γ(t - vx/c²)"""
        gamma = self.lorentz_factor(velocity)
        return gamma * (t - (velocity * x) / (C ** 2))

    def lorentz_transform_position(self, t: float, x: float, velocity: float) -> float:
        """x' = γ(x - vt)"""
        gamma = self.lorentz_factor(velocity)
        return gamma * (x - velocity * t)

    # ==========================================
    # GENERAL RELATIVITY
    # ==========================================

    def spacetime_interval(self, event1: SpacetimeEvent, event2: SpacetimeEvent) -> float:
        """
        ds² = -c²dt² + dx² + dy² + dz² (Minkowski Metric)
        Negative for timelike, Positive for spacelike, Zero for lightlike.
        """
        dt = event2.t - event1.t
        dx = event2.x - event1.x
        dy = event2.y - event1.y
        dz = event2.z - event1.z
        
        return -(C ** 2) * (dt ** 2) + (dx ** 2) + (dy ** 2) + (dz ** 2)

    def schwarzschild_radius(self, mass: float) -> float:
        """r_s = 2GM/c² (Event Horizon radius)"""
        return (2 * G * mass) / (C ** 2)

    def gravitational_time_dilation(self, proper_time: float, mass: float, radius: float) -> float:
        """
        Δt = Δτ / √(1 - r_s/r)
        Clocks run slower in stronger gravitational fields.
        """
        r_s = self.schwarzschild_radius(mass)
        if radius <= r_s:
            return float('inf')  # Inside event horizon
        factor = math.sqrt(1 - r_s / radius)
        return proper_time / factor

    def geodesic_deviation(self, mass: float, radius: float) -> float:
        """
        Simplified: Curvature ∝ GM/r³
        Represents how much spacetime is curved at a distance r from mass M.
        """
        if radius <= 0: return float('inf')
        return G * mass / (radius ** 3)

    def gravitational_wave_strain(self, mass1: float, mass2: float, distance: float, separation: float) -> float:
        """
        h ≈ (4G²M₁M₂) / (c⁴ r d)
        Strain amplitude from binary system at distance r.
        """
        if distance <= 0 or separation <= 0:
            return 0.0
        return (4 * (G ** 2) * mass1 * mass2) / ((C ** 4) * distance * separation)

# ==========================================
# SIMULATION
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("   ⛺  TENT v4.0  |  RELATIVITY ENGINE")
    print("   PHASE 195: SPACETIME, LORENTZ, GRAVITY")
    print("="*60 + "\n")
    
    engine = RelativityEngine()
    
    # 1. LORENTZ FACTOR
    print("--- LORENTZ FACTOR ---")
    for v_frac in [0.1, 0.5, 0.9, 0.99]:
        v = v_frac * C
        gamma = engine.lorentz_factor(v)
        print(f"   v = {v_frac}c: γ = {gamma:.4f}")
    
    # 2. TIME DILATION
    print("\n--- TIME DILATION ---")
    proper_time = 1.0  # 1 second
    for v_frac in [0.5, 0.9, 0.99]:
        v = v_frac * C
        dilated = engine.time_dilation(proper_time, v)
        print(f"   v = {v_frac}c: 1s proper → {dilated:.4f}s observed")
    
    # 3. E = mc²
    print("\n--- MASS-ENERGY EQUIVALENCE ---")
    mass = 1.0  # 1 kg
    energy = engine.mass_energy_equivalence(mass)
    print(f"   1 kg of matter = {energy:.3e} J")
    print(f"   (≈ {energy / 4.184e12:.1f} kilotons of TNT)")
    
    # 4. SCHWARZSCHILD RADIUS
    print("\n--- SCHWARZSCHILD RADIUS (Event Horizon) ---")
    sun_mass = 1.989e30  # kg
    r_s_sun = engine.schwarzschild_radius(sun_mass)
    earth_mass = 5.972e24
    r_s_earth = engine.schwarzschild_radius(earth_mass)
    print(f"   Sun:   r_s = {r_s_sun / 1000:.2f} km")
    print(f"   Earth: r_s = {r_s_earth * 1000:.2f} mm")
    
    # 5. GRAVITATIONAL WAVES
    print("\n--- GRAVITATIONAL WAVE STRAIN ---")
    # Binary neutron stars at 100 Mpc
    m_ns = 1.4 * sun_mass
    distance = 100 * 3.086e22  # 100 Mpc in meters
    separation = 100e3  # 100 km
    h = engine.gravitational_wave_strain(m_ns, m_ns, distance, separation)
    print(f"   NS-NS binary at 100 Mpc: h ≈ {h:.2e}")
    
    print("\n>> RELATIVITY ENGINE OPERATIONAL.")
