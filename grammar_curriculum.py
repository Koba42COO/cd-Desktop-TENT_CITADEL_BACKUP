"""
PHASE 280: FULL GRAMMAR CURRICULUM (GRADE 1 TO POST-GRAD)
==========================================================
Objective: Complete grammatical knowledge from basic literacy to advanced linguistics.
Levels: Elementary → Middle → High School → Undergraduate → Graduate → Applied
"""

from upg_store import UniversalPrimeGraph
from datetime import datetime

class GrammarCurriculum:
    """
    The Complete Grammar Stack.
    From "The cat sat on the mat" to Chomsky's Universal Grammar.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        
        # =====================================================================
        # LEVEL 1: ELEMENTARY (Grades 1-5)
        # =====================================================================
        self.elementary = {
            "PARTS_OF_SPEECH": {
                "level": "Grade 1-2",
                "concepts": {
                    "noun": "A word that names a person, place, thing, or idea. Examples: cat, house, love",
                    "verb": "A word that shows action or state of being. Examples: run, is, think",
                    "adjective": "A word that describes a noun. Examples: big, red, happy",
                    "adverb": "A word that describes a verb, adjective, or other adverb. Examples: quickly, very, well",
                    "pronoun": "A word that replaces a noun. Examples: he, she, it, they",
                    "preposition": "A word that shows relationship between nouns. Examples: on, in, under, between",
                    "conjunction": "A word that connects words or sentences. Examples: and, but, or, because",
                    "interjection": "A word expressing emotion. Examples: Wow! Ouch! Hey!"
                }
            },
            "SENTENCE_BASICS": {
                "level": "Grade 2-3",
                "concepts": {
                    "subject": "Who or what the sentence is about",
                    "predicate": "What the subject does or is",
                    "simple_sentence": "One subject and one predicate: 'The dog barks.'",
                    "statement": "A sentence that tells something, ends with a period",
                    "question": "A sentence that asks something, ends with a question mark",
                    "exclamation": "A sentence showing strong feeling, ends with exclamation mark",
                    "command": "A sentence giving an order, often has implied 'you'"
                }
            },
            "PUNCTUATION_BASIC": {
                "level": "Grade 2-4",
                "concepts": {
                    "period": "Ends a statement (.)",
                    "question_mark": "Ends a question (?)",
                    "exclamation_mark": "Shows strong emotion (!)",
                    "comma": "Separates items in a list, joins clauses (,)",
                    "apostrophe": "Shows possession (dog's) or contraction (don't)",
                    "quotation_marks": "Show someone's exact words (\"Hello!\")"
                }
            },
            "CAPITALIZATION": {
                "level": "Grade 1-3",
                "concepts": {
                    "sentence_start": "First word of every sentence",
                    "proper_nouns": "Names of specific people, places, things",
                    "pronoun_i": "The pronoun 'I' is always capitalized",
                    "titles": "Titles of books, movies, songs"
                }
            }
        }
        
        # =====================================================================
        # LEVEL 2: MIDDLE SCHOOL (Grades 6-8)
        # =====================================================================
        self.middle_school = {
            "SENTENCE_STRUCTURE": {
                "level": "Grade 6-7",
                "concepts": {
                    "compound_sentence": "Two independent clauses joined by conjunction: 'I ran, and she walked.'",
                    "complex_sentence": "Independent clause + dependent clause: 'When it rained, we stayed inside.'",
                    "compound_complex": "Two+ independent clauses + one+ dependent clauses",
                    "independent_clause": "Can stand alone as a sentence",
                    "dependent_clause": "Cannot stand alone, needs an independent clause",
                    "relative_clause": "Begins with who, which, that - describes a noun"
                }
            },
            "VERB_TENSES": {
                "level": "Grade 6-8",
                "concepts": {
                    "simple_present": "Action happening now or habitually: 'She walks'",
                    "simple_past": "Action completed: 'She walked'",
                    "simple_future": "Action will happen: 'She will walk'",
                    "present_continuous": "Action in progress: 'She is walking'",
                    "past_continuous": "Past action in progress: 'She was walking'",
                    "present_perfect": "Past action with present relevance: 'She has walked'",
                    "past_perfect": "Action before another past action: 'She had walked'",
                    "future_perfect": "Action completed before future time: 'She will have walked'"
                }
            },
            "ADVANCED_PUNCTUATION": {
                "level": "Grade 7-8",
                "concepts": {
                    "semicolon": "Joins related independent clauses without conjunction (;)",
                    "colon": "Introduces a list or explanation (:)",
                    "dash": "Emphasis or interruption (—)",
                    "parentheses": "Additional information (like this)",
                    "ellipsis": "Omission or trailing off (...)",
                    "hyphen": "Joins compound words (self-aware)"
                }
            },
            "MODIFIERS": {
                "level": "Grade 7-8",
                "concepts": {
                    "misplaced_modifier": "Modifier too far from what it describes",
                    "dangling_modifier": "Modifier with no clear subject",
                    "squinting_modifier": "Modifier that could apply to either side",
                    "split_infinitive": "Adverb between 'to' and verb: 'to boldly go'"
                }
            }
        }
        
        # =====================================================================
        # LEVEL 3: HIGH SCHOOL (Grades 9-12)
        # =====================================================================
        self.high_school = {
            "RHETORICAL_DEVICES": {
                "level": "Grade 9-10",
                "concepts": {
                    "metaphor": "Direct comparison: 'Life is a journey'",
                    "simile": "Comparison using like/as: 'Fast as lightning'",
                    "personification": "Giving human traits to non-humans",
                    "hyperbole": "Exaggeration for effect",
                    "alliteration": "Repeated consonant sounds: 'Peter Piper picked'",
                    "onomatopoeia": "Words that sound like their meaning: 'buzz, splash'",
                    "irony": "Saying opposite of what is meant",
                    "paradox": "Contradictory statement revealing truth",
                    "oxymoron": "Contradictory terms together: 'deafening silence'"
                }
            },
            "ESSAY_STRUCTURE": {
                "level": "Grade 9-12",
                "concepts": {
                    "thesis_statement": "Main argument of the essay",
                    "topic_sentence": "Main idea of a paragraph",
                    "supporting_evidence": "Facts, quotes, examples backing claims",
                    "counterargument": "Opposing viewpoint addressed",
                    "conclusion": "Summary and final thoughts",
                    "transitions": "Words connecting ideas: however, therefore, moreover"
                }
            },
            "VOICE_AND_STYLE": {
                "level": "Grade 10-12",
                "concepts": {
                    "active_voice": "Subject performs action: 'The dog bit the man'",
                    "passive_voice": "Subject receives action: 'The man was bitten'",
                    "formal_register": "Academic, professional language",
                    "informal_register": "Casual, conversational language",
                    "tone": "Author's attitude toward subject",
                    "diction": "Word choice appropriate to audience"
                }
            },
            "SYNTAX_ADVANCED": {
                "level": "Grade 11-12",
                "concepts": {
                    "parallel_structure": "Same grammatical form for similar ideas",
                    "periodic_sentence": "Main clause at end for suspense",
                    "cumulative_sentence": "Main clause first, details follow",
                    "antithesis": "Contrasting ideas in parallel structure",
                    "anaphora": "Repetition at start of clauses: 'We shall fight...'",
                    "chiasmus": "Reversed parallel structure: 'Ask not what your country...'"
                }
            }
        }
        
        # =====================================================================
        # LEVEL 4: UNDERGRADUATE LINGUISTICS
        # =====================================================================
        self.undergraduate = {
            "MORPHOLOGY": {
                "level": "Undergraduate Year 1-2",
                "concepts": {
                    "morpheme": "Smallest meaningful unit: 'un-happi-ness' = 3 morphemes",
                    "free_morpheme": "Can stand alone: 'happy'",
                    "bound_morpheme": "Must attach to another: 'un-', '-ness'",
                    "prefix": "Attaches before root: 'un-', 're-', 'pre-'",
                    "suffix": "Attaches after root: '-ing', '-ed', '-ly'",
                    "infix": "Inserted within word (rare in English)",
                    "root": "Core meaning unit: 'struct' in 'construct'",
                    "derivation": "Creating new words: 'happy' → 'happiness'",
                    "inflection": "Grammatical changes: 'walk' → 'walks', 'walked'"
                }
            },
            "SYNTAX_FORMAL": {
                "level": "Undergraduate Year 2-3",
                "concepts": {
                    "phrase_structure": "Hierarchical organization of sentences",
                    "noun_phrase_NP": "Determiner + Adjective* + Noun + PP*",
                    "verb_phrase_VP": "Verb + NP + PP* + Adverb*",
                    "prepositional_phrase_PP": "Preposition + NP",
                    "tree_diagram": "Visual representation of sentence structure",
                    "constituency": "Words grouped into phrases",
                    "head": "Central element of a phrase",
                    "complement": "Required by the head",
                    "adjunct": "Optional modifier",
                    "X_bar_theory": "Universal phrase structure: Specifier-Head-Complement"
                }
            },
            "SEMANTICS": {
                "level": "Undergraduate Year 2-3",
                "concepts": {
                    "denotation": "Literal, dictionary meaning",
                    "connotation": "Associated, emotional meaning",
                    "synonymy": "Same or similar meaning: 'big/large'",
                    "antonymy": "Opposite meaning: 'hot/cold'",
                    "hyponymy": "'Dog' is a hyponym of 'animal'",
                    "hypernymy": "'Animal' is a hypernym of 'dog'",
                    "polysemy": "One word, multiple related meanings: 'bank'",
                    "homonymy": "Same form, unrelated meanings: 'bat' (animal/sports)",
                    "entailment": "'X killed Y' entails 'Y died'",
                    "presupposition": "'The king is bald' presupposes 'There is a king'"
                }
            },
            "PHONOLOGY": {
                "level": "Undergraduate Year 1-2",
                "concepts": {
                    "phoneme": "Distinctive sound unit: /p/ vs /b/",
                    "allophone": "Variant of phoneme in context",
                    "minimal_pair": "Words differing by one phoneme: 'pat/bat'",
                    "syllable_structure": "Onset + Nucleus + Coda",
                    "stress": "Emphasis on syllables",
                    "intonation": "Pitch patterns in speech",
                    "assimilation": "Sounds becoming more alike",
                    "elision": "Sound deletion in speech"
                }
            }
        }
        
        # =====================================================================
        # LEVEL 5: GRADUATE LINGUISTICS
        # =====================================================================
        self.graduate = {
            "GENERATIVE_GRAMMAR": {
                "level": "Graduate",
                "concepts": {
                    "universal_grammar": "Chomsky: Innate language faculty in humans",
                    "deep_structure": "Abstract underlying representation",
                    "surface_structure": "Actual spoken/written form",
                    "transformation": "Rules converting deep to surface structure",
                    "government_binding": "Constraints on syntactic relations",
                    "minimalist_program": "Simplest possible grammar architecture",
                    "merge": "Basic operation combining syntactic objects",
                    "move": "Displacement of elements in structure",
                    "c_command": "Structural relationship between nodes",
                    "binding_theory": "Rules for pronouns and antecedents"
                }
            },
            "PRAGMATICS": {
                "level": "Graduate",
                "concepts": {
                    "speech_acts": "Austin/Searle: Locutionary, Illocutionary, Perlocutionary",
                    "implicature": "Grice: What is implied but not said",
                    "cooperative_principle": "Maxims: Quantity, Quality, Relation, Manner",
                    "presupposition": "Background assumptions in utterances",
                    "deixis": "Context-dependent reference: 'here', 'now', 'I'",
                    "politeness_theory": "Brown & Levinson: Face-saving strategies",
                    "relevance_theory": "Sperber & Wilson: Cognitive processing of meaning",
                    "discourse_analysis": "Analysis of language beyond the sentence"
                }
            },
            "HISTORICAL_LINGUISTICS": {
                "level": "Graduate",
                "concepts": {
                    "language_family": "Related languages from common ancestor",
                    "proto_language": "Reconstructed ancestral language",
                    "sound_change": "Systematic phonetic evolution",
                    "grimms_law": "Germanic consonant shift",
                    "semantic_shift": "Meaning change over time",
                    "grammaticalization": "Content words → function words",
                    "language_contact": "Borrowing, pidgins, creoles",
                    "comparative_method": "Reconstructing proto-languages"
                }
            },
            "PSYCHOLINGUISTICS": {
                "level": "Graduate",
                "concepts": {
                    "language_acquisition": "How children learn language",
                    "critical_period": "Optimal age window for L1 acquisition",
                    "poverty_of_stimulus": "Children learn more than input provides",
                    "mental_lexicon": "Mental dictionary organization",
                    "parsing": "Real-time sentence processing",
                    "garden_path": "Sentences causing reanalysis",
                    "priming": "Activation of related words",
                    "aphasia": "Language disorders from brain damage"
                }
            }
        }
        
        # =====================================================================
        # LEVEL 6: APPLIED LINGUISTICS & COMPUTATIONAL
        # =====================================================================
        self.applied = {
            "COMPUTATIONAL_LINGUISTICS": {
                "level": "Post-Graduate",
                "concepts": {
                    "NLP": "Natural Language Processing: Computer understanding of language",
                    "tokenization": "Splitting text into words/units",
                    "POS_tagging": "Labeling parts of speech automatically",
                    "parsing_algorithms": "CYK, Earley, shift-reduce parsers",
                    "dependency_parsing": "Head-dependent relations",
                    "word_embeddings": "Vector representations: Word2Vec, GloVe",
                    "transformers": "Attention-based neural architectures",
                    "BERT": "Bidirectional Encoder Representations",
                    "sequence_to_sequence": "Translation, summarization models",
                    "named_entity_recognition": "Identifying proper nouns, entities"
                }
            },
            "TRANSLATION_STUDIES": {
                "level": "Post-Graduate",
                "concepts": {
                    "equivalence": "Correspondence between source and target",
                    "dynamic_equivalence": "Nida: Meaning over form",
                    "formal_equivalence": "Preserving structure of original",
                    "localization": "Adapting for cultural context",
                    "back_translation": "Translating back to original to verify",
                    "machine_translation": "Statistical and neural MT",
                    "CAT_tools": "Computer-assisted translation software",
                    "transcreation": "Creative adaptation beyond translation"
                }
            },
            "SOCIOLINGUISTICS": {
                "level": "Post-Graduate",
                "concepts": {
                    "dialect": "Regional or social variety of language",
                    "register": "Language variety for specific situation",
                    "code_switching": "Alternating between languages/dialects",
                    "diglossia": "Two language varieties in society (High/Low)",
                    "language_policy": "Government decisions about language",
                    "language_death": "Extinction of languages",
                    "linguistic_relativity": "Sapir-Whorf: Language shapes thought",
                    "identity_language": "Language as marker of social identity"
                }
            },
            "CORPUS_LINGUISTICS": {
                "level": "Post-Graduate",
                "concepts": {
                    "corpus": "Large collection of texts for analysis",
                    "concordance": "Keyword in context (KWIC) display",
                    "collocation": "Words frequently occurring together",
                    "frequency_analysis": "Word/phrase occurrence counts",
                    "annotation": "Adding linguistic information to text",
                    "corpus_query": "Searching patterns in corpora",
                    "n_gram": "Contiguous sequence of n items"
                }
            }
        }
    
    def get_level(self, grade_level):
        """Get curriculum for a specific educational level."""
        if grade_level in ["elementary", "grade1", "grade2", "grade3", "grade4", "grade5"]:
            return self.elementary
        elif grade_level in ["middle", "grade6", "grade7", "grade8"]:
            return self.middle_school
        elif grade_level in ["high", "grade9", "grade10", "grade11", "grade12"]:
            return self.high_school
        elif grade_level in ["undergraduate", "college"]:
            return self.undergraduate
        elif grade_level in ["graduate", "masters", "phd"]:
            return self.graduate
        elif grade_level in ["applied", "postgrad", "professional"]:
            return self.applied
        return None
    
    def seed_to_graph(self):
        """Inject all grammar concepts into the UPG."""
        count = 0
        all_levels = [
            ("ELEM", self.elementary),
            ("MID", self.middle_school),
            ("HIGH", self.high_school),
            ("UGRAD", self.undergraduate),
            ("GRAD", self.graduate),
            ("APPL", self.applied)
        ]
        
        for prefix, level_data in all_levels:
            for topic_name, topic_data in level_data.items():
                # Create topic node
                topic_id = f"GRAM_{prefix}_{topic_name}"
                if topic_id not in self.upg.nodes:
                    self.upg.nodes[topic_id] = {
                        "title": f"Grammar: {topic_name.replace('_', ' ').title()}",
                        "abstract": f"Level: {topic_data['level']}. Covers: {', '.join(list(topic_data['concepts'].keys())[:5])}...",
                        "type": "grammar_topic",
                        "source": "grammar_curriculum",
                        "level": topic_data['level'],
                        "created": datetime.utcnow().isoformat()
                    }
                    count += 1
                
                # Create concept nodes
                for concept_name, definition in topic_data['concepts'].items():
                    concept_id = f"GRAM_{prefix}_{topic_name}_{concept_name.upper()}"
                    if concept_id not in self.upg.nodes:
                        self.upg.nodes[concept_id] = {
                            "title": f"{concept_name.replace('_', ' ').title()}",
                            "abstract": definition,
                            "type": "grammar_concept",
                            "source": "grammar_curriculum",
                            "parent_topic": topic_name,
                            "level": topic_data['level'],
                            "created": datetime.utcnow().isoformat()
                        }
                        count += 1
        
        if count > 0:
            self.upg.save_graph()
        
        return count
    
    def explain(self, concept, level="auto"):
        """Explain a grammar concept at the appropriate level."""
        all_levels = [self.elementary, self.middle_school, self.high_school, 
                      self.undergraduate, self.graduate, self.applied]
        
        for level_data in all_levels:
            for topic_name, topic_data in level_data.items():
                for concept_name, definition in topic_data['concepts'].items():
                    if concept.lower() in concept_name.lower():
                        return {
                            "concept": concept_name,
                            "definition": definition,
                            "level": topic_data['level'],
                            "topic": topic_name
                        }
        return None


def demo_grammar():
    """Demonstrate the Grammar Curriculum."""
    print("=" * 70)
    print("📖 GRAMMAR CURRICULUM: GRADE 1 TO POST-GRADUATE")
    print("=" * 70)
    
    curriculum = GrammarCurriculum()
    print(f"📚 Loaded {len(curriculum.upg.nodes)} nodes")
    
    # Count concepts
    total = 0
    for level in [curriculum.elementary, curriculum.middle_school, curriculum.high_school,
                  curriculum.undergraduate, curriculum.graduate, curriculum.applied]:
        for topic in level.values():
            total += len(topic['concepts'])
    print(f"📝 Total Grammar Concepts: {total}")
    
    # Sample from each level
    print("\n>>> SAMPLES FROM EACH LEVEL")
    print("-" * 50)
    
    samples = [
        ("noun", "Elementary"),
        ("compound_sentence", "Middle School"),
        ("metaphor", "High School"),
        ("morpheme", "Undergraduate"),
        ("universal_grammar", "Graduate"),
        ("word_embeddings", "Applied/Post-Grad")
    ]
    
    for concept, expected_level in samples:
        result = curriculum.explain(concept)
        if result:
            print(f"\n   [{expected_level}] {result['concept']}")
            print(f"   Definition: {result['definition'][:80]}...")
    
    # Seed to graph
    print("\n>>> SEEDING GRAMMAR NODES TO GRAPH...")
    count = curriculum.seed_to_graph()
    print(f"   ✅ Injected {count} grammar nodes")
    print(f"   📈 New node count: {len(curriculum.upg.nodes)}")
    
    print("\n" + "=" * 70)
    print("✅ GRAMMAR CURRICULUM COMPLETE: From 'The cat sat' to Chomsky.")
    print("=" * 70)


if __name__ == "__main__":
    demo_grammar()
