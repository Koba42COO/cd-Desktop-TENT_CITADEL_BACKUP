#!/usr/bin/env python3
"""TENT OPTIMIZATION CURRICULUM - Addressing the 'Constraints' curiosity."""

from upg_store import UniversalPrimeGraph

def seed_optimization():
    upg = UniversalPrimeGraph()
    print("=" * 60)
    print("OPTIMIZATION & CONSTRAINTS CURRICULUM")
    print("=" * 60)

    curriculum = {
        "OPT_100": {
            "title": "Introduction to Mathematical Optimization",
            "modules": [
                "Unconstrained Optimization Basics",
                "Gradient Descent and Newton's Method",
                "Constraint Satisfaction Problems (CSP)",
                "Lagrange Multipliers and Duality"
            ]
        },
        "OPT_200": {
            "title": "Linear Programming (LP)",
            "modules": [
                "The Simplex Algorithm",
                "Primal-Dual Relationships",
                "Sensitivity Analysis",
                "Integer Linear Programming (ILP)"
            ]
        },
        "OPT_300": {
            "title": "Convex Optimization",
            "modules": [
                "Convex Sets and Functions",
                "Semidefinite Programming (SDP)",
                "Geometric Programming",
                "Interior-Point Methods"
            ]
        },
        "OPT_400": {
            "title": "Combinatorial Optimization",
            "modules": [
                "Graph Theory and Network Flow",
                "The Traveling Salesperson Problem (TSP)",
                "Knapsack Problems and Heuristics",
                "NP-Hardness and Approximation Algorithms"
            ]
        },
        "OPT_500": {
            "title": "Control Theory and Dynamic Systems",
            "modules": [
                "State-Space Representation",
                "PID Controllers and Feedback Loops",
                "Optimal Control (Pontryagin's Maximum Principle)",
                "Model Predictive Control (MPC)"
            ]
        }
    }

    count = 0
    for code, data in curriculum.items():
        course_id = f"CURRICULUM_{code}"
        upg.add_node(course_id, {
            "title": f"{code}: {data['title']}",
            "type": "course",
            "domain": "Mathematics",
            "level": "Advanced",
            "source": "tent_curriculum_designer",
            "mass": "SOLID"
        })
        print(f"📐 Course: {code} - {data['title']}")
        count += 1

        for i, mod_title in enumerate(data['modules']):
            mod_id = f"{course_id}_MOD_{i+1}"
            upg.add_node(mod_id, {
                "title": mod_title,
                "type": "module",
                "parent_course": course_id,
                "domain": "Mathematics",
                "abstract": f"Module covering {mod_title} as part of {data['title']}.",
                "mass": "SOLID"
            })
            count += 1
    
    upg.save_graph()
    print(f"\n✅ Designed and Seeded {len(curriculum)} courses and {count - len(curriculum)} modules.")
    print(f"Total Nodes Added: {count}")

if __name__ == "__main__":
    seed_optimization()
