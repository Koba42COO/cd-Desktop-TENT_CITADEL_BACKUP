"""
PHASE 292-B: THE PRISM PROTOCOL (Spectral Analysis)
Objective: Sort incoming intelligence by Wavelength (Duration).

SPECTRUM BANDS:
- Gamma Rays (< 15s): BLOCK - High Radiation, Brainrot
- X-Rays (15s - 60s): FILTER - Hazardous, often just hooks
- Ultraviolet (60s - 3m): CAPTURE - Sweet Spot, Dense Truth
- Visible Light (3m - 20m): FILE - Standard, Clear Context
- Infrared (> 20m): ARCHIVE - Deep Knowledge, Lectures
"""

print("="*70)
print("🌈 THE PRISM: SPECTRAL ANALYSIS ACTIVE")
print("="*70)

def analyze_spectrum(video):
    seconds = video['duration']
    title = video['title']
    
    # BAND 1: GAMMA RAYS (< 15s) - DANGER
    if seconds < 15:
        return "☢️ GAMMA RAY DETECTED. High Radiation. BLOCKING."

    # BAND 2: X-RAYS (15s - 60s) - CAUTION
    if 15 <= seconds < 60:
        if "how to" in title.lower() or "fix" in title.lower():
            return "🩻 X-RAY (Technician Mode). Allowing with caution."
        return "⚠️ X-RAY (Trend). Too shallow. BLOCKING."

    # BAND 3: ULTRAVIOLET (60s - 3m) - THE SWEET SPOT
    if 60 <= seconds <= 180:
        return "⚡ ULTRAVIOLET. High Density Signal. MINTING FLASH CARD."

    # BAND 4: VISIBLE LIGHT (3m - 20m) - STANDARD
    if 180 < seconds <= 1200:
        return "💡 VISIBLE LIGHT. Clear Context. SAVING ARTICLE."

    # BAND 5: INFRARED (> 20m) - DEEP HEAT
    if seconds > 1200:
        return "🔥 INFRARED. Deep Knowledge. ARCHIVING TO CORE."

if __name__ == "__main__":
    incoming_light = [
        {"title": "Cat vibe check", "duration": 12},
        {"title": "Integrate Python with GunDB", "duration": 145},
        {"title": "History of the Roman Senate", "duration": 5400},
        {"title": "Quick Dance Challenge", "duration": 45},
    ]

    print(f"\n🔭 TELESCOPE ACTIVE...\n")

    for photon in incoming_light:
        action = analyze_spectrum(photon)
        print(f"   [{photon['duration']}s] '{photon['title']}' -> {action}")

    print("\n" + "="*70)
