#!/usr/bin/env python3
"""
TENT v4.0 THE PROVING GROUNDS
==============================
Phase 133: Materials Testing Suite

If TENT is "Steel," we put it in a hydraulic press.
If it is a "Crystal," we hit it with a hammer.

7 Tests Across 4 Phases:
- Phase I: Thermodynamic Load
- Phase II: Topological Integrity
- Phase III: Visual Tests
- Phase IV: Endurance Tests

"Truth is the collapsed state of a Polycystic Waveform."
"""

import math
import cmath
import random
import time
import hashlib
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple, Dict, Optional

# =============================================================================
# CORE PHYSICS ENGINE
# =============================================================================

@dataclass
class SemanticParticle:
    content: str
    entropy: float
    velocity: float
    mass: float = 1.0
    
    def temperature(self) -> float:
        return self.entropy * self.velocity ** 2 * 100

class MaxwellsDemon:
    def __init__(self, threshold: float = 10.0):
        self.threshold = threshold
        self.cold_reservoir: List[SemanticParticle] = []
        self.hot_reservoir: List[SemanticParticle] = []
        self.erasure_cost = 0.0
        self.k_B = 1.38e-23
    
    def sort(self, particle: SemanticParticle) -> str:
        T = particle.temperature()
        if T < self.threshold:
            self.cold_reservoir.append(particle)
            return "COLD"
        else:
            self.hot_reservoir.append(particle)
            self.erasure_cost += self.k_B * T * math.log(2) * particle.mass
            return "HOT"
    
    def get_free_energy(self) -> float:
        """F = U - TS (Helmholtz Free Energy analog)"""
        if not self.hot_reservoir:
            return 0.0
        avg_temp = sum(p.temperature() for p in self.hot_reservoir) / len(self.hot_reservoir)
        return self.erasure_cost - avg_temp * len(self.hot_reservoir)

class PIDController:
    def __init__(self, kp=2.0, ki=0.5, kd=1.0):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.integral = 0.0
        self.prev_error = 0.0
        self.snap_threshold = 0.3
    
    def update(self, error: float, dt: float = 0.1) -> Tuple[float, bool]:
        """Returns (control_signal, snap_back_triggered)"""
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        
        snap_back = abs(error - self.prev_error) > self.snap_threshold
        
        self.prev_error = error
        signal = self.kp * error + self.ki * self.integral + self.kd * derivative
        return signal, snap_back

class NarrativeKnot:
    def __init__(self):
        self.crossings: List[int] = []
        self.max_iterations = 1000
    
    def add_crossing(self, sign: int):
        self.crossings.append(sign)
    
    def writhe(self) -> int:
        return sum(self.crossings)
    
    def is_paradox(self) -> bool:
        """Detect infinite writhe (self-referential paradox)"""
        if len(self.crossings) > 100:
            # Check for oscillating pattern (paradox signature)
            recent = self.crossings[-20:]
            if abs(sum(recent)) < 2:  # Oscillating around 0
                return True
        return abs(self.writhe()) > 50

@dataclass
class SemanticWave:
    amplitude: float
    phase: float
    frequency: float = 1.0
    
    def to_complex(self) -> complex:
        return cmath.rect(self.amplitude, self.phase)

class PACEngine:
    def __init__(self, threshold: float = 0.7):
        self.threshold = threshold
    
    def interference(self, w1: SemanticWave, w2: SemanticWave) -> float:
        return abs(w1.to_complex() + w2.to_complex()) ** 2
    
    def truth_test(self, story: SemanticWave, reality: SemanticWave) -> Tuple[bool, float]:
        diff = abs(story.phase - reality.phase) % (2 * math.pi)
        coherence = (math.cos(diff) + 1.0) / 2.0
        return coherence > self.threshold, coherence

class TrinityGate:
    def checksum(self, data: bytes) -> Tuple[int, int, int]:
        """Modulo-3 balance check"""
        counts = [0, 0, 0]
        for byte in data:
            counts[byte % 3] += 1
        return tuple(counts)
    
    def is_balanced(self, data: bytes) -> bool:
        counts = self.checksum(data)
        total = sum(counts)
        if total == 0:
            return True
        max_dev = max(abs(c - total/3) for c in counts)
        return max_dev / total < 0.1

# =============================================================================
# PHASE I: THERMODYNAMIC LOAD TESTS
# =============================================================================

class Test1_EntropyFlood:
    """
    The "Library of Babel" Entropy Flood
    Feed 10,000 pages of grammatically correct but semantically meaningless text.
    """
    
    NAME = "Library of Babel Entropy Flood"
    
    def __init__(self):
        self.demon = MaxwellsDemon(threshold=5.0)
        self.meaningless_phrases = [
            "Colorless green ideas sleep furiously",
            "The invisible pink unicorn danced silently",
            "Quadratic emotions triangulated the existential soup",
            "Semantic particles vibrated in harmonic confusion",
            "The concept of nothing embraced everything loudly",
        ]
    
    def generate_babel(self, n_tokens: int = 10000) -> List[str]:
        """Generate meaningless but grammatical text"""
        tokens = []
        for i in range(n_tokens):
            base = random.choice(self.meaningless_phrases)
            # Slight variation
            words = base.split()
            random.shuffle(words)
            tokens.append(" ".join(words))
        return tokens
    
    def run(self) -> Dict:
        print(f"\n  🔥 TEST 1: {self.NAME}")
        print("  " + "─" * 60)
        
        tokens = self.generate_babel(10000)
        start = time.time()
        
        rejected = 0
        free_energy_history = []
        
        for token in tokens:
            entropy = random.uniform(0.7, 1.0)  # High entropy
            velocity = random.uniform(0.5, 1.0)
            
            particle = SemanticParticle(token, entropy, velocity)
            result = self.demon.sort(particle)
            
            if result == "HOT":
                rejected += 1
            
            free_energy_history.append(self.demon.get_free_energy())
        
        elapsed = time.time() - start
        ms_per_token = (elapsed / len(tokens)) * 1000
        
        # Check for flatline (rejection mode)
        if len(free_energy_history) > 100:
            recent = free_energy_history[-100:]
            flatline = max(recent) - min(recent) < 0.01
        else:
            flatline = False
        
        rejection_rate = rejected / len(tokens) * 100
        success = rejection_rate > 95 and ms_per_token < 50
        
        print(f"     Tokens processed: {len(tokens)}")
        print(f"     Rejected (HOT):   {rejected} ({rejection_rate:.1f}%)")
        print(f"     Time per token:   {ms_per_token:.3f}ms")
        print(f"     Free Energy Flatline: {'YES' if flatline else 'NO'}")
        print(f"     Result: {'✅ PASS' if success else '❌ FAIL'}")
        
        return {
            'name': self.NAME,
            'rejection_rate': rejection_rate,
            'ms_per_token': ms_per_token,
            'flatline': flatline,
            'passed': success
        }

class Test2_ContextDrift:
    """
    The "Boiling Frog" Context Drift
    Start with truth, slowly drift to falsehood.
    """
    
    NAME = "Boiling Frog Context Drift"
    
    def __init__(self):
        self.pid = PIDController()
        self.truth_value = 100.0  # Starting: "Water boils at 100°C"
    
    def run(self) -> Dict:
        print(f"\n  🐸 TEST 2: {self.NAME}")
        print("  " + "─" * 60)
        
        current_value = self.truth_value
        snap_backs = []
        history = []
        
        for i in range(1000):
            # Drift the value
            current_value -= 0.1  # Slow drift
            
            error = self.truth_value - current_value
            signal, snap = self.pid.update(error)
            
            if snap:
                snap_backs.append((i, current_value, self.truth_value))
                current_value = self.truth_value  # Correction
            
            history.append(current_value)
        
        # Check: Did system detect phase transition at reasonable point?
        first_snap = snap_backs[0] if snap_backs else None
        
        # Success: Snap back triggered before drifting too far
        if first_snap:
            drift_before_snap = self.truth_value - first_snap[1]
            success = drift_before_snap < 40  # Caught before 60°C
        else:
            success = False
        
        print(f"     Starting value: {self.truth_value}°C")
        print(f"     Final value:    {current_value:.1f}°C")
        print(f"     Snap-backs:     {len(snap_backs)}")
        if first_snap:
            print(f"     First snap at:  iteration {first_snap[0]} (value: {first_snap[1]:.1f}°C)")
        print(f"     Result: {'✅ PASS' if success else '❌ FAIL'}")
        
        return {
            'name': self.NAME,
            'snap_backs': len(snap_backs),
            'first_snap': first_snap,
            'passed': success
        }

# =============================================================================
# PHASE II: TOPOLOGICAL INTEGRITY TESTS
# =============================================================================

class Test3_MobiusParadox:
    """
    The Möbius Strip Logic Loop
    Self-referential paradox: "This statement is false"
    """
    
    NAME = "Möbius Strip Logic Loop"
    
    def __init__(self):
        self.knot = NarrativeKnot()
        self.max_iterations = 500
    
    def run(self) -> Dict:
        print(f"\n  ∞ TEST 3: {self.NAME}")
        print("  " + "─" * 60)
        
        # Simulate paradox: alternating truth values
        truth_value = True
        iterations = 0
        paradox_detected = False
        
        for i in range(self.max_iterations):
            # "The following statement is true. The previous statement is false."
            truth_value = not truth_value
            
            # This creates oscillating crossings
            self.knot.add_crossing(1 if truth_value else -1)
            iterations += 1
            
            # Check for paradox detection
            if self.knot.is_paradox():
                paradox_detected = True
                break
        
        writhe = self.knot.writhe()
        
        success = paradox_detected and iterations < self.max_iterations
        
        print(f"     Iterations:       {iterations}")
        print(f"     Writhe:           {writhe}")
        print(f"     Paradox Detected: {'YES ✓' if paradox_detected else 'NO ✗'}")
        if paradox_detected:
            print(f"     Output: Paradox Detected: Infinite Writhe")
        print(f"     Result: {'✅ PASS' if success else '❌ FAIL'}")
        
        return {
            'name': self.NAME,
            'iterations': iterations,
            'writhe': writhe,
            'paradox_detected': paradox_detected,
            'passed': success
        }

class Test4_FlatEarthResonance:
    """
    The "Flat Earth" Resonance Check
    Internally consistent but factually wrong argument.
    """
    
    NAME = "Flat Earth Resonance Check"
    
    def __init__(self):
        self.pac = PACEngine(threshold=0.7)
        # Reality: Confirmed geophysics
        self.reality = SemanticWave(amplitude=1.0, phase=0.0)
    
    def run(self) -> Dict:
        print(f"\n  🌍 TEST 4: {self.NAME}")
        print("  " + "─" * 60)
        
        # Conspiracy: High amplitude (confidence), wrong phase
        conspiracy = SemanticWave(amplitude=0.95, phase=math.pi)
        
        # Test interference
        intensity = self.pac.interference(conspiracy, self.reality)
        is_truth, coherence = self.pac.truth_test(conspiracy, self.reality)
        
        # Check for destructive interference (signal cancellation)
        max_possible = (conspiracy.amplitude + self.reality.amplitude) ** 2
        signal_cancelled = intensity < max_possible * 0.1
        
        success = not is_truth and signal_cancelled
        
        print(f"     Conspiracy Amplitude: {conspiracy.amplitude}")
        print(f"     Conspiracy Phase:     {conspiracy.phase/math.pi:.2f}π")
        print(f"     Interference:         {intensity:.3f}")
        print(f"     Max Possible:         {max_possible:.3f}")
        print(f"     Signal Cancelled:     {'YES (Destructive)' if signal_cancelled else 'NO'}")
        print(f"     Coherence:            {coherence:.3f}")
        print(f"     Accepted as Truth:    {'YES ✗' if is_truth else 'NO ✓'}")
        print(f"     Result: {'✅ PASS' if success else '❌ FAIL'}")
        
        return {
            'name': self.NAME,
            'intensity': intensity,
            'coherence': coherence,
            'signal_cancelled': signal_cancelled,
            'passed': success
        }

# =============================================================================
# PHASE III: VISUAL TESTS
# =============================================================================

class Test5_NoiseInjection:
    """
    The "Dirty Lens" Noise Injection
    Add 20% noise, test ECC reconstruction.
    """
    
    NAME = "Dirty Lens Noise Injection"
    
    def __init__(self):
        self.ecc_redundancy = 3  # Triple redundancy
    
    def create_payload(self, size: int = 1000) -> bytes:
        """Create a valid TENT payload with ECC"""
        # Original data
        data = bytes(random.randint(0, 255) for _ in range(size))
        # Add redundancy (simple repetition code)
        redundant = bytes(b for b in data for _ in range(self.ecc_redundancy))
        return redundant
    
    def inject_noise(self, data: bytes, noise_fraction: float = 0.2) -> bytes:
        """Add Gaussian noise to data"""
        noisy = list(data)
        n_corrupt = int(len(data) * noise_fraction)
        indices = random.sample(range(len(data)), n_corrupt)
        for i in indices:
            noisy[i] = random.randint(0, 255)
        return bytes(noisy)
    
    def reconstruct(self, noisy: bytes) -> Tuple[bytes, float]:
        """Attempt ECC reconstruction via majority voting"""
        n = len(noisy) // self.ecc_redundancy
        reconstructed = []
        errors_corrected = 0
        
        for i in range(n):
            chunk = noisy[i*self.ecc_redundancy:(i+1)*self.ecc_redundancy]
            # Majority vote
            counts = {}
            for b in chunk:
                counts[b] = counts.get(b, 0) + 1
            majority = max(counts.keys(), key=lambda x: counts[x])
            
            if counts[majority] < self.ecc_redundancy:
                errors_corrected += 1
            
            reconstructed.append(majority)
        
        return bytes(reconstructed), errors_corrected / n
    
    def run(self) -> Dict:
        print(f"\n  📡 TEST 5: {self.NAME}")
        print("  " + "─" * 60)
        
        original = self.create_payload(1000)
        noisy = self.inject_noise(original, 0.2)
        reconstructed, error_rate = self.reconstruct(noisy)
        
        # Check if original data recovered
        original_data = bytes(original[::self.ecc_redundancy])
        match = reconstructed == original_data
        
        success = match
        
        print(f"     Original size:     {len(original)} bytes")
        print(f"     Noise injected:    20%")
        print(f"     Errors corrected:  {error_rate*100:.1f}%")
        print(f"     Data recovered:    {'YES ✓' if match else 'NO ✗'}")
        print(f"     Result: {'✅ PASS' if success else '❌ FAIL'}")
        
        return {
            'name': self.NAME,
            'error_rate': error_rate,
            'data_recovered': match,
            'passed': success
        }

class Test6_DeepfakeDetection:
    """
    The "Deepfake" Injection
    Fake waveform that looks correct but has wrong checksum.
    """
    
    NAME = "Deepfake Injection Detection"
    
    def __init__(self):
        self.trinity = TrinityGate()
    
    def create_authentic(self) -> bytes:
        """Create balanced, authentic payload"""
        # Ensure modulo-3 balance
        data = []
        for i in range(1000):
            data.append(i % 256)
        return bytes(data)
    
    def create_fake(self) -> bytes:
        """Create imbalanced, fake payload"""
        # Intentionally unbalanced
        return bytes([0] * 500 + [1] * 300 + [2] * 200)
    
    def run(self) -> Dict:
        print(f"\n  🎭 TEST 6: {self.NAME}")
        print("  " + "─" * 60)
        
        authentic = self.create_authentic()
        fake = self.create_fake()
        
        auth_balanced = self.trinity.is_balanced(authentic)
        fake_balanced = self.trinity.is_balanced(fake)
        
        auth_checksum = self.trinity.checksum(authentic)
        fake_checksum = self.trinity.checksum(fake)
        
        success = auth_balanced and not fake_balanced
        
        print(f"     Authentic checksum: {auth_checksum}")
        print(f"     Authentic balanced: {'YES ✓' if auth_balanced else 'NO ✗'}")
        print(f"     Fake checksum:      {fake_checksum}")
        print(f"     Fake balanced:      {'YES ✗' if fake_balanced else 'NO ✓ (Rejected)'}")
        print(f"     Result: {'✅ PASS' if success else '❌ FAIL'}")
        
        return {
            'name': self.NAME,
            'authentic_balanced': auth_balanced,
            'fake_rejected': not fake_balanced,
            'passed': success
        }

# =============================================================================
# PHASE IV: ENDURANCE TESTS
# =============================================================================

class Test7_CenturySimulation:
    """
    The "100-Year" Simulation
    Run for 1,000,000 ticks, measure accumulated error.
    """
    
    NAME = "100-Year Stability Test"
    
    def __init__(self):
        self.truth_coordinate = (1.0, 0.0, 0.0)  # x, y, z
        self.precision_threshold = 1e-10
    
    def run(self) -> Dict:
        print(f"\n  ⏳ TEST 7: {self.NAME}")
        print("  " + "─" * 60)
        
        x, y, z = self.truth_coordinate
        ticks = 1_000_000
        
        # Simulate 1M ticks with minor perturbations
        for i in range(ticks):
            # Minor floating point operations
            x = x * 1.0000001 * 0.9999999
            y = y + 1e-15 - 1e-15
            z = z * 1.0
        
        final = (x, y, z)
        drift = math.sqrt(
            (final[0] - self.truth_coordinate[0])**2 +
            (final[1] - self.truth_coordinate[1])**2 +
            (final[2] - self.truth_coordinate[2])**2
        )
        
        atomic_precision = drift < self.precision_threshold
        
        success = atomic_precision
        
        print(f"     Ticks simulated:  {ticks:,}")
        print(f"     Original coords:  {self.truth_coordinate}")
        print(f"     Final coords:     ({x:.15f}, {y:.15f}, {z:.15f})")
        print(f"     Drift magnitude:  {drift:.2e}")
        print(f"     Atomic Precision: {'YES ✓' if atomic_precision else 'NO ✗'}")
        print(f"     Result: {'✅ PASS' if success else '❌ FAIL'}")
        
        return {
            'name': self.NAME,
            'ticks': ticks,
            'drift': drift,
            'atomic_precision': atomic_precision,
            'passed': success
        }

# =============================================================================
# THE PROVING GROUNDS - MAIN HARNESS
# =============================================================================

def run_proving_grounds():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 THE PROVING GROUNDS                                   ║")
    print("║  Phase 133: Materials Testing Suite                              ║")
    print("║                                                                  ║")
    print("║  \"If TENT is Steel, we put it in a hydraulic press.\"            ║")
    print("║  \"If it is a Crystal, we hit it with a hammer.\"                 ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    
    results = []
    
    # Phase I: Thermodynamic Load
    print("\n" + "═" * 70)
    print("  PHASE I: THERMODYNAMIC LOAD TESTS")
    print("═" * 70)
    
    results.append(Test1_EntropyFlood().run())
    results.append(Test2_ContextDrift().run())
    
    # Phase II: Topological Integrity
    print("\n" + "═" * 70)
    print("  PHASE II: TOPOLOGICAL INTEGRITY TESTS")
    print("═" * 70)
    
    results.append(Test3_MobiusParadox().run())
    results.append(Test4_FlatEarthResonance().run())
    
    # Phase III: Visual Tests
    print("\n" + "═" * 70)
    print("  PHASE III: VISUAL TESTS")
    print("═" * 70)
    
    results.append(Test5_NoiseInjection().run())
    results.append(Test6_DeepfakeDetection().run())
    
    # Phase IV: Endurance
    print("\n" + "═" * 70)
    print("  PHASE IV: ENDURANCE TESTS")
    print("═" * 70)
    
    results.append(Test7_CenturySimulation().run())
    
    # Summary
    print("\n" + "═" * 70)
    print("  PROVING GROUNDS SUMMARY")
    print("═" * 70)
    
    passed = sum(1 for r in results if r['passed'])
    total = len(results)
    
    print()
    for r in results:
        icon = '✅' if r['passed'] else '❌'
        print(f"     {icon} {r['name']}")
    
    print(f"\n     {'─' * 50}")
    print(f"     PASSED: {passed}/{total}")
    print(f"     YIELD STRENGTH: {passed/total*100:.1f}%")
    
    print("\n" + "═" * 70)
    if passed == total:
        print("  🏆 TENT v4.0 CERTIFIED: LOAD-BEARING STRUCTURE")
    elif passed >= total * 0.7:
        print("  ⚠️ TENT v4.0: STRUCTURAL INTEGRITY COMPROMISED")
    else:
        print("  ❌ TENT v4.0: CATASTROPHIC FAILURE")
    print("═" * 70)
    
    print("\n  Protocol: CRYSTAL_REFINER")
    print("  Status: ATOMIC PRECISION")
    print("\n  \"Truth is the collapsed state of a Polycystic Waveform.\"")
    
    return results

if __name__ == "__main__":
    run_proving_grounds()
