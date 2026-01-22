"""
PHASE 289: LEGAL KNOWLEDGE INGESTION
=====================================
Comprehensive curriculum covering:
1. US Law (Constitution, USC, Case Law, Regulations)
2. International Law (UK, EU, Common Law, Civil Law systems)
3. Governance History (Magna Carta → Modern Constitutional Democracy)
4. Legal Philosophy (Laws as reactions to events, precedent doctrine)
"""

from datetime import datetime
from upg_store import UniversalPrimeGraph

class LegalCurriculum:
    """
    The Jurisprudence Engine.
    Seeds comprehensive legal knowledge into the Universal Prime Graph.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        
        # ========== US LAW SOURCES ==========
        self.us_law_sources = {
            # Primary Sources
            "US_CONSTITUTION": {
                "title": "United States Constitution",
                "abstract": "The supreme law of the United States. Establishes the framework of federal government with three branches: Executive, Legislative, Judicial. Includes Bill of Rights (first 10 amendments) and subsequent amendments.",
                "source": "archives.gov/constitution",
                "year": 1787,
                "type": "primary_law"
            },
            "US_CODE": {
                "title": "United States Code (USC)",
                "abstract": "The official compilation of federal statutory law. Organized into 54 Titles covering all areas of federal law from Agriculture to War.",
                "source": "uscode.house.gov",
                "type": "statutory_law"
            },
            "CODE_OF_FEDERAL_REGULATIONS": {
                "title": "Code of Federal Regulations (CFR)",
                "abstract": "The codification of rules made by federal agencies. Implements and interprets statutory law. Published by the Federal Register.",
                "source": "ecfr.gov",
                "type": "regulatory_law"
            },
            "FEDERAL_REGISTER": {
                "title": "Federal Register",
                "abstract": "Daily journal of the US government. Contains proposed rules, final rules, executive orders, and other official documents.",
                "source": "federalregister.gov",
                "type": "official_publication"
            },
            
            # Case Law
            "SUPREME_COURT_DECISIONS": {
                "title": "US Supreme Court Decisions",
                "abstract": "Binding precedent for all federal and state courts. Interprets Constitution and federal law. Available via SCOTUS blog, oyez.org, and supreme.justia.com.",
                "source": "supremecourt.gov",
                "type": "case_law"
            },
            "CIRCUIT_COURT_OPINIONS": {
                "title": "Federal Circuit Court Opinions",
                "abstract": "Appellate decisions from 13 federal circuits. Binding precedent within their circuit. Available via CourtListener and PACER.",
                "source": "courtlistener.com",
                "type": "case_law"
            },
            
            # Public Repositories
            "CONGRESS_GOV": {
                "title": "Congress.gov",
                "abstract": "Official source for US legislative information. Bills, resolutions, congressional record, committee reports. Replaces THOMAS.",
                "source": "congress.gov",
                "type": "legislative_source"
            },
            "GOVINFO": {
                "title": "GovInfo (GPO)",
                "abstract": "Government Publishing Office repository. Contains Congressional Record, Federal Register, CFR, USC, and historical documents.",
                "source": "govinfo.gov",
                "type": "official_repository"
            },
            "COURTLISTENER": {
                "title": "CourtListener / Free Law Project",
                "abstract": "Free, open database of court opinions, oral arguments, and PACER documents. Machine-readable legal data.",
                "source": "courtlistener.com",
                "type": "open_repository"
            },
            "LEGAL_INFO_INSTITUTE": {
                "title": "Cornell Legal Information Institute (LII)",
                "abstract": "Free access to US law. USC, CFR, Supreme Court opinions, and legal encyclopedias. Wex legal dictionary.",
                "source": "law.cornell.edu",
                "type": "educational_repository"
            }
        }
        
        # ========== LANDMARK US LAW ==========
        self.landmark_us_law = {
            "BILL_OF_RIGHTS": {
                "title": "Bill of Rights (1791)",
                "abstract": "First 10 amendments to Constitution. Guarantees: speech, religion, press, assembly (1st); arms (2nd); quartering (3rd); search/seizure (4th); due process (5th); fair trial (6th-8th); reserved rights (9th-10th).",
                "reactive_to": "Anti-Federalist concerns about federal overreach"
            },
            "13TH_AMENDMENT": {
                "title": "13th Amendment (1865)",
                "abstract": "Abolished slavery and involuntary servitude except as punishment for crime.",
                "reactive_to": "Civil War and abolitionist movement"
            },
            "14TH_AMENDMENT": {
                "title": "14th Amendment (1868)",
                "abstract": "Defines citizenship, due process, equal protection. Foundation for civil rights law. Incorporation doctrine applies Bill of Rights to states.",
                "reactive_to": "Post-Civil War need to protect freed slaves' rights"
            },
            "CIVIL_RIGHTS_ACT_1964": {
                "title": "Civil Rights Act of 1964",
                "abstract": "Prohibits discrimination based on race, color, religion, sex, national origin. Title VII covers employment. Title II covers public accommodations.",
                "reactive_to": "Civil Rights Movement, Jim Crow laws, MLK activism"
            },
            "VOTING_RIGHTS_ACT_1965": {
                "title": "Voting Rights Act of 1965",
                "abstract": "Prohibits racial discrimination in voting. Section 5 required preclearance for changes in covered jurisdictions (gutted by Shelby County v. Holder 2013).",
                "reactive_to": "Selma marches, ongoing voter suppression"
            },
            "SHERMAN_ANTITRUST_ACT": {
                "title": "Sherman Antitrust Act (1890)",
                "abstract": "First federal antitrust law. Prohibits monopolies and conspiracies in restraint of trade.",
                "reactive_to": "Gilded Age monopolies (Standard Oil, railroads)"
            },
            "SECURITIES_ACT_1933": {
                "title": "Securities Act of 1933",
                "abstract": "Requires registration of securities and disclosure to investors. 'Truth in securities' law.",
                "reactive_to": "Stock market crash of 1929, Great Depression"
            },
            "PATRIOT_ACT": {
                "title": "USA PATRIOT Act (2001)",
                "abstract": "Expanded surveillance, investigation, detention powers. Controversial balance of security vs. civil liberties.",
                "reactive_to": "September 11, 2001 terrorist attacks"
            },
            "DODD_FRANK": {
                "title": "Dodd-Frank Wall Street Reform Act (2010)",
                "abstract": "Financial regulation reform. Created CFPB, Volcker Rule, systemic risk oversight.",
                "reactive_to": "2008 financial crisis, bank bailouts"
            }
        }
        
        # ========== INTERNATIONAL LEGAL SYSTEMS ==========
        self.international_law = {
            # United Kingdom
            "UK_MAGNA_CARTA": {
                "title": "Magna Carta (1215)",
                "abstract": "Foundation of English constitutional law. Established rule of law, habeas corpus principles, limits on royal power. 'No free man shall be imprisoned except by lawful judgment.'",
                "jurisdiction": "UK/Common Law",
                "reactive_to": "Barons' revolt against King John's arbitrary rule"
            },
            "UK_BILL_OF_RIGHTS_1689": {
                "title": "English Bill of Rights (1689)",
                "abstract": "Established parliamentary sovereignty, free elections, freedom of speech in Parliament. Constitutional monarchy foundation.",
                "jurisdiction": "UK",
                "reactive_to": "Glorious Revolution, overthrow of James II"
            },
            "UK_HUMAN_RIGHTS_ACT": {
                "title": "Human Rights Act 1998 (UK)",
                "abstract": "Incorporates European Convention on Human Rights into UK law. Courts must interpret legislation compatibly with Convention rights.",
                "jurisdiction": "UK",
                "reactive_to": "Need to enforce ECHR domestically"
            },
            "UK_LEGISLATION_GOV": {
                "title": "legislation.gov.uk",
                "abstract": "Official UK legislation repository. Primary and secondary legislation, explanatory notes, revision tracking.",
                "source": "legislation.gov.uk",
                "type": "official_repository"
            },
            
            # European Union
            "EU_TREATIES": {
                "title": "EU Founding Treaties",
                "abstract": "Treaty of Rome (1957), Maastricht (1992), Lisbon (2007). Establish EU institutions, competencies, fundamental rights. Supremacy of EU law.",
                "jurisdiction": "EU",
                "reactive_to": "WWII devastation, desire for European integration"
            },
            "EU_CHARTER_FUNDAMENTAL_RIGHTS": {
                "title": "EU Charter of Fundamental Rights",
                "abstract": "Legally binding rights: dignity, freedoms, equality, solidarity, citizens' rights, justice. Binding on EU institutions and member states implementing EU law.",
                "jurisdiction": "EU",
                "year": 2000
            },
            "GDPR": {
                "title": "General Data Protection Regulation (GDPR)",
                "abstract": "EU data privacy regulation. Consent, data minimization, right to erasure, breach notification. Extraterritorial effect.",
                "jurisdiction": "EU",
                "year": 2018,
                "reactive_to": "Digital age privacy concerns, Cambridge Analytica"
            },
            "EUR_LEX": {
                "title": "EUR-Lex",
                "abstract": "Official EU law database. Treaties, regulations, directives, case law of Court of Justice of EU.",
                "source": "eur-lex.europa.eu",
                "type": "official_repository"
            },
            
            # Civil Law Systems
            "NAPOLEONIC_CODE": {
                "title": "Napoleonic Code (1804)",
                "abstract": "French civil code. Foundation of civil law systems worldwide. Systematic codification replacing feudal law. Influenced Louisiana, Quebec, Latin America.",
                "jurisdiction": "Civil Law",
                "reactive_to": "French Revolution, need for uniform law"
            },
            "GERMAN_CIVIL_CODE": {
                "title": "Bürgerliches Gesetzbuch (BGB)",
                "abstract": "German Civil Code (1900). Highly systematic, abstract. Influenced Japan, China, Greece, Brazil. Five books: General, Obligations, Property, Family, Succession.",
                "jurisdiction": "Civil Law"
            },
            
            # International Bodies
            "UN_CHARTER": {
                "title": "United Nations Charter (1945)",
                "abstract": "Foundational treaty of UN. Establishes Security Council, General Assembly, ICJ. Principles: sovereign equality, peaceful settlement, prohibition of force.",
                "jurisdiction": "International",
                "reactive_to": "WWII, failure of League of Nations"
            },
            "UDHR": {
                "title": "Universal Declaration of Human Rights (1948)",
                "abstract": "Foundation of international human rights law. 30 articles covering civil, political, economic, social, cultural rights. Not legally binding but customary international law.",
                "jurisdiction": "International",
                "reactive_to": "Holocaust, WWII atrocities"
            },
            "GENEVA_CONVENTIONS": {
                "title": "Geneva Conventions (1949)",
                "abstract": "International humanitarian law. Protection of wounded/sick, POWs, civilians during armed conflict. War crimes jurisdiction.",
                "jurisdiction": "International",
                "reactive_to": "WWII atrocities, need for updated laws of war"
            },
            "ICC_ROME_STATUTE": {
                "title": "Rome Statute (ICC) (1998)",
                "abstract": "Established International Criminal Court. Jurisdiction over genocide, crimes against humanity, war crimes, aggression.",
                "jurisdiction": "International",
                "reactive_to": "Rwanda genocide, Yugoslav wars"
            }
        }
        
        # ========== GOVERNANCE HISTORY ==========
        self.governance_evolution = {
            "ANCIENT_CODES": {
                "title": "Ancient Legal Codes",
                "abstract": "Code of Hammurabi (1754 BCE), Laws of Manu (India), Twelve Tables (Rome), Torah. First attempts at systematic written law. 'Eye for an eye' proportionality.",
                "era": "Ancient"
            },
            "ROMAN_LAW": {
                "title": "Roman Law Tradition",
                "abstract": "Corpus Juris Civilis (Justinian Code, 534 CE). Foundation of civil law systems. Legal persons, contracts, property, procedure. Rediscovery in medieval universities.",
                "era": "Classical/Medieval"
            },
            "FEUDAL_LAW": {
                "title": "Feudal Legal Systems",
                "abstract": "Decentralized, based on land tenure. Lord-vassal relationships. Manorial courts, ecclesiastical courts. Limited central authority.",
                "era": "Medieval"
            },
            "COMMON_LAW_ORIGIN": {
                "title": "Common Law Development",
                "abstract": "English common law from 12th century. Precedent (stare decisis), jury trials, writs system. Royal courts unified law across realm. Blackstone's Commentaries (1765).",
                "era": "Medieval-Modern"
            },
            "ENLIGHTENMENT_LAW": {
                "title": "Enlightenment Legal Philosophy",
                "abstract": "Natural rights (Locke), social contract (Rousseau), separation of powers (Montesquieu). Foundation for constitutional democracy. Influenced US and French revolutions.",
                "era": "Enlightenment"
            },
            "CONSTITUTIONAL_ERA": {
                "title": "Age of Constitutions",
                "abstract": "Written constitutions limit government power. US Constitution (1787), French Declaration (1789). Checks and balances, enumerated powers, individual rights.",
                "era": "Modern"
            },
            "INTERNATIONAL_ORDER": {
                "title": "Post-WWII International Order",
                "abstract": "United Nations, Bretton Woods, human rights framework. Multilateral institutions, international law, crime tribunals. Response to world wars.",
                "era": "Contemporary"
            }
        }
        
        # ========== LEGAL PHILOSOPHY ==========
        self.legal_philosophy = {
            "REACTIVE_NATURE": {
                "title": "Laws as Reactive Instruments",
                "abstract": "Most laws are responses to events that already occurred, not anticipatory. Pattern: Harm → Public Outcry → Legislative Response → Enforcement. Examples: Sarbanes-Oxley (Enron), GDPR (data breaches), Patriot Act (9/11).",
                "type": "legal_theory"
            },
            "STARE_DECISIS": {
                "title": "Doctrine of Precedent (Stare Decisis)",
                "abstract": "'Stand by things decided.' Courts follow prior rulings. Promotes consistency, predictability, stability. Distinguishing vs. overruling precedent.",
                "type": "legal_doctrine"
            },
            "NATURAL_LAW": {
                "title": "Natural Law Theory",
                "abstract": "Moral principles inherent in nature/reason. Higher law binds positive law. Aquinas, Locke, Finnis. 'Unjust law is no law at all.'",
                "type": "jurisprudence"
            },
            "LEGAL_POSITIVISM": {
                "title": "Legal Positivism",
                "abstract": "Law is command of sovereign backed by sanction. Separation of law and morality. Austin, Hart, Kelsen. Law is what is enacted, not what ought to be.",
                "type": "jurisprudence"
            },
            "CRITICAL_LEGAL_STUDIES": {
                "title": "Critical Legal Studies",
                "abstract": "Law is politics by other means. Legal rules are indeterminate, shaped by power. Duncan Kennedy, Roberto Unger. Deconstruction of legal reasoning.",
                "type": "jurisprudence"
            },
            "LAW_AND_ECONOMICS": {
                "title": "Law and Economics",
                "abstract": "Economic analysis of legal rules. Efficiency, incentives, transaction costs. Coase theorem, Posner. Cost-benefit analysis of legal institutions.",
                "type": "legal_theory"
            }
        }
        
        # ========== LEGAL RESOURCES ==========
        self.legal_resources = {
            # Open Access
            "GOOGLE_SCHOLAR_CASE_LAW": {
                "title": "Google Scholar Case Law",
                "abstract": "Free searchable database of US case law. Federal and state courts. Citation tracking. scholar.google.com",
                "type": "search_engine",
                "access": "free"
            },
            "JUSTIA": {
                "title": "Justia",
                "abstract": "Free legal information. US Supreme Court, federal circuits, state courts. Annotations, legal guides. justia.com",
                "type": "repository",
                "access": "free"
            },
            "OYEZ": {
                "title": "Oyez (SCOTUS Audio)",
                "abstract": "Supreme Court oral argument recordings, case summaries, justice voting records. oyez.org",
                "type": "multimedia",
                "access": "free"
            },
            "CASELAW_ACCESS_PROJECT": {
                "title": "Caselaw Access Project (Harvard)",
                "abstract": "Digitized US case law from all state and federal courts. 6.7 million cases. API access. case.law",
                "type": "open_data",
                "access": "free"
            },
            "WORLDLII": {
                "title": "World Legal Information Institute (WorldLII)",
                "abstract": "Free global legal information. Links to national legal databases worldwide. worldlii.org",
                "type": "portal",
                "access": "free"
            },
            
            # Academic/Commercial
            "WESTLAW": {
                "title": "Westlaw (Thomson Reuters)",
                "abstract": "Comprehensive legal research platform. Cases, statutes, secondary sources, citators (KeyCite). Commercial subscription.",
                "type": "commercial_database",
                "access": "subscription"
            },
            "LEXISNEXIS": {
                "title": "LexisNexis",
                "abstract": "Legal research database. Cases, statutes, law reviews, news. Shepard's Citations. Commercial subscription.",
                "type": "commercial_database",
                "access": "subscription"
            },
            "HEINONLINE": {
                "title": "HeinOnline",
                "abstract": "Law journal library. Historical legal materials, treaties, congressional documents. Academic/institutional access.",
                "type": "academic_database",
                "access": "institutional"
            }
        }
        
        # ========== MAJOR LEGAL TREATISES ==========
        self.legal_treatises = {
            "BLACKSTONE_COMMENTARIES": {
                "title": "Blackstone's Commentaries on the Laws of England (1765-1769)",
                "abstract": "Foundational English common law treatise. Organized law into Rights of Persons, Rights of Things, Private Wrongs, Public Wrongs. Influenced American founders.",
                "author": "William Blackstone"
            },
            "CORPUS_JURIS_SECONDUM": {
                "title": "Corpus Juris Secundum (CJS)",
                "abstract": "Comprehensive American legal encyclopedia. Topic-based organization with case citations. West Publishing.",
                "type": "legal_encyclopedia"
            },
            "AMERICAN_JURISPRUDENCE": {
                "title": "American Jurisprudence 2d",
                "abstract": "Legal encyclopedia covering all areas of US law. Practical guidance with forms and practice aids. LexisNexis.",
                "type": "legal_encyclopedia"
            },
            "RESTATEMENTS_OF_LAW": {
                "title": "Restatements of the Law (ALI)",
                "abstract": "American Law Institute synthesizes common law. Torts, Contracts, Property, Agency, Trusts. Influential but not binding. 'Best' rules.",
                "type": "secondary_source"
            },
            "PROSSER_TORTS": {
                "title": "Prosser and Keeton on Torts",
                "abstract": "Leading tort law treatise. Negligence, strict liability, intentional torts, defamation. Cited by courts.",
                "author": "William Prosser"
            },
            "WILLISTON_CONTRACTS": {
                "title": "Williston on Contracts",
                "abstract": "Comprehensive contract law treatise. Formation, interpretation, performance, breach, remedies.",
                "author": "Samuel Williston"
            },
            "TRIBE_CONSTITUTIONAL_LAW": {
                "title": "American Constitutional Law (Laurence Tribe)",
                "abstract": "Leading constitutional law treatise. Structure, rights, judicial review. Highly influential.",
                "author": "Laurence H. Tribe"
            }
        }
        
    def seed_all(self):
        """Seed all legal knowledge into UPG."""
        total = 0
        
        # Seed each category
        categories = [
            ("US_LAW_SOURCE", self.us_law_sources),
            ("LANDMARK_US", self.landmark_us_law),
            ("INTERNATIONAL", self.international_law),
            ("GOVERNANCE_HISTORY", self.governance_evolution),
            ("LEGAL_PHILOSOPHY", self.legal_philosophy),
            ("LEGAL_RESOURCE", self.legal_resources),
            ("LEGAL_TREATISE", self.legal_treatises)
        ]
        
        for prefix, category in categories:
            for key, data in category.items():
                node_id = f"{prefix}_{key}"
                if node_id not in self.upg.nodes:
                    self.upg.nodes[node_id] = {
                        "title": data.get("title", key),
                        "abstract": data.get("abstract", ""),
                        "type": "legal_knowledge",
                        "category": prefix,
                        "source": data.get("source", "legal_curriculum"),
                        "jurisdiction": data.get("jurisdiction", "US"),
                        "reactive_to": data.get("reactive_to", None),
                        "year": data.get("year", None),
                        "mass": "SOLID",
                        "created": datetime.utcnow().isoformat()
                    }
                    total += 1
        
        self.upg.save_graph()
        return total


def main():
    """Execute legal knowledge ingestion."""
    print("=" * 70)
    print("⚖️  LEGAL KNOWLEDGE INGESTION | PHASE 289")
    print("=" * 70)
    
    curriculum = LegalCurriculum()
    print(f"📚 Starting nodes: {len(curriculum.upg.nodes)}")
    
    count = curriculum.seed_all()
    
    print(f"\n✅ INJECTED: {count} legal nodes")
    print(f"📊 Final node count: {len(curriculum.upg.nodes)}")
    
    print("\n📖 CATEGORIES SEEDED:")
    print("   • US Law Sources (Constitution, USC, CFR, Case Law)")
    print("   • Landmark US Legislation (Bill of Rights → Dodd-Frank)")
    print("   • International Law (UK, EU, Civil Law, UN Treaties)")
    print("   • Governance History (Hammurabi → Modern)")
    print("   • Legal Philosophy (Reactive Law, Precedent, Positivism)")
    print("   • Legal Resources (Open & Commercial Databases)")
    print("   • Major Treatises (Blackstone, Prosser, Williston)")
    
    print("\n🔑 KEY INSIGHT SEEDED:")
    print("   'Laws are REACTIVE instruments - responses to harm'")
    print("   Pattern: Harm → Outcry → Legislation → Enforcement")
    print("=" * 70)


if __name__ == "__main__":
    main()
