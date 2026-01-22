import zlib
import math
from collections import Counter

class VacuumGaugeResult:
    def __init__(self, density):
        self.density_score = density

class VacuumGauge:
    """
    The TENT Vacuum Gauge.
    Measures the 'Density' of information.
    
    Principles:
    1. High Entropy + Low Compression = Noise (Flux).
    2. Low Entropy + High Structure = Order (Solid).
    3. High Density = Rich Information (Signal).
    """
    def analyze(self, text):
        if not text:
            return VacuumGaugeResult(0.0)
            
        # 1. Shannon Entropy
        entropy = self.calculate_entropy(text)
        
        # 2. Compression Ratio (Structure)
        compressed = zlib.compress(text.encode())
        ratio = len(text) / len(compressed) if len(compressed) > 0 else 0
        
        # 3. Density Score
        # We want high density to mean "Rich Meaning".
        # Pure noise has high entropy but low 'meaningful' density in TENT terms?
        # Actually, let's align with TENT:
        # Solid = High Structure (High Ratio).
        # Flux = Randomness (Low Ratio).
        
        density = (ratio * 10.0) / (entropy + 1.0)
        
        return VacuumGaugeResult(density)

    def calculate_entropy(self, text):
        prob = [float(text.count(c)) / len(text) for c in dict.fromkeys(list(text))]
        entropy = -sum([p * math.log(p) / math.log(2.0) for p in prob])
        return entropy
