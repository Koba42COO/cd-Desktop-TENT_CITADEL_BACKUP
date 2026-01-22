#!/usr/bin/env python3
"""TENT BUSINESS & LABOR CURRICULUM - Structured knowledge on Markets & Administration."""

from upg_store import UniversalPrimeGraph

def seed_business_labor():
    upg = UniversalPrimeGraph()
    print("=" * 60)
    print("BUSINESS & LABOR MARKETS CURRICULUM DESIGNER")
    print("=" * 60)

    curriculum = {
        "LABOR_101": {
            "title": "Labor Economics: Supply and Demand",
            "modules": [
                "The Labor Supply Curve: Leisure vs Income",
                "Labor Demand: Marginal Revenue Product",
                "Market Equilibrium in Labor Markets",
                "Elasticity of Labor Supply and Demand"
            ]
        },
        "LABOR_200": {
            "title": "Wage Determination and Inequality",
            "modules": [
                "Compensating Wage Differentials",
                "Human Capital Theory: Education as Investment",
                "The Economics of Discrimination",
                "Minimum Wage and Price Floors"
            ]
        },
        "LABOR_300": {
            "title": "Labor Market Frictions",
            "modules": [
                "Search and Matching Theory",
                "Unemployment Types: Frictional, Structural, Cyclical",
                "Labor Mobility and Migration",
                "Monopsony in Labor Markets"
            ]
        },
        "BUS_100": {
            "title": "Business Administration Fundamentals",
            "modules": [
                "Organizational Structure and Design",
                "Operations Management Basics",
                "Financial Accounting for Managers",
                "Marketing Mix and Strategy"
            ]
        },
        "BUS_200": {
            "title": "Corporate Strategy",
            "modules": [
                "Porter's Five Forces Analysis",
                "Competitive Advantage and Value Chains",
                "Strategic Alliances and M&A",
                "Corporate Social Responsibility (CSR)"
            ]
        },
        "BUS_300": {
            "title": "Entrepreneurship and Innovation",
            "modules": [
                "Venture Capital and Funding Stages",
                "Lean Startup Methodology",
                "Product-Market Fit",
                "Disruptive Innovation Theory"
            ]
        }
    }

    count = 0
    for code, data in curriculum.items():
        # Course Node
        course_id = f"CURRICULUM_{code}"
        upg.add_node(course_id, {
            "title": f"{code}: {data['title']}",
            "type": "course",
            "domain": "Business & Labor",
            "level": "Undergraduate",
            "source": "tent_curriculum_designer",
            "mass": "SOLID"
        })
        print(f"💼 Course: {code} - {data['title']}")
        count += 1

        # Module Nodes
        for i, mod_title in enumerate(data['modules']):
            mod_id = f"{course_id}_MOD_{i+1}"
            upg.add_node(mod_id, {
                "title": mod_title,
                "type": "module",
                "parent_course": course_id,
                "domain": "Business & Labor",
                "abstract": f"Module covering {mod_title} as part of {data['title']}.",
                "mass": "SOLID"
            })
            count += 1
    
    upg.save_graph()
    print(f"\n✅ Designed and Seeded {len(curriculum)} courses and {count - len(curriculum)} modules.")
    print(f"Total Nodes Added: {count}")

if __name__ == "__main__":
    seed_business_labor()
