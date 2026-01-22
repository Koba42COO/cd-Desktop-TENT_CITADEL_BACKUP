"""
PHASE 293: THE CHORUS (COUNCIL PODCAST GENERATOR)
Objective: Convert Council Debate Logs into a Multi-Speaker Audio Drama.
"""

# PREREQUISITES:
# pip install TTS pydub
# You also need 4 reference audio clips (wav files) to clone the voices.

try:
    import torch
    from TTS.api import TTS
    from pydub import AudioSegment
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False
    print("⚠️  TTS or pydub not installed. Chorus in SILENT mode.")

import os

# 1. LOAD THE MODEL (Coqui XTTS v2)
device = "cuda" if torch.cuda.is_available() else "cpu"
_tts = None

def load_voice_engine():
    global _tts
    if not AUDIO_AVAILABLE: return False
    
    print(f"   ⚙️  LOADING XTTS MODEL ON {device.upper()}...")
    try:
        _tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
        return True
    except Exception as e:
        print(f"   ⚠️  Voice Model Load Failed: {e}")
        return False

# 2. DEFINING THE CAST
# Paths to reference audio files
VOICE_BANK = {
    "Sun Tzu": "./voices/sun_tzu_reference.wav",
    "Jiang":   "./voices/jiang_reference.wav",
    "Prime":   "./voices/prime_reference.wav",
    "Feynman": "./voices/feynman_reference.wav"
}

def generate_podcast(debate_script, filename="council_debate.mp3"):
    """
    Generate audio for a list of (speaker, text) tuples.
    """
    if not AUDIO_AVAILABLE or _tts is None:
        print("   [SILENT] Generating transcript only (No Audio Engine)")
        return

    combined_audio = AudioSegment.empty()
    
    temp_dir = "temp_audio"
    os.makedirs(temp_dir, exist_ok=True)

    for i, (speaker, text) in enumerate(debate_script):
        print(f"   🔴 RECORDING: {speaker}...")
        output_filename = os.path.join(temp_dir, f"line_{i}_{speaker}.wav")
        
        # Check if we have a reference voice
        ref_wav = VOICE_BANK.get(speaker)
        if not ref_wav or not os.path.exists(ref_wav):
            print(f"      ⚠️  Missing voice sample for {speaker}. Skipping.")
            continue
            
        try:
            _tts.tts_to_file(
                text=text,
                file_path=output_filename,
                speaker_wav=ref_wav,
                language="en"
            )
            
            line_audio = AudioSegment.from_wav(output_filename)
            combined_audio += line_audio + AudioSegment.silent(duration=300)
        except Exception as e:
            print(f"      ❌ Generaton failed: {e}")

    # Export
    combined_audio.export(filename, format="mp3")
    print(f"✅ PODCAST GENERATED: '{filename}'")
