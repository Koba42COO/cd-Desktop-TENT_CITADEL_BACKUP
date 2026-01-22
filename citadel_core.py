"""
PHASE 298: CITADEL CORE (THE MASTER LOOP)
Objective: Integrate all subsystems (Brain, Eyes, Library) into one Sovereign Daemon.
"""

import time
import sys
import os

# Add modules directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

# IMPORT THE SUB-SYSTEMS
try:
    from modules import brain          # The Spark Plug (Phi-3)
    from modules import event_horizon  # The Prism (YouTube)
    from modules import citadel_bridge # The Library (Kiwix)
    from modules import constitution   # The Law
    from modules import tool_belt      # The Hands (Phase 301)
    from modules import physics_daemon # The Calculator (Phase 302)
    SKELETON_MODE = False
except ImportError as e:
    print(f"⚠️  WARNING: Sub-systems not found ({e}). Running in SKELETON MODE.")
    SKELETON_MODE = True

print("="*60)
print("🏰 CITADEL OS v5.1: SYSTEM STARTUP")
print("   HARDWARE: Apple M3 Max (Detected)")
print("   STATUS: SOVEREIGN")
print("="*60)

def system_check():
    """Checks if the Library and Brain are active."""
    if SKELETON_MODE:
        print("   ⚠️  SKELETON MODE: Core modules not loaded")
        return
    
    # 1. Check Offline Library
    try:
        library_status = citadel_bridge.check_status()
        print(f"   📚 LIBRARY LINK: {library_status}")
    except:
        print("   📚 LIBRARY LINK: OFFLINE")

    # 2. Check Brain
    print(f"   🧠 SPARK PLUG: STANDBY")
    
    # 3. Check Constitution
    print(f"   ⚖️  CONSTITUTION: LOADED")

def skeleton_think(prompt):
    """Fallback when modules aren't loaded."""
    return "SKELETON MODE: Brain not loaded. Please ensure modules are installed."

def main_loop():
    while True:
        try:
            user_input = input("\n>> COMMAND: ")
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("   SYSTEM HALT. SAVING STATE...")
                break

            if SKELETON_MODE:
                print(f"   TENT: {skeleton_think(user_input)}")
                continue

            # 1. THE CONSTITUTIONAL CHECK
            if constitution.veto(user_input):
                print("   🛑 BLOCKED: Violation of Core Directive.")
                continue

            # 2. THE ROUTING (Online vs Offline)
            if citadel_bridge.is_offline():
                # We are Dark. Use Kiwix + Local Brain.
                print("   [OFFLINE MODE]")
                print("   [OFFLINE MODE]")
                kiwix_context = citadel_bridge.search_kiwix(user_input)
                physics_context = citadel_bridge.search_physics_library(user_input)
                
                full_context = f"{kiwix_context}\n\n{physics_context}"
                response = brain.think(user_input, full_context)
            else:
                # We are Live. We can use tools.
                if "ingest" in user_input.lower():
                    print("   📡 ACTIVATING EVENT HORIZON...")
                    event_horizon.scan_curriculum()
                    response = "Ingestion complete."
                else:
                    response = brain.think(user_input)
            
            # --- AGENCY LOOP (Start of Phase 301) ---
            if "<execute>" in response:
                import re
                print("   🛠️  DETECTED TOOL USE REQUEST.")
                
                # Extract code between tags
                code_match = re.search(r'<execute>(.*?)</execute>', response, re.DOTALL)
                if code_match:
                    code_to_run = code_match.group(1).strip()
                    tool_output = tool_belt.execute_python(code_to_run)
                    
                    # Feed the result back to the Brain
                    follow_up_prompt = f"Using this tool output, answer the user: {tool_output}"
                    response = brain.think(follow_up_prompt)
            # ----------------------------------------

            print(f"   TENT: {response}")


        except KeyboardInterrupt:
            print("\n   SYSTEM HALT. SAVING STATE...")
            sys.exit()

if __name__ == "__main__":
    system_check()
    main_loop()
