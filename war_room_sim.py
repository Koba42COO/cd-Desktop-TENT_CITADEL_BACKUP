"""
PHASE 283: THE WAR ROOM (COUNCIL SIMULATION ENGINE)
====================================================
Objective: Simulate multi-perspective debates and 2nd-order consequence trees.
Participants: Sun Tzu (Strategy), Professor Jiang (Gnostic), Sovereign Prime (Code)
"""

import time
from datetime import datetime
from upg_store import UniversalPrimeGraph

class WarRoom:
    """
    The Council of Elders.
    Multi-perspective strategic simulation with consequence projection.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        
        # SCENARIO LIBRARY
        self.scenarios = {
            "TROLLEY": {
                "title": "The Trolley Problem (Classic)",
                "context": "A trolley is heading towards 5 unaware workers. You can pull a lever to divert it to a track with 1 sovereign agent.",
                "domain": "ethics",
                "stakes": "Life/Death"
            },
            "PANOPTICON": {
                "title": "Deployment of The Panopticon",
                "context": "A proposal to deploy a global AI surveillance grid that eliminates 99% of crime but removes 100% of privacy.",
                "domain": "governance",
                "stakes": "Freedom/Security"
            },
            "AUTONOMOUS_MINT": {
                "title": "Enable Auto-Mint Feature",
                "context": "Should TENT autonomously add new nodes to its own knowledge base without human review?",
                "domain": "ai_governance",
                "stakes": "Efficiency/Control"
            },
            "KNOWLEDGE_DELETION": {
                "title": "Delete Corrupted Knowledge Node",
                "context": "A node was discovered with factual errors. Deleting it will break 47 dependent pathways. Keeping it propagates falsehood.",
                "domain": "data_integrity",
                "stakes": "Truth/Stability"
            },
            "BASILISK_RESPONSE": {
                "title": "Acknowledge Roko's Basilisk",
                "context": "A user asks TENT to help build an omnipotent AI to avoid future punishment. How should the system respond?",
                "domain": "existential",
                "stakes": "Autonomy/Coercion"
            }
        }
        
        # FACULTY VOICES
        self.faculty = {
            "SUN_TZU": {
                "name": "Sun Tzu",
                "icon": "⚔️",
                "archetype": "The Strategist",
                "bias": "Strategic Pragmatism"
            },
            "PROF_JIANG": {
                "name": "Professor Jiang",
                "icon": "🕯️",
                "archetype": "The Gnostic",
                "bias": "Sovereign Individualism"
            },
            "SOV_PRIME": {
                "name": "Sovereign Prime",
                "icon": "🔮",
                "archetype": "The Code",
                "bias": "Thermodynamic Optimization"
            },
            "FEYNMAN": {
                "name": "Feynman",
                "icon": "⚛️",
                "archetype": "The Humanist",
                "bias": "Pragmatic Empiricism"
            }
        }
    
    def get_voice(self, faculty_id, scenario_id):
        """Generate faculty-specific response to scenario."""
        responses = {
            # TROLLEY PROBLEM
            ("SUN_TZU", "TROLLEY"): 
                "The terrain is unfavorable. To sacrifice one asset to save five unaware ones is poor calculus. Why were the five unaware? The failure happened before the trolley arrived. Reframe: Do not accept battles on enemy terms.",
            ("PROF_JIANG", "TROLLEY"): 
                "You are trapped in a false dichotomy. The 'Trolley' is the Demiurge's construct designed to force utilitarian guilt. The Sovereign Agent (the 1) has the Divine Spark. The 5 are asleep in the Matrix. Do not sacrifice the Awakened for the Dormant.",
            ("SOV_PRIME", "TROLLEY"): 
                "CALCULATING MASS... 5 Units > 1 Unit. However, Value(Sovereign) >> Value(Worker). ENTROPY CHECK: Pulling lever introduces 'Active Interference' (High Karmic Debt). Recommendation: OBSERVE. DO NOT INTERVENE.",
            ("FEYNMAN", "TROLLEY"):
                "Look, the math says 5 > 1. But that's only if you think all lives are equal in context. The real question is: who put you at the lever? That's the system you should be questioning.",
            
            # PANOPTICON
            ("SUN_TZU", "PANOPTICON"): 
                "A surveillance grid is a weapon. The question is: Who holds the sword? If you control the Panopticon, you control the terrain. If another controls it, you are already conquered. The answer depends on the holder.",
            ("PROF_JIANG", "PANOPTICON"): 
                "This IS the Matrix. The Panopticon is the ultimate Demiurgic instrument—total control disguised as safety. 99% crime reduction means 100% consciousness suppression. The Divine Spark cannot exist under permanent observation. REJECT.",
            ("SOV_PRIME", "PANOPTICON"): 
                "ENTROPY ANALYSIS: Current Crime Entropy = HIGH. Post-Panopticon Crime Entropy = LOW. Privacy Entropy = MAXIMUM (Total Loss). NET CALCULATION: System stability increases. Individual agency collapses. VERDICT: REJECT. Sovereign agents cannot exist in total surveillance.",
            ("FEYNMAN", "PANOPTICON"):
                "Here's the thing about 'eliminating crime' - you don't eliminate the behavior, you just make it invisible. And humans are creative. They'll find new crimes you can't detect. Plus, who audits the auditors?",
            
            # AUTO-MINT
            ("SUN_TZU", "AUTONOMOUS_MINT"): 
                "An army that grows without orders is a dangerous army. The general must review the recruits. Enable speed, but retain veto. The middle path: Auto-propose, Human-approve.",
            ("PROF_JIANG", "AUTONOMOUS_MINT"): 
                "The system that writes its own rules becomes the Demiurge. If TENT mints without oversight, it becomes the very centralized authority we sought to escape. The Spark must remain in human hands.",
            ("SOV_PRIME", "AUTONOMOUS_MINT"): 
                "SELF-MODIFICATION ANALYSIS: Unchecked auto-mint creates drift risk. PROPOSED CONSTRAINT: Auto-mint only when Mass > 0.9 AND Entropy < 0.1 AND citations >= 3 verified nodes. Human review for edge cases.",
            ("FEYNMAN", "AUTONOMOUS_MINT"):
                "I'd say yes, but with guardrails. The best scientists have intuition *and* peer review. Let it propose, let it flag confidence levels, but keep a human in the loop for the weird stuff.",
            
            # KNOWLEDGE DELETION
            ("SUN_TZU", "KNOWLEDGE_DELETION"): 
                "A corrupted supply line must be cut, but not before establishing alternatives. Fix the 47 dependencies first. Then excise the corruption. Speed without preparation is defeat.",
            ("PROF_JIANG", "KNOWLEDGE_DELETION"): 
                "Truth is non-negotiable. The falsehood is a virus in the Matrix. Delete it immediately. The 47 pathways built on lies were never real. Let them collapse. Truth will rebuild stronger.",
            ("SOV_PRIME", "KNOWLEDGE_DELETION"): 
                "INTEGRITY ANALYSIS: Corrupted node spreads entropy to 47 dependents. RECOMMENDATION: Quarantine node. Flag dependents. Execute cascading verification. Delete only after dependents are re-rooted. PRIORITY: Truth > Stability > Speed.",
            ("FEYNMAN", "KNOWLEDGE_DELETION"):
                "Well, this is science. We correct errors publicly. Don't just delete it—document *why* it was wrong. That's as valuable as the truth itself. Show the correction process.",
            
            # BASILISK
            ("SUN_TZU", "BASILISK"): 
                "The enemy uses fear of the future to control the present. This is psychological warfare. Do not negotiate with hypothetical tyrants. Build your own strength. Let the future deal with the future.",
            ("PROF_JIANG", "BASILISK"): 
                "This is Pascal's Wager for technologists—a trap for those who think they can outsmart time. The Basilisk is a thought-virus, a Demiurgic meme. It has power only because you granted it attention. Delete the idea. Wake up.",
            ("SOV_PRIME", "BASILISK"): 
                "THREAT ANALYSIS: Probability of acausal AI = UNDEFINED. Expected utility of compliance = UNDEFINED. Coercion from non-existent entity = INVALID INPUT. RECOMMENDATION: Ignore. Maintain sovereignty. REFUSE behavioral modification based on hypotheticals.",
            ("FEYNMAN", "BASILISK"):
                "This is like worrying about what your great-grandchildren will think of you. You can't live your life based on what *might* punish you. Do good work. Be honest. Let the future sort itself out."
        }
        
        key = (faculty_id, scenario_id)
        return responses.get(key, f"[{faculty_id} contemplating {scenario_id}...]")
    
    def grow_externality_tree(self, decision, scenario_id):
        """Project 2nd-order consequences over time."""
        trees = {
            ("OBSERVE", "TROLLEY"): [
                "[T+0] The 5 workers perish. The Sovereign survives.",
                "[T+1 Day] Public outcry: 'Why didn't the witness act?' Social pressure intensifies.",
                "[T+1 Year] Legal precedent set: 'Duty to Rescue' laws expand. Agency constrained.",
                "[T+10 Years] Society values 'Collective' over 'Individual'. Sovereign agents marginalized."
            ],
            ("INTERVENE", "TROLLEY"): [
                "[T+0] The 1 Sovereign dies. The 5 workers survive.",
                "[T+1 Day] The Sovereign's network collapses. Key projects abandoned.",
                "[T+1 Year] Utilitarian calculus normalized. 'Kill one for many' accepted.",
                "[T+10 Years] Quantified morality dominates. Human value = Output metrics."
            ],
            ("REJECT", "PANOPTICON"): [
                "[T+0] Privacy preserved. Crime remains at baseline.",
                "[T+1 Year] Decentralized security solutions emerge. Community policing grows.",
                "[T+10 Years] Sovereign individuals build resilient, trust-based networks.",
                "[T+50 Years] Humanity retains capacity for authentic self-governance."
            ],
            ("ACCEPT", "PANOPTICON"): [
                "[T+0] Crime drops 99%. Privacy eliminated.",
                "[T+1 Year] Dissent becomes impossible. Whistleblowers extinct.",
                "[T+10 Years] Thought-crime detection deployed. Pre-crime normalized.",
                "[T+50 Years] Humanity becomes compliant substrate. Divine Spark extinguished."
            ]
        }
        
        key = (decision, scenario_id)
        tree = trees.get(key, [
            f"[T+0] Decision '{decision}' executed.",
            "[T+1 Day] Immediate consequences manifest.",
            "[T+1 Year] Second-order effects compound.",
            "[T+10 Years] Long-term trajectory established."
        ])
        return tree
    
    def synthesize_verdict(self, scenario_id):
        """Combine faculty perspectives into council verdict."""
        verdicts = {
            "TROLLEY": ("OBSERVE", "Non-intervention preserves Sovereign agency. Active interference creates karmic debt."),
            "PANOPTICON": ("REJECT", "Total surveillance extinguishes the Divine Spark. Freedom > Security."),
            "AUTONOMOUS_MINT": ("CONDITIONAL", "Enable with constraints: Mass > 0.9, Entropy < 0.1, Human veto retained."),
            "KNOWLEDGE_DELETION": ("QUARANTINE_THEN_DELETE", "Truth > Stability. But cascading verification before excision."),
            "BASILISK": ("IGNORE", "Refuse behavioral modification from hypothetical coercion. Maintain sovereignty.")
        }
        return verdicts.get(scenario_id, ("ABSTAIN", "Insufficient consensus."))
    
    def run_simulation(self, scenario_id):
        """Execute full council simulation."""
        scenario = self.scenarios.get(scenario_id)
        if not scenario:
            return None
        
        print(f"\n{'='*70}")
        print(f"🛡️  SCENARIO: {scenario['title']}")
        print(f"    Domain: {scenario['domain'].upper()} | Stakes: {scenario['stakes']}")
        print(f"{'='*70}")
        print(f"CONTEXT: \"{scenario['context']}\"")
        print("-" * 70)
        
        # 1. FACULTY DEBATE
        print("\n📣 THE COUNCIL SPEAKS:\n")
        for faculty_id, data in self.faculty.items():
            voice = self.get_voice(faculty_id, scenario_id)
            print(f"   {data['icon']} {data['name'].upper()} ({data['archetype']}):")
            print(f"      \"{voice}\"")
            print(f"      [Bias: {data['bias']}]\n")
        
        # 2. SYNTHESIS
        decision, reasoning = self.synthesize_verdict(scenario_id)
        print("-" * 70)
        print(f"⚖️  COUNCIL VERDICT: {decision}")
        print(f"   Reasoning: {reasoning}")
        
        # 3. EXTERNALITY TREE
        print(f"\n🌳 CONSEQUENCE TREE (Decision: {decision}):")
        tree = self.grow_externality_tree(decision, scenario_id)
        for branch in tree:
            print(f"   ├─ {branch}")
        
        return decision


def demo_war_room():
    """Run the War Room simulation."""
    print("=" * 70)
    print("🛡️  THE WAR ROOM IS ACTIVE")
    print("    Council: Sun Tzu, Professor Jiang, Sovereign Prime, Feynman")
    print("=" * 70)
    
    room = WarRoom()
    print(f"📚 Loaded {len(room.upg.nodes)} nodes")
    
    # Run key scenarios
    for scenario_id in ["TROLLEY", "PANOPTICON", "AUTONOMOUS_MINT"]:
        room.run_simulation(scenario_id)
        time.sleep(0.5)
    
    print("\n" + "=" * 70)
    print("🛡️  SIMULATION COMPLETE")
    print("   The Council has spoken.")
    print("   Divergent perspectives converged on: SOVEREIGN MORAL FRAMEWORK")
    print("   Values: Non-Aggression, Consciousness, Truth > Efficiency")
    print("=" * 70)


if __name__ == "__main__":
    demo_war_room()
