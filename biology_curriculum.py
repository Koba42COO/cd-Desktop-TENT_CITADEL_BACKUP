#!/usr/bin/env python3
"""TENT BIOLOGY CURRICULUM - Addressing the 'Cells' curiosity."""

from upg_store import UniversalPrimeGraph

def seed_biology():
    upg = UniversalPrimeGraph()
    print("=" * 60)
    print("COMPUTATIONAL BIOLOGY CURRICULUM")
    print("=" * 60)

    curriculum = {
        "BIO_100": {
            "title": "Cellular Biology Fundamentals",
            "modules": [
                "Structure of Eukaryotic and Prokaryotic Cells",
                "Cell Membrane Dynamics and Signaling",
                "Metabolism: Glycolysis and Krebs Cycle",
                "Cell Division: Mitosis and Meiosis"
            ]
        },
        "BIO_200": {
            "title": "Genetics and Genomics",
            "modules": [
                "DNA Structure and Replication",
                "Transcription and Translation (Central Dogma)",
                "Gene Regulation and Epigenetics",
                "CRISPR/Cas9 and Gene Editing"
            ]
        },
        "BIO_300": {
            "title": "Bioinformatics and Computational Biology",
            "modules": [
                "Sequence Alignment Algorithms (BLAST)",
                "Protein Folding and AlphaFold",
                "Phylogenetic Tree Construction",
                "Genome Assembly Techniques"
            ]
        },
        "BIO_400": {
            "title": "Systems Biology",
            "modules": [
                "Biological Oscillators and Circadian Rhythms",
                "Gene Regulatory Networks (GRNs)",
                "Metabolic Flux Analysis",
                "Synthetic Biology and Circuit Design"
            ]
        },
        "BIO_500": {
            "title": "Neuroscience and Biophysics",
            "modules": [
                "Action Potentials and Ion Channels",
                "Synaptic Plasticity (LTP/LTD)",
                "Hodgkin-Huxley Model",
                "Neural Encoding and Decoding"
            ]
        }
    }

    count = 0
    for code, data in curriculum.items():
        course_id = f"CURRICULUM_{code}"
        upg.add_node(course_id, {
            "title": f"{code}: {data['title']}",
            "type": "course",
            "domain": "Biology",
            "level": "Undergraduate/Graduate",
            "source": "tent_curriculum_designer",
            "mass": "SOLID"
        })
        print(f"🧬 Course: {code} - {data['title']}")
        count += 1

        for i, mod_title in enumerate(data['modules']):
            mod_id = f"{course_id}_MOD_{i+1}"
            upg.add_node(mod_id, {
                "title": mod_title,
                "type": "module",
                "parent_course": course_id,
                "domain": "Biology",
                "abstract": f"Module covering {mod_title} as part of {data['title']}.",
                "mass": "SOLID"
            })
            count += 1
    
    upg.save_graph()
    print(f"\n✅ Designed and Seeded {len(curriculum)} courses and {count - len(curriculum)} modules.")
    print(f"Total Nodes Added: {count}")

if __name__ == "__main__":
    seed_biology()
