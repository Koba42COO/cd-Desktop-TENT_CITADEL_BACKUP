#!/usr/bin/env python3
"""
TENT v4.1 CARTOGRAPHER v2 (STANDALONE EDITION)
==============================================
Phase 236: The Debris Field

Objective:
Render the Battle Map of the Sovereign Agent WITHOUT external dependencies.
- INNER SYSTEM: The Architect + Minted Truths (Blue)
- OUTER RIM: The Graveyard of Rejected Noise (Red) (Oort Cloud)

Output: tent_universe_v2.html
"""

import json
import os
import sys
import webbrowser
from datetime import datetime

# --- CONFIG ---
UPG_FILE = "universal_prime_graph.json" 
OUTPUT_HTML = "tent_universe_v2.html"

def load_data():
    if not os.path.exists(UPG_FILE):
        print(f"⚠️  UPG FILE NOT FOUND: {UPG_FILE}")
        return {"nodes": {}, "ledger": []}
    
    with open(UPG_FILE, 'r') as f:
        return json.load(f)

def generate_html_content(nodes_data, ledger_data):
    """
    Constructs the Vis.js data structure and embeds it into a single HTML file.
    """
    
    vis_nodes = []
    vis_edges = []
    
    # 1. THE CORE
    # ------------------
    # The Void (Central Black Hole)
    vis_nodes.append({
        "id": "0", "label": "THE VOID", "color": "#000000", 
        "size": 60, "shape": "dot", "borderWidth": 4, 
        "color": {"border": "#333333", "background": "#000000"},
        "font": {"color": "white", "size": 20, "face": "Courier New"}
    })
    
    # The Architect (You, orbiting the Void slightly)
    vis_nodes.append({
        "id": "2", "label": "ARCHITECT", "color": "#FFD700", 
        "size": 50, "shape": "star", 
        "color": {"border": "#DAA520", "background": "#FFD700"},
        "font": {"color": "#FFD700", "size": 16, "face": "Courier New"}
    })
    vis_edges.append({"from": "2", "to": "0", "length": 200, "color": {"color": "#333333", "opacity": 0.3}})

    # 2. INNER SYSTEM (Minted Truths)
    # ------------------
    for key, node in nodes_data.items():
        node_id = str(key)
        label = node.get('title', 'Unknown')[:20] + "..."
        
        vis_nodes.append({
            "id": node_id,
            "label": label,
            "title": f"{node.get('title')}\nMass: {node.get('mass')}",
            "color": "#00BFFF", # Deep Sky Blue
            "size": 20,
            "shape": "dot"
        })
        
        # Connect to Architect
        vis_edges.append({
            "from": node_id, "to": "2", 
            "length": 150, # Arbitrary orbit distance
            "color": {"color": "#1E90FF", "opacity": 0.6}
        })

    # 3. OUTER RIM (The Debris Field)
    # ------------------
    # Process Ledger for rejections
    # Limit to 500 to save browser performance
    debris_count = 0
    recent_history = list(reversed(ledger_data))
    
    for entry in recent_history:
        if debris_count > 500: break
        
        verdict = entry.get('verdict', 'FAIL')
        if "REJECTED" in str(verdict):
            d_id = f"DEBRIS_{debris_count}"
            score = float(entry.get('score', 0))
            
            # Bright Red for "Almost Passed", Dark Red for "Garbage"
            # Score 0.9 -> Bright (#FF0000)
            # Score 0.0 -> Dark (#330000)
            red_val = int(score * 255)
            hex_color = f"#{red_val:02x}0000"
            if red_val < 50: hex_color = "#330000" # Floor brightness
            
            vis_nodes.append({
                "id": d_id,
                "label": "", # No text for debris, just dots
                "title": f"REJECTED: {entry.get('title')}\nScore: {score:.4f}",
                "color": hex_color,
                "size": 5,
                "shape": "circle"
            })
            
            # Connect to Void (0) with LONG edges
            # This pushes them away from the center
            vis_edges.append({
                "from": d_id, "to": "0",
                "length": 1200, # Far orbit
                "color": {"color": "#220000", "opacity": 0.2},
                "physics": False # Let them drift? No, need physics for layout
            })
            debris_count += 1
            
    return vis_nodes, vis_edges, debris_count

def generate_map():
    print(">> [CARTOGRAPHER v2] SCANNING THE BATTLEFIELD...")
    data = load_data()
    nodes, edges, debris_count = generate_html_content(data.get("nodes", {}), data.get("ledger", []))
    
    print(f">> [DATA] FOUND {len(data.get('nodes', {}))} MINTED TRUTHS.")
    print(f">> [RENDER] VISUALIZING {debris_count} DEBRIS PARTICLES.")

    # HTML TEMPLATE
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <title>TENT v4.1: The Debris Field</title>
      <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
      <style type="text/css">
        body {{ margin: 0; background-color: #050505; color: white; font-family: 'Courier New', monospace; overflow: hidden; }}
        #mynetwork {{ width: 100vw; height: 100vh; }}
        #hud {{ position: absolute; top: 10px; left: 10px; z-index: 10; background: rgba(0,0,0,0.7); padding: 10px; border: 1px solid #333; }}
        h1 {{ margin: 0; font-size: 16px; color: #FFD700; }}
        p {{ margin: 5px 0 0 0; font-size: 12px; color: #aaa; }}
      </style>
    </head>
    <body>
      <div id="hud">
        <h1>SOVEREIGN BATTLE MAP</h1>
        <p>Architect: Node 002 (You)</p>
        <p>Minted Truths: {len(data.get('nodes', {}))}</p>
        <p>Rejected Debris: {debris_count}</p>
        <p>Bias Setting: 0.787 (Active)</p>
      </div>
      <div id="mynetwork"></div>
      <script type="text/javascript">
        var nodes = new vis.DataSet({json.dumps(nodes)});
        var edges = new vis.DataSet({json.dumps(edges)});

        var container = document.getElementById('mynetwork');
        var data = {{ nodes: nodes, edges: edges }};
        var options = {{
            nodes: {{ borderWidth: 1 }},
            layout: {{ improvedLayout: false }},
            physics: {{
                forceAtlas2Based: {{
                    gravitationalConstant: -100,
                    centralGravity: 0.005,
                    springLength: 200,
                    springConstant: 0.08,
                    damping: 0.4,
                    avoidOverlap: 0
                }},
                maxVelocity: 50,
                solver: 'forceAtlas2Based',
                stabilization: {{ iterations: 150 }}
            }},
            interaction: {{ hover: true, tooltipDelay: 200 }}
        }};
        var network = new vis.Network(container, data, options);
      </script>
    </body>
    </html>
    """

    with open(OUTPUT_HTML, "w") as f:
        f.write(html)
        
    print(f">> [EXPORT] WRITING {OUTPUT_HTML}...")
    print(">> [LAUNCH] OPENING THE OORT CLOUD...")
    
    # Try to open, but also print the path
    path = "file://" + os.path.realpath(OUTPUT_HTML)
    print(f"   -> URL: {path}")
    webbrowser.open(path)

if __name__ == "__main__":
    generate_map()
