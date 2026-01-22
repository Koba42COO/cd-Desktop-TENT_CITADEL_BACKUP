"""
CITADEL BRIDGE MODULE (THE LIBRARY)
Interface to Kiwix offline Wikipedia and local knowledge.
"""

import os
import requests

KIWIX_PORT = 8080
KIWIX_URL = f"http://localhost:{KIWIX_PORT}"
LIBRARY_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'library')

def check_status():
    """Check if Kiwix server is running."""
    try:
        r = requests.get(KIWIX_URL, timeout=2)
        if r.status_code == 200:
            return "ONLINE"
    except:
        pass
    return "OFFLINE"

def is_offline():
    """Check if we're in offline mode (no internet)."""
    try:
        requests.get("https://google.com", timeout=3)
        return False
    except:
        return True

def search_kiwix(query):
    """Search the local Kiwix library."""
    status = check_status()
    if status != "ONLINE":
        return f"[KIWIX OFFLINE] Cannot search for: {query}"
    
    try:
        # Kiwix search endpoint
        search_url = f"{KIWIX_URL}/search?pattern={query}"
        r = requests.get(search_url, timeout=5)
        if r.status_code == 200:
            # Extract first result text (simplified)
            return r.text[:1000]
    except Exception as e:
        return f"Search error: {e}"
    
    return "No results found."

def list_zim_files():
    """List available .zim files in library."""
    if not os.path.exists(LIBRARY_PATH):
        return []
    return [f for f in os.listdir(LIBRARY_PATH) if f.endswith('.zim')]

def get_library_stats():
    """Get stats about the local library."""
    zim_files = list_zim_files()
    return {
        "kiwix_status": check_status(),
        "zim_files": len(zim_files),
        "offline_mode": is_offline()
    }

# -----------------------------------------------------
# PDF TEXTBOOK MODULE (Phase 305)
# -----------------------------------------------------
from pypdf import PdfReader

def read_textbook(book_name, query):
    """
    Search a specific physics book for a concept.
    Expected location: data/library/physics/{book_name}.pdf
    """
    # Sanitize book_name (add .pdf if missing)
    if not book_name.endswith('.pdf'):
        book_name += ".pdf"
        
    path = os.path.join(LIBRARY_PATH, 'physics', book_name)
    print(f"   📖 OPENING TEXTBOOK: {book_name}...")
    
    if not os.path.exists(path):
        return f"LIBRARY ERROR: Book '{book_name}' not found in {path}"

    try:
        reader = PdfReader(path)
        # (Simple Search - Advanced RAG would use vectors)
        results = []
        hits = 0
        
        # Scan first 100 pages or full book? 
        # Textbooks are huge. Let's limit scan or assume full scan is needed but slow.
        # User snippet implied full scan but "break after 3 hits".
        
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and query.lower() in text.lower():
                # Extract a snippet around the match? Or whole page?
                # User snippet return "f'[Page {i+1}] {text[:300]}...'" which is the start of the page.
                # Maybe better to find the match index.
                results.append(f"[Page {i+1}] {text[:500]}...")
                hits += 1
                if hits >= 3: break # Just get top 3 hits
        
        if not results:
            return "No results found in textbook."
            
        return "\n\n".join(results)
    except Exception as e:
        return f"LIBRARY ERROR: Could not read book. ({e})"

def search_physics_library(query):
    """
    Search all PDF textbooks in data/library/physics/
    """
    physics_dir = os.path.join(LIBRARY_PATH, 'physics')
    if not os.path.exists(physics_dir):
        return ""
        
    results = []
    # Auto-discover PDFs
    for filename in os.listdir(physics_dir):
        if filename.endswith('.pdf'):
            result = read_textbook(filename, query)
            if "No results found" not in result and "LIBRARY ERROR" not in result:
                results.append(f"--- FROM {filename} ---\n{result}")
    
    if not results:
        return ""
        
    return "\n\n".join(results)
