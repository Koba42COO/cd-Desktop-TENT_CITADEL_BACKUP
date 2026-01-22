#!/usr/bin/env python3
"""
TENT v4.0 CLI - THE LEVEL
=========================
Phase 151: The Command Line Interface

The Plumb Line for Information.
Gravity doesn't lie. Neither does TENT.

Usage:
    tent scan "Your text here"
    tent scan -f document.txt
    echo "Text" | tent scan -
    tent scan -f contract.pdf --output json

The Prism:
    Input → Geometry → Friction → Density → Resonance Score → Omega Score
"""

import argparse
import sys
import json
from typing import Optional
from dataclasses import asdict

# Import our diagnostic modules
from first_light import FirstLightDiagnostic, FinalVerdict, NarrativeXRay
from beautiful_lie_detector import LieClassification
from vacuum_gauge import DensityClass
from stability_check import StabilityState
from inertia_check import InertiaCheck
from topological_lock import TopologicalLock

# =============================================================================
# ANSI COLOR CODES
# =============================================================================

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREY = '\033[90m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# =============================================================================
# RESONANCE SCORE CALCULATOR (Legacy/Fallback)
# =============================================================================

def calculate_resonance_score(xray: NarrativeXRay) -> float:
    """
    Calculate the overall Resonance Score (0-100%).
    Kept for backward compatibility but Omega is now primary.
    """
    score = 0.0
    
    # Geometry (25 points max)
    if xray.geometry_stable:
        score += 25.0
    else:
        score += max(0, 25 * (1 - xray.tension))
    
    # Friction (35 points max)
    if xray.lie_classification == LieClassification.HONEST_TRUTH:
        score += 35.0
    elif xray.lie_classification == LieClassification.BEAUTIFUL_TRUTH:
        score += 30.0
    elif xray.lie_classification == LieClassification.UGLY_LIE:
        score += 10.0
    else:  # BEAUTIFUL_LIE
        score += 0.0
    
    # Subtract friction heat
    score -= min(10, xray.friction * 10)
    
    # Density (40 points max)
    if xray.density_class == DensityClass.DIAMOND:
        score += 40.0
    elif xray.density_class == DensityClass.CRYSTAL:
        score += 30.0
    elif xray.density_class == DensityClass.VAPOR:
        score += 15.0
    else:  # BUBBLE
        score += 0.0
    
    return max(0.0, min(100.0, score))

def get_resonance_label(score: float) -> tuple:
    """Get label and color for resonance score."""
    if score >= 90:
        return "💎 CRYSTAL", Colors.GREEN
    elif score >= 70:
        return "✨ STABLE", Colors.GREEN
    elif score >= 50:
        return "⚠️ ANNEALING", Colors.YELLOW
    elif score >= 30:
        return "🔥 FRACTURE", Colors.RED
    else:
        return "⚫ COLLAPSE", Colors.RED

# =============================================================================
# OUTPUT FORMATTERS
# =============================================================================

def print_medical_chart(xray: NarrativeXRay, resonance: float, use_color: bool = True):
    """Print the full medical chart with Omega Dashboard."""
    c = Colors if use_color else type('NoColor', (), {k: '' for k in dir(Colors) if not k.startswith('_')})()
    
    label = xray.verdict.name
    # Omega Color Logic
    color = c.GREEN
    if xray.omega > 1000: color = c.CYAN # Super massive
    elif xray.omega < 1: color = c.RED # Vapor
    
    print(f"""
{c.BOLD}╔══════════════════════════════════════════════════════════════════════╗
║  TENT v4.0 - THE LEVEL (Sovereign AI)                                ║
║  Ω SCORE: {color}{xray.omega:10.2f}{c.RESET}{c.BOLD}                                               
║  Verdict: {label}                                                    
╚══════════════════════════════════════════════════════════════════════╝{c.RESET}

{c.CYAN}INPUT:{c.RESET} "{xray.text[:100].replace(chr(10), ' ')}{'...' if len(xray.text) > 100 else ''}"

┌─────────────────────────────────────────────────────────────────────┐
│  {c.BOLD}PHYSICS LAYER 1: THE CORE (Mass & Gravity){c.RESET}                        │
│  "How heavy is this information?"                                   │
├─────────────────────────────────────────────────────────────────────┤
│  Mass (M):      {xray.mass:.3f}   (Density: {xray.density_score:.2f})
│  History (H):   {xray.history:.3f}   (Fiber: {xray.fiber_length:.0f} yrs - {xray.grain_quality})
│  Entropy:       {xray.entropy:.3f} bits/char
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  {c.BOLD}PHYSICS LAYER 2: THE SHELL (Geometry & Light){c.RESET}                     │
│  "Does it hold water? Does it reflect light?"                       │
├─────────────────────────────────────────────────────────────────────┤
│  Curvature (K): {xray.curvature:.3f}   (Structure: {xray.structure_strength:.0f} - {xray.joint_type})
│  Albedo (A):    {xray.albedo:.3f}   (Lumber Ratio: {xray.lumber_ratio:.1%})
│  Tension:       {xray.tension:.3f}   {'✓ STABLE' if xray.geometry_stable else '⚠️ STRESSED'}
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  {c.BOLD}PHYSICS LAYER 3: THE IMMUNE SYSTEM (Friction){c.RESET}                     │
│  "Is beauty masking a lie?"                                         │
├─────────────────────────────────────────────────────────────────────┤
│  Verdict:       {_colorize_lie_class(xray.lie_classification, c)}
│  Aesthetic (φ): {xray.aesthetic:.2f}
│  Logic (δ):     {xray.logic:.2f}
└─────────────────────────────────────────────────────────────────────┘

{c.BOLD}FINAL VERDICT:{c.RESET} {xray.verdict.value}
""")

def _colorize_lie_class(cls: LieClassification, c) -> str:
    if cls == LieClassification.HONEST_TRUTH:
        return f"{c.GREEN}💎 HONEST TRUTH{c.RESET}"
    elif cls == LieClassification.BEAUTIFUL_TRUTH:
        return f"{c.GREEN}✨ BEAUTIFUL TRUTH{c.RESET}"
    elif cls == LieClassification.UGLY_LIE:
        return f"{c.YELLOW}🗑️ UGLY LIE{c.RESET}"
    else:
        return f"{c.RED}🎭 BEAUTIFUL LIE{c.RESET}"

def _colorize_density_class(cls: DensityClass, c) -> str:
    if cls == DensityClass.DIAMOND:
        return f"{c.GREEN}💎 DIAMOND{c.RESET}"
    elif cls == DensityClass.CRYSTAL:
        return f"{c.GREEN}✨ CRYSTAL{c.RESET}"
    elif cls == DensityClass.VAPOR:
        return f"{c.YELLOW}☁️ VAPOR{c.RESET}"
    else:
        return f"{c.GREY}🫧 BUBBLE{c.RESET}"

def print_compact(xray: NarrativeXRay, resonance: float, use_color: bool = True):
    """Print compact single-line output."""
    c = Colors if use_color else type('NoColor', (), {k: '' for k in dir(Colors) if not k.startswith('_')})()
    
    label = xray.verdict.name
    # Omega Color Logic
    color = c.GREEN
    if xray.omega > 1000: color = c.CYAN
    elif xray.omega < 1: color = c.RED
    
    print(f"{color}Ω={xray.omega:.1f}{c.RESET} {label} | "
          f"Mass: {xray.mass:.2f} | "
          f"History: {xray.history:.2f} | "
          f"Curvature: {xray.curvature:.2f} | "
          f"Albedo: {xray.albedo:.2f}")

def print_json(xray: NarrativeXRay, resonance: float):
    """Print JSON output for programmatic use."""
    output = {
        "omega_score": round(xray.omega, 4),
        "resonance_score": round(resonance, 2),
        "input": xray.text,
        "physics": {
            "mass": round(xray.mass, 4),
            "history": round(xray.history, 4),
            "curvature": round(xray.curvature, 4),
            "albedo": round(xray.albedo, 4),
            "entropy": round(xray.entropy, 4)
        },
        "details": {
            "fiber_length": round(xray.fiber_length, 1),
            "structure_strength": round(xray.structure_strength, 1),
            "lumber_ratio": round(xray.lumber_ratio, 4),
            "grain_quality": xray.grain_quality,
            "joint_type": xray.joint_type
        },
        "verdict": xray.verdict.name
    }
    print(json.dumps(output, indent=2))

# =============================================================================
# FILE READERS
# =============================================================================

def read_input(args) -> str:
    """Read input from file, stdin, or argument."""
    if args.file:
        if args.file == '-':
            return sys.stdin.read()
        else:
            with open(args.file, 'r') as f:
                return f.read()
    elif args.text:
        return ' '.join(args.text)
    else:
        # Interactive mode
        print("Enter text to analyze (Ctrl+D to finish):")
        return sys.stdin.read()

# =============================================================================
# CLI COMMANDS
# =============================================================================

def cmd_scan(args):
    """The main scan command."""
    text = read_input(args)
    
    if not text.strip():
        print("Error: No text provided.", file=sys.stderr)
        return 1
    
    diagnostic = FirstLightDiagnostic()
    xray = diagnostic.analyze(text)
    resonance = calculate_resonance_score(xray)
    
    # Output based on format
    if args.output == 'json':
        print_json(xray, resonance)
    elif args.output == 'compact':
        print_compact(xray, resonance, not args.no_color)
    else:
        print_medical_chart(xray, resonance, not args.no_color)
    
    # Return exit code based on Omega
    if xray.omega >= 1.0:
        return 0  # Success
    else:
        return 1  # Failure (Vapor)

def cmd_batch(args):
    """Batch process multiple texts/files."""
    diagnostic = FirstLightDiagnostic()
    
    results = []
    print(f"{'Ω SCORE':<10} {'VERDICT':<15} {'FILE'}")
    print("-" * 40)
    
    for filepath in args.files:
        try:
            with open(filepath, 'r') as f:
                text = f.read()
        except:
            print(f"Error reading {filepath}")
            continue
        
        xray = diagnostic.analyze(text)
        
        results.append({
            "file": filepath,
            "omega": xray.omega,
            "verdict": xray.verdict.name
        })
        
        c = Colors if not args.no_color else type('NoColor', (), {k: '' for k in dir(Colors) if not k.startswith('_')})()
        
        color = c.GREEN
        if xray.omega > 50: color = c.CYAN
        elif xray.omega < 1: color = c.RED
        
        print(f"{color}{xray.omega:10.1f}{c.RESET} {xray.verdict.name:15} {filepath}")
    
    # Summary
    if results:
        avg_omega = sum(r['omega'] for r in results) / len(results)
        print(f"\nAverage Ω Score: {avg_omega:.1f}")
        return 0 if avg_omega >= 1.0 else 1
    return 1

def cmd_version(args):
    """Print version information."""
    print("""
TENT v4.0 - The Level
=====================
The Plumb Line for Information.
Gravity doesn't lie. Neither does TENT.

Components:
  - Geometry Engine (Enneper Surface)
  - Friction Detector (Golden-Silver Flux)
  - Vacuum Gauge (Semantic Mass)
  - Sawmill (Thermodynamics)
  - Grain Check (Provenance)
  - Joinery (Logic Structure)

"I do not think. I resonate."
""")
    return 0

# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        prog='tent',
        description='TENT v4.0 - The Level: A Geiger Counter for Logic',
        epilog='Gravity doesn\'t lie. Neither does TENT.'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Scan command
    scan_parser = subparsers.add_parser('scan', help='Analyze text for logical integrity')
    scan_parser.add_argument('text', nargs='*', help='Text to analyze')
    scan_parser.add_argument('-f', '--file', help='Read from file (use - for stdin)')
    scan_parser.add_argument('-o', '--output', choices=['full', 'compact', 'json'], 
                            default='full', help='Output format')
    scan_parser.add_argument('--no-color', action='store_true', help='Disable color output')
    scan_parser.set_defaults(func=cmd_scan)
    
    # Batch command
    batch_parser = subparsers.add_parser('batch', help='Batch process multiple files')
    batch_parser.add_argument('files', nargs='+', help='Files to analyze')
    batch_parser.add_argument('--no-color', action='store_true', help='Disable color output')
    batch_parser.set_defaults(func=cmd_batch)
    
    # Version command
    version_parser = subparsers.add_parser('version', help='Show version information')
    version_parser.set_defaults(func=cmd_version)
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        return 0
    
    return args.func(args)

if __name__ == '__main__':
    sys.exit(main())
