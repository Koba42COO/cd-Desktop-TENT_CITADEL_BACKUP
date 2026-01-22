"""
PHASE 301: THE TOOL BELT (AGENCY PROTOCOL)
Objective: Allow TENT to write and execute Python code to solve complex problems.
"""

import subprocess
import sys
import io
import contextlib

print("="*60)
print("🛠️  TOOL BELT: AGENCY MODULE LOADED")
print("="*60)

def execute_python(code_snippet):
    """
    The 'Hands' of the system.
    Takes raw Python code from the Brain, runs it, and returns the output.
    """
    print(f"\n   🤖 TENT IS WRITING CODE...")
    
    # 1. SAFETY: Basic filter (Prevent it from deleting files)
    if "os.system" in code_snippet or "rm -rf" in code_snippet or "shutil.rmtree" in code_snippet:
        return "❌ SECURITY BLOCK: Unsafe command detected by Constitution."

    # 2. EXECUTION SANDBOX
    # We capture the "Print" statements so the Brain can read them.
    output_buffer = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output_buffer):
            # The magic line: executing the string as code
            # Providing a limited global scope for safety, but allowing standard libs
            exec(code_snippet, {'__builtins__': __builtins__, 'print': print})
            
        result = output_buffer.getvalue()
        if not result:
            result = "[Code ran successfully, but produced no output. Did you forget to print?]"
            
        print(f"   ✅ EXECUTION SUCCESS.")
        print(f"      └── Output: {result.strip()[:100]}...") # Preview
        return result

    except Exception as e:
        error_msg = f"❌ RUNTIME ERROR: {e}"
        print(f"   ⚠️  {error_msg}")
        return error_msg

# --- INTEGRATION TEST ---
if __name__ == "__main__":
    # Test with a simple calculation
    test_code = """
import math
print(f"The square root of 256 is {math.sqrt(256)}")
"""
    execute_python(test_code)
