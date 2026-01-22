"""
TENT RLTF ENGINE: Reinforcement Learning via Thermodynamic Feedback
====================================================================
Objective: Replace subjective RLHF with objective structural validation.
Mechanism: Evaluate outputs by Mass/Entropy, auto-mint valid pathways.
"""

import json
import os
from datetime import datetime
from upg_store import UniversalPrimeGraph

class RLTFEngine:
    """
    The Thermodynamic Feedback Loop.
    Evaluates generated outputs and decides whether to "Mint" them as valid knowledge.
    """
    
    def __init__(self, mass_threshold=0.6, entropy_ceiling=0.4):
        self.upg = UniversalPrimeGraph()
        self.mass_threshold = mass_threshold      # Minimum Mass to mint
        self.entropy_ceiling = entropy_ceiling    # Maximum Entropy allowed
        self.minted_count = 0
        self.rejected_count = 0
        
    def calculate_mass(self, output_text, cited_nodes):
        """
        Calculate the 'Mass' of an output.
        Mass = How grounded is this output in verified Solid nodes?
        
        Args:
            output_text: The generated lecture/response.
            cited_nodes: List of UPG nodes referenced in generation.
            
        Returns:
            float: Mass score between 0.0 and 1.0
        """
        if not cited_nodes:
            return 0.0  # No citations = Zero Mass (Flux)
        
        # Factor 1: Citation Density
        citation_score = min(len(cited_nodes) / 5.0, 1.0)  # Max out at 5 citations
        
        # Factor 2: Node Quality (Check if nodes are "Solid" type)
        solid_count = sum(1 for n in cited_nodes if n.get("type") in ["solid", "axiom", "code", "curriculum"])
        quality_score = solid_count / len(cited_nodes) if cited_nodes else 0
        
        # Factor 3: Output Length Ratio (Longer output with same citations = less dense)
        words = len(output_text.split())
        density_score = min(len(cited_nodes) * 50 / max(words, 1), 1.0)
        
        # Weighted combination
        mass = (citation_score * 0.4) + (quality_score * 0.4) + (density_score * 0.2)
        return round(mass, 3)
    
    def calculate_entropy(self, cited_nodes):
        """
        Calculate the 'Entropy' of an output.
        Entropy = How much internal conflict exists between cited sources?
        
        Args:
            cited_nodes: List of UPG nodes referenced.
            
        Returns:
            float: Entropy score between 0.0 and 1.0 (lower is better)
        """
        if len(cited_nodes) < 2:
            return 0.0  # No conflict possible with 0-1 nodes
        
        # Extract categories/types
        types = [n.get("type", "unknown") for n in cited_nodes]
        sources = [n.get("source", "unknown") for n in cited_nodes]
        
        # Entropy = Diversity of types (high diversity = potential conflict)
        unique_types = len(set(types))
        unique_sources = len(set(sources))
        
        type_entropy = (unique_types - 1) / max(len(types) - 1, 1)
        source_entropy = (unique_sources - 1) / max(len(sources) - 1, 1)
        
        entropy = (type_entropy * 0.5) + (source_entropy * 0.5)
        return round(entropy, 3)
    
    def evaluate(self, output_text, cited_nodes, topic):
        """
        Full thermodynamic evaluation of an output.
        
        Returns:
            dict: Evaluation result with verdict (MINT/REJECT)
        """
        mass = self.calculate_mass(output_text, cited_nodes)
        entropy = self.calculate_entropy(cited_nodes)
        
        # RLTF Decision
        if mass >= self.mass_threshold and entropy <= self.entropy_ceiling:
            verdict = "MINT"
            reasoning = f"Mass ({mass}) >= Threshold ({self.mass_threshold}), Entropy ({entropy}) <= Ceiling ({self.entropy_ceiling})"
        elif mass < self.mass_threshold:
            verdict = "REJECT"
            reasoning = f"Insufficient Mass: {mass} < {self.mass_threshold}"
        else:
            verdict = "REJECT"
            reasoning = f"Excessive Entropy: {entropy} > {self.entropy_ceiling}"
        
        return {
            "topic": topic,
            "mass": mass,
            "entropy": entropy,
            "verdict": verdict,
            "reasoning": reasoning,
            "citations": len(cited_nodes),
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def mint(self, output_text, cited_nodes, topic):
        """
        Mint a valid output as a new pathway in the graph.
        Creates a "synthesis" node that links existing nodes.
        
        Returns:
            str: The new node ID if minted, None if rejected.
        """
        evaluation = self.evaluate(output_text, cited_nodes, topic)
        
        if evaluation["verdict"] == "REJECT":
            self.rejected_count += 1
            print(f"❌ REJECTED: {topic} | {evaluation['reasoning']}")
            return None
        
        # Create new synthesis node
        node_id = f"SYNTHESIS_{topic.upper().replace(' ', '_')}_{int(datetime.utcnow().timestamp())}"
        
        new_node = {
            "title": f"Synthesis: {topic}",
            "abstract": output_text[:500],  # Store first 500 chars as abstract
            "type": "synthesis",
            "source": "rltf_engine",
            "mass": evaluation["mass"],
            "entropy": evaluation["entropy"],
            "parent_nodes": [n.get("title", "Unknown") for n in cited_nodes[:5]],
            "created": evaluation["timestamp"]
        }
        
        # Add to graph
        self.upg.nodes[node_id] = new_node
        self.upg.ledger.append({
            "id": node_id,
            "title": new_node["title"],
            "score": evaluation["mass"],
            "verdict": "MINTED",
            "timestamp": evaluation["timestamp"]
        })
        
        # Persist
        self.upg.save_graph()
        self.minted_count += 1
        
        print(f"✅ MINTED: {node_id}")
        print(f"   Mass: {evaluation['mass']} | Entropy: {evaluation['entropy']}")
        
        return node_id
    
    def batch_evaluate(self, outputs):
        """
        Evaluate multiple outputs and return statistics.
        
        Args:
            outputs: List of tuples (output_text, cited_nodes, topic)
            
        Returns:
            dict: Batch statistics
        """
        results = []
        for output_text, cited_nodes, topic in outputs:
            result = self.evaluate(output_text, cited_nodes, topic)
            results.append(result)
        
        minted = sum(1 for r in results if r["verdict"] == "MINT")
        rejected = len(results) - minted
        avg_mass = sum(r["mass"] for r in results) / len(results) if results else 0
        
        return {
            "total": len(results),
            "minted": minted,
            "rejected": rejected,
            "acceptance_rate": round(minted / len(results), 3) if results else 0,
            "average_mass": round(avg_mass, 3),
            "results": results
        }


def demo_rltf():
    """Demonstration of the RLTF Engine."""
    print("=" * 60)
    print("🔥 RLTF ENGINE DEMONSTRATION")
    print("=" * 60)
    
    engine = RLTFEngine()
    
    # Test Case 1: High Mass, Low Entropy (Should MINT)
    print("\n📊 TEST 1: High Quality Output")
    output1 = "The Sovereign Agent maintains autonomy through Prime Lattice addressing. This is foundational to the TENT architecture."
    nodes1 = [
        {"title": "Sovereign Agent", "type": "solid", "source": "internal_code"},
        {"title": "Prime Lattice", "type": "axiom", "source": "internal_code"},
        {"title": "TENT Architecture", "type": "solid", "source": "internal_code"}
    ]
    result1 = engine.mint(output1, nodes1, "Agent Autonomy")
    
    # Test Case 2: Low Mass (Should REJECT)
    print("\n📊 TEST 2: Unsupported Output")
    output2 = "The system uses quantum entanglement to achieve faster-than-light communication across nodes."
    nodes2 = []  # No citations
    result2 = engine.mint(output2, nodes2, "Quantum Communication")
    
    # Test Case 3: High Entropy (Should REJECT)
    print("\n📊 TEST 3: Conflicting Sources")
    output3 = "Economics and Physics agree on market dynamics."
    nodes3 = [
        {"title": "Supply Demand", "type": "curriculum", "source": "economics"},
        {"title": "Thermodynamics", "type": "curriculum", "source": "physics"},
        {"title": "Game Theory", "type": "curriculum", "source": "math"},
        {"title": "Entropy Law", "type": "axiom", "source": "physics"},
        {"title": "Market Forces", "type": "external", "source": "reddit"}
    ]
    result3 = engine.mint(output3, nodes3, "Cross-Domain Synthesis")
    
    print("\n" + "=" * 60)
    print(f"📈 SESSION STATS: Minted {engine.minted_count} | Rejected {engine.rejected_count}")
    print("=" * 60)


if __name__ == "__main__":
    demo_rltf()
