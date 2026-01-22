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
