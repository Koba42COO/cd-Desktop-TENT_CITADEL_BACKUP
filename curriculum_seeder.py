#!/usr/bin/env python3
"""
TENT CURRICULUM SEEDER
======================
Seeds a comprehensive AI/ML curriculum into the Universal Prime Graph.

18 Categories | 106 Courses | 530 Modules
"""

import json
import re
from pathlib import Path
from typing import Dict, List
from upg_store import UniversalPrimeGraph

CURRICULUM: Dict[str, Dict[str, List[str]]] = {
    "general education core": {
        "GEN101 Academic Writing and Rhetoric": ["writing process and revision", "argumentation and evidence", "style, clarity, and voice", "research literacy", "ethics of citation"],
        "GEN102 Critical Thinking and Logic": ["argument structure", "formal and informal fallacies", "inductive and deductive reasoning", "causal reasoning", "decision frameworks"],
        "GEN103 Quantitative Reasoning": ["units and dimensional analysis", "estimation and approximation", "probability in everyday decisions", "graph literacy", "modeling real-world problems"],
        "GEN104 Public Speaking": ["audience analysis", "speech structure", "visual aids", "persuasion techniques", "q and a handling"],
        "GEN105 Information Literacy": ["source credibility", "search strategies", "bias detection", "synthesis of sources", "intellectual honesty"],
        "GEN106 Ethics and Civic Responsibility": ["ethical frameworks", "stakeholder analysis", "social impact analysis", "responsible innovation", "civic institutions"],
        "GEN107 Creative Expression": ["visual arts survey", "music and performance survey", "creative writing survey", "design thinking", "portfolio critique"],
    },
    "mathematics core": {
        "MATH101 Discrete Mathematics": ["sets, functions, relations", "proof techniques", "graphs and trees", "counting and combinatorics", "recurrence relations"],
        "MATH111 Calculus I": ["limits and continuity", "derivatives and applications", "definite integrals", "fundamental theorem", "numerical integration"],
        "MATH112 Calculus II": ["techniques of integration", "series and convergence", "parametric equations", "polar coordinates", "differential equations (intro)"],
        "MATH221 Linear Algebra": ["vectors and spaces", "linear transformations", "eigenvalues and eigenvectors", "orthogonality", "matrix decompositions"],
        "MATH231 Probability and Statistics": ["distributions", "expectation and variance", "estimation", "hypothesis testing", "regression basics"],
        "MATH241 Differential Equations": ["first-order odes", "second-order odes", "systems of odes", "laplace transforms", "stability analysis"],
        "MATH301 Optimization": ["convexity", "unconstrained optimization", "constrained optimization", "duality", "numerical methods"],
        "MATH311 Stochastic Processes": ["markov chains", "poisson processes", "brownian motion", "queues", "applications"],
        "MATH321 Real Analysis (Intro)": ["metric spaces", "sequences and series", "continuity and compactness", "differentiation and integration", "convergence theorems"],
    },
    "computer science core": {
        "CS101 Programming Fundamentals": ["variables and control flow", "functions and recursion", "basic data types", "debugging practices", "complexity intuition"],
        "CS201 Data Structures": ["arrays and lists", "stacks and queues", "trees and heaps", "hash tables", "graphs"],
        "CS221 Algorithms": ["divide and conquer", "dynamic programming", "greedy algorithms", "graph algorithms", "complexity analysis"],
        "CS231 Computer Architecture": ["instruction sets", "pipelining", "memory hierarchy", "parallelism", "performance models"],
        "CS241 Operating Systems": ["processes and threads", "scheduling", "memory management", "file systems", "concurrency"],
        "CS251 Networks": ["osi and tcp-ip", "routing and congestion", "transport protocols", "network security", "distributed systems intro"],
        "CS261 Databases": ["relational models", "sql and normalization", "indexing and optimization", "transactions", "nosql overview"],
        "CS271 Software Engineering": ["requirements and design", "testing strategy", "ci/cd", "code review", "project management"],
        "CS281 Programming Languages": ["syntax and semantics", "type systems", "runtime models", "functional programming", "language implementation"],
        "CS291 Compilers (Intro)": ["lexing and parsing", "asts and ir", "optimization overview", "code generation", "tooling"],
    },
    "data science core": {
        "DS101 Data Wrangling": ["cleaning and normalization", "joins and merges", "missing data", "data quality checks", "pipelines"],
        "DS201 Exploratory Data Analysis": ["summary statistics", "distribution analysis", "correlation and association", "visualization techniques", "outlier analysis"],
        "DS221 Statistical Inference": ["sampling distributions", "confidence intervals", "hypothesis testing", "power analysis", "multiple testing"],
        "DS231 Regression Models": ["linear regression", "glms", "regularization", "model diagnostics", "feature selection"],
        "DS241 Causal Inference (Intro)": ["counterfactuals", "causal graphs", "confounding and bias", "matching and stratification", "instrumental variables (intro)"],
        "DS251 Data Visualization": ["visual encoding", "storytelling with data", "dashboard design", "accessibility", "ethical visualization"],
        "DS261 Experimentation and A/B Testing": ["experiment design", "metrics and guardrails", "sequential testing", "variance reduction", "interpreting results"],
        "DS271 Reproducible Research": ["versioning", "experiment tracking", "data lineage", "reporting pipelines", "open science practices"],
    },
    "machine learning and ai": {
        "ML201 Supervised Learning": ["linear models", "tree-based models", "bias and variance", "cross-validation", "evaluation metrics"],
        "ML211 Unsupervised Learning": ["clustering", "dimensionality reduction", "representation learning", "density estimation", "anomaly detection"],
        "ML221 Probabilistic Modeling": ["bayesian inference", "graphical models", "variational inference", "mcmc (intro)", "uncertainty estimation"],
        "ML231 Deep Learning Foundations": ["backpropagation", "optimizers", "regularization", "initialization", "training dynamics"],
        "ML241 CNNs, RNNs, Transformers": ["convolutions", "sequence modeling", "attention mechanisms", "pretraining and finetuning", "scaling effects"],
        "ML251 Generative Models": ["autoregressive models", "vaes", "gans", "diffusion models", "evaluation of generative models"],
        "ML261 Reinforcement Learning": ["mdps", "value iteration", "policy gradients", "exploration strategies", "offline rl (intro)"],
        "ML271 MLOps and Deployment": ["model serving", "monitoring and drift", "ci/cd for ml", "feature stores", "reliability practices"],
        "ML281 Interpretability": ["feature attribution", "concept analysis", "probing techniques", "mechanistic interpretability (intro)", "limitations"],
        "ML291 Robustness and Safety": ["adversarial examples", "distribution shift", "calibration and uncertainty", "alignment strategies", "red teaming"],
    },
    "systems and infrastructure": {
        "SYS201 Distributed Systems": ["consistency models", "replication", "consensus", "sharding", "failure modes"],
        "SYS211 Performance Engineering": ["profiling", "latency vs throughput", "caching", "capacity planning", "benchmarking"],
        "SYS221 Security Engineering": ["threat modeling", "authentication and authorization", "secure coding", "incident response", "security testing"],
        "SYS231 Cryptography (Applied)": ["symmetric crypto", "public-key crypto", "hashes and macs", "key management", "protocol basics"],
        "SYS241 Cloud Architecture": ["networking basics", "compute and storage", "infrastructure as code", "cost optimization", "resilience patterns"],
        "SYS251 Observability and SRE": ["logging", "metrics and tracing", "slos and slas", "incident response", "postmortems"],
        "SYS261 Storage Systems": ["b-trees and lsms", "indexing", "transactions", "replication and backups", "performance tradeoffs"],
        "SYS271 Streaming Systems": ["event time vs processing time", "windowing", "exactly-once semantics", "backpressure", "stream architectures"],
        "SYS281 API Design and Integration": ["rest and rpc", "schema design", "versioning", "rate limiting", "integration testing"],
    },
    "physics core": {
        "PHY101 Classical Mechanics": ["kinematics", "newton's laws", "work and energy", "momentum", "rotational dynamics"],
        "PHY111 Electromagnetism": ["electrostatics", "circuits", "magnetostatics", "maxwell's equations", "em waves"],
        "PHY121 Thermodynamics": ["laws of thermodynamics", "heat engines", "entropy", "phase transitions", "thermodynamic potentials"],
        "PHY201 Statistical Mechanics": ["microcanonical ensemble", "canonical ensemble", "partition functions", "fluctuations", "applications"],
        "PHY211 Quantum Mechanics": ["wavefunctions", "operators", "schrodinger equation", "angular momentum", "perturbation theory"],
        "PHY221 Optics": ["geometric optics", "wave optics", "interference and diffraction", "polarization", "lasers"],
        "PHY231 Solid-State Physics (Intro)": ["crystal structure", "band theory", "semiconductors", "phonons", "devices overview"],
    },
    "chemistry core": {
        "CHEM101 General Chemistry": ["atomic structure", "chemical bonding", "stoichiometry", "thermochemistry", "equilibrium"],
        "CHEM111 Organic Chemistry": ["structure and bonding", "reaction mechanisms", "functional groups", "stereochemistry", "spectroscopy (intro)"],
        "CHEM121 Physical Chemistry (Intro)": ["thermodynamics", "kinetics", "quantum chemistry basics", "phase diagrams", "electrochemistry"],
        "CHEM131 Analytical Chemistry (Intro)": ["measurement and error", "spectroscopy methods", "chromatography", "calibration", "quality control"],
        "CHEM141 Materials Chemistry": ["polymers", "ceramics", "metals and alloys", "nanomaterials", "applications"],
    },
    "biology core": {
        "BIO101 Cell and Molecular Biology": ["cell structure", "dna and rna basics", "gene expression", "cell signaling", "cell cycle"],
        "BIO111 Genetics and Genomics": ["mendelian genetics", "population genetics", "genomic technologies", "variation and disease", "ethical considerations"],
        "BIO121 Biochemistry": ["proteins and enzymes", "metabolism", "bioenergetics", "nucleic acids", "regulation"],
        "BIO131 Physiology": ["organ systems", "homeostasis", "neurophysiology (intro)", "endocrine system", "cardiovascular system"],
        "BIO141 Evolutionary Biology": ["natural selection", "speciation", "phylogenetics", "population dynamics", "coevolution"],
        "BIO151 Systems Biology (Intro)": ["networks in biology", "omics data", "pathway modeling", "dynamical systems", "applications"],
    },
    "engineering core": {
        "ENG101 Circuits and Electronics": ["dc analysis", "ac analysis", "op-amps", "filters", "digital basics"],
        "ENG111 Control Systems": ["feedback control", "stability and margins", "pid controllers", "state space models", "discretization"],
        "ENG121 Signal Processing": ["sampling theory", "fourier analysis", "filtering", "spectral analysis", "applications"],
        "ENG131 Embedded Systems": ["microcontrollers", "sensors and actuators", "real-time constraints", "communication protocols", "power management"],
        "ENG141 Mechanical Systems (Intro)": ["statics", "dynamics", "material strength", "vibrations", "cad (intro)"],
        "ENG151 Materials Science": ["crystal structure", "phase diagrams", "mechanical properties", "failure modes", "processing methods"],
        "ENG161 Design Methodology": ["requirements analysis", "prototyping", "human factors", "reliability and safety", "design reviews"],
    },
    "economics and finance": {
        "ECON101 Microeconomics": ["supply and demand", "consumer theory", "firm theory", "market structures", "welfare economics"],
        "ECON111 Macroeconomics": ["gdp and inflation", "monetary policy", "fiscal policy", "business cycles", "growth models"],
        "ECON121 Game Theory": ["normal-form games", "nash equilibrium", "repeated games", "mechanism design (intro)", "auctions"],
        "ECON131 Behavioral Economics": ["heuristics and biases", "prospect theory", "time inconsistency", "nudges", "policy applications"],
        "FIN101 Financial Accounting": ["statements and reporting", "revenue and expense recognition", "cash flow analysis", "ratio analysis", "ethics and compliance"],
        "FIN111 Corporate Finance": ["time value of money", "capital budgeting", "cost of capital", "capital structure", "risk management"],
        "FIN121 Markets and Trading (Intro)": ["market microstructure", "asset classes", "portfolio basics", "derivatives overview", "regulation"],
    },
    "social sciences": {
        "SOC101 Psychology": ["cognition and perception", "learning and memory", "motivation", "social psychology", "psychometrics (intro)"],
        "SOC111 Sociology": ["social structures", "culture and identity", "inequality", "institutions", "social change"],
        "SOC121 Political Science": ["political systems", "comparative politics", "public policy", "international relations", "governance"],
        "SOC131 Anthropology (Intro)": ["human evolution", "cultural anthropology", "field methods", "ethnography", "ethics"],
        "SOC141 Public Policy (Intro)": ["policy analysis", "regulatory frameworks", "cost-benefit analysis", "stakeholders", "impact evaluation"],
        "SOC151 Organizational Behavior": ["motivation and teams", "leadership", "decision making", "change management", "organizational culture"],
    },
    "humanities": {
        "HUM101 Philosophy of Science": ["scientific explanation", "theory change", "demarcation", "realism vs instrumentalism", "case studies"],
        "HUM111 Epistemology": ["knowledge and justification", "skepticism", "rationalism and empiricism", "reliabilism", "social epistemology"],
        "HUM121 Ethics in Technology": ["privacy and surveillance", "fairness and bias", "human autonomy", "safety and harm", "governance"],
        "HUM131 History of Science and Technology": ["scientific revolutions", "industrialization", "computing history", "biotechnology history", "contemporary trends"],
        "HUM141 Literature and Cultural Studies (Survey)": ["narrative forms", "cultural theory", "media analysis", "representation and power", "critical writing"],
        "HUM151 Logic and Language (Intro)": ["formal semantics", "pragmatics", "philosophy of language", "meaning and reference", "language and mind"],
    },
    "communication and design": {
        "COM101 Scientific Writing": ["paper structure", "methodological clarity", "results presentation", "peer review", "responsible reporting"],
        "COM111 Technical Documentation": ["api docs", "architecture docs", "versioning", "release notes", "documentation tooling"],
        "COM121 Data Storytelling": ["narrative structure", "visual encoding", "audience adaptation", "ethics of persuasion", "impact measurement"],
        "COM131 Product Design": ["user research", "problem framing", "prototyping", "evaluation", "design systems"],
        "COM141 Human-Computer Interaction": ["interaction design", "cognitive models", "usability testing", "accessibility", "human-centered design"],
        "COM151 UX Research": ["interview techniques", "surveys", "diary studies", "analysis methods", "research ops"],
        "COM161 Visual Design Principles": ["typography", "color theory", "layout and grids", "visual hierarchy", "brand systems"],
    },
    "law policy and governance": {
        "LAW101 Privacy Law (Intro)": ["data protection principles", "consent and rights", "cross-border data", "regulatory frameworks", "compliance basics"],
        "LAW111 IP and Technology Law (Intro)": ["copyright", "patents", "trade secrets", "open-source licenses", "enforcement"],
        "LAW121 AI Governance Frameworks": ["model risk assessment", "accountability structures", "safety standards", "auditing practices", "regulatory trends"],
        "LAW131 Risk Management": ["risk identification", "risk quantification", "mitigation planning", "crisis response", "governance reporting"],
        "LAW141 Compliance Fundamentals": ["compliance programs", "controls and audits", "ethics hotlines", "policy maintenance", "continuous monitoring"],
    },
    "applied domain tracks": {
        "APD201 Robotics and Autonomy": ["kinematics", "planning", "perception", "control", "safety"],
        "APD211 Cybersecurity": ["threat models", "network defense", "app security", "incident response", "forensics (intro)"],
        "APD221 Healthcare Systems": ["clinical workflows", "data standards", "regulatory landscape", "decision support", "quality metrics"],
        "APD231 Climate and Energy Systems": ["energy markets", "grid fundamentals", "climate modeling", "policy frameworks", "mitigation strategies"],
        "APD241 Space Systems": ["orbital mechanics", "spacecraft subsystems", "communication links", "mission design", "space policy"],
        "APD251 Computational Finance": ["time series modeling", "risk models", "portfolio optimization", "market microstructure", "algorithmic trading (intro)"],
        "APD261 Bioinformatics": ["sequence analysis", "genomic pipelines", "structural bioinformatics", "omics integration", "applications"],
        "APD271 Computational Linguistics": ["syntax and parsing", "semantic representation", "language modeling", "evaluation", "bias and fairness"],
        "APD281 Computer Vision": ["image processing", "detection and segmentation", "representation learning", "multimodal vision", "evaluation"],
        "APD291 Geospatial Analytics": ["spatial data formats", "coordinate systems", "remote sensing", "spatial modeling", "geo visualization"],
    },
    "research and professional practice": {
        "RES301 Research Methods": ["literature review", "study design", "data management", "ethics and irb", "publication pipeline"],
        "RES311 Experimental Design": ["hypothesis formulation", "factorial designs", "power analysis", "measurement quality", "replication strategies"],
        "RES321 Measurement Theory": ["validity and reliability", "instrument design", "error analysis", "calibration", "measurement bias"],
        "RES331 Reproducibility and Ethics": ["open science practices", "reproducible pipelines", "responsible ai", "data ethics", "governance"],
        "RES341 Capstone Project": ["problem selection", "milestones and reviews", "deliverables", "evaluation criteria", "presentation"],
        "RES351 Internship or Practicum": ["role definition", "professional standards", "mentorship", "evaluation", "reflection"],
    },
}

def _slugify(text: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "_", text.upper()).strip("_")

def seed_curriculum() -> dict:
    upg = UniversalPrimeGraph()
    stats = {"categories": 0, "courses": 0, "modules": 0}
    for category, courses in CURRICULUM.items():
        category_node = f"CURR_{_slugify(category)}"
        upg.add_node(category_node, {"title": category, "type": "category", "mass": "SOLID"})
        stats["categories"] += 1
        for course, modules in courses.items():
            course_node = f"{category_node}_{_slugify(course)}"
            upg.add_node(course_node, {"title": course, "type": "course", "category": category, "mass": "SOLID"})
            stats["courses"] += 1
            for module in modules:
                module_node = f"{course_node}_{_slugify(module)}"
                upg.add_node(module_node, {"title": module, "type": "module", "course": course, "mass": "SOLID"})
                stats["modules"] += 1
    upg.save_graph()
    return stats

def main() -> None:
    print("=" * 60)
    print("TENT CURRICULUM SEEDER")
    print("=" * 60)
    stats = seed_curriculum()
    print(f"\n✅ Seeded: {stats['categories']} categories, {stats['courses']} courses, {stats['modules']} modules")
    print(f"   Total: {stats['categories'] + stats['courses'] + stats['modules']} nodes")
    with open("curriculum_index.json", "w") as f:
        json.dump(CURRICULUM, f, indent=2)
    print("✅ Exported: curriculum_index.json")

if __name__ == "__main__":
    main()
