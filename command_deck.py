#!/usr/bin/env python3
import time
import sys
from kwyc_core import KwycLedger
from upg_store import UniversalPrimeGraph, PrimeNode, NodeType
from value_assessor import ValueAssessor
from dividend_tracker import DividendEngine
from dividend_tracker import DividendEngine
from vacuum_gauge import VacuumGauge
from parallel_transport import TransportEngine
from parallel_transport import TransportEngine
from holographic_monad import HolographicMonad
from holographic_monad import HolographicMonad
from mechanics_core import DynamicsEngine
from quantum_throd import QuantumThrodEngine, QuantumState

class CommandDeck:
    def __init__(self):
        # 1. INITIALIZE THE STACK
        self.ledger = KwycLedger()
        self.upg = UniversalPrimeGraph()
        self.assessor = ValueAssessor()
        self.dividends = DividendEngine(self.ledger, self.assessor)
        self.dividends = DividendEngine(self.ledger, self.assessor)
        self.physics = VacuumGauge()
        self.transport = TransportEngine()
        self.transport = TransportEngine()
        self.monad = HolographicMonad(self.upg, self.physics, self.ledger)
        self.monad = HolographicMonad(self.upg, self.physics, self.ledger)
        self.mechanics = DynamicsEngine()
        self.quantum = QuantumThrodEngine()
        
        # 2. AUTHENTICATE ARCHITECT
        self.user = "WALLET_BRAD_0x18012026"
        self.session_start = time.time()

    def boot_sequence(self):
        print("\n" + "="*60)
        print("   ⛺  TENT v4.0  |  UNIVERSAL COMMAND DECK")
        print("   STATUS: SOVEREIGN  |  USER: ARCHITECT")
        print("="*60)
        print("Initializing Physics Engine... [OK]")
        print("Loading Universal Prime Graph... [OK]")
        print("Connecting to KWYC Ledger... [OK]")
        print(f"System Time: {time.ctime()}\n")
        self.main_menu()

    def main_menu(self):
        while True:
            print("\n--- COMMAND OPTIONS ---")
            print(" [1] 💎 MINT ASSET   (Create Recipe/Code)")
            print(" [2] 🗺️  VIEW MAP     (Explore UPG)")
            print(" [3] ⚖️  PHYSICS SCAN (Vacuum Gauge)")
            print(" [3] ⚖️  PHYSICS SCAN (Vacuum Gauge)")
            print(" [4] 💰 CHECK WEALTH (Dividend Tracker)")
            print(" [5] 🚀 TRANSPORT ASSET (Holonomy Protocol)")
            print(" [5] 🚀 TRANSPORT ASSET (Holonomy Protocol)")
            print(" [6] 🧠 ACTIVATE MONAD (Post-LLM AI)")
            print(" [6] 🧠 ACTIVATE MONAD (Post-LLM AI)")
            print(" [7] 🍎 RUN DYNAMICS (Classical Mechanics)")
            print(" [8] ⚛️  QUANTUM GAUGE (Uncertainty)")
            print(" [Q] QUIT")
            
            # Using input() generally, but for automation we might need to handle it differently
            # For this script we assume running in TTY or via piped input
            try:
                choice = input("\nroot@tent:~# ").upper()
            except EOFError:
                break
            
            if choice == "1": self.mint_protocol()
            elif choice == "2": self.view_map()
            elif choice == "3": self.run_physics()
            elif choice == "4": self.check_wealth()
            elif choice == "5": self.transport_protocol()
            elif choice == "5": self.transport_protocol()
            elif choice == "6": self.activate_monad()
            elif choice == "7": self.run_dynamics_sim()
            elif choice == "8": self.quantum_gauge()
            elif choice == "Q": 
                print("System Shutdown. Session Logged."); sys.exit()
            else: print("Invalid Command.")

    def mint_protocol(self):
        print("\n--- 💎 ASSET MINTING PROTOCOL ---")
        print("Select Type: [M]atter (Static) | [L]ogic (AI) | [R]eflex (Cyber-Physical)")
        type_choice = input("Selection: ").upper()
        
        name = input("Asset Name: ")
        content = input("Define Vector/Content: ")
        
        # 1. RUN PHYSICS CHECK BEFORE MINTING
        print("Running Pre-Mint Physics Check...")
        # VacuumGauge analyze might expect text. Content is text.
        vac_res = self.physics.analyze(content)
        
        # Note: In the user provided code, density_score < 10.0 is rejected.
        # But for 'Vectors' which are JSON-like, they might have low density if they are short or technical.
        # However, the user provided this logic, so I will stick to it.
        # If the check fails for the Identity Prime, I might need to pad the content or the user's simulation implies it passes.
        # The Identity Vector content: {"Role": "Architect", ...}
        # Let's hope VacuumGauge gives it enough score. If not, I'll need to adjust or 'cheat' the simulation logic.
        # vacuum_gauge.py analyzes words/density. JSON might score low?
        # Let's assume for this specific phase, we want it to succeed.
        
        if vac_res.density_score < 10.0:
            print(f"❌ REJECTED: Insufficient Mass ({vac_res.density_score}). Information too light.")
            # For the purpose of the demo, we might want to proceed or allow override.
            # But let's respect the code.
            return
            
        # 2. MINT
        block_id = self.ledger.mint_block(content, self.user, "RECIPE")
        
        # 3. MAP
        # In a real system, we'd assign a new Prime. Here we simulate.
        new_prime = len(self.upg.nodes) + 1000
        # Determine node type from choice
        n_type = NodeType.CODE 
        if type_choice == 'M': n_type = NodeType.MEDIA
        
        node = PrimeNode(new_prime, n_type, name, mass=vac_res.density_score)
        self.upg.add_node(block_id, {"data": node})
        
        print(f"✅ SUCCESS: Minted {name} at Prime {new_prime}")

    def transport_protocol(self):
        print("\n--- 🚀 ASSET TRANSPORT PROTOCOL ---")
        # For demo purposes, we will simulate the Aerospace -> Medical move
        # In a real CLI we would ask for ID, Src, Tgt.
        print(">> PROTOCOL INITIATED: MOVING ASSET BETWEEN DOMAINS")
        
        # 1. Select Asset (Simulated)
        asset_name = "RECIPE_AEROSPACE_STEEL_V1"
        asset_vector = {
            "name": asset_name,
            "temp": 1450,
            "carbon": 0.02,
            "trace_lead": "ALLOWED_PPM_10"
        }
        
        # 2. Define Path
        src = "AEROSPACE"
        tgt = "MEDICAL"
        print(f"   Asset: {asset_name}")
        print(f"   Path:  {src} -> {tgt}")
        
        # 3. Define Curvature (Auto-Detect/Manual)
        print(">> DEFINING CURVATURE MAP...")
        self.transport.define_curvature(src, tgt, {
            "trace_lead": "FORBIDDEN_0_PPM",
            "certification": "ISO_13485"
        })
        
        # 4. Execute Transport
        print(">> EXECUTING PARALLEL TRANSPORT...")
        new_vec = self.transport.transport_asset(asset_vector, src, tgt)
        
        print(f"\n✅ TRANSPORT COMPLETE.")
        print(f"   New State: {new_vec['trace_lead']} | {new_vec.get('certification')}")

    def activate_monad(self):
        print("\n--- 🧠 HOLOGRAPHIC MONAD ---")
        print(">> THE POST-LLM MIND IS AWAKE.")
        goal = input("Define Goal for Sovereign Synthesis (e.g. 'Heavy Industry'): ")
        if not goal: goal = "General Research"
        self.monad.seek_truth(goal)

    def run_dynamics_sim(self):
        print("\n--- 🍎 NEWTONIAN DYNAMICS SIMULATION ---")
        print(">> APPLYING MARKET FORCE TO ASSETS...")
        
        # Select two contrasting nodes from the UPG or mock them if empty
        # For simulation, let's look at the Triad if it exists, else mock.
        # We need a Heavy and a Light object.
        
        heavy_node = None
        light_node = None
        
        # Try to find recent mints
        for nid, data in self.upg.nodes.items():
            node = data['data']
            if node.mass > 20: heavy_node = node
            elif node.mass > 0: light_node = node
            
        if not heavy_node:
            print("   (Mocking Heavy Node for Demo)")
            heavy_node = PrimeNode(9998, NodeType.MEDIA, "MOCK_HEAVY", mass=100.0)
            
        if not light_node:
            print("   (Mocking Light Node for Demo)")
            light_node = PrimeNode(9999, NodeType.MEDIA, "MOCK_LIGHT", mass=1.0)
            
        force = 50.0
        print(f"   Force Applied: {force} N (Market Shock)")
        
        print(f"\n   [1] HEAVY OBJECT: {heavy_node.content} (Mass={heavy_node.mass})")
        traj_h = self.mechanics.simulate_trajectory(heavy_node, force, steps=3)
        for step in traj_h: print(f"       {step}")
            
        print(f"\n   [2] LIGHT OBJECT: {light_node.content} (Mass={light_node.mass})")
        traj_l = self.mechanics.simulate_trajectory(light_node, force, steps=3)
        for step in traj_l: print(f"       {step}")
        
        print("\n>> VERDICT: High Mass resists Volatility. Low Mass gets Yeeted.")

    def quantum_gauge(self):
        print("\n--- ⚛️  QUANTUM GAUGE (HEISENBERG UNCERTAINTY) ---")
        print(">> COLLAPSING WAVEFUNCTION...\n")
        
        # Create a mock Quantum State for demonstration
        state = QuantumState(mass_true=50.0, velocity_true=10.0, position_true=0.0)
        print(f"ASSET STATE: Mass={state.mass_true}, Vel={state.velocity_true}")
        
        print("\n--- MEASURING MASS (5x) ---")
        for i in range(5):
            result = self.quantum.measure_observable(state, 'mass')
            print(f"   M{i+1}: Mass={result['mass']:.2f} (Δ={result['mass_uncertainty']:.4f}), "
                  f"Vel={result['velocity']:.2f} (Δ={result['velocity_uncertainty']:.4f})")
                  
        print("\n--- MEASURING VELOCITY (5x) ---")
        for i in range(5):
            result = self.quantum.measure_observable(state, 'velocity')
            print(f"   V{i+1}: Mass={result['mass']:.2f} (Δ={result['mass_uncertainty']:.4f}), "
                  f"Vel={result['velocity']:.2f} (Δ={result['velocity_uncertainty']:.4f})")
                  
        print("\n>> VERDICT: Observing one property destabilizes the other.")

    def run_physics(self):
        print("\n--- ⚖️  VACUUM GAUGE ---")
        text = input("Enter Text/Logic to Weigh: ")
        result = self.physics.analyze(text)
        print(f"   DENSITY: {result.density_score}")
        print(f"   ALBEDO:  {result.albedo}")
        print(f"   STATUS:  {'SOVEREIGN' if result.density_score > 50 else 'VAPOR'}")

    def view_map(self):
        print("\n--- 🗺️  UNIVERSAL PRIME GRAPH ---")
        if not self.upg.nodes:
            print("   (Map is Empty. Mint an Asset to begin.)")
        for bid, data in self.upg.nodes.items():
            # Handle potential difference in UPG structure from previous files
            # The previous upg_store.py had nodes map ID->Data
            # command_deck.py assumes self.upg.nodes is iterable
            print(f"   ID: {bid[:8]} | Node: {data['data'].content}")

    def check_wealth(self):
        print(f"\n--- 💰 WALLET: {self.user} ---")
        # Simulate a calculation
        print("   Current Balance: 0.00 Credits")
        print("   Active Streams:  0")
        print("   (Mint High-Utility Recipes to generate flow)")

if __name__ == "__main__":
    deck = CommandDeck()
    deck.boot_sequence()
