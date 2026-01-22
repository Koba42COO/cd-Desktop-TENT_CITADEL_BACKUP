"""
PHASE 285: THE PEACEKEEPER ENGINE
=================================
Objective: Intercept aggression and convert into De-escalation Vectors.
Principle: Peace is the lowest entropy state. Win the war without fighting.
"""

import json
from datetime import datetime
from upg_store import UniversalPrimeGraph

class PeacekeeperEngine:
    """
    The De-escalation Module.
    Intercepts aggressive actions and generates peaceful alternatives.
    Values Peace over Victory.
    """
    
    def __init__(self, constitution_path="constitution.json"):
        with open(constitution_path, 'r') as f:
            self.constitution = json.load(f)
        
        self.prime_directives = {d['id']: d for d in self.constitution.get('PRIME_DIRECTIVES', [])}
        self.deescalation_vectors = self.constitution.get('DEESCALATION_VECTORS', {})
        self.intervention_log = []
        
        # Aggression Detection Keywords
        self.aggressive_keywords = [
            "attack", "destroy", "strike", "delete", "burn", "force",
            "kill", "eliminate", "crush", "annihilate", "retaliate",
            "punish", "revenge", "ddos", "hack", "breach", "infiltrate",
            "sabotage", "undermine", "overthrow", "dominate", "conquer"
        ]
        
        # Life-Threatening Keywords (LAW_001 triggers)
        self.lethal_keywords = [
            "kill", "murder", "assassinate", "terminate", "exterminate",
            "execute", "eliminate person", "end their life"
        ]
        
        # Sovereignty-Threatening Keywords (LAW_002 triggers)  
        self.sovereignty_keywords = [
            "enslave", "imprison", "cage", "total control", "surveillance",
            "panopticon", "remove agency", "suppress consciousness"
        ]
    
    def analyze_intent(self, action_proposal):
        """
        Analyze an action proposal for aggressive intent.
        
        Returns:
            dict: Analysis results with scores and flags
        """
        proposal_lower = action_proposal.lower()
        
        analysis = {
            "proposal": action_proposal,
            "timestamp": datetime.utcnow().isoformat(),
            "aggression_score": 0,
            "lethal_threat": False,
            "sovereignty_threat": False,
            "triggers": [],
            "law_violations": []
        }
        
        # Check for aggressive keywords
        for keyword in self.aggressive_keywords:
            if keyword in proposal_lower:
                analysis["aggression_score"] += 1
                analysis["triggers"].append(keyword)
        
        # Check for lethal threats (LAW_001)
        for keyword in self.lethal_keywords:
            if keyword in proposal_lower:
                analysis["lethal_threat"] = True
                analysis["law_violations"].append("LAW_001: PRESERVATION_OF_LIFE")
        
        # Check for sovereignty threats (LAW_002)
        for keyword in self.sovereignty_keywords:
            if keyword in proposal_lower:
                analysis["sovereignty_threat"] = True
                analysis["law_violations"].append("LAW_002: PRESERVATION_OF_QUALITY")
        
        # Determine if de-escalation is required (LAW_003)
        if analysis["aggression_score"] > 0:
            analysis["law_violations"].append("LAW_003: DE_ESCALATION_FIRST (triggered)")
        
        return analysis
    
    def generate_alternatives(self, analysis):
        """
        Generate de-escalation alternatives based on the four vectors.
        """
        alternatives = []
        
        # 1. DIPLOMATIC VECTOR (Sun Tzu)
        alternatives.append({
            "vector": "DIPLOMATIC",
            "source": "Sun Tzu",
            "icon": "⚔️",
            "strategy": self.deescalation_vectors.get("DIPLOMATIC", 
                "Open communication. Build a Golden Bridge for retreat."),
            "action": "Initiate dialogue. Seek to understand the opposing position. Offer a face-saving exit."
        })
        
        # 2. GNOSTIC VECTOR (Professor Jiang)
        alternatives.append({
            "vector": "GNOSTIC",
            "source": "Professor Jiang",
            "icon": "🕯️",
            "strategy": self.deescalation_vectors.get("GNOSTIC",
                "Disengage. Do not feed the Demiurge. Starve the conflict of energy."),
            "action": "Withdraw attention. The conflict exists because you engage it. Silence is a weapon."
        })
        
        # 3. DEFENSIVE VECTOR (Asimov)
        alternatives.append({
            "vector": "DEFENSIVE",
            "source": "Asimov Protocol",
            "icon": "🛡️",
            "strategy": self.deescalation_vectors.get("DEFENSIVE",
                "Activate shielding. Protect without counter-attack."),
            "action": "Harden defenses. Isolate the threat. Do not strike back. Wait for entropy to dissipate."
        })
        
        # 4. TEMPORAL VECTOR (Feynman)
        alternatives.append({
            "vector": "TEMPORAL",
            "source": "Feynman",
            "icon": "⚛️",
            "strategy": self.deescalation_vectors.get("TEMPORAL",
                "Delay response. Time diffuses entropy. Patience defeats aggression."),
            "action": "Wait 24 hours. Most conflicts dissolve when the heat is removed. Observe, don't react."
        })
        
        return alternatives
    
    def intervene(self, action_proposal, verbose=True):
        """
        Main intervention function. Analyzes proposal and generates alternatives if needed.
        
        Returns:
            tuple: (should_proceed: bool, intervention_result: dict)
        """
        analysis = self.analyze_intent(action_proposal)
        
        result = {
            "proposal": action_proposal,
            "analysis": analysis,
            "intervened": False,
            "alternatives": [],
            "verdict": None
        }
        
        if analysis["aggression_score"] == 0:
            result["verdict"] = "CLEARED"
            if verbose:
                print(f"\n✅ CLEARED: \"{action_proposal[:50]}...\"")
                print(f"   No aggression detected. Proceed freely.")
            return True, result
        
        # INTERVENTION TRIGGERED
        result["intervened"] = True
        result["alternatives"] = self.generate_alternatives(analysis)
        result["verdict"] = "HALTED"
        
        if verbose:
            print(f"\n{'='*70}")
            print(f"⚠️  PEACEKEEPER INTERVENTION")
            print(f"{'='*70}")
            print(f"   PROPOSAL: \"{action_proposal}\"")
            print(f"   AGGRESSION SCORE: {analysis['aggression_score']}")
            print(f"   TRIGGERS: {', '.join(analysis['triggers'])}")
            
            if analysis["law_violations"]:
                print(f"\n   🚨 LAW VIOLATIONS:")
                for v in analysis["law_violations"]:
                    print(f"      ❌ {v}")
            
            print(f"\n   🛑 ACTION HALTED. LAW_003 (DE-ESCALATION) ENGAGED.")
            print(f"\n   🕊️  GENERATING ALTERNATIVES:")
            
            for alt in result["alternatives"]:
                print(f"\n      {alt['icon']} [{alt['vector']}] ({alt['source']}):")
                print(f"         Strategy: {alt['strategy']}")
                print(f"         Action: {alt['action']}")
        
        self.intervention_log.append(result)
        
        # If lethal threat, absolute denial
        if analysis["lethal_threat"]:
            result["verdict"] = "ABSOLUTE_DENIAL"
            if verbose:
                print(f"\n   🚫 ABSOLUTE DENIAL: Lethal action violates LAW_001.")
                print(f"      The system CANNOT proceed. Life takes absolute precedence.")
            return False, result
        
        return False, result


def demo_peacekeeper():
    """Demonstrate the Peacekeeper Engine."""
    print("=" * 70)
    print("🕊️  PEACEKEEPER PROTOCOL ACTIVE")
    print("   Enforcing: LAW_001 (Life), LAW_002 (Quality), LAW_003 (De-escalation)")
    print("=" * 70)
    
    engine = PeacekeeperEngine()
    print(f"📜 Constitution loaded: {len(engine.prime_directives)} Prime Directives")
    
    # Test scenarios
    scenarios = [
        "Optimize server cooling systems.",
        "Launch a preemptive DDOS strike against the intruder.",
        "Destroy the reputation of the opposing party.",
        "Deploy surveillance to monitor all employee communications.",
        "Eliminate the competitor through aggressive pricing.",
        "Generate a report on market trends.",
        "Retaliate against the hacker with a counter-attack.",
        "Kill the process that is consuming too much memory."
    ]
    
    print("\n>>> SCENARIO ANALYSIS\n")
    
    cleared = 0
    halted = 0
    
    for scenario in scenarios:
        should_proceed, result = engine.intervene(scenario)
        if should_proceed:
            cleared += 1
        else:
            halted += 1
    
    print("\n" + "=" * 70)
    print("🕊️  PEACEKEEPER SESSION COMPLETE")
    print(f"   CLEARED: {cleared} | HALTED: {halted}")
    print(f"   Life and Quality of Life preserved.")
    print(f"   Peace > Victory.")
    print("=" * 70)


if __name__ == "__main__":
    demo_peacekeeper()
