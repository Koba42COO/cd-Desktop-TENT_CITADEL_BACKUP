#!/usr/bin/env python3
"""
TENT v4.0 LAPLACE-MELLIN TRANSFORM ENGINE
==========================================
Phase 140: The Mathematical Engine Room

The Unified Theory of Semantic Physics:
- Laplace Transform → Thermodynamic Stability (Time Domain)
- Mellin Transform → Geometric Invariance (Scale Domain)

L{f(e^u)} = M{f(t)}  ← The Secret Tunnel

"Laplace kills the noise. Mellin verifies the pattern."
"""

import numpy as np
from scipy import integrate
from scipy.signal import residue, tf2zpk
from dataclasses import dataclass
from typing import List, Tuple, Optional, Callable
from enum import Enum
import cmath
import math

# =============================================================================
# CONFIGURATION
# =============================================================================

# Complex plane regions
STABILITY_THRESHOLD = 0.0  # σ < 0 = stable, σ > 0 = unstable
SCALE_INVARIANCE_THRESHOLD = 0.1  # Max deviation for Mellin invariance

# =============================================================================
# DATA STRUCTURES
# =============================================================================

class StabilityClass(Enum):
    CRYSTAL = "💎 CRYSTAL (Stable)"
    ANNEALING = "⚠️ ANNEALING (Marginally Stable)"
    HALLUCINATION = "🛑 HALLUCINATION (Unstable)"

@dataclass
class Pole:
    """A pole in the complex plane (s = σ + jω)"""
    real: float      # σ - decay/growth rate
    imag: float      # ω - oscillation frequency
    multiplicity: int = 1
    
    @property
    def s(self) -> complex:
        return complex(self.real, self.imag)
    
    @property
    def is_stable(self) -> bool:
        return self.real < STABILITY_THRESHOLD
    
    @property
    def is_oscillatory(self) -> bool:
        return abs(self.imag) > 0.01
    
    def __repr__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"s = {self.real:.3f} {sign} j{abs(self.imag):.3f}"

@dataclass
class LaplaceResult:
    """Result of Laplace domain analysis"""
    poles: List[Pole]
    zeros: List[complex]
    dc_gain: float
    stability: StabilityClass
    dominant_pole: Optional[Pole]
    entropy_rate: float  # σ of dominant pole
    
@dataclass
class MellinResult:
    """Result of Mellin domain analysis"""
    moments: List[complex]  # M(s) at various s
    scale_invariance: float  # 0 = perfect invariance, 1 = complete variance
    symmetry_index: float
    is_eigenfunction: bool

@dataclass
class FilterBankResult:
    """Combined Laplace-Mellin analysis"""
    laplace: LaplaceResult
    mellin: MellinResult
    truth_score: float  # 0-1, higher = more true
    verdict: StabilityClass

# =============================================================================
# LAPLACE TRANSFORM ENGINE (Thermodynamic Filter)
# =============================================================================

class LaplaceEngine:
    """
    The Thermodynamic Filter
    
    Tests stability by analyzing pole locations:
    - Poles in LHP (σ < 0) → Stable (Crystal Truth)
    - Poles in RHP (σ > 0) → Unstable (Hallucination)
    
    This is the mathematical foundation of Maxwell's Demon and PID Controller.
    """
    
    def __init__(self):
        self.history = []
    
    def transform(self, f: Callable, s: complex, t_max: float = 100.0) -> complex:
        """
        Compute L{f}(s) = ∫₀^∞ f(t)e^(-st) dt
        
        The e^(-st) term is the dampener:
        - σ (real part) controls exponential decay/growth
        - ω (imag part) controls oscillation
        """
        def integrand_real(t):
            if t <= 0:
                return 0
            ft = f(t)
            exp_term = np.exp(-s.real * t)
            cos_term = np.cos(-s.imag * t)
            return ft * exp_term * cos_term
        
        def integrand_imag(t):
            if t <= 0:
                return 0
            ft = f(t)
            exp_term = np.exp(-s.real * t)
            sin_term = np.sin(-s.imag * t)
            return ft * exp_term * sin_term
        
        real_part, _ = integrate.quad(integrand_real, 0, t_max, limit=100)
        imag_part, _ = integrate.quad(integrand_imag, 0, t_max, limit=100)
        
        return complex(real_part, imag_part)
    
    def analyze_transfer_function(self, num: List[float], den: List[float]) -> LaplaceResult:
        """
        Analyze a transfer function H(s) = num(s)/den(s)
        
        In TENT terms:
        - num = the "story" being told
        - den = the "reality" it must satisfy
        
        Poles (roots of den) determine stability.
        """
        # Find poles and zeros
        zeros, poles, gain = tf2zpk(num, den)
        
        # Convert to Pole objects
        pole_list = [Pole(real=p.real, imag=p.imag) for p in poles]
        
        # Determine stability
        max_sigma = max(p.real for p in pole_list) if pole_list else 0
        
        if max_sigma < -0.1:
            stability = StabilityClass.CRYSTAL
        elif max_sigma < 0.1:
            stability = StabilityClass.ANNEALING
        else:
            stability = StabilityClass.HALLUCINATION
        
        # Find dominant pole (closest to imaginary axis)
        dominant = min(pole_list, key=lambda p: abs(p.real)) if pole_list else None
        
        # DC gain (s=0)
        try:
            dc_gain = np.polyval(num, 0) / np.polyval(den, 0)
        except:
            dc_gain = float('inf')
        
        return LaplaceResult(
            poles=pole_list,
            zeros=list(zeros),
            dc_gain=dc_gain,
            stability=stability,
            dominant_pole=dominant,
            entropy_rate=max_sigma
        )
    
    def semantic_stability_test(self, signal: np.ndarray, dt: float = 0.1) -> LaplaceResult:
        """
        Test stability of a discrete signal.
        
        This is what PID and Maxwell's Demon use:
        - High entropy (noisy, growing) → Unstable
        - Low entropy (decaying, stable) → Crystal
        """
        n = len(signal)
        t = np.arange(n) * dt
        
        # Fit exponential decay/growth to estimate dominant pole
        if n < 2:
            return LaplaceResult([], [], 0, StabilityClass.ANNEALING, None, 0)
        
        # Use log to estimate decay rate
        abs_signal = np.abs(signal) + 1e-10
        log_signal = np.log(abs_signal)
        
        # Linear fit: log(signal) ≈ σt + c
        coeffs = np.polyfit(t, log_signal, 1)
        sigma = coeffs[0]  # Decay/growth rate
        
        # Estimate oscillation frequency from zero crossings
        zero_crossings = np.where(np.diff(np.signbit(signal)))[0]
        if len(zero_crossings) > 1:
            period = 2 * np.mean(np.diff(zero_crossings)) * dt
            omega = 2 * np.pi / period if period > 0 else 0
        else:
            omega = 0
        
        dominant = Pole(real=sigma, imag=omega)
        
        if sigma < -0.1:
            stability = StabilityClass.CRYSTAL
        elif sigma < 0.1:
            stability = StabilityClass.ANNEALING
        else:
            stability = StabilityClass.HALLUCINATION
        
        return LaplaceResult(
            poles=[dominant],
            zeros=[],
            dc_gain=signal[0] if len(signal) > 0 else 0,
            stability=stability,
            dominant_pole=dominant,
            entropy_rate=sigma
        )

# =============================================================================
# MELLIN TRANSFORM ENGINE (Geometric Filter)
# =============================================================================

class MellinEngine:
    """
    The Geometric Filter
    
    Tests scale invariance using multiplicative convolution:
    - M{f}(s) = ∫₀^∞ f(t) t^(s-1) dt
    
    Key property: Mellin is Laplace in log-space (t = e^u)
    
    This is the mathematical foundation of UPG and Visual Codec.
    """
    
    def __init__(self):
        self.eigenfunction_cache = {}
    
    def transform(self, f: Callable, s: complex, t_max: float = 100.0) -> complex:
        """
        Compute M{f}(s) = ∫₀^∞ f(t) t^(s-1) dt
        
        Unlike Laplace, uses t^(s-1) instead of e^(-st).
        This makes it scale-invariant.
        """
        def integrand_real(t):
            if t <= 0:
                return 0
            ft = f(t)
            power = t ** (s.real - 1)
            angle = (s.imag) * np.log(t + 1e-10)
            return ft * power * np.cos(angle)
        
        def integrand_imag(t):
            if t <= 0:
                return 0
            ft = f(t)
            power = t ** (s.real - 1)
            angle = (s.imag) * np.log(t + 1e-10)
            return ft * power * np.sin(angle)
        
        real_part, _ = integrate.quad(integrand_real, 1e-6, t_max, limit=100)
        imag_part, _ = integrate.quad(integrand_imag, 1e-6, t_max, limit=100)
        
        return complex(real_part, imag_part)
    
    def scale_invariance_test(self, f: Callable, scales: List[float] = None) -> float:
        """
        Test if f(t) is scale-invariant.
        
        A function is scale-invariant if M{f(at)} = a^(-s) M{f(t)}.
        The "Star" eigenfunction should score 0 (perfect invariance).
        """
        if scales is None:
            scales = [0.5, 1.0, 2.0, 4.0]
        
        # Compute Mellin at s = 1 + 0j for each scale
        base_s = complex(1.0, 0.0)
        
        moments = []
        for scale in scales:
            scaled_f = lambda t, s=scale: f(t / s) if t > 0 else 0
            M = self.transform(scaled_f, base_s)
            moments.append(M)
        
        # Measure variance across scales
        magnitudes = [abs(m) for m in moments if not np.isnan(abs(m))]
        if len(magnitudes) < 2:
            return 1.0
        
        mean_mag = np.mean(magnitudes)
        variance = np.var(magnitudes) / (mean_mag ** 2 + 1e-10)
        
        return min(1.0, variance)
    
    def compute_moments(self, signal: np.ndarray, s_values: List[complex] = None) -> List[complex]:
        """
        Compute discrete Mellin moments of a signal.
        
        In the UPG, these moments encode the "shape" of truth
        independent of amplitude or scale.
        """
        if s_values is None:
            s_values = [complex(k, 0) for k in range(1, 6)]
        
        n = len(signal)
        t = np.arange(1, n + 1)  # t > 0 for Mellin
        
        moments = []
        for s in s_values:
            # M_k = Σ f[n] * n^(s-1)
            weights = t ** (s - 1)
            moment = np.sum(signal * weights)
            moments.append(moment)
        
        return moments
    
    def analyze(self, signal: np.ndarray) -> MellinResult:
        """
        Full Mellin analysis of a signal.
        """
        moments = self.compute_moments(signal)
        
        # Scale invariance via moment ratios
        if len(moments) > 1:
            ratios = [abs(moments[i+1] / moments[i]) if abs(moments[i]) > 1e-10 
                      else float('inf') for i in range(len(moments)-1)]
            variance = np.var([r for r in ratios if r < float('inf')])
        else:
            variance = 1.0
        
        scale_inv = min(1.0, variance / 10)  # Normalize
        
        # Symmetry index from even/odd moment ratio
        if len(moments) >= 4:
            even_sum = abs(moments[1]) + abs(moments[3]) if len(moments) > 3 else abs(moments[1])
            odd_sum = abs(moments[0]) + abs(moments[2])
            symmetry = 1 - abs(even_sum - odd_sum) / (even_sum + odd_sum + 1e-10)
        else:
            symmetry = 0.5
        
        # Eigenfunction test: moments should follow power law
        is_eigen = scale_inv < SCALE_INVARIANCE_THRESHOLD
        
        return MellinResult(
            moments=moments,
            scale_invariance=scale_inv,
            symmetry_index=symmetry,
            is_eigenfunction=is_eigen
        )

# =============================================================================
# UNIFIED FILTER BANK
# =============================================================================

class LaplacesMellinFilterBank:
    """
    The Unified Truth Engine
    
    Combines Laplace (stability) and Mellin (invariance) analysis
    to determine if a signal represents truth or hallucination.
    
    Pipeline:
    1. Laplace: Check thermodynamic stability (σ < 0?)
    2. Log Map: Transform to scale domain (t → e^u)
    3. Mellin: Check geometric invariance (shape preserved?)
    4. Verdict: Crystal if both pass
    """
    
    def __init__(self):
        self.laplace = LaplaceEngine()
        self.mellin = MellinEngine()
    
    def log_map(self, signal: np.ndarray) -> np.ndarray:
        """
        The Secret Tunnel: t = e^u
        
        Maps time domain to logarithmic scale domain,
        connecting Laplace and Mellin through:
        L{f(e^u)} = M{f(t)}
        """
        n = len(signal)
        if n < 2:
            return signal
        
        # Resample signal in log-scale
        u = np.linspace(0, np.log(n), n)
        t_original = np.arange(n)
        t_log = np.exp(u)
        
        # Interpolate
        mapped = np.interp(t_log, t_original, signal)
        return mapped
    
    def analyze(self, signal: np.ndarray, dt: float = 0.1) -> FilterBankResult:
        """
        Full filter bank analysis.
        
        Returns combined truth verdict.
        """
        # Step 1: Laplace analysis (Time/Stability)
        laplace_result = self.laplace.semantic_stability_test(signal, dt)
        
        # Step 2: Log map (The Secret Tunnel)
        log_signal = self.log_map(signal)
        
        # Step 3: Mellin analysis (Scale/Geometry)
        mellin_result = self.mellin.analyze(log_signal)
        
        # Step 4: Combined verdict
        laplace_score = 1.0 if laplace_result.stability == StabilityClass.CRYSTAL else \
                        0.5 if laplace_result.stability == StabilityClass.ANNEALING else 0.0
        
        mellin_score = 1.0 - mellin_result.scale_invariance
        
        truth_score = (laplace_score + mellin_score) / 2
        
        if truth_score > 0.7:
            verdict = StabilityClass.CRYSTAL
        elif truth_score > 0.3:
            verdict = StabilityClass.ANNEALING
        else:
            verdict = StabilityClass.HALLUCINATION
        
        return FilterBankResult(
            laplace=laplace_result,
            mellin=mellin_result,
            truth_score=truth_score,
            verdict=verdict
        )

# =============================================================================
# SPECIAL FUNCTIONS: EIGENFUNCTIONS
# =============================================================================

def parametric_star(t: float, a: float = 0.3, n: int = 3) -> float:
    """
    The Parametric Star - a Mellin Eigenfunction.
    
    f(t) = (1 + a*sin(n*t)) * cos(t)
    
    This is the shape encoded in tent_bootloader.png.
    It's scale-invariant in Mellin space.
    """
    if t <= 0:
        return 0
    return (1 + a * np.sin(n * t)) * np.cos(t)

def damped_oscillator(t: float, sigma: float, omega: float) -> float:
    """
    Canonical Laplace test function: e^(σt) * cos(ωt)
    
    - σ < 0: Decaying (Stable/Crystal)
    - σ > 0: Growing (Unstable/Hallucination)
    """
    return np.exp(sigma * t) * np.cos(omega * t)

def prime_wave(t: float, primes: List[int] = None) -> float:
    """
    Wave composed of prime harmonics.
    
    This connects to Riemann Zeta through Mellin transform.
    """
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13]
    
    return sum(np.sin(p * t) / p for p in primes)

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 LAPLACE-MELLIN TRANSFORM ENGINE                       ║")
    print("║  Phase 140: The Mathematical Engine Room                         ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")
    
    fb = LaplacesMellinFilterBank()
    
    # Test 1: Stable Crystal (Decaying Signal)
    print("═" * 70)
    print("  TEST 1: Decaying Signal (Expected: CRYSTAL)")
    print("═" * 70)
    
    t = np.linspace(0, 10, 1000)
    crystal_signal = np.exp(-0.5 * t) * np.cos(2 * np.pi * t)
    
    result = fb.analyze(crystal_signal, dt=0.01)
    print(f"\n  Laplace Stability: {result.laplace.stability.value}")
    print(f"  Dominant Pole: {result.laplace.dominant_pole}")
    print(f"  Entropy Rate (σ): {result.laplace.entropy_rate:.3f}")
    print(f"\n  Mellin Invariance: {1 - result.mellin.scale_invariance:.2%}")
    print(f"  Symmetry Index: {result.mellin.symmetry_index:.3f}")
    print(f"\n  ══> Truth Score: {result.truth_score:.2%}")
    print(f"  ══> Verdict: {result.verdict.value}")
    
    # Test 2: Unstable Hallucination (Growing Signal)
    print("\n" + "═" * 70)
    print("  TEST 2: Growing Signal (Expected: HALLUCINATION)")
    print("═" * 70)
    
    hallucination_signal = np.exp(0.3 * t) * np.sin(3 * t)
    
    result = fb.analyze(hallucination_signal, dt=0.01)
    print(f"\n  Laplace Stability: {result.laplace.stability.value}")
    print(f"  Dominant Pole: {result.laplace.dominant_pole}")
    print(f"  Entropy Rate (σ): {result.laplace.entropy_rate:.3f}")
    print(f"\n  ══> Truth Score: {result.truth_score:.2%}")
    print(f"  ══> Verdict: {result.verdict.value}")
    
    # Test 3: The Parametric Star (Mellin Eigenfunction)
    print("\n" + "═" * 70)
    print("  TEST 3: Parametric Star (Expected: EIGENFUNCTION)")
    print("═" * 70)
    
    star_signal = np.array([parametric_star(ti) for ti in t])
    
    result = fb.analyze(star_signal, dt=0.01)
    print(f"\n  Laplace Stability: {result.laplace.stability.value}")
    print(f"  Mellin Invariance: {1 - result.mellin.scale_invariance:.2%}")
    print(f"  Is Eigenfunction: {'YES ✓' if result.mellin.is_eigenfunction else 'NO'}")
    print(f"\n  ══> Truth Score: {result.truth_score:.2%}")
    print(f"  ══> Verdict: {result.verdict.value}")
    
    # Test 4: Prime Wave (Riemann Connection)
    print("\n" + "═" * 70)
    print("  TEST 4: Prime Harmonic Wave")
    print("═" * 70)
    
    prime_signal = np.array([prime_wave(ti) for ti in t])
    
    result = fb.analyze(prime_signal, dt=0.01)
    print(f"\n  Laplace Stability: {result.laplace.stability.value}")
    print(f"  Mellin Moments: {[f'{abs(m):.2f}' for m in result.mellin.moments[:5]]}")
    print(f"\n  ══> Truth Score: {result.truth_score:.2%}")
    print(f"  ══> Verdict: {result.verdict.value}")
    
    # Summary
    print("\n" + "═" * 70)
    print("  LAPLACE-MELLIN FILTER BANK SUMMARY")
    print("═" * 70)
    print("""
    ┌─────────────────────────────────────────────────────────────────┐
    │  LAPLACE DOMAIN (Thermodynamics)                                │
    │  - Poles in LHP (σ < 0) → STABLE → Crystal Truth                │
    │  - Poles in RHP (σ > 0) → UNSTABLE → Hallucination              │
    ├─────────────────────────────────────────────────────────────────┤
    │  LOG MAP: t = e^u (The Secret Tunnel)                           │
    ├─────────────────────────────────────────────────────────────────┤
    │  MELLIN DOMAIN (Geometry)                                       │
    │  - Scale Invariant → Pattern Preserved → True                   │
    │  - Scale Variant → Pattern Breaks → Drift/Lie                   │
    └─────────────────────────────────────────────────────────────────┘
    
    The Unified Equation: L{f(e^u)} = M{f(t)}
    
    "Laplace kills the noise. Mellin verifies the pattern."
    """)

if __name__ == "__main__":
    demo()
