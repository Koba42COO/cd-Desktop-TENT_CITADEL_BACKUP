#!/usr/bin/env python3
"""TENT ECONOMICS CURRICULUM - Bridging the identified knowledge gap."""

from upg_store import UniversalPrimeGraph

def seed_economics():
    upg = UniversalPrimeGraph()
    print("=" * 60)
    print("ECONOMICS CURRICULUM DESIGNER")
    print("=" * 60)

    # 1. Define the Curriculum Structure
    curriculum = {
        "ECON_100": {
            "title": "Foundations of Modern Economics",
            "modules": [
                "Principles of Scarcity and Choice",
                "Supply and Demand Dynamics",
                "Market Equilibrium",
                "Elasticity and Consumer Surplus"
            ]
        },
        "ECON_200": {
            "title": "Microeconomic Theory",
            "modules": [
                "Consumer Theory and Utility Maximization",
                "Producer Theory and Cost Minimization",
                "Market Structures: Perfect Competition vs Monopoly",
                "Oligopoly and Strategic Behavior"
            ]
        },
        "ECON_201": {
            "title": "Macroeconomic Theory",
            "modules": [
                "GDP and National Income Accounting",
                "Inflation and Unemployment",
                "fiscal Policy and Government Spending",
                "Monetary Policy and Central Banking"
            ]
        },
        "ECON_300": {
            "title": "Game Theory & Strategic Interaction",
            "modules": [
                "Nash Equilibrium Foundations",
                "Prisoner's Dilemma and Cooperation",
                "Sequential Games and Backward Induction",
                "Evolutionary Game Theory"
            ]
        },
        "ECON_350": {
            "title": "Behavioral Economics and Psychology",
            "modules": [
                "Heuristics and Biases in Decision Making",
                "Prospect Theory and Loss Aversion",
                "Intertemporal Choice and Hyperbolic Discounting",
                "Nudging and Choice Architecture"
            ]
        },
        "ECON_400": {
            "title": "Econometrics and Data Analysis",
            "modules": [
                "Linear Regression Models",
                "Causal Inference in Social Sciences",
                "Time Series Analysis",
                "Panel Data Methods"
            ]
        },
        "ECON_500": {
            "title": "Digital Economy and Tokenomics",
            "modules": [
                "Network Effects and Platform Economics",
                "Cryptoeconomics and Mechanism Design",
                "Economics of Artificial Intelligence",
                "Information Asymmetry in Digital Markets"
            ]
        }
    }

    # 2. Seed into UPG
    count = 0
    for code, data in curriculum.items():
        # Create Course Node
        course_id = f"CURRICULUM_{code}"
        upg.add_node(course_id, {
            "title": f"{code}: {data['title']}",
            "type": "course",
            "domain": "Economics",
            "level": "Undergraduate/Graduate",
            "source": "tent_curriculum_designer",
            "mass": "SOLID"
        })
        print(f"📚 Course: {code} - {data['title']}")
        count += 1

        # Create Module Nodes
        for i, mod_title in enumerate(data['modules']):
            mod_id = f"{course_id}_MOD_{i+1}"
            upg.add_node(mod_id, {
                "title": mod_title,
                "type": "module",
                "parent_course": course_id,
                "domain": "Economics",
                "abstract": f"Module covering {mod_title} as part of {data['title']}.",
                "mass": "SOLID"
            })
            # Link module to course (implicit via parent_course, but could be explicit edge)
            count += 1
    
    upg.save_graph()
    print(f"\n✅ Designed and Seeded {len(curriculum)} courses and {count - len(curriculum)} modules.")
    print(f"Total Nodes Added: {count}")

if __name__ == "__main__":
    seed_economics()
