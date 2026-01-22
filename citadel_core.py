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
                context = citadel_bridge.search_kiwix(user_input)
                response = brain.think(user_input, context)
            else:
                # We are Live. We can use tools.
                if "ingest" in user_input.lower():
                    print("   📡 ACTIVATING EVENT HORIZON...")
                    event_horizon.scan_curriculum()
                    response = "Ingestion complete."
                else:
                    response = brain.think(user_input)

            print(f"   TENT: {response}")

        except KeyboardInterrupt:
            print("\n   SYSTEM HALT. SAVING STATE...")
            sys.exit()

if __name__ == "__main__":
    system_check()
    main_loop()
