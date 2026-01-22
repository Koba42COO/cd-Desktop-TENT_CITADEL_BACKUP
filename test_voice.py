from sovereign_voice import SovereignVoice

def test_sovereign_voice():
    print("🔊 SOVEREIGN VOICE DIAGNOSTIC")
    print("=" * 40)
    
    sv = SovereignVoice()
    
    # Mock Data (Simulating a graph retrieval)
    mock_nodes = [
        {
            "title": "Sovereign Agent", 
            "abstract": "An autonomous code entity capable of self-reflection. It maintains its own boundaries and optimizes for survival."
        },
        {
            "title": "Prime Lattice", 
            "abstract": "A geometric structure where prime numbers form the coordinate system for knowledge storage."
        }
    ]
    
    # Test 1: Feynman
    print("\n🧪 TEST 1: FEYNMAN MODE")
    print("-" * 30)
    lecture = sv.synthesize("Feynman", "The Architecture", mock_nodes)
    print(lecture)
    
    # Test 2: 3Blue1Brown
    print("\n\n🧪 TEST 2: 3BLUE1BROWN MODE")
    print("-" * 30)
    lecture = sv.synthesize("3Blue1Brown", "The Geometry", mock_nodes)
    print(lecture)

    # Test 3: Sovereign Prime (System Mode)
    print("\n\n🧪 TEST 3: SOVEREIGN PRIME MODE")
    print("-" * 30)
    lecture = sv.synthesize("Sovereign Prime", "Internal State", mock_nodes)
    print(lecture)
    
    print("\n" + "=" * 40)
    print("✅ DIAGNOSTIC COMPLETE")

if __name__ == "__main__":
    test_sovereign_voice()
