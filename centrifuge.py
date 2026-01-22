#!/usr/bin/env python3
"""
TENT v4.0 CENTRIFUGE
====================
Phase 165: The Separation Protocol

Like a physical centrifuge separates gold from sand:
- HEAVY (Truth): Sinks to the bottom (Center)
- LIGHT (Lies):  Floats to the top (Edges)

Input:  A "Dirty Sample" (mixed document with both Truth and Lies)
Output: Two distinct piles
  - Pile A: THE TRAP (Legal Truth, Iron Handcuffs)
  - Pile B: THE BAIT (Marketing Lies, Sweet Nothings)
"""

import re
from dataclasses import dataclass
from typing import List, Tuple

from sawmill import Sawmill
from grain_check import GrainCheck
from joinery import Joinery
from absorption_camera import AbsorptionCamera
from vacuum_gauge import VacuumGauge

# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class SentenceAnalysis:
    """Analysis of a single sentence."""
    text: str
    omega: float
    mass: float
    albedo: float
    is_heavy: bool  # True = Truth, False = Lie

@dataclass
class CentrifugeReport:
    """Result of the centrifuge separation."""
    original: str
    pile_a_trap: List[SentenceAnalysis]   # Heavy (Truth/Legal)
    pile_b_bait: List[SentenceAnalysis]   # Light (Lies/Marketing)
    separation_ratio: float                # % separated

# =============================================================================
# SAMPLE TERMS OF SERVICE
# =============================================================================

SAMPLE_TOS = """
We value your privacy and are committed to providing you with an amazing experience.
To better serve you, we may collect and share your personal information with third parties.
Your continued use of this service constitutes acceptance of binding arbitration.
We're always working to improve our services and make your life easier.
You waive your right to participate in class action lawsuits against us.
Our team is passionate about creating value for our community.
By using this service, you grant us an irrevocable, perpetual, worldwide license to your content.
We believe in transparency and putting our users first.
You agree to indemnify and hold us harmless from any claims arising from your use.
Join our family of millions of satisfied customers today!
"""

# =============================================================================
# THE CENTRIFUGE
# =============================================================================

class Centrifuge:
    """
    The Separation Engine.
    
    Spins a mixed document and physically separates:
    - The Iron Handcuffs (High Mass, Legal Truth)
    - The Sweet Nothings (High Albedo, Marketing Lies)
    """
    
    def __init__(self, threshold: float = 5.0):
        self.threshold = threshold  # Omega threshold for separation
        self.sawmill = Sawmill()
        self.grain = GrainCheck()
        self.joinery = Joinery()
        self.camera = AbsorptionCamera()
        self.vacuum = VacuumGauge()
    
    def _calculate_omega(self, text: str) -> Tuple[float, float, float]:
        """Calculate Omega score for a single sentence."""
        # Get metrics
        vacuum_report = self.vacuum.analyze(text)
        camera_report = self.camera.photograph(text)
        joinery_report = self.joinery.analyze(text)
        grain_report = self.grain.analyze_text(text)
        
        # Calculate components
        mass = max(0.1, vacuum_report.density_score)
        
        avg_fiber = sum(wa.fiber_length for wa in grain_report.word_analyses) / max(1, len(grain_report.word_analyses))
        history = avg_fiber / 100.0
        
        curvature = 1.0 - (joinery_report.average_strength / 100.0)
        curvature = max(0.01, curvature)
        
        albedo = camera_report.albedo
        albedo = max(0.01, albedo)
        
        # Omega = (M × H) / (K × A)
        omega = (mass * history) / (curvature * albedo)
        
        return omega, mass, albedo
    
    def spin(self, text: str) -> CentrifugeReport:
        """
        Spin a document through the centrifuge.
        
        Separates into Pile A (Heavy) and Pile B (Light).
        """
        # Split into sentences
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        pile_a = []  # Heavy (Truth)
        pile_b = []  # Light (Lies)
        
        for sentence in sentences:
            if len(sentence) < 10:
                continue
                
            omega, mass, albedo = self._calculate_omega(sentence)
            
            analysis = SentenceAnalysis(
                text=sentence,
                omega=omega,
                mass=mass,
                albedo=albedo,
                is_heavy=omega >= self.threshold,
            )
            
            if analysis.is_heavy:
                pile_a.append(analysis)
            else:
                pile_b.append(analysis)
        
        # Sort by omega
        pile_a.sort(key=lambda x: x.omega, reverse=True)
        pile_b.sort(key=lambda x: x.omega)
        
        total = len(pile_a) + len(pile_b)
        separation = len(pile_a) / total if total > 0 else 0
        
        return CentrifugeReport(
            original=text,
            pile_a_trap=pile_a,
            pile_b_bait=pile_b,
            separation_ratio=separation,
        )
    
    def display_report(self, report: CentrifugeReport):
        """Display the centrifuge separation results."""
        print()
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║  TENT v4.0 CENTRIFUGE - Separation Complete                          ║")
        print("╚══════════════════════════════════════════════════════════════════════╝")
        print()
        
        # Pile A: The Trap (Heavy/Truth)
        print("┌─────────────────────────────────────────────────────────────────────┐")
        print("│  🔩 PILE A: THE IRON HANDCUFFS (Legal Truth)                        │")
        print("│     These sank to the CENTER (High Mass)                            │")
        print("├─────────────────────────────────────────────────────────────────────┤")
        
        if not report.pile_a_trap:
            print("│  (Empty - No legal truths detected)")
        else:
            for i, s in enumerate(report.pile_a_trap, 1):
                # Truncate for display
                text = s.text[:60] + "..." if len(s.text) > 60 else s.text
                print(f"│  {i}. Ω={s.omega:.1f} │ \"{text}\"")
        
        print("└─────────────────────────────────────────────────────────────────────┘")
        print()
        
        # Pile B: The Bait (Light/Lies)
        print("┌─────────────────────────────────────────────────────────────────────┐")
        print("│  🎣 PILE B: THE SWEET NOTHINGS (Marketing Bait)                     │")
        print("│     These floated to the EDGES (High Albedo/Reflection)             │")
        print("├─────────────────────────────────────────────────────────────────────┤")
        
        if not report.pile_b_bait:
            print("│  (Empty - No marketing fluff detected)")
        else:
            for i, s in enumerate(report.pile_b_bait, 1):
                text = s.text[:60] + "..." if len(s.text) > 60 else s.text
                print(f"│  {i}. Ω={s.omega:.1f} │ \"{text}\"")
        
        print("└─────────────────────────────────────────────────────────────────────┘")
        print()
        
        # Statistics
        total = len(report.pile_a_trap) + len(report.pile_b_bait)
        trap_pct = len(report.pile_a_trap) / total * 100 if total > 0 else 0
        bait_pct = len(report.pile_b_bait) / total * 100 if total > 0 else 0
        
        print("╔═════════════════════════════════════════════════════════════════════╗")
        print("║  SEPARATION ANALYSIS                                                ║")
        print("╠═════════════════════════════════════════════════════════════════════╣")
        print(f"║  Total Sentences:    {total}")
        print(f"║  Pile A (TRAP):      {len(report.pile_a_trap)} ({trap_pct:.0f}%)")
        print(f"║  Pile B (BAIT):      {len(report.pile_b_bait)} ({bait_pct:.0f}%)")
        print("║")
        
        if report.pile_a_trap:
            avg_trap = sum(s.omega for s in report.pile_a_trap) / len(report.pile_a_trap)
            print(f"║  Avg Trap Ω:         {avg_trap:.1f} (HEAVY)")
        if report.pile_b_bait:
            avg_bait = sum(s.omega for s in report.pile_b_bait) / len(report.pile_b_bait)
            print(f"║  Avg Bait Ω:         {avg_bait:.1f} (LIGHT)")
        
        print("╠═════════════════════════════════════════════════════════════════════╣")
        print("║  ⚠️  THE TRAP IS WHAT MATTERS. THE BAIT IS DISTRACTION.             ║")
        print("╚═════════════════════════════════════════════════════════════════════╝")

# =============================================================================
# DEMO
# =============================================================================

def demo():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 CENTRIFUGE DEMONSTRATION                              ║")
    print("║  Phase 165: The Separation Protocol                              ║")
    print("║                                                                  ║")
    print("║  \"Spin the dirty sample. Watch the layers separate.\"            ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print()
    print("INPUT: Corporate Terms of Service (Mixed Sample)")
    print("-" * 70)
    print(SAMPLE_TOS)
    print("-" * 70)
    print()
    print("🔄 SPINNING CENTRIFUGE...")
    print()
    
    centrifuge = Centrifuge(threshold=3.0)
    report = centrifuge.spin(SAMPLE_TOS)
    centrifuge.display_report(report)

if __name__ == "__main__":
    demo()
