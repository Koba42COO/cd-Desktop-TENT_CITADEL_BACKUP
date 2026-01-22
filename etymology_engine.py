"""
PHASE 278: FULL CROSS-LANGUAGE ETYMOLOGY ENGINE
================================================
Objective: Map words across ALL languages to shared Prime coordinates.
Insight: All human languages encode the same fundamental truths differently.
"""

from upg_store import UniversalPrimeGraph
from datetime import datetime

class EtymologyEngine:
    """
    The Universal Semantic Core.
    Maps words from any language to their Prime meaning through etymological roots.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        
        # THE PRIME CONCEPTS (Language-Independent Truths)
        self.prime_concepts = {
            "FIRE": {
                "essence": "Transformation through heat, energy release",
                "physics_link": "COMBUSTION, PLASMA_STATE",
                "roots": {
                    "english": "fire",
                    "latin": "ignis",
                    "greek": "πῦρ (pyr)",
                    "sanskrit": "अग्नि (agni)",
                    "german": "Feuer",
                    "spanish": "fuego",
                    "japanese": "火 (hi)",
                    "chinese": "火 (huǒ)",
                    "arabic": "نار (nar)",
                    "hindi": "आग (aag)"
                }
            },
            "WATER": {
                "essence": "Fluidity, life-giving, adaptation",
                "physics_link": "LIQUID_STATE, H2O_MOLECULE",
                "roots": {
                    "english": "water",
                    "latin": "aqua",
                    "greek": "ὕδωρ (hydor)",
                    "sanskrit": "जल (jala)",
                    "german": "Wasser",
                    "spanish": "agua",
                    "japanese": "水 (mizu)",
                    "chinese": "水 (shuǐ)",
                    "arabic": "ماء (ma')",
                    "hindi": "पानी (paani)"
                }
            },
            "TRUTH": {
                "essence": "Alignment with reality, verification",
                "physics_link": "DATA_INTEGRITY, VERIFICATION",
                "roots": {
                    "english": "truth",
                    "latin": "veritas",
                    "greek": "ἀλήθεια (aletheia)",
                    "sanskrit": "सत्य (satya)",
                    "german": "Wahrheit",
                    "spanish": "verdad",
                    "japanese": "真実 (shinjitsu)",
                    "chinese": "真理 (zhēnlǐ)",
                    "arabic": "حقيقة (haqiqa)",
                    "hindi": "सत्य (satya)"
                }
            },
            "KNOWLEDGE": {
                "essence": "Verified information, understanding",
                "physics_link": "INFORMATION_THEORY, ENTROPY_LOW",
                "roots": {
                    "english": "knowledge",
                    "latin": "scientia",
                    "greek": "γνῶσις (gnosis)",
                    "sanskrit": "ज्ञान (jnana)",
                    "german": "Wissen",
                    "spanish": "conocimiento",
                    "japanese": "知識 (chishiki)",
                    "chinese": "知識 (zhīshì)",
                    "arabic": "علم (ilm)",
                    "hindi": "ज्ञान (gyaan)"
                }
            },
            "LOVE": {
                "essence": "Attraction, bonding, care",
                "physics_link": "ATTRACTION_PHYSICS, BONDING_ENERGY",
                "roots": {
                    "english": "love",
                    "latin": "amor",
                    "greek": "ἀγάπη (agape), ἔρως (eros)",
                    "sanskrit": "प्रेम (prema)",
                    "german": "Liebe",
                    "spanish": "amor",
                    "japanese": "愛 (ai)",
                    "chinese": "愛 (ài)",
                    "arabic": "حب (hub)",
                    "hindi": "प्रेम (prem)"
                }
            },
            "DEATH": {
                "essence": "Transformation, entropy increase, cycle completion",
                "physics_link": "ENTROPY_MAX, STATE_TRANSITION",
                "roots": {
                    "english": "death",
                    "latin": "mors",
                    "greek": "θάνατος (thanatos)",
                    "sanskrit": "मृत्यु (mrityu)",
                    "german": "Tod",
                    "spanish": "muerte",
                    "japanese": "死 (shi)",
                    "chinese": "死 (sǐ)",
                    "arabic": "موت (mawt)",
                    "hindi": "मृत्यु (mrityu)"
                }
            },
            "LIGHT": {
                "essence": "Electromagnetic radiation, visibility, clarity",
                "physics_link": "PHOTON, ELECTROMAGNETIC_SPECTRUM",
                "roots": {
                    "english": "light",
                    "latin": "lux",
                    "greek": "φῶς (phos)",
                    "sanskrit": "प्रकाश (prakasha)",
                    "german": "Licht",
                    "spanish": "luz",
                    "japanese": "光 (hikari)",
                    "chinese": "光 (guāng)",
                    "arabic": "نور (nur)",
                    "hindi": "प्रकाश (prakash)"
                }
            },
            "MIND": {
                "essence": "Consciousness, information processing, awareness",
                "physics_link": "NEURAL_NETWORK, COMPUTATION",
                "roots": {
                    "english": "mind",
                    "latin": "mens",
                    "greek": "νοῦς (nous)",
                    "sanskrit": "मनस् (manas)",
                    "german": "Geist",
                    "spanish": "mente",
                    "japanese": "心 (kokoro)",
                    "chinese": "心 (xīn)",
                    "arabic": "عقل (aql)",
                    "hindi": "मन (man)"
                }
            },
            "CHAOS": {
                "essence": "Disorder, unpredictability, high entropy",
                "physics_link": "ENTROPY_HIGH, STOCHASTIC",
                "roots": {
                    "english": "chaos",
                    "latin": "chaos",
                    "greek": "χάος (khaos)",
                    "sanskrit": "अव्यवस्था (avyavastha)",
                    "german": "Chaos",
                    "spanish": "caos",
                    "japanese": "混沌 (konton)",
                    "chinese": "混沌 (hùndùn)",
                    "arabic": "فوضى (fawda)",
                    "hindi": "अराजकता (arajakta)",
                    "genz": "skibidi"  # Cross-generational link!
                }
            },
            "ORDER": {
                "essence": "Structure, predictability, low entropy",
                "physics_link": "ENTROPY_LOW, CRYSTALLINE",
                "roots": {
                    "english": "order",
                    "latin": "ordo",
                    "greek": "κόσμος (kosmos)",
                    "sanskrit": "व्यवस्था (vyavastha)",
                    "german": "Ordnung",
                    "spanish": "orden",
                    "japanese": "秩序 (chitsujo)",
                    "chinese": "秩序 (zhìxù)",
                    "arabic": "نظام (nizam)",
                    "hindi": "व्यवस्था (vyavastha)"
                }
            },
            "POWER": {
                "essence": "Energy transfer rate, influence, capability",
                "physics_link": "WATTS, FORCE_APPLIED",
                "roots": {
                    "english": "power",
                    "latin": "potentia",
                    "greek": "δύναμις (dynamis)",
                    "sanskrit": "शक्ति (shakti)",
                    "german": "Macht",
                    "spanish": "poder",
                    "japanese": "力 (chikara)",
                    "chinese": "力 (lì)",
                    "arabic": "قوة (quwa)",
                    "hindi": "शक्ति (shakti)"
                }
            },
            "TIME": {
                "essence": "Sequence of events, entropy direction",
                "physics_link": "TEMPORAL_DIMENSION, ARROW_OF_TIME",
                "roots": {
                    "english": "time",
                    "latin": "tempus",
                    "greek": "χρόνος (chronos)",
                    "sanskrit": "काल (kala)",
                    "german": "Zeit",
                    "spanish": "tiempo",
                    "japanese": "時 (toki)",
                    "chinese": "時 (shí)",
                    "arabic": "وقت (waqt)",
                    "hindi": "समय (samay)"
                }
            }
        }
    
    def lookup(self, word, language="auto"):
        """
        Find the Prime concept for any word in any language.
        """
        word_lower = word.lower()
        
        for concept_id, data in self.prime_concepts.items():
            for lang, root in data["roots"].items():
                if language != "auto" and lang != language:
                    continue
                if word_lower in root.lower():
                    return {
                        "word": word,
                        "language": lang,
                        "prime_concept": concept_id,
                        "essence": data["essence"],
                        "physics_link": data["physics_link"],
                        "cognates": data["roots"]
                    }
        
        return {"word": word, "status": "NOT_FOUND"}
    
    def translate_via_prime(self, word, from_lang, to_lang):
        """
        Translate by finding the shared Prime concept, not dictionary lookup.
        """
        lookup = self.lookup(word, from_lang)
        if lookup.get("status") == "NOT_FOUND":
            return {"error": f"Unknown word: {word}"}
        
        target_word = lookup["cognates"].get(to_lang)
        return {
            "source": f"{word} ({from_lang})",
            "target": f"{target_word} ({to_lang})",
            "prime_bridge": lookup["prime_concept"],
            "essence": lookup["essence"]
        }
    
    def show_etymology_tree(self, concept_id):
        """
        Display the full etymology tree for a Prime concept.
        """
        if concept_id not in self.prime_concepts:
            return None
        
        data = self.prime_concepts[concept_id]
        return {
            "concept": concept_id,
            "essence": data["essence"],
            "physics": data["physics_link"],
            "languages": data["roots"]
        }
    
    def seed_to_graph(self):
        """
        Inject all etymology nodes into the UPG.
        """
        count = 0
        for concept_id, data in self.prime_concepts.items():
            node_id = f"ETYM_{concept_id}"
            
            if node_id not in self.upg.nodes:
                # Create the Prime concept node
                self.upg.nodes[node_id] = {
                    "title": f"Etymology: {concept_id}",
                    "abstract": f"{data['essence']}. Physics: {data['physics_link']}",
                    "type": "etymology_root",
                    "source": "etymology_engine",
                    "languages": list(data["roots"].keys()),
                    "cognates": data["roots"],
                    "created": datetime.utcnow().isoformat()
                }
                count += 1
                
                # Create language-specific alias nodes
                for lang, word in data["roots"].items():
                    alias_id = f"ETYM_{concept_id}_{lang.upper()}"
                    if alias_id not in self.upg.nodes:
                        self.upg.nodes[alias_id] = {
                            "title": f"{word} ({lang})",
                            "abstract": f"{lang.capitalize()} word for {concept_id}. Root: {word}",
                            "type": "etymology_alias",
                            "source": "etymology_engine",
                            "parent_concept": concept_id,
                            "language": lang,
                            "created": datetime.utcnow().isoformat()
                        }
                        count += 1
        
        if count > 0:
            self.upg.save_graph()
        
        return count


def demo_etymology():
    """Demonstrate the Etymology Engine."""
    print("=" * 70)
    print("📜 ETYMOLOGY ENGINE: CROSS-LANGUAGE PRIME MAPPING")
    print("=" * 70)
    
    engine = EtymologyEngine()
    print(f"📚 Loaded {len(engine.upg.nodes)} nodes")
    print(f"🌍 Prime Concepts: {len(engine.prime_concepts)}")
    
    # 1. LOOKUP TESTS
    print("\n>>> TEST 1: WORD LOOKUP (ANY LANGUAGE)")
    print("-" * 50)
    
    test_words = ["fire", "πῦρ", "agni", "火", "Feuer", "fuego"]
    for word in test_words:
        result = engine.lookup(word)
        if result.get("prime_concept"):
            print(f"   [{word}] → PRIME: {result['prime_concept']} | {result['essence'][:40]}...")
    
    # 2. TRANSLATION VIA PRIME
    print("\n>>> TEST 2: TRANSLATION VIA SEMANTIC BRIDGE")
    print("-" * 50)
    
    translations = [
        ("veritas", "latin", "japanese"),
        ("satya", "sanskrit", "arabic"),
        ("光", "chinese", "german"),
        ("chaos", "english", "genz")
    ]
    
    for word, from_l, to_l in translations:
        result = engine.translate_via_prime(word, from_l, to_l)
        print(f"   {result.get('source', word)} → {result.get('target', '?')} via [{result.get('prime_bridge', '?')}]")
    
    # 3. ETYMOLOGY TREE
    print("\n>>> TEST 3: FULL ETYMOLOGY TREE")
    print("-" * 50)
    
    tree = engine.show_etymology_tree("CHAOS")
    print(f"   CONCEPT: {tree['concept']}")
    print(f"   ESSENCE: {tree['essence']}")
    print(f"   COGNATES:")
    for lang, word in tree['languages'].items():
        print(f"      • {lang}: {word}")
    
    # 4. SEED TO GRAPH
    print("\n>>> SEEDING ETYMOLOGY NODES TO GRAPH...")
    count = engine.seed_to_graph()
    print(f"   ✅ Injected {count} etymology nodes")
    print(f"   📈 New node count: {len(engine.upg.nodes)}")
    
    print("\n" + "=" * 70)
    print("✅ ETYMOLOGY ENGINE COMPLETE: All languages share Prime Truth.")
    print("=" * 70)


if __name__ == "__main__":
    demo_etymology()
