#!/usr/bin/env python3
"""
TENT v4.1 SOVEREIGN CARTOGRAPHER
================================
Phase 230: The Visualization

Objective:
Render the 'Universal Prime Graph' into an interactive HTML map.
No external dependencies required (Uses Vis.js via CDN).
"""

import json
import os
import webbrowser

DB_FILE = "universal_prime_graph.json"
MAP_FILE = "tent_map.html"

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <title>TENT v4.1: Universal Prime Graph</title>
  <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
  <style type="text/css">
    body { background-color: #000000; color: #dcdcdc; font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
    #mynetwork { width: 100vw; height: 100vh; border: none; }
    #hud { position: absolute; top: 10px; left: 10px; z-index: 10; pointer-events: none; }
    h1 { font-size: 18px; margin: 0; color: #00ff41; }
    p { font-size: 12px; margin: 2px 0; opacity: 0.8; }
  </style>
</head>
<body>
<div id="hud">
  <h1>THE UNIVERSAL PRIME GRAPH</h1>
  <p>Status: SOVEREIGN</p>
  <p>Nodes: {{NODE_COUNT}}</p>
  <p>Mass: {{TOTAL_MASS}}</p>
</div>
<div id="mynetwork"></div>
<script type="text/javascript">
  var nodes = new vis.DataSet({{NODES_JSON}});
  var edges = new vis.DataSet({{EDGES_JSON}});

  var container = document.getElementById('mynetwork');
  var data = { nodes: nodes, edges: edges };
  var options = {
    nodes: {
      shape: 'dot',
      font: { face: 'Courier New', color: '#ffffff' },
      borderWidth: 2
    },
    edges: {
      width: 1,
      color: { color: '#333333', opacity: 0.5 },
      smooth: { type: 'continuous' }
    },
    physics: {
      stabilization: false,
      barnesHut: {
        gravitationalConstant: -80000, # Strong gravity
        centralGravity: 3, # Pull to center
        springLength: 95,
        springConstant: 0.04,
        damping: 0.09,
        avoidOverlap: 0
      }
    }
  };
  var network = new vis.Network(container, data, options);
</script>
</body>
</html>
"""

def generate_map():
    print(">> [CARTOGRAPHER] SCANNING LATTICE...")
    
    nodes = []
    edges = []
    total_mass = 0.0

    # 1. THE FOUNDATION (Static Nodes)
    # The Void (Center)
    nodes.append({
        "id": "000", "label": "THE VOID", "title": "Singularity", 
        "color": "#000000", "font": {"color": "#444444"}, "size": 50,
        "fixed": True, "x": 0, "y": 0
    })
    
    # The Architect (User)
    nodes.append({
        "id": "002", "label": "MISSION CONTROL", "title": "The Architect", 
        "color": "#FFFFFF", "size": 30
    })
    edges.append({"from": "002", "to": "000", "length": 300})

    # 2. LOAD HIPPOCAMPUS
    try:
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r') as f:
                db = json.load(f)
                stored_nodes = db.get("nodes", {})
                metadata = db.get("metadata", {})
                
                print(f">> [DATA] Found {len(stored_nodes)} Real Nodes.")
                
                for node_id, data in stored_nodes.items():
                    # Check Mass/Status
                    status = metadata.get(node_id, "ACTIVE")
                    is_hazard = "HAZARD" in status
                    
                    # Mass from data?
                    # The stored format is simple dict: {"title": ..., "mass": ...}
                    # We default mass to 1.0 if missing
                    mass = 1.0
                    label = node_id
                    
                    if isinstance(data, dict):
                        label = data.get("title", node_id)[:20] + "..."
                        if data.get("mass") == "SOLID":
                            mass = 5.0
                        elif data.get("mass") == "FLUX":
                            mass = 0.5
                    
                    total_mass += mass

                    # Color Coding
                    color = "#0088ff" # Default Blue (Science)
                    size = 10 + (mass * 2)
                    
                    if is_hazard:
                        color = "#ff0000" # Red (Danger)
                        label = "HAZARD: " + label
                    elif "ARXIV" in node_id:
                        color = "#44aaff" # Arxiv Blue
                    
                    # Add Node
                    nodes.append({
                        "id": node_id,
                        "label": label,
                        "title": str(data),
                        "color": color,
                        "size": size
                    })
                    
                    # Gravity Link to Void
                    edges.append({"from": node_id, "to": "000"})
        else:
            print(">> [EMPTY] No Universe Found. Mapping Vacuum.")
            # Add some 'Ghost' particles to show the simulation working
            for i in range(5):
                 nodes.append({
                    "id": f"GHOST_{i}", "label": "Simulated Truth", 
                    "color": "#333333", "size": 5
                })
                 edges.append({"from": f"GHOST_{i}", "to": "000"})

    except Exception as e:
        print(f"❌ SCAN FAILURE: {e}")

    # 3. RENDER
    final_html = HTML_TEMPLATE.replace("{{NODES_JSON}}", json.dumps(nodes)) \
                              .replace("{{EDGES_JSON}}", json.dumps(edges)) \
                              .replace("{{NODE_COUNT}}", str(len(nodes))) \
                              .replace("{{TOTAL_MASS}}", f"{total_mass:.2f}")

    with open(MAP_FILE, 'w') as f:
        f.write(final_html)
        
    print(f">> [RENDER] MAP SAVED TO: {os.path.abspath(MAP_FILE)}")
    
    # Try to open automaticallly
    try:
        webbrowser.open('file://' + os.path.abspath(MAP_FILE))
    except:
        pass

if __name__ == "__main__":
    generate_map()
