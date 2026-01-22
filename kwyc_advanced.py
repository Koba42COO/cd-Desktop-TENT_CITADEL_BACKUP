#!/usr/bin/env python3
"""
Keep What You Code, Novelty Detection, and Credit Systems
Comprehensive Implementation

This module implements:
1. KWYC (Keep What You Code) - Cryptographic code ownership
2. Novelty Detection - Identifying novel contributions
3. Credit Systems - Fair attribution and rewards
"""

import hashlib
import json
import time
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from collections import defaultdict
import numpy as np
from scipy.spatial.distance import cosine
import networkx as nx


@dataclass
class CodeContribution:
    """Represents a code contribution with metadata"""
    hash: str
    previous_hash: Optional[str]
    owner: str
    owner_public_key: str
    signature: str
    timestamp: str
    code: str
    language: str
    lines: int
    functions: int
    complexity: float
    dependencies: List[str]
    license: str


@dataclass
class NoveltyScore:
    """Novelty analysis results"""
    code_hash: str
    semantic_novelty: float
    structural_novelty: float
    temporal_novelty: float
    combined_novelty: float
    similar_codes: List[str]


@dataclass
class CreditScore:
    """Credit calculation results"""
    code_hash: str
    base_credit: float
    novelty_multiplier: float
    impact_multiplier: float
    final_credit: float
    owner: str


class KWYCSystem:
    """
    Keep What You Code System
    Provides cryptographic proof of code ownership
    """
    
    def __init__(self):
        self.contributions: Dict[str, CodeContribution] = {}
        self.ownership_chains: Dict[str, List[str]] = {}
    
    def hash_code(self, code: str, metadata: Dict[str, Any]) -> str:
        """
        Compute cryptographic hash of code and metadata
        
        Args:
            code: Source code
            metadata: Additional metadata
        
        Returns:
            SHA-256 hash as hex string
        """
        content = code + json.dumps(metadata, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()
    
    def register_contribution(
        self,
        code: str,
        owner: str,
        owner_public_key: str,
        previous_hash: Optional[str] = None,
        language: str = "python",
        license: str = "MIT",
        dependencies: Optional[List[str]] = None
    ) -> CodeContribution:
        """
        Register a new code contribution
        
        Args:
            code: Source code
            owner: Owner identifier
            owner_public_key: Owner's public key
            previous_hash: Hash of previous contribution (for chain)
            language: Programming language
            license: License type
            dependencies: List of dependency hashes
        
        Returns:
            CodeContribution object
        """
        # Calculate code metrics
        lines = len(code.split('\n'))
        functions = code.count('def ') + code.count('function ')
        complexity = self._calculate_complexity(code)
        
        # Create metadata
        metadata = {
            'language': language,
            'lines': lines,
            'functions': functions,
            'complexity': complexity,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Compute hash
        code_hash = self.hash_code(code, metadata)
        
        # Create signature (simplified - in production, use real crypto)
        signature = self._sign(code_hash, owner_public_key)
        
        # Create contribution
        contribution = CodeContribution(
            hash=code_hash,
            previous_hash=previous_hash,
            owner=owner,
            owner_public_key=owner_public_key,
            signature=signature,
            timestamp=datetime.utcnow().isoformat(),
            code=code,
            language=language,
            lines=lines,
            functions=functions,
            complexity=complexity,
            dependencies=dependencies or [],
            license=license
        )
        
        # Store
        self.contributions[code_hash] = contribution
        
        # Update ownership chain
        if previous_hash:
            if previous_hash in self.ownership_chains:
                self.ownership_chains[code_hash] = self.ownership_chains[previous_hash] + [code_hash]
            else:
                self.ownership_chains[code_hash] = [previous_hash, code_hash]
        else:
            self.ownership_chains[code_hash] = [code_hash]
        
        return contribution
    
    def verify_ownership(self, code_hash: str, owner: str) -> bool:
        """
        Verify ownership of a code contribution
        
        Args:
            code_hash: Hash of the contribution
            owner: Owner to verify
        
        Returns:
            True if owner is verified
        """
        if code_hash not in self.contributions:
            return False
        
        contribution = self.contributions[code_hash]
        return contribution.owner == owner
    
    def get_ownership_chain(self, code_hash: str) -> List[str]:
        """
        Get the ownership chain for a contribution
        
        Args:
            code_hash: Hash of the contribution
        
        Returns:
            List of hashes in the chain
        """
        return self.ownership_chains.get(code_hash, [])
    
    def _calculate_complexity(self, code: str) -> float:
        """Calculate cyclomatic complexity (simplified)"""
        complexity = 1  # Base complexity
        complexity += code.count('if ') + code.count('elif ')
        complexity += code.count('for ') + code.count('while ')
        complexity += code.count('except ') + code.count('catch ')
        complexity += code.count('and ') + code.count('or ')
        return float(complexity)
    
    def _sign(self, message: str, public_key: str) -> str:
        """Create signature (simplified - use real crypto in production)"""
        return hashlib.sha256((message + public_key).encode()).hexdigest()


class NoveltyDetector:
    """
    Novelty Detection System
    Identifies novel code contributions
    """
    
    def __init__(self, kwyc_system: KWYCSystem):
        self.kwyc = kwyc_system
        self.code_embeddings: Dict[str, np.ndarray] = {}
        self.weights = {
            'semantic': 0.4,
            'structural': 0.3,
            'temporal': 0.3
        }
    
    def embed_code(self, code: str) -> np.ndarray:
        """
        Embed code into vector space
        
        Args:
            code: Source code
        
        Returns:
            Embedding vector
        """
        # Simplified embedding: use character n-grams
        # In production, use AST parsing and neural embeddings
        n = 3
        ngrams = [code[i:i+n] for i in range(len(code) - n + 1)]
        vector = np.zeros(256)  # 256-dimensional vector
        
        for ngram in ngrams:
            idx = hash(ngram) % 256
            vector[idx] += 1
        
        # Normalize
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        
        return vector
    
    def compute_semantic_similarity(self, code1: str, code2: str) -> float:
        """
        Compute semantic similarity between two code snippets
        
        Args:
            code1: First code snippet
            code2: Second code snippet
        
        Returns:
            Similarity score in [0, 1]
        """
        v1 = self.embed_code(code1)
        v2 = self.embed_code(code2)
        
        # Cosine similarity
        similarity = 1 - cosine(v1, v2)
        return max(0.0, min(1.0, similarity))
    
    def compute_structural_similarity(self, code1: str, code2: str) -> float:
        """
        Compute structural similarity (simplified AST comparison)
        
        Args:
            code1: First code snippet
            code2: Second code snippet
        
        Returns:
            Similarity score in [0, 1]
        """
        # Extract structure: function names, class names, control flow
        def extract_structure(code):
            structure = []
            structure.append(code.count('def '))
            structure.append(code.count('class '))
            structure.append(code.count('if '))
            structure.append(code.count('for '))
            structure.append(code.count('while '))
            structure.append(code.count('return '))
            return np.array(structure)
        
        s1 = extract_structure(code1)
        s2 = extract_structure(code2)
        
        # Normalize
        norm1 = np.linalg.norm(s1)
        norm2 = np.linalg.norm(s2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        # Cosine similarity
        similarity = np.dot(s1, s2) / (norm1 * norm2)
        return max(0.0, min(1.0, similarity))
    
    def analyze_novelty(self, code: str, code_hash: str) -> NoveltyScore:
        """
        Analyze code for novelty
        
        Args:
            code: Source code to analyze
            code_hash: Hash of the code
        
        Returns:
            NoveltyScore object
        """
        # Get all existing contributions
        existing_hashes = list(self.kwyc.contributions.keys())
        
        if len(existing_hashes) == 0:
            # First contribution is always novel
            return NoveltyScore(
                code_hash=code_hash,
                semantic_novelty=1.0,
                structural_novelty=1.0,
                temporal_novelty=1.0,
                combined_novelty=1.0,
                similar_codes=[]
            )
        
        # Compute similarities
        semantic_similarities = []
        structural_similarities = []
        similar_codes = []
        
        for existing_hash in existing_hashes:
            existing_contrib = self.kwyc.contributions[existing_hash]
            existing_code = existing_contrib.code
            
            sem_sim = self.compute_semantic_similarity(code, existing_code)
            struct_sim = self.compute_structural_similarity(code, existing_code)
            
            semantic_similarities.append(sem_sim)
            structural_similarities.append(struct_sim)
            
            # Track similar codes (threshold: 0.7)
            if sem_sim > 0.7 or struct_sim > 0.7:
                similar_codes.append(existing_hash)
        
        # Novelty scores (inverse of similarity)
        max_sem_sim = max(semantic_similarities) if semantic_similarities else 0.0
        max_struct_sim = max(structural_similarities) if structural_similarities else 0.0
        
        semantic_novelty = 1.0 - max_sem_sim
        structural_novelty = 1.0 - max_struct_sim
        
        # Temporal novelty: check if this is first appearance
        temporal_novelty = 1.0 if len(similar_codes) == 0 else 0.0
        
        # Combined novelty
        combined_novelty = (
            self.weights['semantic'] * semantic_novelty +
            self.weights['structural'] * structural_novelty +
            self.weights['temporal'] * temporal_novelty
        )
        
        return NoveltyScore(
            code_hash=code_hash,
            semantic_novelty=semantic_novelty,
            structural_novelty=structural_novelty,
            temporal_novelty=temporal_novelty,
            combined_novelty=combined_novelty,
            similar_codes=similar_codes
        )


class CreditSystem:
    """
    Credit System
    Calculates and distributes credit for contributions
    """
    
    def __init__(self, kwyc_system: KWYCSystem, novelty_detector: NoveltyDetector):
        self.kwyc = kwyc_system
        self.novelty = novelty_detector
        self.usage_counts: Dict[str, int] = defaultdict(int)
        self.credit_scores: Dict[str, CreditScore] = {}
        
        # Parameters
        self.alpha = 1.0  # LOC weight
        self.beta = 5.0  # Complexity weight
        self.gamma = 2.0  # Novelty bonus factor
        self.delta = 0.5  # Impact multiplier factor
    
    def calculate_credit(self, code_hash: str) -> CreditScore:
        """
        Calculate credit for a code contribution
        
        Args:
            code_hash: Hash of the contribution
        
        Returns:
            CreditScore object
        """
        if code_hash not in self.kwyc.contributions:
            raise ValueError(f"Contribution {code_hash} not found")
        
        contribution = self.kwyc.contributions[code_hash]
        
        # Base credit
        base_credit = (
            self.alpha * contribution.lines +
            self.beta * contribution.complexity
        )
        
        # Get novelty score
        novelty_score = self.novelty.analyze_novelty(
            contribution.code,
            code_hash
        )
        
        # Novelty multiplier
        novelty_multiplier = 1.0 + self.gamma * novelty_score.combined_novelty
        
        # Impact multiplier (based on usage)
        usage = self.usage_counts.get(code_hash, 0)
        impact_multiplier = 1.0 + self.delta * np.log(1 + usage)
        
        # Final credit
        final_credit = base_credit * novelty_multiplier * impact_multiplier
        
        credit_score = CreditScore(
            code_hash=code_hash,
            base_credit=base_credit,
            novelty_multiplier=novelty_multiplier,
            impact_multiplier=impact_multiplier,
            final_credit=final_credit,
            owner=contribution.owner
        )
        
        self.credit_scores[code_hash] = credit_score
        return credit_score
    
    def record_usage(self, code_hash: str):
        """Record that code is being used"""
        self.usage_counts[code_hash] += 1
    
    def get_user_credit(self, owner: str) -> float:
        """
        Get total credit for a user
        
        Args:
            owner: Owner identifier
        
        Returns:
            Total credit
        """
        total = 0.0
        for contrib_hash, contrib in self.kwyc.contributions.items():
            if contrib.owner == owner:
                if contrib_hash in self.credit_scores:
                    total += self.credit_scores[contrib_hash].final_credit
                else:
                    # Calculate if not already done
                    credit = self.calculate_credit(contrib_hash)
                    total += credit.final_credit
        return total
    
    def distribute_rewards(self, total_reward: float) -> Dict[str, float]:
        """
        Distribute rewards proportionally based on credit
        
        Args:
            total_reward: Total reward amount
        
        Returns:
            Dictionary mapping owners to rewards
        """
        # Calculate total credit
        total_credit = sum(
            score.final_credit
            for score in self.credit_scores.values()
        )
        
        if total_credit == 0:
            return {}
        
        # Distribute proportionally
        rewards = {}
        for score in self.credit_scores.values():
            owner = score.owner
            if owner not in rewards:
                rewards[owner] = 0.0
            rewards[owner] += (score.final_credit / total_credit) * total_reward
        
        return rewards


# Example Usage

if __name__ == "__main__":
    print("=" * 80)
    print("Keep What You Code, Novelty Detection, and Credit Systems")
    print("=" * 80)
    print()
    
    # Initialize systems
    kwyc = KWYCSystem()
    novelty = NoveltyDetector(kwyc)
    credit = CreditSystem(kwyc, novelty)
    
    # Example 1: Register first contribution
    print("Example 1: Register First Contribution")
    print("-" * 80)
    
    code1 = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
    
    contrib1 = kwyc.register_contribution(
        code=code1,
        owner="alice",
        owner_public_key="alice_pub_key_123",
        language="python"
    )
    
    print(f"Registered: {contrib1.hash[:16]}...")
    print(f"Owner: {contrib1.owner}")
    print(f"Lines: {contrib1.lines}, Complexity: {contrib1.complexity}")
    
    # Analyze novelty
    novelty1 = novelty.analyze_novelty(code1, contrib1.hash)
    print(f"Novelty Score: {novelty1.combined_novelty:.3f}")
    print(f"  Semantic: {novelty1.semantic_novelty:.3f}")
    print(f"  Structural: {novelty1.structural_novelty:.3f}")
    print(f"  Temporal: {novelty1.temporal_novelty:.3f}")
    
    # Calculate credit
    credit1 = credit.calculate_credit(contrib1.hash)
    print(f"Credit: {credit1.final_credit:.2f}")
    print(f"  Base: {credit1.base_credit:.2f}")
    print(f"  Novelty Multiplier: {credit1.novelty_multiplier:.2f}x")
    print()
    
    # Example 2: Register similar contribution (low novelty)
    print("Example 2: Register Similar Contribution (Low Novelty)")
    print("-" * 80)
    
    code2 = """
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
"""
    
    contrib2 = kwyc.register_contribution(
        code=code2,
        owner="bob",
        owner_public_key="bob_pub_key_456",
        previous_hash=contrib1.hash,
        language="python"
    )
    
    print(f"Registered: {contrib2.hash[:16]}...")
    
    # Analyze novelty (should be low due to similarity)
    novelty2 = novelty.analyze_novelty(code2, contrib2.hash)
    print(f"Novelty Score: {novelty2.combined_novelty:.3f}")
    print(f"Similar Codes: {len(novelty2.similar_codes)}")
    
    # Calculate credit (should be lower due to low novelty)
    credit2 = credit.calculate_credit(contrib2.hash)
    print(f"Credit: {credit2.final_credit:.2f}")
    print()
    
    # Example 3: Register novel contribution
    print("Example 3: Register Novel Contribution (High Novelty)")
    print("-" * 80)
    
    code3 = """
class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    
    def add_node(self, node_id, data=None):
        self.nodes[node_id] = data
    
    def add_edge(self, from_node, to_node, weight=1):
        self.edges.append((from_node, to_node, weight))
    
    def shortest_path(self, start, end):
        # Dijkstra's algorithm implementation
        distances = {start: 0}
        visited = set()
        # ... implementation ...
        return distances.get(end, float('inf'))
"""
    
    contrib3 = kwyc.register_contribution(
        code=code3,
        owner="charlie",
        owner_public_key="charlie_pub_key_789",
        previous_hash=contrib2.hash,
        language="python"
    )
    
    print(f"Registered: {contrib3.hash[:16]}...")
    
    # Analyze novelty (should be high)
    novelty3 = novelty.analyze_novelty(code3, contrib3.hash)
    print(f"Novelty Score: {novelty3.combined_novelty:.3f}")
    
    # Record usage
    credit.record_usage(contrib3.hash)
    credit.record_usage(contrib3.hash)
    credit.record_usage(contrib3.hash)
    
    # Calculate credit (should be high due to novelty and usage)
    credit3 = credit.calculate_credit(contrib3.hash)
    print(f"Credit: {credit3.final_credit:.2f}")
    print(f"  Base: {credit3.base_credit:.2f}")
    print(f"  Novelty Multiplier: {credit3.novelty_multiplier:.2f}x")
    print(f"  Impact Multiplier: {credit3.impact_multiplier:.2f}x")
    print()
    
    # Example 4: User credit summary
    print("Example 4: User Credit Summary")
    print("-" * 80)
    
    for owner in ["alice", "bob", "charlie"]:
        total = credit.get_user_credit(owner)
        print(f"{owner}: {total:.2f} credits")
    print()
    
    # Example 5: Reward distribution
    print("Example 5: Reward Distribution")
    print("-" * 80)
    
    total_reward = 10000.0
    rewards = credit.distribute_rewards(total_reward)
    
    for owner, reward in rewards.items():
        print(f"{owner}: ${reward:.2f}")
    print()
    
    print("=" * 80)
    print("✓ System Demonstration Complete")
    print("=" * 80)
