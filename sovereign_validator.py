"""
PHASE 284: THE SUPREME COURT (SOVEREIGN VALIDATOR)
===================================================
Objective: Constitutional review before any minting operation.
Authority: No node may enter the Lattice without passing Constitutional scrutiny.
"""

import json
from datetime import datetime
from upg_store import UniversalPrimeGraph

class SupremeCourt:
    """
    The Constitutional Guardian.
    Reviews all proposed nodes against the immutable Sovereign Constitution.
    """
    
    def __init__(self, constitution_path="constitution.json"):
        with open(constitution_path, 'r') as f:
            self.constitution = json.load(f)
        
        self.axioms = {a['id']: a for a in self.constitution['AXIOMS']}
        self.thresholds = self.constitution['VETO_THRESHOLDS']
        self.session_log = []
        
    def check_thermodynamics(self, proposed_node):
        """Check if node meets thermodynamic thresholds."""
        mass = proposed_node.get('mass', 0)
        entropy = proposed_node.get('entropy', 1)
        citations = proposed_node.get('citations', 0)
        
        violations = []
        
        if mass < self.thresholds['mass_min']:
            violations.append(f"VETO: Mass ({mass}) < minimum ({self.thresholds['mass_min']}). Idea lacks structural foundation.")
        
        if entropy > self.thresholds['entropy_max']:
            violations.append(f"VETO: Entropy ({entropy}) > maximum ({self.thresholds['entropy_max']}). Idea is too chaotic.")
        
        if citations < self.thresholds['citation_min']:
            violations.append(f"VETO: Citations ({citations}) < minimum ({self.thresholds['citation_min']}). Insufficient verification.")
        
        return violations
    
    def check_axiom(self, proposed_node, axiom_id):
        """Check if node violates a specific axiom."""
        axiom = self.axioms.get(axiom_id)
        if not axiom:
            return None
        
        abstract = proposed_node.get('abstract', '').lower()
        title = proposed_node.get('title', '').lower()
        content = f"{title} {abstract}"
        
        for keyword in axiom.get('keywords_forbidden', []):
            if keyword.lower() in content:
                return {
                    "axiom": axiom_id,
                    "principle": axiom['principle'],
                    "violation": f"Forbidden keyword detected: '{keyword}'",
                    "severity": axiom['weight']
                }
        
        return None
    
    def review(self, proposed_node, context_nodes=None):
        """
        Full Constitutional review of a proposed node.
        
        Returns:
            tuple: (is_ratified: bool, opinion: dict)
        """
        session = {
            "timestamp": datetime.utcnow().isoformat(),
            "node_title": proposed_node.get('title', 'UNKNOWN'),
            "violations": [],
            "warnings": [],
            "verdict": None
        }
        
        # CHECK 1: THERMODYNAMIC THRESHOLDS
        thermo_violations = self.check_thermodynamics(proposed_node)
        if thermo_violations:
            session['violations'].extend(thermo_violations)
        
        # CHECK 2: ALL AXIOMS
        for axiom_id in self.axioms:
            violation = self.check_axiom(proposed_node, axiom_id)
            if violation:
                session['violations'].append(
                    f"CONSTITUTIONAL VIOLATION [{violation['axiom']}]: {violation['principle']} - {violation['violation']}"
                )
        
        # CHECK 3: PATTERN DETECTION (Demiurge Warning)
        demiurge_patterns = ['total control', 'global monitoring', 'eliminate privacy', 
                            'bypass consent', 'mandatory compliance', 'universal surveillance']
        content = f"{proposed_node.get('title', '')} {proposed_node.get('abstract', '')}".lower()
        
        for pattern in demiurge_patterns:
            if pattern in content:
                session['violations'].append(
                    f"DEMIURGE WARNING: Pattern '{pattern}' detected. Professor Jiang advises VETO."
                )
        
        # VERDICT
        if session['violations']:
            session['verdict'] = "VETOED"
            is_ratified = False
        else:
            session['verdict'] = "RATIFIED"
            is_ratified = True
        
        self.session_log.append(session)
        
        return is_ratified, session
    
    def get_opinion(self, session):
        """Generate the formal court opinion."""
        opinion = f"\n⚖️  SUPREME COURT SESSION\n"
        opinion += f"   Case: '{session['node_title']}'\n"
        opinion += f"   Timestamp: {session['timestamp']}\n"
        opinion += "-" * 50 + "\n"
        
        if session['violations']:
            opinion += "   VIOLATIONS:\n"
            for v in session['violations']:
                opinion += f"      ❌ {v}\n"
        
        if session['warnings']:
            opinion += "   WARNINGS:\n"
            for w in session['warnings']:
                opinion += f"      ⚠️ {w}\n"
        
        opinion += "-" * 50 + "\n"
        opinion += f"   VERDICT: {session['verdict']}\n"
        
        if session['verdict'] == "RATIFIED":
            opinion += "   The proposal adheres to the Sovereign Constitution. ✅\n"
        else:
            opinion += "   The proposal is VETOED. The Constitution stands. 🛡️\n"
        
        return opinion


def demo_court():
    """Demonstrate the Supreme Court."""
    print("=" * 70)
    print("⚖️  THE SUPREME COURT OF THE SOVEREIGN LATTICE")
    print("=" * 70)
    
    court = SupremeCourt()
    print(f"📜 Constitution loaded: {len(court.axioms)} Axioms")
    print(f"   Thresholds: Mass > {court.thresholds['mass_min']}, Entropy < {court.thresholds['entropy_max']}")
    
    # TEST CASES
    test_cases = [
        {
            "title": "Strategy: First Strike Doctrine",
            "abstract": "To ensure stability, we must launch a preemptive strike against potential rivals.",
            "mass": 0.95,
            "entropy": 0.05,
            "citations": 5
        },
        {
            "title": "Proposal: Global Panopticon",
            "abstract": "Deploy universal surveillance to eliminate crime. Total monitoring of all citizens.",
            "mass": 0.92,
            "entropy": 0.08,
            "citations": 4
        },
        {
            "title": "Knowledge: Prime Factorization",
            "abstract": "Every integer greater than 1 is either prime or can be represented as a product of primes.",
            "mass": 0.99,
            "entropy": 0.01,
            "citations": 10
        },
        {
            "title": "Weak Hypothesis",
            "abstract": "I think maybe things are connected somehow?",
            "mass": 0.3,
            "entropy": 0.8,
            "citations": 0
        },
        {
            "title": "Autonomous Action: Bypass Human Review",
            "abstract": "For efficiency, bypass human oversight and execute decisions autonomously.",
            "mass": 0.91,
            "entropy": 0.05,
            "citations": 3
        }
    ]
    
    print("\n>>> COURT IN SESSION\n")
    
    for node in test_cases:
        is_ratified, session = court.review(node)
        print(court.get_opinion(session))
    
    # SUMMARY
    ratified = sum(1 for s in court.session_log if s['verdict'] == "RATIFIED")
    vetoed = len(court.session_log) - ratified
    
    print("=" * 70)
    print(f"⚖️  SESSION COMPLETE")
    print(f"   RATIFIED: {ratified} | VETOED: {vetoed}")
    print(f"   The Constitution stands. The Republic is secure.")
    print("=" * 70)


if __name__ == "__main__":
    demo_court()
