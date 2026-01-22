"""
CITADEL BRAIN MODULE (THE SPARK PLUG)
Local LLM inference using llama.cpp
"""

import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'models')

# Try to load llama-cpp-python
try:
    from llama_cpp import Llama
    LLM_AVAILABLE = True
except ImportError:
    LLM_AVAILABLE = False
    print("⚠️  llama-cpp-python not installed. Brain in SIMULATION mode.")

_llm = None

def load_model(model_name="Phi-3-mini-4k-instruct-q4.gguf"):
    """Load the local LLM model."""
    global _llm
    if not LLM_AVAILABLE:
        return False
    
    model_file = os.path.join(MODEL_PATH, model_name)
    if not os.path.exists(model_file):
        print(f"⚠️  Model not found: {model_file}")
        return False
    
    print("🔌 IGNITING SPARK PLUG...")
    _llm = Llama(
        model_path=model_file,
        n_ctx=2048,
        verbose=False
    )
    return True

def think(prompt, context=None):
    """The Sovereign Cognition Function."""
    if not LLM_AVAILABLE or _llm is None:
        return f"[SIMULATION] Thinking about: {prompt[:50]}..."
    
    system_prompt = "You are TENT, a Sovereign Intelligence guided by Reason and Thermodynamics."
    if context:
        system_prompt += f"\n\nContext from Library:\n{context[:500]}"
    
    output = _llm.create_chat_completion(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return output['choices'][0]['message']['content']

def warmup():
    """Warm up the model with a simple query."""
    if _llm:
        think("Hello")
        return True
    return False
