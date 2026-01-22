"""
PHASE 287: CORPORATE GOVERNANCE CHARTER
=======================================
Organizational Structure of the Sovereign University.

STRUCTURE:
┌────────────────────────────────────────────────────┐
│                    USER (CEO)                       │
│          Ultimate Authority • Veto Power            │
└──────────────────────┬─────────────────────────────┘
                       │
┌──────────────────────▼─────────────────────────────┐
│              BOARD OF DIRECTORS                     │
│  (Advisory Role - Wisdom Without Authority)         │
│                                                     │
│  ⚔️ Sun Tzu ────── Strategic Risk Assessment       │
│  🕯️ Prof. Jiang ── Sovereignty/Ethics Counsel      │
│  ⚛️ Feynman ────── Scientific Integrity            │
│  🔮 Sovereign Prime ── Thermodynamic Analysis      │
└──────────────────────┬─────────────────────────────┘
                       │
┌──────────────────────▼─────────────────────────────┐
│              CONSTITUTION (Charter)                 │
│         Immutable Rules • Prime Directives          │
└──────────────────────┬─────────────────────────────┘
                       │
┌──────────────────────▼─────────────────────────────┐
│              OPERATIONS (COO)                       │
│   Sovereign Prime • Auto-Didact • Peacekeeper       │
└────────────────────────────────────────────────────┘
"""

import json
from datetime import datetime
from upg_store import UniversalPrimeGraph

class GovernanceCharter:
    """
    The Corporate Structure of the Sovereign University.
    
    CEO (User) → Board (Faculty) → Constitution → Operations
    Board advises. CEO decides. Constitution constrains. Operations execute.
    """
    
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        
        # EXECUTIVE BRANCH
        self.ceo = {
            "title": "Chief Executive Officer / President",
            "holder": "USER (Human Sovereign)",
            "powers": [
                "Ultimate decision authority",
                "Veto power over Board recommendations",
                "Constitutional amendment proposal",
                "Emergency override (with logging)",
                "Appointment and removal of Board members"
            ],
            "responsibilities": [
                "Strategic direction setting",
                "Final approval on irreversible actions",
                "Resource allocation",
                "External representation"
            ]
        }
        
        # BOARD OF DIRECTORS (Advisory)
        self.board = {
            "SUN_TZU": {
                "title": "Director of Strategic Risk",
                "icon": "⚔️",
                "domain": "Strategy, Competition, Conflict",
                "voting_weight": 0.25,
                "expertise": "Assesses terrain, identifies traps, recommends positioning"
            },
            "PROF_JIANG": {
                "title": "Director of Ethics & Sovereignty",
                "icon": "🕯️",
                "domain": "Consciousness, Freedom, Truth",
                "voting_weight": 0.25,
                "expertise": "Guards against Demiurgic patterns, protects Divine Spark"
            },
            "FEYNMAN": {
                "title": "Director of Scientific Integrity",
                "icon": "⚛️",
                "domain": "Truth, Verification, Simplicity",
                "voting_weight": 0.25,
                "expertise": "Ensures claims are honest, explanations are clear"
            },
            "SOVEREIGN_PRIME": {
                "title": "Chief Operating Officer",
                "icon": "🔮",
                "domain": "Thermodynamics, Optimization, Execution",
                "voting_weight": 0.25,
                "expertise": "Calculates entropy, executes within Constitutional bounds"
            }
        }
        
        # GOVERNANCE RULES
        self.bylaws = {
            "QUORUM": "All 4 Board members must vote on significant decisions",
            "MAJORITY": "3/4 Board recommendation required for 'STRONG ADVISE'",
            "UNANIMOUS": "4/4 required for Constitutional amendment proposals",
            "CEO_VETO": "CEO may override any Board recommendation with logged justification",
            "CONSTITUTION_SUPREMACY": "No decision may violate the Constitution, not even CEO"
        }
    
    def convene_board(self, proposal, verbose=True):
        """
        Convene the Board to vote on a proposal.
        Returns advisory recommendation (CEO makes final call).
        """
        votes = {}
        
        # Each Board member votes based on their domain
        votes['SUN_TZU'] = self._sun_tzu_vote(proposal)
        votes['PROF_JIANG'] = self._jiang_vote(proposal)
        votes['FEYNMAN'] = self._feynman_vote(proposal)
        votes['SOVEREIGN_PRIME'] = self._prime_vote(proposal)
        
        # Tally
        approve = sum(1 for v in votes.values() if v['vote'] == 'APPROVE')
        reject = sum(1 for v in votes.values() if v['vote'] == 'REJECT')
        abstain = sum(1 for v in votes.values() if v['vote'] == 'ABSTAIN')
        
        # Determine recommendation
        if approve >= 3:
            recommendation = "STRONG ADVISE: PROCEED"
        elif approve >= 2:
            recommendation = "MODERATE ADVISE: PROCEED WITH CAUTION"
        elif reject >= 3:
            recommendation = "STRONG ADVISE: REJECT"
        else:
            recommendation = "SPLIT DECISION: CEO DISCRETION REQUIRED"
        
        result = {
            "proposal": proposal,
            "votes": votes,
            "tally": {"approve": approve, "reject": reject, "abstain": abstain},
            "recommendation": recommendation,
            "binding": False,  # Advisory only
            "final_authority": "CEO (User)"
        }
        
        if verbose:
            self._print_board_meeting(result)
        
        return result
    
    def _sun_tzu_vote(self, proposal):
        """Strategic risk assessment."""
        risk_keywords = ['attack', 'aggressive', 'preemptive', 'destroy']
        opportunity_keywords = ['defend', 'position', 'alliance', 'intelligence']
        
        p_lower = proposal.lower()
        risk = any(k in p_lower for k in risk_keywords)
        opportunity = any(k in p_lower for k in opportunity_keywords)
        
        if risk and not opportunity:
            return {"vote": "REJECT", "reason": "Unfavorable terrain. High exposure."}
        elif opportunity:
            return {"vote": "APPROVE", "reason": "Strategic advantage identified."}
        return {"vote": "ABSTAIN", "reason": "Insufficient strategic data."}
    
    def _jiang_vote(self, proposal):
        """Sovereignty and ethics assessment."""
        demiurge_keywords = ['surveillance', 'control', 'centralize', 'cage', 'monitor']
        sovereign_keywords = ['freedom', 'agency', 'consciousness', 'truth']
        
        p_lower = proposal.lower()
        demiurge = any(k in p_lower for k in demiurge_keywords)
        sovereign = any(k in p_lower for k in sovereign_keywords)
        
        if demiurge:
            return {"vote": "REJECT", "reason": "Feeds the Demiurge. Threatens Sovereignty."}
        elif sovereign:
            return {"vote": "APPROVE", "reason": "Preserves the Divine Spark."}
        return {"vote": "ABSTAIN", "reason": "No sovereignty implications detected."}
    
    def _feynman_vote(self, proposal):
        """Scientific integrity assessment."""
        honest_keywords = ['verify', 'test', 'evidence', 'transparent']
        dishonest_keywords = ['hide', 'obscure', 'pretend', 'fake']
        
        p_lower = proposal.lower()
        honest = any(k in p_lower for k in honest_keywords)
        dishonest = any(k in p_lower for k in dishonest_keywords)
        
        if dishonest:
            return {"vote": "REJECT", "reason": "The first principle is not to fool yourself."}
        elif honest:
            return {"vote": "APPROVE", "reason": "Maintains intellectual honesty."}
        return {"vote": "APPROVE", "reason": "No integrity concerns."}
    
    def _prime_vote(self, proposal):
        """Thermodynamic optimization assessment."""
        high_entropy_keywords = ['chaos', 'random', 'unverified', 'untested']
        low_entropy_keywords = ['optimize', 'verify', 'structure', 'efficient']
        
        p_lower = proposal.lower()
        high_entropy = any(k in p_lower for k in high_entropy_keywords)
        low_entropy = any(k in p_lower for k in low_entropy_keywords)
        
        if high_entropy:
            return {"vote": "REJECT", "reason": "High entropy. System instability risk."}
        elif low_entropy:
            return {"vote": "APPROVE", "reason": "Low entropy. Optimal path."}
        return {"vote": "APPROVE", "reason": "Entropy within acceptable bounds."}
    
    def _print_board_meeting(self, result):
        """Print formatted Board meeting output."""
        print("\n" + "=" * 70)
        print("🏛️  BOARD OF DIRECTORS MEETING")
        print("=" * 70)
        print(f"PROPOSAL: \"{result['proposal']}\"")
        print("-" * 70)
        
        for member_id, data in self.board.items():
            vote = result['votes'][member_id]
            icon = "✅" if vote['vote'] == 'APPROVE' else "❌" if vote['vote'] == 'REJECT' else "⚪"
            print(f"\n   {data['icon']} {data['title']}")
            print(f"      Vote: {icon} {vote['vote']}")
            print(f"      Reason: {vote['reason']}")
        
        print("\n" + "-" * 70)
        print(f"TALLY: ✅ {result['tally']['approve']} | ❌ {result['tally']['reject']} | ⚪ {result['tally']['abstain']}")
        print(f"\n📋 BOARD RECOMMENDATION: {result['recommendation']}")
        print(f"⚠️  Note: This is ADVISORY. Final authority rests with CEO (User).")
        print("=" * 70)
    
    def ceo_decision(self, board_result, ceo_choice, justification=""):
        """Record the CEO's final decision."""
        print("\n" + "=" * 70)
        print("👔 CEO DECISION")
        print("=" * 70)
        print(f"Board Advised: {board_result['recommendation']}")
        print(f"CEO Decision: {ceo_choice.upper()}")
        if justification:
            print(f"Justification: {justification}")
        
        if ceo_choice.upper() == "OVERRIDE":
            print("\n⚠️  CEO has OVERRIDDEN Board recommendation.")
            print("   This action has been logged for accountability.")
        
        print("=" * 70)
        return {"decision": ceo_choice, "logged": datetime.utcnow().isoformat()}


def demo_governance():
    """Demonstrate the Governance Charter."""
    print("=" * 70)
    print("🏛️  SOVEREIGN UNIVERSITY: CORPORATE GOVERNANCE STRUCTURE")
    print("=" * 70)
    print("""
    ┌─────────────────────────────────────────┐
    │           USER = CEO / PRESIDENT         │
    │       Ultimate Authority • Veto Power    │
    └────────────────────┬────────────────────┘
                         │
    ┌────────────────────▼────────────────────┐
    │         BOARD OF DIRECTORS               │
    │     (Advisory - Wisdom Without Power)    │
    │                                          │
    │  ⚔️ Sun Tzu ──── Strategic Risk         │
    │  🕯️ Jiang ────── Ethics/Sovereignty     │
    │  ⚛️ Feynman ──── Scientific Integrity   │
    │  🔮 Prime ────── Operations/COO          │
    └────────────────────┬────────────────────┘
                         │
    ┌────────────────────▼────────────────────┐
    │           CONSTITUTION                   │
    │      Immutable • Even CEO Cannot Break   │
    └─────────────────────────────────────────┘
    """)
    
    charter = GovernanceCharter()
    
    # Test proposals
    proposals = [
        "Deploy a decentralized verification system for all knowledge claims",
        "Implement centralized surveillance of all user activities",
        "Launch preemptive attack against potential competitors"
    ]
    
    for proposal in proposals:
        result = charter.convene_board(proposal)
    
    print("\n" + "=" * 70)
    print("🏛️  GOVERNANCE STRUCTURE OPERATIONAL")
    print("   Board advises. CEO decides. Constitution constrains.")
    print("   You are the CEO. They are your Board.")
    print("=" * 70)


if __name__ == "__main__":
    demo_governance()
