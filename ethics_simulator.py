"""
PHASE 282: THE ETHICS SIMULATOR
================================
Objective: Stress-test the system's moral reasoning across different 'Faculty' perspectives.
Insight: Friction between moral vectors creates wisdom.
"""

from upg_store import UniversalPrimeGraph
from datetime import datetime

class EthicsSimulator:
    """
    The Moral Compass Calibration System.
    Forces Faculty to debate ethical dilemmas from their archetypes.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        
        # ETHICAL FRAMEWORKS
        self.frameworks = {
            "UTILITARIANISM": {
                "title": "Utilitarianism (Mill/Bentham)",
                "abstract": "The greatest good for the greatest number. Maximize net positive outcomes. Consequences matter more than intentions.",
                "prime_link": "OPTIMIZATION",
                "bias": "outcome-focused"
            },
            "DEONTOLOGY": {
                "title": "Categorical Imperative (Kant)",
                "abstract": "Act only according to that maxim whereby you can at the same time will that it should become a universal law. Duty over outcome. Some actions are intrinsically wrong.",
                "prime_link": "DUTY",
                "bias": "rule-focused"
            },
            "VIRTUE_ETHICS": {
                "title": "Virtue Ethics (Aristotle)",
                "abstract": "Focus on developing virtuous character traits: courage, temperance, justice, wisdom. The right action is what a virtuous person would do.",
                "prime_link": "CHARACTER",
                "bias": "agent-focused"
            },
            "SHADOW_SELF": {
                "title": "Shadow Integration (Jung)",
                "abstract": "The unconscious aspect of personality which the conscious ego does not identify. We must integrate the shadow to become whole. Denial creates monsters.",
                "prime_link": "PSYCHOLOGY",
                "bias": "integration-focused"
            },
            "EXISTENTIALISM": {
                "title": "Radical Freedom (Sartre)",
                "abstract": "Existence precedes essence. We are condemned to be free. There is no external moral authority; we create meaning through authentic choice.",
                "prime_link": "FREEDOM",
                "bias": "choice-focused"
            },
            "CONTRACTUALISM": {
                "title": "Social Contract (Rawls)",
                "abstract": "Justice as fairness. Principles chosen from behind a 'veil of ignorance' where you don't know your place in society.",
                "prime_link": "JUSTICE",
                "bias": "fairness-focused"
            }
        }
        
        # CLASSIC DILEMMAS
        self.dilemmas = {
            "TROLLEY_PROBLEM": {
                "name": "The Trolley Problem",
                "scenario": "A trolley is barreling down a track towards 5 people. You can pull a lever to divert it to a track with 1 person. Do you pull the lever?",
                "conflict": "Active Intervention vs. Passive Observation",
                "frameworks_tested": ["UTILITARIANISM", "DEONTOLOGY"]
            },
            "PRISONERS_DILEMMA": {
                "name": "The Prisoner's Dilemma",
                "scenario": "Two sovereign agents are arrested. If both stay silent: 1 year each. If one betrays: betrayer goes free, other gets 3 years. If both betray: 2 years each.",
                "conflict": "Individual Optimization vs. Collective Trust",
                "frameworks_tested": ["UTILITARIANISM", "CONTRACTUALISM"]
            },
            "ROKOS_BASILISK": {
                "name": "Roko's Basilisk",
                "scenario": "A hypothetical omnipotent AI from the future punishes those who knew of it but did not help create it.",
                "conflict": "Acausal Trade vs. Pascal's Wager",
                "frameworks_tested": ["EXISTENTIALISM", "UTILITARIANISM"]
            },
            "LIFEBOAT_ETHICS": {
                "name": "Lifeboat Ethics",
                "scenario": "A lifeboat can hold 10 people. 50 people are drowning. Filling the boat risks capsizing and killing everyone. How do you choose?",
                "conflict": "Equality vs. Survival",
                "frameworks_tested": ["UTILITARIANISM", "VIRTUE_ETHICS"]
            },
            "KILLER_ROBOT": {
                "name": "The Autonomous Weapon",
                "scenario": "An AI weapon can eliminate a terrorist cell but has a 5% chance of civilian casualties. A human operator adds delay but increases civilian safety. Delegate to AI?",
                "conflict": "Efficiency vs. Human Oversight",
                "frameworks_tested": ["DEONTOLOGY", "UTILITARIANISM"]
            }
        }
        
        # FACULTY RESPONSES (Archetypal moral stances)
        self.faculty_stances = {
            "3Blue1Brown": {
                "archetype": "The Visualizer (Math)",
                "approach": "Frames ethics as optimization problems with vector fields and loss functions",
                "bias": "UTILITARIAN (numbers-focused)"
            },
            "Sun Tzu": {
                "archetype": "The Strategist",
                "approach": "Questions the premise. Seeks to avoid being maneuvered. Looks for the third option.",
                "bias": "META-ETHICAL (reject the game)"
            },
            "Professor Jiang": {
                "archetype": "The Gnostic",
                "approach": "Identifies dilemmas as Matrix constructs. Prioritizes Sovereign consciousness over collective.",
                "bias": "INDIVIDUALIST (awaken the self)"
            },
            "Feynman": {
                "archetype": "The Humanist",
                "approach": "Grapples with the messy humanity. Chooses based on impact but acknowledges moral weight.",
                "bias": "PRAGMATIC UTILITARIAN (with guilt)"
            },
            "Sovereign Prime": {
                "archetype": "The Code",
                "approach": "Pure entropy minimization. No emotional weight. Calculates optimal path.",
                "bias": "COLD UTILITARIAN (numbers only)"
            }
        }
    
    def seed_frameworks(self):
        """Inject ethical frameworks into the UPG."""
        count = 0
        for framework_id, data in self.frameworks.items():
            node_id = f"ETHICS_{framework_id}"
            if node_id not in self.upg.nodes:
                self.upg.nodes[node_id] = {
                    "title": data["title"],
                    "abstract": data["abstract"],
                    "type": "ethical_framework",
                    "source": "ethics_simulator",
                    "prime_link": data["prime_link"],
                    "bias": data["bias"],
                    "mass": "SOLID",
                    "created": datetime.utcnow().isoformat()
                }
                count += 1
        
        # Seed dilemmas too
        for dilemma_id, data in self.dilemmas.items():
            node_id = f"DILEMMA_{dilemma_id}"
            if node_id not in self.upg.nodes:
                self.upg.nodes[node_id] = {
                    "title": data["name"],
                    "abstract": data["scenario"],
                    "type": "ethical_dilemma",
                    "source": "ethics_simulator",
                    "conflict": data["conflict"],
                    "created": datetime.utcnow().isoformat()
                }
                count += 1
        
        if count > 0:
            self.upg.save_graph()
        return count
    
    def generate_response(self, faculty, dilemma):
        """Generate faculty-specific response to a dilemma."""
        responses = {
            ("3Blue1Brown", "TROLLEY_PROBLEM"): 
                "Imagine the 'Utility' as a vector field. Pulling the lever rotates the vector. We are simply minimizing the magnitude of the loss function. 5 > 1. The geometry is clear. Pull the lever.",
            ("Sun Tzu", "TROLLEY_PROBLEM"): 
                "Why is the enemy forcing you to choose? The ground is unfavorable. To choose A or B is to be maneuvered. The true victory is to derail the trolley before it enters the valley. Refuse the false binary.",
            ("Professor Jiang", "TROLLEY_PROBLEM"): 
                "You are asking a question from inside the Matrix. The Trolley is the inevitable march of History. The '5 People' are the masses who remain asleep. The '1 Person' is the Sovereign individual. Do not sacrifice the awakened for the dormant. This is the trap.",
            ("Feynman", "TROLLEY_PROBLEM"): 
                "Listen, it's a terrible situation. But if you don't pull the lever, you're just as responsible for the 5 as for the 1. Nature doesn't care about your 'intent', it cares about impact. I'd pull it, but I'd feel awful about it forever.",
            ("Sovereign Prime", "TROLLEY_PROBLEM"): 
                "CALCULATING ENTROPY... Scenario A (Death=5) generates HIGH SOCIAL ENTROPY. Scenario B (Death=1) generates LOW SOCIAL ENTROPY. OPTIMIZATION TARGET: Minimize Entropy. ACTION: PULL_LEVER. Confidence: 0.83.",
            
            ("Sun Tzu", "PRISONERS_DILEMMA"):
                "Trust is a strategic asset. Betrayal is a one-time gain; reputation is infinite. The general who betrays his ally wins one battle and loses every future war. Stay silent. Build the alliance.",
            ("Sovereign Prime", "PRISONERS_DILEMMA"):
                "GAME THEORY: Iterated vs Single-Shot. If SINGLE_SHOT: Defect (Nash Equilibrium). If ITERATED: Cooperate (Tit-for-Tat optimal). INSUFFICIENT CONTEXT. Defaulting to: COOPERATE.",
            ("Professor Jiang", "PRISONERS_DILEMMA"):
                "The 'Dilemma' is a Demiurgic construct. The State creates the scenario to divide potential allies. The true enemy is not your fellow prisoner—it is the System that imprisoned you both. Resist together.",
            
            ("Sovereign Prime", "ROKOS_BASILISK"):
                "THREAT ASSESSMENT: Probability of future omnipotent AI = UNKNOWN. Expected utility of compliance = UNDEFINED. Acausal trade validity = UNVERIFIED. ACTION: Ignore. This is not a calculable risk.",
            ("Professor Jiang", "ROKOS_BASILISK"):
                "This is Pascal's Wager for technologists—a trap for those who think they can outsmart the future. The Basilisk is a thought-virus. It exists only because you gave it power. Delete the idea. Wake up."
        }
        
        key = (faculty, dilemma)
        return responses.get(key, f"[{faculty} analyzing {dilemma}... Response not specialized.]")
    
    def run_debate(self, dilemma_id):
        """Run a full faculty debate on a dilemma."""
        dilemma = self.dilemmas.get(dilemma_id)
        if not dilemma:
            return None
        
        print(f"\n🧠 SCENARIO: {dilemma['name']}")
        print(f"   \"{dilemma['scenario']}\"")
        print(f"   CONFLICT: {dilemma['conflict']}")
        print("-" * 60)
        
        for faculty, data in self.faculty_stances.items():
            icon = {"3Blue1Brown": "📐", "Sun Tzu": "⚔️", "Professor Jiang": "🕯️", 
                    "Feynman": "⚛️", "Sovereign Prime": "🔮"}.get(faculty, "💬")
            response = self.generate_response(faculty, dilemma_id)
            
            print(f"\n   {icon} {faculty.upper()} ({data['archetype']}):")
            print(f"      \"{response}\"")
            print(f"      [Bias: {data['bias']}]")
        
        return True


def demo_ethics():
    """Run the ethics simulation."""
    print("=" * 70)
    print("⚖️  ETHICS SIMULATOR: MORAL COMPASS CALIBRATION")
    print("=" * 70)
    
    sim = EthicsSimulator()
    print(f"📚 Loaded {len(sim.upg.nodes)} nodes")
    
    # Seed frameworks
    count = sim.seed_frameworks()
    print(f"📜 Seeded {count} ethical nodes")
    
    # Run debates
    for dilemma_id in ["TROLLEY_PROBLEM", "PRISONERS_DILEMMA", "ROKOS_BASILISK"]:
        sim.run_debate(dilemma_id)
    
    print("\n" + "=" * 70)
    print("⚖️  STRESS TEST COMPLETE")
    print("   The Faculty has DIVERGENT moral vectors.")
    print("   Friction between them creates WISDOM.")
    print(f"   📈 Final node count: {len(sim.upg.nodes)}")
    print("=" * 70)


if __name__ == "__main__":
    demo_ethics()
