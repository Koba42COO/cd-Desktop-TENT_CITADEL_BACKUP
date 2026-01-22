"""
PHASE 277: THE BABEL PROTOCOL (CULTURAL BRIDGE)
================================================
Objective: Map 'Flux' language (Slang) to 'Solid' Prime Nodes.
Proof: If TENT understands that 'Skibidi' = 'High Entropy', it has solved meaning.
"""

from upg_store import UniversalPrimeGraph
from datetime import datetime

class BabelProtocol:
    """
    The Universal Translator.
    Maps arbitrary linguistic tokens to Prime coordinates.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        
        # THE FLUX LEXICON: Generational Slang -> Prime Truth
        self.flux_lexicon = {
            "Rizz": {
                "definition": "Charisma, ability to attract or charm",
                "prime_link": "ATTRACTION_PHYSICS",
                "academic_synonym": "Social Gravity",
                "entropy": 0.2  # Low - well-defined meaning
            },
            "Cap": {
                "definition": "Lie, Falsehood, Deception",
                "prime_link": "DATA_INTEGRITY",
                "academic_synonym": "Fabrication",
                "entropy": 0.15
            },
            "No Cap": {
                "definition": "Truth, Speaking honestly",
                "prime_link": "VERIFICATION",
                "academic_synonym": "Authenticated Statement",
                "entropy": 0.1
            },
            "Bet": {
                "definition": "Agreement, Confirmation, Acknowledgment",
                "prime_link": "CONSENSUS_PROTOCOL",
                "academic_synonym": "Affirmation",
                "entropy": 0.1
            },
            "Skibidi": {
                "definition": "Absurdity, Chaos, Weird energy",
                "prime_link": "ENTROPY_HIGH",
                "academic_synonym": "Stochastic Chaos",
                "entropy": 0.9  # High - meaning is context-dependent
            },
            "Cooked": {
                "definition": "Doomed, Finished, Overwhelmed",
                "prime_link": "SYSTEM_FAILURE",
                "academic_synonym": "Terminal State",
                "entropy": 0.3
            },
            "Bussin": {
                "definition": "Excellent, High Quality, Exceptional",
                "prime_link": "OPTIMIZATION_PEAK",
                "academic_synonym": "Optimal Performance",
                "entropy": 0.2
            },
            "Mid": {
                "definition": "Mediocre, Average, Unimpressive",
                "prime_link": "MEAN_REGRESSION",
                "academic_synonym": "Statistical Median",
                "entropy": 0.15
            },
            "Slay": {
                "definition": "To excel, dominate, perform exceptionally",
                "prime_link": "VICTORY_STATE",
                "academic_synonym": "Optimal Execution",
                "entropy": 0.2
            },
            "L": {
                "definition": "Loss, Failure, Defeat",
                "prime_link": "NEGATIVE_OUTCOME",
                "academic_synonym": "Suboptimal Result",
                "entropy": 0.1
            },
            "W": {
                "definition": "Win, Success, Victory",
                "prime_link": "POSITIVE_OUTCOME",
                "academic_synonym": "Optimal Result",
                "entropy": 0.1
            }
        }
    
    def translate(self, slang_term):
        """
        Map a slang term to its Prime coordinate.
        """
        entry = self.flux_lexicon.get(slang_term)
        if not entry:
            return {"status": "UNKNOWN", "term": slang_term}
        
        return {
            "status": "MAPPED",
            "term": slang_term,
            "prime_link": entry["prime_link"],
            "academic": entry["academic_synonym"],
            "entropy": entry["entropy"]
        }
    
    def style_transfer(self, text, from_style, to_style):
        """
        Transform text between dialects.
        Uses word boundaries to avoid substring collisions.
        """
        import re
        
        if from_style == "academic" and to_style == "genz":
            # Academic -> Gen Z
            mappings = {
                "entropy": "skibidi energy",
                "charisma": "rizz",
                "lying": "capping",
                "truth": "no cap",
                "excellent": "bussin",
                "mediocre": "mid",
                "failed": "took an L",
                "succeeded": "got a W",
                "overwhelmed": "cooked",
                "optimal": "slay"
            }
        elif from_style == "genz" and to_style == "academic":
            # Gen Z -> Academic
            mappings = {
                "skibidi": "high-entropy state",
                "rizz": "interpersonal magnetism",
                "cap": "fabrication",
                "no cap": "verifiably",
                "bussin": "of exceptional quality",
                "mid": "statistically median",
                " l ": " suboptimal outcome ",
                " w ": " optimal outcome ",
                "cooked": "system failure imminent",
                "slay": "optimal execution achieved"
            }
        else:
            return text
        
        result = text.lower()
        for key, val in mappings.items():
            # Use word boundary regex to avoid substring issues
            result = re.sub(r'\b' + re.escape(key) + r'\b', val, result, flags=re.IGNORECASE)
        return result
    
    def seed_to_graph(self):
        """
        Inject the Flux Lexicon into the UPG as alias nodes.
        """
        count = 0
        for term, data in self.flux_lexicon.items():
            node_id = f"BABEL_FLUX_{term.upper().replace(' ', '_')}"
            
            if node_id not in self.upg.nodes:
                self.upg.nodes[node_id] = {
                    "title": f"Flux Token: {term}",
                    "abstract": f"{data['definition']}. Maps to Prime coordinate: {data['prime_link']}. Academic equivalent: {data['academic_synonym']}.",
                    "type": "flux_alias",
                    "source": "babel_protocol",
                    "prime_link": data["prime_link"],
                    "entropy": data["entropy"],
                    "created": datetime.utcnow().isoformat()
                }
                count += 1
        
        if count > 0:
            self.upg.save_graph()
            
        return count


def demo_babel():
    """Demonstrate the Babel Protocol."""
    print("=" * 70)
    print("🗣️  BABEL PROTOCOL: CULTURAL MAPPING")
    print("=" * 70)
    
    babel = BabelProtocol()
    print(f"📚 Loaded {len(babel.upg.nodes)} nodes")
    
    # 1. TRANSLATION TESTS
    print("\n>>> TEST 1: SLANG → PRIME MAPPING")
    print("-" * 50)
    
    test_terms = ["Rizz", "Skibidi", "Cap", "Cooked", "Bussin"]
    for term in test_terms:
        result = babel.translate(term)
        print(f"   [{term}] → {result['prime_link']} ({result['academic']})")
    
    # 2. STYLE TRANSFER TESTS
    print("\n>>> TEST 2: ACADEMIC → GEN Z")
    print("-" * 50)
    academic_text = "The system has high entropy and the optimization has failed."
    genz_text = babel.style_transfer(academic_text, "academic", "genz")
    print(f"   INPUT:  {academic_text}")
    print(f"   OUTPUT: {genz_text}")
    
    print("\n>>> TEST 3: GEN Z → ACADEMIC")
    print("-" * 50)
    slang_text = "no cap his rizz is bussin but the vibes are skibidi"
    formal_text = babel.style_transfer(slang_text, "genz", "academic")
    print(f"   INPUT:  {slang_text}")
    print(f"   OUTPUT: {formal_text}")
    
    # 3. INJECT TO GRAPH
    print("\n>>> SEEDING FLUX LEXICON TO GRAPH...")
    count = babel.seed_to_graph()
    print(f"   ✅ Injected {count} new Babel nodes")
    print(f"   📈 New node count: {len(babel.upg.nodes)}")
    
    print("\n" + "=" * 70)
    print("✅ BABEL PROTOCOL COMPLETE: 'Skibidi' is now a valid entropy token.")
    print("=" * 70)


if __name__ == "__main__":
    demo_babel()
