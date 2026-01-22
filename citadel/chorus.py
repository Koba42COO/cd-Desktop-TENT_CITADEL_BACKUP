"""
THE CHORUS: VOICE ENGINE
=========================
Protocol Walden Phase 293: The Voice

Gives TENT the power of speech.
Uses macOS native TTS with persona-based voice selection.
"""

import os
import subprocess
import sys
import hashlib
from datetime import datetime

# Voice mappings for different personas
VOICE_PERSONAS = {
    # Sovereign/Default voice - authoritative, clear
    "sovereign": {
        "voice": "Alex",       # Clear American male
        "rate": 180,           # Words per minute
        "description": "The Sovereign Voice - clear, authoritative"
    },
    # Sun Tzu - wise, measured
    "sun_tzu": {
        "voice": "Daniel",     # British male
        "rate": 160,
        "description": "The Strategist - wise and measured"
    },
    # Professor Jiang - contemplative
    "jiang": {
        "voice": "Samantha",   # American female
        "rate": 170,
        "description": "The Philosopher - contemplative and deep"
    },
    # Feynman - enthusiastic, curious
    "feynman": {
        "voice": "Fred",       # Quirky male
        "rate": 200,
        "description": "The Scientist - enthusiastic and curious"
    },
    # System/Warning voice
    "system": {
        "voice": "Victoria",   # Neutral female
        "rate": 190,
        "description": "System announcements"
    },
    # Constitutional/Legal voice
    "constitution": {
        "voice": "Tom",        # Deep male
        "rate": 150,
        "description": "Constitutional authority - slow and deliberate"
    }
}

# Cache directory for saving audio files
AUDIO_CACHE = "./citadel/audio/"


class Chorus:
    """
    The Voice of the Citadel.
    Transforms text into speech using macOS native TTS.
    """
    
    def __init__(self):
        os.makedirs(AUDIO_CACHE, exist_ok=True)
        self.available_voices = self._get_available_voices()
        self.default_persona = "sovereign"
        
    def _get_available_voices(self):
        """Get list of available macOS voices."""
        try:
            result = subprocess.run(
                ["say", "-v", "?"],
                capture_output=True,
                text=True
            )
            voices = []
            for line in result.stdout.strip().split('\n'):
                if line:
                    # Parse voice name (first word before language code)
                    parts = line.split()
                    if parts:
                        voices.append(parts[0])
            return voices
        except:
            return []
    
    def list_voices(self):
        """List available voices with language info."""
        try:
            result = subprocess.run(
                ["say", "-v", "?"],
                capture_output=True,
                text=True
            )
            return result.stdout
        except:
            return "Voice listing not available"
    
    def speak(self, text, persona="sovereign", save_audio=False):
        """
        Speak the given text using the specified persona.
        
        Args:
            text: The text to speak
            persona: Voice persona to use (sovereign, sun_tzu, jiang, feynman, system, constitution)
            save_audio: If True, save audio to file and return path
        
        Returns:
            True if speech completed, or audio file path if save_audio=True
        """
        # Get persona settings
        settings = VOICE_PERSONAS.get(persona, VOICE_PERSONAS["sovereign"])
        voice = settings["voice"]
        rate = settings["rate"]
        
        # Check if voice is available, fallback to default if not
        if voice not in self.available_voices and self.available_voices:
            voice = self.available_voices[0]
        
        # Clean text for speech
        clean_text = self._clean_for_speech(text)
        
        if save_audio:
            # Generate unique filename
            text_hash = hashlib.md5(clean_text[:100].encode()).hexdigest()[:8]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{persona}_{timestamp}_{text_hash}.aiff"
            filepath = os.path.join(AUDIO_CACHE, filename)
            
            # Save to file
            subprocess.run([
                "say",
                "-v", voice,
                "-r", str(rate),
                "-o", filepath,
                clean_text
            ])
            return filepath
        else:
            # Speak directly
            subprocess.run([
                "say",
                "-v", voice,
                "-r", str(rate),
                clean_text
            ])
            return True
    
    def _clean_for_speech(self, text):
        """Clean text for better speech synthesis."""
        # Remove markdown formatting
        import re
        
        # Remove code blocks
        text = re.sub(r'```[\s\S]*?```', '', text)
        text = re.sub(r'`[^`]+`', '', text)
        
        # Remove URLs
        text = re.sub(r'https?://\S+', '', text)
        
        # Remove special characters that cause issues
        text = text.replace('*', '')
        text = text.replace('#', '')
        text = text.replace('_', ' ')
        text = text.replace('|', ',')
        
        # Clean up whitespace
        text = ' '.join(text.split())
        
        return text
    
    def announce(self, message, persona="system"):
        """Quick announcement in system voice."""
        self.speak(message, persona=persona)
    
    def constitutional_warning(self, violation):
        """Speak a constitutional warning."""
        warning = f"Constitutional violation detected. {violation}. Action blocked by Prime Directive."
        self.speak(warning, persona="constitution")
    
    def narrate_faculty(self, speaker, message):
        """Narrate a faculty member's response."""
        persona_map = {
            "Sun Tzu": "sun_tzu",
            "Professor Jiang": "jiang",
            "Feynman": "feynman",
            "Richard Feynman": "feynman",
            "Sovereign": "sovereign",
            "TENT": "sovereign"
        }
        persona = persona_map.get(speaker, "sovereign")
        self.speak(f"{speaker} says: {message}", persona=persona)


class PodcastEngine:
    """
    NotebookLM-style podcast generator.
    Creates multi-voice dialogues from content.
    """
    
    def __init__(self):
        self.chorus = Chorus()
        self.transcript = []
    
    def generate_episode(self, topic, content, speakers=None):
        """
        Generate a podcast-style discussion.
        
        Args:
            topic: Episode topic
            content: Source content to discuss
            speakers: List of speaker personas (defaults to Sun Tzu vs Jiang debate)
        """
        if speakers is None:
            speakers = ["sun_tzu", "jiang"]
        
        print(f"\n🎙️ GENERATING PODCAST: {topic}")
        print("=" * 50)
        
        # Opening
        self.chorus.speak(f"Welcome to The Citadel Podcast. Today's topic: {topic}", persona="system")
        
        # Introduction by Sovereign
        intro = f"I am your host. We gather today to examine: {topic}. Let us hear from our distinguished faculty."
        self.chorus.speak(intro, persona="sovereign")
        self.transcript.append(("Sovereign", intro))
        
        # For now, we'll create a simple structure
        # In full implementation, this would use the Spark Plug to generate dialogue
        
        print("\n📝 Episode structure ready.")
        print("   To generate full AI-driven dialogue, integrate with Spark Plug.")
        
        return self.transcript
    
    def debate(self, proposition, pro_speaker="sun_tzu", con_speaker="jiang"):
        """Create a debate between two faculty members."""
        print(f"\n⚔️ DEBATE MODE")
        print(f"   Proposition: {proposition}")
        print(f"   PRO: {pro_speaker}")
        print(f"   CON: {con_speaker}")
        
        self.chorus.speak(f"The motion before us: {proposition}", persona="sovereign")
        # Further implementation would use Spark Plug to generate actual debate content


def demo():
    """Demonstrate the Chorus capabilities."""
    print("=" * 60)
    print("🎵 THE CHORUS: VOICE ENGINE DEMO")
    print("=" * 60)
    
    chorus = Chorus()
    
    # Show available voices
    print("\n📋 Available Voices:")
    print(f"   Found {len(chorus.available_voices)} voices")
    
    # Demo each persona
    print("\n🎭 Voice Personas:")
    for name, settings in VOICE_PERSONAS.items():
        print(f"   • {name}: {settings['description']}")
    
    # Speak a test message
    print("\n🔊 Speaking test message...")
    chorus.speak("The Citadel is online. The Monarch lives. Protocol Walden is complete.", 
                 persona="sovereign")
    
    print("\n✅ Demo complete.")


if __name__ == "__main__":
    demo()
