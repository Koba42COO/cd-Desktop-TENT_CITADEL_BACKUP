#!/usr/bin/env python3
import math
import random
from dataclasses import dataclass
from typing import List, Tuple, Literal
from enum import Enum

# Physical Constants
HBAR = 1.054571817e-34  # Reduced Planck Constant (J·s)
C = 299792458  # Speed of Light (m/s)
ALPHA_EM = 1/137  # Fine Structure Constant

class ParticleType(Enum):
    FERMION = "Fermion"  # Half-integer spin (matter)
    BOSON = "Boson"  # Integer spin (forces)

class InteractionVertex(Enum):
    QED = "γ"  # Photon (Electromagnetic)
    QCD = "g"  # Gluon (Strong)
    WEAK = "W/Z"  # Weak bosons
    HIGGS = "H"  # Higgs

@dataclass
class FieldExcitation:
    """A particle is an excitation of the underlying quantum field."""
    name: str
    particle_type: ParticleType
    mass: float  # kg
    spin: float  # 0, 1/2, 1, 3/2, 2...
    charge: float  # Elementary charges
    color: str  # QCD color charge (None for leptons)

@dataclass
class Propagator:
    """Virtual particle propagator in Feynman diagrams."""
    particle: FieldExcitation
    momentum_squared: float  # q² (GeV²)
    amplitude: complex

class QFTEngine:
    """
    TENT v4.0 Quantum Field Theory Engine.
    
    Unifies all physics into a single framework:
    - Particles = Field Excitations
    - Interactions = Vertex Functions
    - Amplitudes = Feynman Diagrams
    """

    def __init__(self):
        # Standard Model Particles (Simplified)
        self.particles = {
            'electron': FieldExcitation('electron', ParticleType.FERMION, 9.109e-31, 0.5, -1, None),
            'photon': FieldExcitation('photon', ParticleType.BOSON, 0, 1, 0, None),
            'quark_u': FieldExcitation('up_quark', ParticleType.FERMION, 3.5e-30, 0.5, 2/3, 'RGB'),
            'quark_d': FieldExcitation('down_quark', ParticleType.FERMION, 7e-30, 0.5, -1/3, 'RGB'),
            'gluon': FieldExcitation('gluon', ParticleType.BOSON, 0, 1, 0, 'octet'),
            'higgs': FieldExcitation('higgs', ParticleType.BOSON, 2.23e-25, 0, 0, None),
            'w_boson': FieldExcitation('W_boson', ParticleType.BOSON, 1.43e-25, 1, 1, None),
            'z_boson': FieldExcitation('Z_boson', ParticleType.BOSON, 1.63e-25, 1, 0, None),
        }

    def create_excitation(self, field_name: str, energy: float) -> FieldExcitation:
        """Create a particle from a field with given energy."""
        if field_name in self.particles:
            return self.particles[field_name]
        return FieldExcitation(f"UNKNOWN_{field_name}", ParticleType.FERMION, 0, 0, 0, None)

    def calculate_propagator(self, particle: FieldExcitation, q_squared: float) -> Propagator:
        """
        Calculate the propagator amplitude for a virtual particle.
        For a massive particle: 1/(q² - m²c⁴ + iε)
        """
        m_c4 = (particle.mass * C ** 2) ** 2 if particle.mass > 0 else 0
        epsilon = 1e-10  # Infinitesimal regularization
        denominator = q_squared - m_c4 + 1j * epsilon
        amplitude = 1 / denominator if abs(denominator) > 0 else 0
        return Propagator(particle, q_squared, amplitude)

    def vertex_coupling(self, interaction: InteractionVertex) -> float:
        """Return the coupling constant for a given interaction."""
        couplings = {
            InteractionVertex.QED: math.sqrt(4 * math.pi * ALPHA_EM),  # ~0.303
            InteractionVertex.QCD: 1.0,  # Strong coupling (runs with energy)
            InteractionVertex.WEAK: 0.65,  # Weak coupling
            InteractionVertex.HIGGS: 0.5,  # Yukawa coupling (varies)
        }
        return couplings.get(interaction, 0.0)

    def feynman_amplitude(self, incoming: List[FieldExcitation], outgoing: List[FieldExcitation],
                          vertex: InteractionVertex) -> complex:
        """
        Calculate a simplified Feynman diagram amplitude.
        |M|² ∝ g² × (propagator terms)
        """
        g = self.vertex_coupling(vertex)
        
        # Simplified: count vertices and propagators
        n_vertices = min(len(incoming), len(outgoing))
        
        # Base amplitude
        amplitude = (g ** (2 * n_vertices)) * 1j
        
        return amplitude

    def cross_section(self, amplitude: complex, flux: float) -> float:
        """
        σ = |M|² / flux
        Cross-section from amplitude-squared.
        """
        return abs(amplitude) ** 2 / flux if flux > 0 else 0.0

    def renormalize(self, bare_value: float, cutoff: float, scale: float) -> float:
        """
        Simplified renormalization: absorb UV divergence into running coupling.
        g_ren = g_bare + (β₀/4π) × g³ × ln(Λ/μ)
        """
        if cutoff <= 0 or scale <= 0:
            return bare_value
        beta_0 = 0.5  # Simplified beta function coefficient
        log_factor = math.log(cutoff / scale)
        return bare_value * (1 + beta_0 * bare_value ** 2 * log_factor / (4 * math.pi))

    def vacuum_bubble(self) -> complex:
        """
        Zero-point energy contribution from vacuum fluctuations.
        Represents particle-antiparticle pairs popping in/out.
        """
        return complex(random.gauss(0, 0.01), random.gauss(0, 0.01))

# ==========================================
# SIMULATION
# ==========================================
if __name__ == "__main__":
    print("="*60)
    print("   ⛺  TENT v4.0  |  QUANTUM FIELD THEORY ENGINE")
    print("   PHASE 196: PARTICLES, FEYNMAN, RENORMALIZATION")
    print("="*60 + "\n")
    
    engine = QFTEngine()
    
    # 1. FIELD EXCITATIONS (Particles)
    print("--- STANDARD MODEL PARTICLES ---")
    for name, p in list(engine.particles.items())[:5]:
        print(f"   {p.name}: {p.particle_type.value}, spin={p.spin}, m={p.mass:.2e} kg")
    
    # 2. PROPAGATORS
    print("\n--- PROPAGATORS ---")
    electron = engine.particles['electron']
    photon = engine.particles['photon']
    prop_e = engine.calculate_propagator(electron, q_squared=1e-30)
    prop_γ = engine.calculate_propagator(photon, q_squared=1e-30)
    print(f"   Electron propagator: |A| = {abs(prop_e.amplitude):.4e}")
    print(f"   Photon propagator:   |A| = {abs(prop_γ.amplitude):.4e}")
    
    # 3. VERTEX COUPLINGS
    print("\n--- VERTEX COUPLINGS ---")
    for v in InteractionVertex:
        g = engine.vertex_coupling(v)
        print(f"   {v.value}: g = {g:.4f}")
    
    # 4. FEYNMAN AMPLITUDE (e⁻e⁻ → e⁻e⁻ via γ)
    print("\n--- FEYNMAN AMPLITUDE (e⁻e⁻ scattering) ---")
    amp = engine.feynman_amplitude([electron, electron], [electron, electron], InteractionVertex.QED)
    sigma = engine.cross_section(amp, flux=1.0)
    print(f"   Amplitude |M| = {abs(amp):.6f}")
    print(f"   Cross-section σ ∝ {sigma:.6f}")
    
    # 5. RENORMALIZATION
    print("\n--- RENORMALIZATION ---")
    bare_g = 0.3
    g_ren = engine.renormalize(bare_g, cutoff=1e19, scale=1e2)  # Planck to weak scale
    print(f"   Bare coupling:         g₀ = {bare_g:.4f}")
    print(f"   Renormalized coupling: g  = {g_ren:.4f}")
    
    # 6. VACUUM FLUCTUATIONS
    print("\n--- VACUUM FLUCTUATIONS ---")
    bubbles = [engine.vacuum_bubble() for _ in range(5)]
    print("   Sample zero-point fluctuations:")
    for i, b in enumerate(bubbles):
        print(f"   Ψ{i+1}: {b.real:.4f} + {b.imag:.4f}i")
    
    print("\n>> QUANTUM FIELD THEORY ENGINE OPERATIONAL.")
