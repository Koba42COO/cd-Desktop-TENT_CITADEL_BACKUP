#!/usr/bin/env python3
"""TENT TALENT INTELLIGENCE CURRICULUM - Addressing the 'Hiring' curiosity."""

from upg_store import UniversalPrimeGraph

def seed_talent_intelligence():
    upg = UniversalPrimeGraph()
    print("=" * 60)
    print("TALENT INTELLIGENCE CURRICULUM DESIGNER")
    print("=" * 60)

    curriculum = {
        "HR_100": {
            "title": "Fundamentals of Human Capital",
            "modules": [
                "Evolution of HR: From Admin to Strategy",
                "The Employee Lifecycle Model",
                "Compliance and Employment Law Basics",
                "Diversity, Equity, and Inclusion (DEI) Foundations"
            ]
        },
        "HR_200": {
            "title": "Technical Recruiting & Talent Acquisition",
            "modules": [
                "Sourcing Strategies: Boolean Search & OSINT",
                "Candidate Pipeline Management",
                "Structuring Effective Technical Interviews",
                "Employer Branding and Value Proposition"
            ]
        },
        "HR_300": {
            "title": "Organizational Psychology",
            "modules": [
                "Motivation Theory and Job Design",
                "Group Dynamics and Team Performance",
                "Leadership Styles and Emotional Intelligence",
                "Organizational Culture and Change Management"
            ]
        },
        "HR_350": {
            "title": "Performance Management & Development",
            "modules": [
                "KPIs, OKRs, and Goal Setting",
                "Feedback Loops and Radical Candor",
                "Learning and Development (L&D) Strategies",
                "Retention and Succession Planning"
            ]
        },
        "HR_400": {
            "title": "People Analytics and Data Science",
            "modules": [
                "HR Metrics and Dashboarding",
                "Predictive Analytics for Attrition",
                "Network Analysis of Organizational Communication",
                "Bias Detection in Hiring Algorithms"
            ]
        },
        "HR_500": {
            "title": "The Future of Work",
            "modules": [
                "Remote and Asynchronous Work paradigms",
                "The Gig Economy and Contract Workforces",
                "AI Augmentation in the Workplace",
                "Human-Centric Workspace Design"
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
            "domain": "Talent Intelligence",
            "level": "Professional",
            "source": "tent_curriculum_designer",
            "mass": "SOLID"
        })
        print(f"👥 Course: {code} - {data['title']}")
        count += 1

        # Module Nodes
        for i, mod_title in enumerate(data['modules']):
            mod_id = f"{course_id}_MOD_{i+1}"
            upg.add_node(mod_id, {
                "title": mod_title,
                "type": "module",
                "parent_course": course_id,
                "domain": "Talent Intelligence",
                "abstract": f"Module covering {mod_title} as part of {data['title']}.",
                "mass": "SOLID"
            })
            count += 1
    
    upg.save_graph()
    print(f"\n✅ Designed and Seeded {len(curriculum)} courses and {count - len(curriculum)} modules.")
    print(f"Total Nodes Added: {count}")

if __name__ == "__main__":
    seed_talent_intelligence()
