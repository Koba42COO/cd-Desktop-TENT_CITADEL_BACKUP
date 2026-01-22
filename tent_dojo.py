"""
PHASE 275: THE DOJO (RECURSIVE SELF-IMPROVEMENT)
=================================================
Objective: Generate new knowledge connections and validate them autonomously.
Mechanism: Curiosity → Hypothesis → Thermodynamics → Mint/Prune
"""

import random
import time
import json
from datetime import datetime
from upg_store import UniversalPrimeGraph

class Dojo:
    """
    The Auto-Didact Training Loop.
    Runs autonomously, building synapses between verified nodes.
    """
    
    def __init__(self, entropy_threshold=0.3, min_overlap=1):
        self.upg = UniversalPrimeGraph()
        self.entropy_threshold = entropy_threshold
        self.min_overlap = min_overlap
        self.successes = 0
        self.failures = 0
        self.session_start = datetime.utcnow()
        
    def calculate_entropy(self, node_a, node_b):
        """
        Real thermodynamic check based on structural overlap.
        Lower entropy = more coherent connection.
        """
        # Extract features
        title_a = set(node_a.get('title', '').lower().split())
        title_b = set(node_b.get('title', '').lower().split())
        abstract_a = set(node_a.get('abstract', '').lower().split()[:20])
        abstract_b = set(node_b.get('abstract', '').lower().split()[:20])
        
        # Calculate overlap
        title_overlap = len(title_a & title_b)
        abstract_overlap = len(abstract_a & abstract_b)
        
        # Check type compatibility (same domain = lower entropy)
        type_a = node_a.get('type', 'unknown')
        type_b = node_b.get('type', 'unknown')
        type_match = 1 if type_a == type_b else 0
        
        # Entropy formula: High overlap = Low entropy
        coherence = title_overlap * 3 + abstract_overlap + type_match * 2
        entropy = 1.0 / (1 + coherence * 0.5)
        
        return round(entropy, 3), {
            "title_overlap": title_overlap,
            "abstract_overlap": abstract_overlap,
            "type_match": type_match,
            "coherence_score": coherence
        }
    
    def generate_hypothesis(self, node_a, node_b):
        """
        Attempt to articulate the connection between two nodes.
        """
        # Extract common terms
        words_a = set(node_a.get('title', '').lower().split())
        words_b = set(node_b.get('title', '').lower().split())
        common = words_a & words_b
        
        if common:
            bridge_concept = list(common)[0]
            return f"Both concepts share the dimension '{bridge_concept}'"
        
        # Fallback: Check abstract overlap
        abs_a = set(node_a.get('abstract', '').lower().split()[:30])
        abs_b = set(node_b.get('abstract', '').lower().split()[:30])
        common_abs = abs_a & abs_b - {'the', 'a', 'an', 'is', 'are', 'of', 'in', 'to', 'and'}
        
        if len(common_abs) >= 2:
            return f"Shared conceptual vocabulary: {list(common_abs)[:3]}"
        
        return None  # No solid connection found
    
    def mint_synapse(self, node_a, node_b, hypothesis, entropy):
        """
        Create a new edge/synapse in the graph.
        CONSTITUTIONAL CHECK: Must pass Supreme Court review before minting.
        """
        synapse_id = f"SYNAPSE_{int(datetime.utcnow().timestamp())}"
        
        synapse = {
            "title": f"Synapse: {node_a.get('title', '')[:20]} ↔ {node_b.get('title', '')[:20]}",
            "abstract": hypothesis,
            "type": "synapse",
            "source": "dojo_autodidact",
            "entropy": entropy,
            "mass": 1 - entropy,  # Mass = inverse of entropy
            "citations": 2,  # Both parent nodes count as citations
            "parent_a": node_a.get('title', ''),
            "parent_b": node_b.get('title', ''),
            "created": datetime.utcnow().isoformat()
        }
        
        # CONSTITUTIONAL REVIEW (Phase 284)
        try:
            from sovereign_validator import SupremeCourt
            court = SupremeCourt()
            is_ratified, session = court.review(synapse)
            
            if not is_ratified:
                print(f"    ⚖️ VETOED by Supreme Court: {session['violations'][0]}")
                return None
            else:
                print(f"    ⚖️ RATIFIED by Supreme Court")
        except Exception as e:
            # If validator not available, proceed with caution warning
            print(f"    ⚠️ Constitutional review unavailable: {e}")
        
        self.upg.nodes[synapse_id] = synapse
        self.upg.ledger.append({
            "id": synapse_id,
            "title": synapse["title"],
            "score": 1 - entropy,
            "verdict": "SYNAPSE_MINTED_CONSTITUTIONAL",
            "timestamp": synapse["created"]
        })
        
        return synapse_id
    
    def train_step(self, iteration, persist=False):
        """
        Execute one training iteration.
        
        Args:
            iteration: Step number
            persist: If True, actually write synapses to disk
            
        Returns:
            dict: Training step result
        """
        keys = list(self.upg.nodes.keys())
        if len(keys) < 2:
            return {"status": "ERROR", "reason": "Insufficient nodes"}
        
        # 1. CURIOSITY: Pick random nodes
        key_a, key_b = random.sample(keys, 2)
        node_a = self.upg.nodes[key_a]
        node_b = self.upg.nodes[key_b]
        
        # 2. HYPOTHESIS: Attempt bridge
        hypothesis = self.generate_hypothesis(node_a, node_b)
        
        # 3. THERMODYNAMICS: Calculate entropy
        entropy, metrics = self.calculate_entropy(node_a, node_b)
        
        # 4. VERDICT
        is_solid = entropy < self.entropy_threshold or hypothesis is not None
        
        result = {
            "iteration": iteration,
            "node_a": node_a.get('title', '')[:30],
            "node_b": node_b.get('title', '')[:30],
            "entropy": entropy,
            "metrics": metrics,
            "hypothesis": hypothesis,
            "verdict": "SUCCESS" if is_solid else "REJECTED"
        }
        
        if is_solid:
            self.successes += 1
            if persist and hypothesis:
                synapse_id = self.mint_synapse(node_a, node_b, hypothesis, entropy)
                result["synapse_id"] = synapse_id
        else:
            self.failures += 1
        
        return result
    
    def spar(self, rounds=5, persist=False, verbose=True):
        """
        Run a sparring session.
        
        Args:
            rounds: Number of training iterations
            persist: Write successful synapses to disk
            verbose: Print progress
        """
        if verbose:
            print("=" * 70)
            print(f"🥋 TENT DOJO | NODES: {len(self.upg.nodes)} | ROUNDS: {rounds}")
            print("=" * 70)
        
        results = []
        for i in range(1, rounds + 1):
            result = self.train_step(i, persist=persist)
            results.append(result)
            
            if verbose:
                icon = "✅" if result["verdict"] == "SUCCESS" else "❄️"
                print(f"\n[{i}] {result['node_a']} ↔ {result['node_b']}")
                print(f"    {icon} {result['verdict']} (Entropy: {result['entropy']})")
                if result.get("hypothesis"):
                    print(f"    💡 {result['hypothesis']}")
                if result.get("synapse_id"):
                    print(f"    ✨ MINTED: {result['synapse_id']}")
            
            time.sleep(0.3)
        
        if persist:
            self.upg.save_graph()
        
        if verbose:
            print("\n" + "=" * 70)
            rate = self.successes / max(self.successes + self.failures, 1) * 100
            print(f"📊 SESSION COMPLETE | ✅ {self.successes} | ❄️ {self.failures} | Rate: {rate:.1f}%")
            print(f"📈 NEW NODE COUNT: {len(self.upg.nodes)}")
            print("=" * 70)
        
        return results


def main():
    """Execute a demonstration sparring session."""
    dojo = Dojo()
    dojo.spar(rounds=5, persist=True, verbose=True)


if __name__ == "__main__":
    main()
