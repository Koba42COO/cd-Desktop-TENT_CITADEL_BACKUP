"""
BORWEIN INTEGRAL BREACH TEST
============================
Demonstrates Geometric Containment Failure at n=15.
This explains why 'Perfect Geometry' holds only until complexity
exceeds the container (Sum 1/k > 1).
"""

import numpy as np
import time

# Robust integration fallback if scipy is missing
try:
    from scipy import integrate
    USING_SCIPY = True
except ImportError:
    USING_SCIPY = False
    print("⚠️  Scipy not found. Using numerical integration fallback.")

def sinc(x):
    # Normalized sinc in numpy is sin(pi*x)/(pi*x), but Borwein uses sin(x)/x
    if x == 0: return 1.0
    return np.sin(x) / x

def borwein_integrand(x, limit_n):
    """
    Product of sinc(x/k) for odd k up to limit_n
    """
    result = 1.0
    # Steps: 1, 3, 5 ... limit_n
    for k in range(1, limit_n + 1, 2):
        result *= sinc(x / k)
    return result

def check_containment(n):
    # Calculate the sum of reciprocals (The Geometric Pressure)
    # The condition is sum(1/k) for k=3,5..n < 1
    pressure = sum([1/k for k in range(3, n + 1, 2)])
    return pressure

def integrate_borwein(n):
    if USING_SCIPY:
        # High precision integration
        val, error = integrate.quad(lambda x: borwein_integrand(x, n), 0, np.inf, limit=100)
        return val
    else:
        # Fallback: Trapezoidal rule
        # We need significant range and resolution to catch the 10^-11 diff
        # This might be slow but it proves the concept directionally
        x = np.linspace(0, 10000, 100000) # 0 to 10000 with 0.1 steps (粗い but fast)
        # Actually, let's use a smarter range. Energy decays as 1/x^N.
        # For n=15, decay is very fast.
        
        # High res near zero
        x1 = np.linspace(0, 100, 10000)
        y1 = [borwein_integrand(xi, n) for xi in x1]
        val1 = np.trapz(y1, x1)
        
        # Low res tail
        x2 = np.linspace(100, 10000, 10000)
        y2 = [borwein_integrand(xi, n) for xi in x2]
        val2 = np.trapz(y2, x2)
        
        return val1 + val2

if __name__ == "__main__":
    print("📐 BORWEIN GEOMETRY CHECK")
    print("Target Value: pi/2 = 1.57079632679...")
    print("-" * 65)
    print(f"{'Max N':<6} | {'Sum(1/k)':<10} | {'Status':<10} | {'Integral Result'}")
    print("-" * 65)

    # We check odd numbers from 1 to 17
    target = np.pi / 2
    
    for n in range(1, 18, 2):
        # 1. Check Pressure
        pressure = check_containment(n)
        status = "STABLE" if pressure < 1.0 else "BREACH"
        
        # 2. Integrate
        val = integrate_borwein(n)
        
        diff = val - target
        
        # Formatting
        diff_str = f"{diff:.1e}" if abs(diff) > 1e-15 else "0.0"
        
        print(f"{n:<6} | {pressure:.5f}    | {status:<10} | {val:.11f} (Diff: {diff_str})")
        
    print("-" * 65)
    print("📢 IMPLICATION:")
    print("   At n=15, the Sum(1/k) > 1.")
    print("   The Hypercube spills. Probability leaks.")
    print("   This is the 'Geometric Containment Limit' for Atomic Manufacturing.")
