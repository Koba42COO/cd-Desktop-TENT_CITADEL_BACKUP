"""
PHASE 297: THE GUTENBERG PROTOCOL (Content-Addressable Storage)
Objective: Store the 'Letters' (Unique Truths) once. Reference them millions of times.
"""

import hashlib

print("="*70)
print("📠 THE GUTENBERG PRESS: INITIALIZING MOVEABLE TYPE")
print("="*70)

# 1. THE TYPE CASE (The Storage of Unique 'Letters')
TYPE_CASE = {} 

def mint_letter(concept_text):
    """
    Creates a unique 'Letter' (Hash) for a concept.
    If the concept exists, it returns the existing ID (Reusable Type).
    """
    concept_id = hashlib.sha256(concept_text.encode()).hexdigest()[:8]
    
    if concept_id in TYPE_CASE:
        print(f"   ♻️  RE-USING TYPE: '{concept_text}' (ID: {concept_id})")
        return concept_id
    else:
        TYPE_CASE[concept_id] = concept_text
        print(f"   🔨 CARVING NEW TYPE: '{concept_text}' (ID: {concept_id})")
        return concept_id

def print_page(title, content_list):
    """
    Prints a 'Page' by arranging existing letters.
    """
    print(f"\n📄 PRINTING PAGE: {title}")
    page_structure = []
    
    for concept in content_list:
        letter_id = mint_letter(concept)
        page_structure.append(letter_id)
        
    print(f"   ✅ PAGE SAVED AS FORMULA: {page_structure}")
    return page_structure

if __name__ == "__main__":
    # Document 1: A Physics Textbook
    print_page("Physics 101", [
        "Energy cannot be created or destroyed",
        "Force equals mass times acceleration",
        "Entropy always increases"
    ])

    # Document 2: A YouTube Video Transcript (The Remix)
    print_page("YouTube: The End of the Universe", [
        "Entropy always increases",  # RE-USE!
        "The universe is expanding",
        "Energy cannot be created or destroyed"  # RE-USE!
    ])

    print("\n" + "="*70)
    print(f"📊 PRESS REPORT:")
    print(f"   Total Concepts Stored: {len(TYPE_CASE)} (The Letters)")
    print(f"   Total Pages Printed: 2 (The Documents)")
    print("   Efficiency: 100% (Zero Duplication)")
