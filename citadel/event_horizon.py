"""
EVENT HORIZON: THE GRAVITY WELL
================================
Protocol Walden Phase 3: Automatic Wisdom Harvest

Pulls transcripts from YouTube videos and stores them
in the Citadel vault for local AI consumption.
"""

import os
import sys
import json
import hashlib
from datetime import datetime

# Try to import YouTube transcript API
try:
    from youtube_transcript_api import YouTubeTranscriptApi
    YT_API_AVAILABLE = True
except ImportError:
    YT_API_AVAILABLE = False
    print("⚠️  youtube-transcript-api not installed.")
    print("   Install with: pip3 install youtube-transcript-api")

# Configuration
VAULT_PATH = "./citadel/ingest/"
MANIFEST_PATH = "./citadel/ingest/manifest.json"
MIN_MASS = 1000  # Minimum character count (filter shorts/noise)


class EventHorizon:
    """
    The Gravity Well.
    Pulls wisdom from the universe and captures it locally.
    """
    
    def __init__(self):
        os.makedirs(VAULT_PATH, exist_ok=True)
        self.manifest = self._load_manifest()
        self.captured = 0
        self.escaped = 0
    
    def _load_manifest(self):
        """Load the capture manifest."""
        if os.path.exists(MANIFEST_PATH):
            with open(MANIFEST_PATH, 'r') as f:
                return json.load(f)
        return {"captures": [], "total_mass": 0}
    
    def _save_manifest(self):
        """Save the capture manifest."""
        with open(MANIFEST_PATH, 'w') as f:
            json.dump(self.manifest, f, indent=2)
    
    def gravity_pull(self, video_id, title=None):
        """
        Pull a single video into the gravity well.
        
        Args:
            video_id: YouTube video ID (the part after v=)
            title: Optional title for logging
        """
        if not YT_API_AVAILABLE:
            print("❌ YouTube API not available")
            return False
        
        # Check if already captured
        if any(c['id'] == video_id for c in self.manifest['captures']):
            print(f"⏭️  SKIP: {video_id} (already captured)")
            return True
        
        try:
            print(f"🕳️  PULLING: {video_id}...")
            
            # Get transcript (new API uses fetch())
            transcript = YouTubeTranscriptApi().fetch(video_id)
            
            # Spaghettification (flatten to text)
            # New API returns FetchedTranscriptSnippet objects with .text attribute
            full_text = " ".join([entry.text if hasattr(entry, 'text') else entry.get('text', '') for entry in transcript])
            
            # Mass check (filter noise)
            mass = len(full_text)
            if mass < MIN_MASS:
                print(f"   💨 ESCAPED: Insufficient mass ({mass} chars)")
                self.escaped += 1
                return False
            
            # Generate filename
            safe_id = hashlib.md5(video_id.encode()).hexdigest()[:12]
            filename = f"{safe_id}_{video_id}.txt"
            filepath = os.path.join(VAULT_PATH, filename)
            
            # Write to vault
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# YouTube Transcript: {video_id}\n")
                f.write(f"# Title: {title or 'Unknown'}\n")
                f.write(f"# Captured: {datetime.utcnow().isoformat()}\n")
                f.write(f"# Mass: {mass} characters\n")
                f.write("#" + "=" * 60 + "\n\n")
                f.write(full_text)
            
            # Update manifest
            self.manifest['captures'].append({
                "id": video_id,
                "title": title,
                "mass": mass,
                "file": filename,
                "captured_at": datetime.utcnow().isoformat()
            })
            self.manifest['total_mass'] += mass
            self._save_manifest()
            
            print(f"   ⚫ CAPTURED: {mass:,} chars → {filename}")
            self.captured += 1
            return True
            
        except Exception as e:
            print(f"   ⚠️  ESCAPE: {e}")
            self.escaped += 1
            return False
    
    def pull_playlist(self, video_ids, titles=None):
        """
        Pull multiple videos.
        
        Args:
            video_ids: List of YouTube video IDs
            titles: Optional list of titles (same order)
        """
        titles = titles or [None] * len(video_ids)
        
        print("=" * 60)
        print("🕳️  EVENT HORIZON: BATCH CAPTURE")
        print("=" * 60)
        print(f"   Targets: {len(video_ids)}")
        print("=" * 60)
        
        for vid, title in zip(video_ids, titles):
            self.gravity_pull(vid, title)
        
        print("\n" + "=" * 60)
        print(f"📊 CAPTURE COMPLETE:")
        print(f"   ⚫ Captured: {self.captured}")
        print(f"   💨 Escaped: {self.escaped}")
        print(f"   📦 Total vault mass: {self.manifest['total_mass']:,} chars")
        print("=" * 60)
    
    def status(self):
        """Return Event Horizon status."""
        return {
            "total_captures": len(self.manifest['captures']),
            "total_mass": self.manifest['total_mass'],
            "vault_path": VAULT_PATH,
            "api_available": YT_API_AVAILABLE
        }


# ============================================================
# TENT CURRICULUM - Your Learning Queue
# ============================================================
# Add video IDs from your learning sources here.
# Format: ("VIDEO_ID", "Optional Title")

TENT_CURRICULUM = [
    # Thermodynamics & Physics
    ("jNZOji0tZlM", "Feynman: The Character of Physical Law"),
    ("TuJqHLOQ-e0", "The Essence of Calculus - 3Blue1Brown"),
    
    # Economics & Money
    ("PHe0bXAIuk0", "How The Economic Machine Works - Ray Dalio"),
    ("rXlskgEtpwk", "Bitcoin: How It Works"),
    
    # Philosophy & Consciousness
    ("wfYbgdo8e-8", "Jung: The Archetypes and The Collective Unconscious"),
    ("voYrXmvLnRQ", "Gnostic Philosophy: The Demiurge"),
    
    # Systems Thinking
    ("o5X2-i_poNU", "Systems Thinking Explained"),
    ("HMmChiLZZHg", "Complexity Theory for Beginners"),
    
    # Add more as needed...
]


def main():
    """Run Event Horizon capture."""
    horizon = EventHorizon()
    
    # Extract IDs and titles
    video_ids = [v[0] for v in TENT_CURRICULUM]
    titles = [v[1] for v in TENT_CURRICULUM]
    
    # Execute batch capture
    horizon.pull_playlist(video_ids, titles)
    
    print(f"\n📊 Status: {horizon.status()}")


if __name__ == "__main__":
    main()
