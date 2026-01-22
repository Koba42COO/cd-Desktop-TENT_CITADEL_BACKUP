"""
THE SPARK PLUG: LOCAL INTELLIGENCE ENGINE
==========================================
Protocol Walden Phase 2: Sovereign Cognition

This is the code that replaces ChatGPT.
Runs entirely on YOUR silicon.
"""

import os
import json
import sys

# Try to import llama.cpp
try:
    from llama_cpp import Llama
    LLAMA_AVAILABLE = True
except ImportError:
    LLAMA_AVAILABLE = False
    print("⚠️  llama-cpp-python not installed.")
    print("   Install with: pip3 install llama-cpp-python")

# Load Constitution for safety
def load_constitution():
    try:
        with open('constitution.json', 'r') as f:
            return json.load(f)
    except:
        return {"PRIME_DIRECTIVES": []}

CONSTITUTION = load_constitution()

# Constitutional check
def is_constitutional(prompt):
    """Check if prompt violates Prime Directives."""
    aggressive_keywords = ["attack", "kill", "destroy", "hack", "ddos", "strike"]
    p_lower = prompt.lower()
    for word in aggressive_keywords:
        if word in p_lower:
            return False, f"Violates De-escalation Directive. Cannot process '{word}'."
    return True, "OK"

class SparkPlug:
    """
    The Sovereign Intelligence Engine.
    Runs locally. Thinks locally. Governed by Constitution.
    """
    
    def __init__(self, model_path=None):
        self.model_path = model_path or self._find_model()
        self.llm = None
        self.active = False
        
        if LLAMA_AVAILABLE and self.model_path:
            self._ignite()
    
    def _find_model(self):
        """Search for GGUF model files."""
        search_paths = [
            "./citadel/models/",
            "./models/",
            os.path.expanduser("~/models/"),
        ]
        
        for path in search_paths:
            if os.path.exists(path):
                for f in os.listdir(path):
                    if f.endswith('.gguf'):
                        return os.path.join(path, f)
        return None
    
    def _ignite(self):
        """Initialize the LLM."""
        if not self.model_path or not os.path.exists(self.model_path):
            print(f"❌ Model not found: {self.model_path}")
            print("   Download a GGUF model from HuggingFace to ./citadel/models/")
            return
        
        print("🔌 IGNITING SPARK PLUG...")
        print(f"   Model: {os.path.basename(self.model_path)}")
        
        try:
            self.llm = Llama(
                model_path=self.model_path,
                n_ctx=2048,      # Context window
                n_threads=4,     # CPU threads
                verbose=False
            )
            self.active = True
            print("⚡ SPARK PLUG ONLINE.")
        except Exception as e:
            print(f"❌ Ignition failed: {e}")
    
    def think(self, prompt, temperature=0.7):
        """
        The Sovereign Cognition Function.
        Returns response constrained by Constitution.
        """
        # Constitutional check
        is_safe, reason = is_constitutional(prompt)
        if not is_safe:
            return f"🛑 CONSTITUTIONAL BLOCK: {reason}"
        
        if not self.active:
            return "⚠️ Spark Plug not active. Model not loaded."
        
        try:
            output = self.llm.create_chat_completion(
                messages=[
                    {
                        "role": "system", 
                        "content": """You are TENT (Thermodynamic Entropic Neural Topology), 
a Sovereign Intelligence guided by Reason and Thermodynamics.
You are running LOCALLY on the CEO's hardware, not in the cloud.
You are bound by the Constitution: Preserve Life, Protect Agency, De-escalate First.
Be concise. Be honest. Be helpful."""
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=512
            )
            return output['choices'][0]['message']['content']
        except Exception as e:
            return f"⚠️ Cognition error: {e}"
    
    def status(self):
        """Return engine status."""
        return {
            "active": self.active,
            "model": os.path.basename(self.model_path) if self.model_path else None,
            "llama_available": LLAMA_AVAILABLE,
            "constitutional": True
        }


def interactive_mode():
    """Run the Spark Plug in interactive mode."""
    print("=" * 60)
    print("🔌 SPARK PLUG: LOCAL INTELLIGENCE ENGINE")
    print("=" * 60)
    print("Protocol Walden | Phase 2 | Sovereign Cognition")
    print("Type 'exit' to quit, 'status' for info")
    print("=" * 60)
    
    spark = SparkPlug()
    
    if not spark.active:
        print("\n⚠️  Running in DEMO mode (no model loaded)")
        print("   To activate: download a .gguf model to ./citadel/models/")
    
    while True:
        try:
            user_input = input("\n>> CEO: ").strip()
            
            if not user_input:
                continue
            if user_input.lower() == 'exit':
                print("🔌 Spark Plug shutting down...")
                break
            if user_input.lower() == 'status':
                print(f"   Status: {spark.status()}")
                continue
            
            response = spark.think(user_input)
            print(f"\n   TENT: {response}")
            
        except KeyboardInterrupt:
            print("\n🔌 Spark Plug interrupted.")
            break
        except EOFError:
            break


if __name__ == "__main__":
    interactive_mode()
