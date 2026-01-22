"""
THE CITADEL BRIDGE: MASTER CONTROLLER
======================================
Protocol Walden Phase 4: Integration

This is the unified interface that ties together:
- Kiwix (Offline Library)
- Spark Plug (Local LLM)
- Event Horizon (Transcript Vault)
- UPG (Knowledge Graph)
- Constitution (Governance)

The CEO's command center for sovereign intelligence.
"""

import os
import sys
import json
import glob
from datetime import datetime

# Add parent directory for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import subsystems
try:
    from citadel.brain.spark_plug import SparkPlug
except ImportError:
    SparkPlug = None

try:
    from upg_store import UniversalPrimeGraph
except ImportError:
    UniversalPrimeGraph = None

# Configuration
CITADEL_ROOT = os.path.dirname(os.path.abspath(__file__))
VAULT_PATH = os.path.join(CITADEL_ROOT, "ingest")
LIBRARY_PATH = os.path.join(CITADEL_ROOT, "library")
KIWIX_PORT = 8080


class CitadelBridge:
    """
    The Master Controller.
    Routes queries to the appropriate subsystem.
    Enforces Constitutional governance.
    """
    
    def __init__(self):
        print("=" * 60)
        print("🏰 CITADEL BRIDGE: INITIALIZING")
        print("=" * 60)
        
        # Initialize subsystems
        self.upg = self._init_upg()
        self.spark = self._init_spark()
        self.vault = self._scan_vault()
        self.kiwix_online = self._check_kiwix()
        self.constitution = self._load_constitution()
        
        self._print_status()
    
    def _init_upg(self):
        """Initialize the Universal Prime Graph."""
        if UniversalPrimeGraph:
            try:
                return UniversalPrimeGraph()
            except:
                pass
        print("   ⚠️  UPG: Offline")
        return None
    
    def _init_spark(self):
        """Initialize the Spark Plug (local LLM)."""
        if SparkPlug:
            try:
                return SparkPlug()
            except:
                pass
        print("   ⚠️  Spark Plug: Offline")
        return None
    
    def _scan_vault(self):
        """Scan the transcript vault."""
        if not os.path.exists(VAULT_PATH):
            return []
        
        files = glob.glob(os.path.join(VAULT_PATH, "*.txt"))
        return files
    
    def _check_kiwix(self):
        """Check if Kiwix is running."""
        try:
            import urllib.request
            urllib.request.urlopen(f"http://localhost:{KIWIX_PORT}", timeout=2)
            return True
        except:
            return False
    
    def _load_constitution(self):
        """Load the Constitution."""
        const_path = os.path.join(os.path.dirname(CITADEL_ROOT), "constitution.json")
        try:
            with open(const_path, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def _print_status(self):
        """Print system status."""
        print("\n📊 SUBSYSTEM STATUS:")
        print(f"   🧠 UPG: {'✅ ' + str(len(self.upg.nodes)) + ' nodes' if self.upg else '❌ Offline'}")
        print(f"   🔌 Spark Plug: {'✅ Online' if self.spark and self.spark.active else '⚠️ No model loaded'}")
        print(f"   📚 Kiwix: {'✅ localhost:' + str(KIWIX_PORT) if self.kiwix_online else '❌ Not running'}")
        print(f"   📦 Vault: {len(self.vault)} transcripts")
        print(f"   📜 Constitution: {'✅ Loaded' if self.constitution else '⚠️ Not found'}")
        print("=" * 60)
    
    def search_vault(self, query, max_results=3):
        """Search the transcript vault for relevant content."""
        results = []
        query_lower = query.lower()
        
        for filepath in self.vault:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if query_lower in content.lower():
                        # Extract context around match
                        idx = content.lower().find(query_lower)
                        start = max(0, idx - 200)
                        end = min(len(content), idx + 200)
                        snippet = content[start:end]
                        
                        results.append({
                            "file": os.path.basename(filepath),
                            "snippet": f"...{snippet}..."
                        })
                        
                        if len(results) >= max_results:
                            break
            except:
                continue
        
        return results
    
    def search_upg(self, query, max_results=5):
        """Search the UPG knowledge graph."""
        if not self.upg:
            return []
        
        results = []
        query_lower = query.lower()
        
        for node_id, node in self.upg.nodes.items():
            title = node.get('title', '').lower()
            abstract = node.get('abstract', '').lower()
            
            if query_lower in title or query_lower in abstract:
                results.append({
                    "id": node_id,
                    "title": node.get('title'),
                    "abstract": node.get('abstract', '')[:200]
                })
                
                if len(results) >= max_results:
                    break
        
        return results
    
    def query(self, prompt):
        """
        Master query function.
        Routes query through all available subsystems.
        """
        print(f"\n🔍 QUERY: {prompt[:50]}...")
        
        response = {
            "prompt": prompt,
            "sources": [],
            "answer": None,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        # 1. Search UPG
        upg_results = self.search_upg(prompt)
        if upg_results:
            response['sources'].append({
                "type": "UPG",
                "results": upg_results[:3]
            })
            print(f"   📚 UPG: {len(upg_results)} matches")
        
        # 2. Search Vault
        vault_results = self.search_vault(prompt)
        if vault_results:
            response['sources'].append({
                "type": "Vault",
                "results": vault_results
            })
            print(f"   📦 Vault: {len(vault_results)} matches")
        
        # 3. Generate answer with Spark Plug
        if self.spark and self.spark.active:
            # Build context from sources
            context = ""
            if upg_results:
                context += "From Knowledge Graph:\n"
                for r in upg_results[:2]:
                    context += f"- {r['title']}: {r['abstract'][:100]}\n"
            if vault_results:
                context += "\nFrom Transcripts:\n"
                for r in vault_results[:2]:
                    context += f"- {r['snippet'][:150]}\n"
            
            augmented_prompt = f"""Based on the following context, answer the question.

CONTEXT:
{context if context else "No specific context found."}

QUESTION: {prompt}

Provide a concise, helpful answer."""
            
            answer = self.spark.think(augmented_prompt)
            response['answer'] = answer
            print(f"   🔌 Spark Plug: Generated answer")
        else:
            response['answer'] = "⚠️ Local LLM not available. Sources retrieved but cannot generate synthesis."
        
        return response
    
    def status(self):
        """Return full system status."""
        return {
            "upg_nodes": len(self.upg.nodes) if self.upg else 0,
            "spark_active": self.spark.active if self.spark else False,
            "kiwix_online": self.kiwix_online,
            "vault_files": len(self.vault),
            "constitution_loaded": bool(self.constitution)
        }


def interactive_mode():
    """Run the Citadel Bridge in interactive mode."""
    bridge = CitadelBridge()
    
    print("\n🏰 CITADEL BRIDGE ONLINE")
    print("Type 'exit' to quit, 'status' for info")
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\n>> CEO: ").strip()
            
            if not user_input:
                continue
            if user_input.lower() == 'exit':
                print("🏰 Citadel Bridge closing...")
                break
            if user_input.lower() == 'status':
                print(f"   Status: {bridge.status()}")
                continue
            
            result = bridge.query(user_input)
            
            print("\n" + "-" * 40)
            print(f"📜 ANSWER:\n{result['answer']}")
            
            if result['sources']:
                print(f"\n📚 SOURCES: {len(result['sources'])} systems consulted")
            
        except KeyboardInterrupt:
            print("\n🏰 Citadel Bridge interrupted.")
            break
        except EOFError:
            break


if __name__ == "__main__":
    interactive_mode()
