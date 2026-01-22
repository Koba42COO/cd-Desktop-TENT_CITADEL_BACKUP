"""
THE SPEAKING CITADEL
====================
Brain + Voice = The Monarch Speaks
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chorus import Chorus
from brain.spark_plug import SparkPlug

class SpeakingCitadel:
    def __init__(self, model_path=None):
        print("🏰 SPEAKING CITADEL: INITIALIZING")
        self.chorus = Chorus()
        if model_path is None:
            model_path = os.path.abspath("models/Phi-3-mini-4k-instruct-Q4_K_M.gguf")
        self.spark = SparkPlug(model_path=model_path) if os.path.exists(model_path) else None
        print(f"🧠 Brain: {'online' if self.spark and self.spark.active else 'offline'}")
        print(f"🔊 Voice: {len(self.chorus.available_voices)} voices")
    
    def think_and_speak(self, query, persona="sovereign", speak=True):
        print(f"\n🤔 {query[:50]}...")
        response = self.spark.think(query) if self.spark and self.spark.active else "Brain offline."
        print(f"💭 {response}")
        if speak: self.chorus.speak(response, persona=persona)
        return response
    
    def lecture(self, topic, speaker="sovereign"):
        prompt = f"Give a brief 2-paragraph lecture on: {topic}. Write in flowing prose."
        lecture = self.spark.think(prompt) if self.spark and self.spark.active else f"Cannot lecture on {topic}."
        self.chorus.speak(f"Today's topic: {topic}. {lecture}", persona=speaker)
        return lecture
    
    def debate(self, topic):
        self.chorus.speak(f"Debate: {topic}", persona="sovereign")
        if self.spark and self.spark.active:
            sun = self.spark.think(f"As Sun Tzu, give 2 sentences on: {topic}")
            self.chorus.speak(sun, persona="sun_tzu")
            jiang = self.spark.think(f"As a Gnostic philosopher, counter Sun Tzu on: {topic}")
            self.chorus.speak(jiang, persona="jiang")

def main():
    citadel = SpeakingCitadel()
    print("\n🏰 COMMANDS: 'lecture [topic]', 'debate [topic]', 'exit', or ask anything")
    while True:
        try:
            inp = input("\n>> CEO: ").strip()
            if not inp: continue
            if inp.lower() == 'exit': break
            elif inp.lower().startswith('lecture '): citadel.lecture(inp[8:])
            elif inp.lower().startswith('debate '): citadel.debate(inp[7:])
            else: citadel.think_and_speak(inp)
        except (KeyboardInterrupt, EOFError): break

if __name__ == "__main__": main()
