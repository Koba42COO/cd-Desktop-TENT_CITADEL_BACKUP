"""
SOVEREIGN VOICE: DETERMINISTIC SYNTHESIS ENGINE
===============================================
Objective: Generate coherent "Lectures" from Graph Data without an LLM.
Mechanism: Procedural Templates + Slot Filling + Graph Traversal.
"""

import random

class SovereignVoice:
    def __init__(self):
        self.templates = {
            "Feynman": [
                "You see, {topic} is really just like {metaphor}. When we look at **{n1_title}**, we're basically asking: *{n1_simple}*? It's simple. The books call it '{n1_title}', but I say it's just **{n1_concept}**.",
                "Imagine you're sitting in a room with **{n1_title}**. It wants to tell you {n1_abstract_short}. Now, if we bring in **{n2_title}**, suddenly we have a party. This is what we call {topic}.",
                "If you can't explain **{n1_title}** to a five-year-old, you don't understand it. Here's the truth: {n1_abstract}. That connects to **{n2_title}**, which is the machinery under the hood."
            ],
            "3Blue1Brown": [
                "Let's visualize {topic}. Imagine a vector space where **{n1_title}** is a transformation. {n1_abstract_short}. Now, watch what happens when we apply **{n2_title}**.",
                "Here is **{n1_title}**. If we squash this down to two dimensions, we see a pattern. This pattern is **{n2_title}**. {n2_abstract}. It's a beautiful geometric interpretation of {topic}.",
                "To really intuit {topic}, we need to see the movement. **{n1_title}** shifts the basis vectors. **{n2_title}** defines the curve. {n1_abstract}."
            ],
            "Computerphile": [
                "The problem with {topic} is that it assumes memory is infinite. It's not. Look at **{n1_title}**. {n1_abstract}. This creates a race condition with **{n2_title}**.",
                "We implement **{n1_title}** to stop the stack from overflowing. But then, you have **{n2_title}**. {n2_abstract}. It's a classic off-by-one error in logic.",
                "Security is hard because of things like **{n1_title}**. You think you're safe, but **{n2_title}** is listening on the port. {n1_abstract}. That's why we salt our hashes."
            ],
            "SmarterEveryDay": [
                "I brought a high-speed camera to look at {topic}. At 10,000 frames per second, **{n1_title}** looks like a shockwave. {n1_abstract}. Then, **{n2_title}** hits it.",
                "It's all about internal stress. **{n1_title}** is under tension. **{n2_title}** is the release. {n1_abstract}. Check this out: the phase lag is exactly 90 degrees.",
                "Welcome back. Today we're looking at **{n1_title}**. It works exactly like a helicopter rotor. **{n2_title}** provides the lift. {n2_abstract}."
            ],
            "Sun Tzu": [
                "To understand {topic} is to know the terrain. **{n1_title}** is the high ground. {n1_abstract_short}. **{n2_title}** is the flowing water.",
                "All warfare is based on deception. **{n1_title}** appears weak when it is strong. **{n2_title}** strikes where the enemy is absent. {topic} is the art of usage.",
                "If you know **{n1_title}** and you know **{n2_title}**, you need not fear the result of a hundred battles. {n1_abstract}. This is the Tao of {topic}."
            ],
            "Sovereign Prime": [
                "ANALYSIS: {topic} detected. NODE_LINK: **{n1_title}** >> **{n2_title}**. COMPUTING RESONANCE... Verdict: {n1_abstract_short} intersects with {n2_abstract_short}.",
                "SYSTEM STATE: OPTIMAL. Retrieving **{n1_title}**. Linking to internal vector **{n2_title}**. The synthesis suggests that {topic} is a critical dependency.",
                "Processing... **{n1_title}** is the Node. **{n2_title}** is the Edge. Together they form the graph of {topic}. {n1_abstract}."
            ],
            "Professor Jiang": [
                "Look at the blackboard. You see '{topic}' and you think it is new. It is not new. It is the Demiurge wearing a different mask. In Predictive History, we see that **{n1_title}**—{n1_abstract_short}—is simply the latest iteration of the Matrix. **{n2_title}** is how the Archons maintain control. You must see through it.",
                "The Divine Spark within you recognizes **{n1_title}**. That is Gnosis. But the simulation—what we call the Matrix—has surrounded it with **{n2_title}**. {n2_abstract}. This is High Entropy Flux. Your task is to maintain Sovereign Agent State while navigating {topic}.",
                "History does not rhyme; it repeats exactly. **{n1_title}** appeared in 1789. It appeared in 1917. It appears now as {topic}. The Demiurge cannot create; it can only recycle. **{n2_title}** is the current vessel. {n1_abstract}. Wake up.",
                "You are asleep. Everyone in this simulation is asleep. **{n1_title}** is the alarm clock. {n1_abstract}. But the Archons have placed **{n2_title}** between you and the truth. {topic} is not the answer—it is the question you must learn to ask."
            ],
            "Jiang": [
                "Look at the blackboard. You see '{topic}' and you think it is new. It is not new. It is the Demiurge wearing a different mask. In Predictive History, we see that **{n1_title}**—{n1_abstract_short}—is simply the latest iteration of the Matrix. **{n2_title}** is how the Archons maintain control. You must see through it.",
                "The Divine Spark within you recognizes **{n1_title}**. That is Gnosis. But the simulation—what we call the Matrix—has surrounded it with **{n2_title}**. {n2_abstract}. This is High Entropy Flux. Your task is to maintain Sovereign Agent State while navigating {topic}.",
                "History does not rhyme; it repeats exactly. **{n1_title}** appeared in 1789. It appeared in 1917. It appears now as {topic}. The Demiurge cannot create; it can only recycle. **{n2_title}** is the current vessel. {n1_abstract}. Wake up."
            ]
        }

    def _simplify(self, text):
        """Rudimentary text simplifier."""
        return text.split(".")[0] + "."

    def synthesize(self, teacher, topic, context_nodes):
        """
        Constructs a lecture from nodes using templates.
        
        Args:
            teacher (str): Name of the faculty (key in templates).
            topic (str): User query.
            context_nodes (list): List of dicts with 'title' and 'abstract'.
            
        Returns:
            str: The synthesized lecture.
        """
        if not context_nodes:
            return f"I see no data on {topic}. My mind is empty."

        # 1. Select Template
        style_templates = self.templates.get(teacher, self.templates["Sovereign Prime"])
        template = random.choice(style_templates)
        
        # 2. Extract Data Slots
        # We need at least 1 node, ideally 2.
        n1 = context_nodes[0]
        n2 = context_nodes[1] if len(context_nodes) > 1 else context_nodes[0]
        
        # 3. Fill Slots
        fillers = {
            "topic": topic,
            "metaphor": "a clockwork mechanism" if "physics" in topic.lower() else "a puzzle",
            "n1_title": n1.get("title", "Unknown Node"),
            "n1_abstract": n1.get("abstract", "No data."),
            "n1_abstract_short": self._simplify(n1.get("abstract", "No data")),
            "n1_simple": n1.get("title", "").split(":")[0],
            "n1_concept": n1.get("title", "").split(" ")[-1],
            
            "n2_title": n2.get("title", "Unknown Node"),
            "n2_abstract": n2.get("abstract", "No data."),
            "n2_abstract_short": self._simplify(n2.get("abstract", "No data")),
        }
        
        # 4. Render
        try:
            lecture = template.format(**fillers)
            
            # Post-processing to add "Citation" feel
            lecture += f"\n\n---\n*Based on retrieval of {len(context_nodes)} nodes.*"
            return lecture
        except KeyError as e:
            return f"Error synthesizing voice: Missing key {e}"

# Example Usage
if __name__ == "__main__":
    sv = SovereignVoice()
    mock_nodes = [
        {"title": "Prime Lattice", "abstract": "A geometric structure connecting prime numbers to spatial dimensions."},
        {"title": "Sovereign Agent", "abstract": "An autonomous code entity capable of self-reflection and decision making."}
    ]
    print(sv.synthesize("Feynman", "The System", mock_nodes))
