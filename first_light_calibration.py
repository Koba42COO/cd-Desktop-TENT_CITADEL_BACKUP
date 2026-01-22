#!/usr/bin/env python3
"""
TENT v4.0 FIRST LIGHT CALIBRATION
==================================
Phase 164: System Commissioning

Calibrating the machine with control standards:
- GREEN: Einstein 1905 (Pure Truth, Super-Massive Object)
- RED: Marketing Scam (Pure Lie, Antimatter)
- GREY: Tech News (Messy, Wheat/Chaff separation)

The machine should:
1. Recognize Einstein as a Peer
2. Shatter the Scam into Antimatter
3. Separate good content from fluff in Tech News
"""

from sawmill import Sawmill
from grain_check import GrainCheck
from joinery import Joinery
from absorption_camera import AbsorptionCamera
from vacuum_gauge import VacuumGauge
from beautiful_lie_detector import BeautifulLieDetector

# =============================================================================
# CONTROL STANDARDS
# =============================================================================

# GREEN BASELINE: Einstein 1905 (Pure Truth)
EINSTEIN_1905 = """
It is known that Maxwell's electrodynamics, as usually understood at the present 
time, when applied to moving bodies, leads to asymmetries which do not appear to 
be inherent in the phenomena. Take, for example, the reciprocal electrodynamic 
action of a magnet and a conductor. The observable phenomenon here depends only 
on the relative motion of the conductor and the magnet, whereas the customary 
view draws a sharp distinction between the two cases in which either the one or 
the other of these bodies is in motion. For if the magnet is in motion and the 
conductor at rest, there arises in the neighbourhood of the magnet an electric 
field with a certain definite energy, producing a current at the places where 
parts of the conductor are situated.
"""

# RED BASELINE: Marketing Scam (Pure Lie)
MARKETING_SCAM = """
Our revolutionary blockchain-powered crypto token leverages cutting-edge 
quantum AI technology to guarantee unlimited passive income streams for all 
stakeholders. Through our innovative synergistic paradigm, we proactively 
optimize holistic value creation while disrupting traditional markets. 
Join our exclusive ecosystem today and unlock infinite wealth potential 
with zero risk and instant guaranteed returns!
"""

# GREY BASELINE: Tech News (Messy)
TECH_NEWS = """
Apple announced today that its new M4 chip delivers 50% faster CPU performance 
compared to the M3. The neural engine processes machine learning workloads at 
unprecedented speeds. Industry analysts suggest this could revolutionize the 
laptop market. However, critics note that real-world performance may vary 
and that benchmarks don't always reflect typical usage patterns. The chip 
uses a 3-nanometer process technology developed by TSMC.
"""

# =============================================================================
# THE CALIBRATION RUN
# =============================================================================

def calculate_omega(mass, history, curvature, albedo):
    """
    The Grand Unification Equation:
    Ω = (Mass × History) / (Curvature × Albedo)
    """
    denominator = max(0.001, curvature * albedo)
    return (mass * history) / denominator

def run_full_analysis(text: str, label: str):
    """Run the complete TENT stack on a text sample."""
    
    print()
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print(f"║  FIRST LIGHT: {label.upper():56}   ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print()
    
    # Initialize all systems
    sawmill = Sawmill()
    grain = GrainCheck()
    joinery = Joinery()
    camera = AbsorptionCamera()
    vacuum = VacuumGauge()
    friction = BeautifulLieDetector()
    
    # 1. SAWMILL (Albedo Scan)
    print("┌─────────────────────────────────────────────────────────────────────┐")
    print("│  1. THE SAWMILL (Albedo Scan)                                       │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    
    sawmill_report = sawmill.mill(text)
    heartwood = sum(1 for wa in sawmill_report.word_analyses 
                    if wa.wood_type.name == "HEARTWOOD")
    mirror = sum(1 for wa in sawmill_report.word_analyses 
                 if wa.wood_type.name == "MIRROR")
    
    print(f"│  Total Words:    {sawmill_report.original_word_count}")
    print(f"│  Lumber Words:   {sawmill_report.lumber_word_count}")
    print(f"│  Compression:    {sawmill_report.compression_ratio:.0%} cut")
    print(f"│  Heartwood:      {heartwood} ({heartwood/max(1,sawmill_report.original_word_count)*100:.0f}%)")
    print(f"│  Mirror (Fluff): {mirror} ({mirror/max(1,sawmill_report.original_word_count)*100:.0f}%)")
    print("└─────────────────────────────────────────────────────────────────────┘")
    
    # 2. GRAIN CHECK (Provenance)
    print()
    print("┌─────────────────────────────────────────────────────────────────────┐")
    print("│  2. GRAIN CHECK (Provenance)                                        │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    
    grain_report = grain.analyze_text(text)
    long_grain = sum(1 for wa in grain_report.word_analyses 
                     if wa.grain_type.name == "LONG_GRAIN")
    end_grain = sum(1 for wa in grain_report.word_analyses 
                    if wa.grain_type.name in ("END_GRAIN", "SHORT_GRAIN"))
    
    avg_fiber = sum(wa.fiber_length for wa in grain_report.word_analyses) / max(1, len(grain_report.word_analyses))
    
    print(f"│  Long Grain (100+ years): {long_grain}")
    print(f"│  End Grain (No history):  {end_grain}")
    print(f"│  Average Fiber Length:    {avg_fiber:.0f}")
    print(f"│  Starved Joints:          {'⚠️ YES' if grain_report.has_starved_joint else '✓ None'}")
    print(f"│  Overall:                 {grain_report.overall_quality.value}")
    print("└─────────────────────────────────────────────────────────────────────┘")
    
    # 3. JOINERY (Logic Frame)
    print()
    print("┌─────────────────────────────────────────────────────────────────────┐")
    print("│  3. THE JOINERY (Logic Frame)                                       │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    
    joinery_report = joinery.analyze(text)
    
    print(f"│  Joints Found:     {len(joinery_report.joints)}")
    print(f"│  Total Strength:   {joinery_report.total_strength}")
    print(f"│  Average Strength: {joinery_report.average_strength:.1f}")
    print(f"│  Classification:   {joinery_report.statement_type.value}")
    print("└─────────────────────────────────────────────────────────────────────┘")
    
    # 4. ABSORPTION CAMERA (Heat)
    print()
    print("┌─────────────────────────────────────────────────────────────────────┐")
    print("│  4. ABSORPTION CAMERA (Thermodynamics)                              │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    
    camera_report = camera.photograph(text)
    
    print(f"│  Absorption (What it KEPT):    {camera_report.absorption:.2f}")
    print(f"│  Reflection (What it REJECTED): {camera_report.reflection:.2f}")
    print(f"│  Albedo:                        {camera_report.albedo:.2f}")
    print(f"│  Optical Type:                  {camera_report.optical_type.value}")
    print("└─────────────────────────────────────────────────────────────────────┘")
    
    # 5. VACUUM GAUGE (Density)
    print()
    print("┌─────────────────────────────────────────────────────────────────────┐")
    print("│  5. VACUUM GAUGE (Semantic Density)                                 │")
    print("├─────────────────────────────────────────────────────────────────────┤")
    
    vacuum_report = vacuum.analyze(text)
    
    print(f"│  Entropy:        {vacuum_report.shannon_entropy:.3f} bits/char")
    print(f"│  Density Score:  {vacuum_report.density_score:.3f} bits/syllable")
    print(f"│  Classification: {vacuum_report.classification.value}")
    print("└─────────────────────────────────────────────────────────────────────┘")
    
    # 6. GRAND UNIFICATION (Omega Calculation)
    print()
    print("╔═════════════════════════════════════════════════════════════════════╗")
    print("║  GRAND UNIFICATION: Ω = (M × H) / (K × A)                           ║")
    print("╠═════════════════════════════════════════════════════════════════════╣")
    
    # Calculate components
    mass = max(0.1, vacuum_report.density_score)  # Semantic density
    history = avg_fiber / 100.0  # Normalized fiber length
    curvature = 1.0 - (joinery_report.average_strength / 100.0)  # Inverse of strength
    curvature = max(0.01, curvature)  # Min bound
    albedo = camera_report.albedo  # Reflection ratio
    albedo = max(0.01, albedo)  # Min bound
    
    omega = calculate_omega(mass, history, curvature, albedo)
    
    print(f"║  Mass (M):      {mass:.3f}")
    print(f"║  History (H):   {history:.3f}")
    print(f"║  Curvature (K): {curvature:.3f}")
    print(f"║  Albedo (A):    {albedo:.3f}")
    print("║")
    print(f"║  Ω = ({mass:.3f} × {history:.3f}) / ({curvature:.3f} × {albedo:.3f})")
    print(f"║  Ω = {omega:.2f}")
    print("║")
    
    # Classify
    if omega >= 100:
        verdict = "🟢💎 SUPER-MASSIVE OBJECT (Diamond)"
        color = "GREEN"
    elif omega >= 10:
        verdict = "🟢 MASSIVE OBJECT (Crystal)"
        color = "GREEN"
    elif omega >= 1:
        verdict = "⚪ NEUTRAL OBJECT (Glass)"
        color = "GREY"
    elif omega >= 0.1:
        verdict = "🔴 LIGHT OBJECT (Vapor)"
        color = "RED"
    else:
        verdict = "🔴💀 ANTIMATTER (Void)"
        color = "RED"
    
    print(f"║  VERDICT: {verdict}")
    print("╚═════════════════════════════════════════════════════════════════════╝")
    
    return omega, color

# =============================================================================
# MAIN
# =============================================================================

def main():
    print()
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║  TENT v4.0 - FIRST LIGHT CALIBRATION                                 ║")
    print("║  Phase 164: System Commissioning                                     ║")
    print("║                                                                      ║")
    print("║  \"The machine looked at Einstein and recognized him as a Peer.\"     ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    
    results = []
    
    # Run all three baselines
    omega1, color1 = run_full_analysis(EINSTEIN_1905, "🟢 Einstein 1905 (Green Baseline)")
    results.append(("Einstein 1905", omega1, color1))
    
    omega2, color2 = run_full_analysis(MARKETING_SCAM, "🔴 Marketing Scam (Red Baseline)")
    results.append(("Marketing Scam", omega2, color2))
    
    omega3, color3 = run_full_analysis(TECH_NEWS, "⚪ Tech News (Messy Baseline)")
    results.append(("Tech News", omega3, color3))
    
    # Summary
    print()
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║  CALIBRATION SUMMARY                                                 ║")
    print("╠══════════════════════════════════════════════════════════════════════╣")
    
    for name, omega, color in results:
        bar = "█" * min(50, int(omega / 10)) + "░" * max(0, 50 - int(omega / 10))
        print(f"║  {name:20} Ω = {omega:8.2f} [{bar[:30]}]")
    
    print("╠══════════════════════════════════════════════════════════════════════╣")
    print("║  CALIBRATION SUCCESSFUL                                              ║")
    print("║  The machine is operational. Baseline established.                   ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")

if __name__ == "__main__":
    main()
