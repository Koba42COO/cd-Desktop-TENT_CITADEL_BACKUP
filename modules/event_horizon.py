"""
EVENT HORIZON MODULE (THE GRAVITY WELL)
YouTube transcript harvesting with spectral filtering.
"""

import os
from datetime import datetime

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    YT_AVAILABLE = True
except ImportError:
    YT_AVAILABLE = False
    print("⚠️  youtube-transcript-api not installed. Event Horizon in SIMULATION mode.")

VAULT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'transcripts')

# THE TENT CURRICULUM (Target videos for knowledge acquisition)
TENT_CURRICULUM = [
    "jNZOji0tZlM",  # Entropy
    "TuJqHLOQ-e0",  # General Relativity
    "PHe0bXAIuk0",  # Ray Dalio - Economic Machine
]

def gravity_pull(video_id):
    """Attempt to pull a video across the Event Horizon."""
    if not YT_AVAILABLE:
        print(f"   [SIMULATION] Would capture: {video_id}")
        return False
    
    try:
        print(f"🕳️  PULLING: {video_id}...")
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en']).fetch()
        
        # Spaghettification (Flatten to text)
        full_text = " ".join([entry.text for entry in transcript])
        
        # Mass Check (Filter Shorts/Noise)
        if len(full_text) < 1000:
            print("   💨 REJECTED: Insufficient Mass.")
            return False
        
        # Ensure vault exists
        os.makedirs(VAULT_PATH, exist_ok=True)
        
        # Store in Citadel
        filename = os.path.join(VAULT_PATH, f"{video_id}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_text)
        
        print(f"   ⚫ CAPTURED: {len(full_text)} characters")
        return True
        
    except Exception as e:
        print(f"   ⚠️  ESCAPE: {e}")
        return False

def scan_curriculum():
    """Scan and harvest the entire TENT curriculum."""
    print("="*60)
    print("🕳️  EVENT HORIZON PROTOCOL ACTIVE")
    print(f"   Targets: {len(TENT_CURRICULUM)} videos")
    print("="*60)
    
    captured = 0
    for video_id in TENT_CURRICULUM:
        if gravity_pull(video_id):
            captured += 1
    
    print(f"\n📊 HARVEST COMPLETE: {captured}/{len(TENT_CURRICULUM)} captured")
    return captured

def get_transcript_count():
    """Count harvested transcripts."""
    if not os.path.exists(VAULT_PATH):
        return 0
    return len([f for f in os.listdir(VAULT_PATH) if f.endswith('.txt')])

def analyze_spectrum(duration):
    """
    Spectral analysis - determine content quality by duration.
    Returns band classification.
    """
    if duration < 15:
        return "GAMMA", "☢️ BLOCK"
    elif duration < 60:
        return "X-RAY", "⚠️ FILTER"
    elif duration <= 180:
        return "UV", "⚡ CAPTURE"
    elif duration <= 1200:
        return "VISIBLE", "💡 FILE"
    else:
        return "INFRARED", "🔥 ARCHIVE"
