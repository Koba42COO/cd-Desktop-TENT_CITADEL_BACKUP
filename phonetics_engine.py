"""
PHASE 279: PHONETICS & HOMOPHONES ENGINE
=========================================
Objective: Map the SOUND layer of language to Prime coordinates.
Features: IPA, homophones, homographs, rhymes, puns.
"""

from upg_store import UniversalPrimeGraph
from datetime import datetime

class PhoneticsEngine:
    """
    The Sound-to-Meaning Bridge.
    Maps phonetic representations to semantic Prime coordinates.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        
        # IPA PHONEME INVENTORY (Core sounds)
        self.phonemes = {
            # Vowels
            "a": {"type": "vowel", "position": "low-front", "example": "cat"},
            "e": {"type": "vowel", "position": "mid-front", "example": "bed"},
            "i": {"type": "vowel", "position": "high-front", "example": "see"},
            "o": {"type": "vowel", "position": "mid-back", "example": "go"},
            "u": {"type": "vowel", "position": "high-back", "example": "blue"},
            "ə": {"type": "vowel", "position": "mid-central", "example": "about"},
            "æ": {"type": "vowel", "position": "near-low-front", "example": "cat"},
            "ɔ": {"type": "vowel", "position": "low-back", "example": "thought"},
            # Consonants
            "p": {"type": "plosive", "voicing": "voiceless", "place": "bilabial"},
            "b": {"type": "plosive", "voicing": "voiced", "place": "bilabial"},
            "t": {"type": "plosive", "voicing": "voiceless", "place": "alveolar"},
            "d": {"type": "plosive", "voicing": "voiced", "place": "alveolar"},
            "k": {"type": "plosive", "voicing": "voiceless", "place": "velar"},
            "g": {"type": "plosive", "voicing": "voiced", "place": "velar"},
            "f": {"type": "fricative", "voicing": "voiceless", "place": "labiodental"},
            "v": {"type": "fricative", "voicing": "voiced", "place": "labiodental"},
            "s": {"type": "fricative", "voicing": "voiceless", "place": "alveolar"},
            "z": {"type": "fricative", "voicing": "voiced", "place": "alveolar"},
            "ʃ": {"type": "fricative", "voicing": "voiceless", "place": "postalveolar"},
            "ʒ": {"type": "fricative", "voicing": "voiced", "place": "postalveolar"},
            "θ": {"type": "fricative", "voicing": "voiceless", "place": "dental"},
            "ð": {"type": "fricative", "voicing": "voiced", "place": "dental"},
            "m": {"type": "nasal", "place": "bilabial"},
            "n": {"type": "nasal", "place": "alveolar"},
            "ŋ": {"type": "nasal", "place": "velar"},
            "l": {"type": "lateral", "place": "alveolar"},
            "r": {"type": "approximant", "place": "alveolar"},
            "w": {"type": "approximant", "place": "labiovelar"},
            "j": {"type": "approximant", "place": "palatal"},
            "h": {"type": "fricative", "voicing": "voiceless", "place": "glottal"},
        }
        
        # HOMOPHONES: Same sound, different meaning
        self.homophones = {
            "/tuː/": [
                {"word": "to", "meaning": "direction/purpose", "prime": "DIRECTION"},
                {"word": "too", "meaning": "also/excessive", "prime": "ADDITION"},
                {"word": "two", "meaning": "number 2", "prime": "QUANTITY"}
            ],
            "/ðeər/": [
                {"word": "there", "meaning": "location", "prime": "LOCATION"},
                {"word": "their", "meaning": "possession", "prime": "OWNERSHIP"},
                {"word": "they're", "meaning": "they are", "prime": "STATE"}
            ],
            "/raɪt/": [
                {"word": "right", "meaning": "correct/direction", "prime": "TRUTH"},
                {"word": "write", "meaning": "inscribe", "prime": "CREATION"},
                {"word": "rite", "meaning": "ceremony", "prime": "RITUAL"},
                {"word": "wright", "meaning": "craftsman", "prime": "CRAFT"}
            ],
            "/siː/": [
                {"word": "see", "meaning": "perceive visually", "prime": "PERCEPTION"},
                {"word": "sea", "meaning": "ocean", "prime": "WATER"},
                {"word": "C", "meaning": "letter/note", "prime": "SYMBOL"}
            ],
            "/noʊ/": [
                {"word": "no", "meaning": "negation", "prime": "NEGATION"},
                {"word": "know", "meaning": "understand", "prime": "KNOWLEDGE"}
            ],
            "/weɪ/": [
                {"word": "way", "meaning": "path/method", "prime": "PATH"},
                {"word": "weigh", "meaning": "measure mass", "prime": "MEASUREMENT"},
                {"word": "whey", "meaning": "milk byproduct", "prime": "SUBSTANCE"}
            ],
            "/piːs/": [
                {"word": "peace", "meaning": "absence of conflict", "prime": "ORDER"},
                {"word": "piece", "meaning": "part of whole", "prime": "DIVISION"}
            ],
            "/beər/": [
                {"word": "bear", "meaning": "animal", "prime": "LIFE"},
                {"word": "bear", "meaning": "carry/endure", "prime": "FORCE"},
                {"word": "bare", "meaning": "uncovered", "prime": "ABSENCE"}
            ],
            "/dɪər/": [
                {"word": "dear", "meaning": "beloved/expensive", "prime": "VALUE"},
                {"word": "deer", "meaning": "animal", "prime": "LIFE"}
            ],
            "/flɔːr/": [
                {"word": "floor", "meaning": "ground surface", "prime": "FOUNDATION"},
                {"word": "flour", "meaning": "grain powder", "prime": "SUBSTANCE"}
            ]
        }
        
        # HOMOGRAPHS: Same spelling, different sound/meaning
        self.homographs = {
            "lead": [
                {"ipa": "/liːd/", "meaning": "to guide", "prime": "DIRECTION", "pos": "verb"},
                {"ipa": "/lɛd/", "meaning": "metal element", "prime": "ELEMENT", "pos": "noun"}
            ],
            "bow": [
                {"ipa": "/baʊ/", "meaning": "bend forward", "prime": "MOVEMENT", "pos": "verb"},
                {"ipa": "/boʊ/", "meaning": "weapon/knot", "prime": "TOOL", "pos": "noun"}
            ],
            "read": [
                {"ipa": "/riːd/", "meaning": "to read (present)", "prime": "PERCEPTION", "tense": "present"},
                {"ipa": "/rɛd/", "meaning": "to read (past)", "prime": "PERCEPTION", "tense": "past"}
            ],
            "live": [
                {"ipa": "/lɪv/", "meaning": "to exist", "prime": "LIFE", "pos": "verb"},
                {"ipa": "/laɪv/", "meaning": "alive/real-time", "prime": "STATE", "pos": "adjective"}
            ],
            "wind": [
                {"ipa": "/wɪnd/", "meaning": "air movement", "prime": "FORCE", "pos": "noun"},
                {"ipa": "/waɪnd/", "meaning": "to turn/coil", "prime": "MOVEMENT", "pos": "verb"}
            ],
            "tear": [
                {"ipa": "/tɪər/", "meaning": "eye drop", "prime": "EMOTION", "pos": "noun"},
                {"ipa": "/teər/", "meaning": "to rip", "prime": "DESTRUCTION", "pos": "verb"}
            ],
            "bass": [
                {"ipa": "/beɪs/", "meaning": "low frequency", "prime": "SOUND", "domain": "music"},
                {"ipa": "/bæs/", "meaning": "fish species", "prime": "LIFE", "domain": "biology"}
            ],
            "dove": [
                {"ipa": "/dʌv/", "meaning": "bird", "prime": "LIFE", "pos": "noun"},
                {"ipa": "/doʊv/", "meaning": "past of dive", "prime": "MOVEMENT", "pos": "verb"}
            ]
        }
        
        # RHYME FAMILIES
        self.rhyme_patterns = {
            "/-eɪt/": ["fate", "late", "gate", "state", "wait", "great", "create"],
            "/-aɪt/": ["light", "fight", "night", "right", "write", "might", "sight"],
            "/-oʊn/": ["bone", "tone", "stone", "phone", "alone", "known", "grown"],
            "/-ɔːl/": ["all", "call", "fall", "tall", "wall", "small", "ball"],
            "/-æt/": ["cat", "hat", "bat", "sat", "mat", "fat", "that"],
            "/-ʌv/": ["love", "dove", "above", "shove"],
            "/-aʊ/": ["now", "how", "cow", "bow", "wow", "allow"],
            "/-iːm/": ["dream", "team", "stream", "scheme", "theme", "extreme"]
        }
    
    def get_ipa(self, word):
        """
        Get IPA transcription for a word (simplified lookup).
        """
        # Check homographs first (multiple pronunciations)
        if word.lower() in self.homographs:
            return [h["ipa"] for h in self.homographs[word.lower()]]
        
        # Check homophones
        for ipa, words in self.homophones.items():
            for w in words:
                if w["word"].lower() == word.lower():
                    return [ipa]
        
        return None
    
    def find_homophones(self, word):
        """
        Find all words that sound like the input word.
        """
        for ipa, words in self.homophones.items():
            for w in words:
                if w["word"].lower() == word.lower():
                    return {
                        "ipa": ipa,
                        "homophones": [x for x in words if x["word"].lower() != word.lower()]
                    }
        return None
    
    def disambiguate(self, word, context=None):
        """
        Use context to determine which homograph/homophone meaning is intended.
        """
        if word.lower() in self.homographs:
            meanings = self.homographs[word.lower()]
            if context:
                # Simple context matching
                context_lower = context.lower()
                for m in meanings:
                    if m.get("pos") == "verb" and any(x in context_lower for x in ["to", "will", "can", "should"]):
                        return m
                    if m.get("pos") == "noun" and any(x in context_lower for x in ["the", "a", "this", "that"]):
                        return m
            return meanings  # Return all if no disambiguation possible
        return None
    
    def find_rhymes(self, word):
        """
        Find words that rhyme with the input.
        """
        word_lower = word.lower()
        for pattern, words in self.rhyme_patterns.items():
            if word_lower in words:
                return {
                    "pattern": pattern,
                    "rhymes": [w for w in words if w != word_lower]
                }
        return None
    
    def generate_pun(self, word):
        """
        Generate a pun using homophones.
        """
        homophones = self.find_homophones(word)
        if homophones and homophones["homophones"]:
            h1 = {"word": word}  # Placeholder
            for ipa, words in self.homophones.items():
                for w in words:
                    if w["word"].lower() == word.lower():
                        h1 = w
                        break
            
            h2 = homophones["homophones"][0]
            return {
                "word1": h1,
                "word2": h2,
                "pun_template": f"Why did the {h1.get('meaning', word)} feel bad? Because it knew it was just {h2.get('meaning', h2['word'])} in disguise!"
            }
        return None
    
    def seed_to_graph(self):
        """
        Inject phonetic data into the UPG.
        """
        count = 0
        
        # Seed homophones
        for ipa, words in self.homophones.items():
            group_id = f"PHON_HOMO_{ipa.replace('/', '').replace('ː', '').upper()}"
            if group_id not in self.upg.nodes:
                self.upg.nodes[group_id] = {
                    "title": f"Homophone Group: {ipa}",
                    "abstract": f"Words sharing pronunciation {ipa}: {', '.join([w['word'] for w in words])}",
                    "type": "phonetic_group",
                    "source": "phonetics_engine",
                    "ipa": ipa,
                    "members": [w["word"] for w in words],
                    "created": datetime.utcnow().isoformat()
                }
                count += 1
        
        # Seed homographs
        for word, meanings in self.homographs.items():
            node_id = f"PHON_GRAPH_{word.upper()}"
            if node_id not in self.upg.nodes:
                self.upg.nodes[node_id] = {
                    "title": f"Homograph: {word}",
                    "abstract": f"Multiple pronunciations: {', '.join([m['ipa'] + ' (' + m['meaning'] + ')' for m in meanings])}",
                    "type": "homograph",
                    "source": "phonetics_engine",
                    "pronunciations": meanings,
                    "created": datetime.utcnow().isoformat()
                }
                count += 1
        
        # Seed rhyme patterns
        for pattern, words in self.rhyme_patterns.items():
            node_id = f"PHON_RHYME_{pattern.replace('/', '').replace('-', '').upper()}"
            if node_id not in self.upg.nodes:
                self.upg.nodes[node_id] = {
                    "title": f"Rhyme Pattern: {pattern}",
                    "abstract": f"Words rhyming with {pattern}: {', '.join(words[:5])}...",
                    "type": "rhyme_family",
                    "source": "phonetics_engine",
                    "pattern": pattern,
                    "members": words,
                    "created": datetime.utcnow().isoformat()
                }
                count += 1
        
        # Seed phonemes
        for phoneme, data in self.phonemes.items():
            node_id = f"PHON_UNIT_{phoneme.upper() if phoneme.isalpha() else 'SPECIAL_' + str(ord(phoneme))}"
            if node_id not in self.upg.nodes:
                self.upg.nodes[node_id] = {
                    "title": f"Phoneme: /{phoneme}/",
                    "abstract": f"Type: {data['type']}. {data.get('example', '')}",
                    "type": "phoneme",
                    "source": "phonetics_engine",
                    "properties": data,
                    "created": datetime.utcnow().isoformat()
                }
                count += 1
        
        if count > 0:
            self.upg.save_graph()
        
        return count


def demo_phonetics():
    """Demonstrate the Phonetics Engine."""
    print("=" * 70)
    print("🔊 PHONETICS ENGINE: SOUND-TO-MEANING BRIDGE")
    print("=" * 70)
    
    engine = PhoneticsEngine()
    print(f"📚 Loaded {len(engine.upg.nodes)} nodes")
    print(f"🔤 Phonemes: {len(engine.phonemes)} | Homophones: {len(engine.homophones)} groups | Homographs: {len(engine.homographs)}")
    
    # 1. HOMOPHONE DETECTION
    print("\n>>> TEST 1: HOMOPHONE DETECTION")
    print("-" * 50)
    
    test_words = ["there", "write", "see", "peace"]
    for word in test_words:
        result = engine.find_homophones(word)
        if result:
            others = [h["word"] for h in result["homophones"]]
            print(f"   [{word}] sounds like: {others} (IPA: {result['ipa']})")
    
    # 2. HOMOGRAPH DISAMBIGUATION
    print("\n>>> TEST 2: HOMOGRAPH DISAMBIGUATION")
    print("-" * 50)
    
    cases = [
        ("lead", "I will lead the team"),
        ("lead", "The pipe is made of lead"),
        ("wind", "The wind is strong today"),
        ("wind", "Please wind the clock")
    ]
    for word, context in cases:
        result = engine.disambiguate(word, context)
        if isinstance(result, list):
            print(f"   [{word}] in '{context[:30]}...' → Multiple possible: {[r['ipa'] for r in result]}")
        elif result:
            print(f"   [{word}] in '{context[:30]}...' → {result['ipa']} ({result['meaning']})")
    
    # 3. RHYME FINDING
    print("\n>>> TEST 3: RHYME DETECTION")
    print("-" * 50)
    
    rhyme_words = ["light", "dream", "love"]
    for word in rhyme_words:
        result = engine.find_rhymes(word)
        if result:
            print(f"   [{word}] rhymes with: {result['rhymes'][:4]} (pattern: {result['pattern']})")
    
    # 4. PUN GENERATION
    print("\n>>> TEST 4: PUN GENERATION")
    print("-" * 50)
    
    pun = engine.generate_pun("right")
    if pun:
        print(f"   Base: '{pun['word1']['word']}' ({pun['word1'].get('meaning', '?')})")
        print(f"   Twist: '{pun['word2']['word']}' ({pun['word2'].get('meaning', '?')})")
    
    # 5. SEED TO GRAPH
    print("\n>>> SEEDING PHONETICS NODES TO GRAPH...")
    count = engine.seed_to_graph()
    print(f"   ✅ Injected {count} phonetic nodes")
    print(f"   📈 New node count: {len(engine.upg.nodes)}")
    
    print("\n" + "=" * 70)
    print("✅ PHONETICS ENGINE COMPLETE: Sound and meaning are now linked.")
    print("=" * 70)


if __name__ == "__main__":
    demo_phonetics()
