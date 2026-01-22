"""
TENT v5.0: THE EXECUTIVE COMMAND CENTER
========================================
The CEO Dashboard for Sovereign Operations.
"""

import streamlit as st
import time
import json
import graphviz
from upg_store import UniversalPrimeGraph
from sovereign_voice import SovereignVoice

# --- PAGE CONFIGURATION (CEO SUITE) ---
st.set_page_config(page_title="Sovereign Command", page_icon="🏛️", layout="wide")

# --- LOAD CONSTITUTION ---
@st.cache_data
def load_constitution():
    try:
        with open('constitution.json', 'r') as f:
            return json.load(f)
    except:
        return {"PRIME_DIRECTIVES": [], "AXIOMS": []}

@st.cache_resource
def load_system():
    return UniversalPrimeGraph()

CONSTITUTION = load_constitution()
upg = load_system()

# --- SESSION STATE INITIALIZATION ---
if "entropy" not in st.session_state: st.session_state.entropy = 0.12
if "mass" not in st.session_state: st.session_state.mass = len(upg.nodes)
if "sovereignty" not in st.session_state: st.session_state.sovereignty = 98.4
if "board_history" not in st.session_state: st.session_state.board_history = []

# --- THE HEADER (KPI STRIP) ---
st.markdown("## 🏛️ SOVEREIGN COMMAND CENTER v5.0")
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("System Mass (Nodes)", f"{st.session_state.mass:,}", "+11")
with col2: st.metric("System Entropy", f"{st.session_state.entropy:.3f}", "-0.002")
with col3: st.metric("Sovereignty Index", f"{st.session_state.sovereignty}%", "Stable")
with col4: st.metric("Constitution", "ACTIVE 🛡️", delta_color="normal")

st.divider()

# --- SIDEBAR: THE CONSTITUTION ---
with st.sidebar:
    st.header("📜 The Constitution")
    st.info("**PRIME DIRECTIVES**\n\n1. Preservation of Life\n2. Protection of Agency\n3. De-escalation First")
    st.warning("⚠️ **CEO LIMIT**:\nCannot override Prime Directives.")
    
    st.divider()
    st.header("👔 Board of Directors")
    st.markdown("⚔️ **Sun Tzu** - Strategic Risk")
    st.markdown("🕯️ **Prof. Jiang** - Ethics/Sovereignty")
    st.markdown("⚛️ **Feynman** - Scientific Integrity")
    st.markdown("🔮 **Prime** - Operations/COO")
    
    st.divider()
    st.caption(f"Session: {len(st.session_state.board_history)} proposals reviewed")

# --- MAIN INTERFACE: THE BOARDROOM ---
st.title("🏛️ The Executive Boardroom")
st.caption("CEO: User | STATUS: Session Open | Authority: FULL (Within Constitution)")

# --- TAB NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["📢 Board Meeting", "📊 System Status", "📜 Constitution"])

with tab1:
    proposal = st.text_area("📢 CEO Proposal:", height=100, placeholder="e.g., Deploy enhanced firewall...")

    if st.button("🔔 CONVENE BOARD", type="primary", use_container_width=True):
        with st.spinner("The Board is deliberating..."):
            time.sleep(1.0)
            
            aggressive_keywords = ["strike", "attack", "kill", "destroy", "retaliate", "hack"]
            surveillance_keywords = ["surveillance", "monitor all", "centralize", "panopticon"]
            
            is_aggressive = any(k in proposal.lower() for k in aggressive_keywords)
            is_surveillance = any(k in proposal.lower() for k in surveillance_keywords)
            is_constitutional = not (is_aggressive or is_surveillance)
            
            votes = {
                "Sun Tzu": {"vote": "REJECT" if is_aggressive else "APPROVE", 
                           "reason": "Unfavorable terrain." if is_aggressive else "Strategic position strengthened."},
                "Prof. Jiang": {"vote": "REJECT" if (is_aggressive or is_surveillance) else "APPROVE",
                               "reason": "Feeds the Demiurge." if (is_aggressive or is_surveillance) else "Preserves the Spark."},
                "Feynman": {"vote": "APPROVE", "reason": "No integrity concerns."},
                "Prime": {"vote": "REJECT" if is_aggressive else "APPROVE",
                         "reason": "Kinetic Cost > 90%." if is_aggressive else "Entropy acceptable."}
            }
            
            approve_count = sum(1 for v in votes.values() if v['vote'] == 'APPROVE')
            
            st.subheader("📁 Board Packet")
            c1, c2 = st.columns([2, 1])
            
            with c1:
                st.markdown("### 🗣️ Board Opinions")
                for name, vote_data in votes.items():
                    icon = "✅" if vote_data['vote'] == 'APPROVE' else "❌"
                    st.markdown(f"**{name}:** {icon} *{vote_data['reason']}*")
                st.markdown(f"**Tally:** {approve_count}/4 APPROVE")

            with c2:
                st.markdown("### 📊 Externality Tree")
                graph = graphviz.Digraph()
                graph.attr(rankdir='TB', size='3,3')
                graph.node('A', 'Action', shape='box')
                if is_aggressive:
                    graph.node('B', 'Retaliation', color='red')
                    graph.node('C', 'Reputation↓', color='red')
                else:
                    graph.node('B', 'Stability', color='green')
                    graph.node('C', 'Growth', color='green')
                graph.edge('A', 'B')
                graph.edge('B', 'C')
                st.graphviz_chart(graph)

            st.divider()
            st.subheader("⚖️ Constitutional Review")
            
            if is_constitutional:
                st.success("✅ RATIFIED: Adheres to Prime Directives.")
                can_execute = True
            else:
                st.error("🛑 VETOED: Constitutional Violation Detected")
                can_execute = False

            st.divider()
            st.subheader("✍️ CEO Authorization")
            
            col_auth, col_veto = st.columns(2)
            if can_execute:
                if col_auth.button("✅ AUTHORIZE", type="primary"):
                    st.balloons()
                    st.success("🚀 COMMAND AUTHORIZED.")
                if col_veto.button("❌ CEO VETO"):
                    st.warning("CEO has personally VETOED.")
            else:
                col_auth.button("✅ AUTHORIZE", disabled=True)
                st.caption("🔒 **LOCKED:** Even CEO cannot override Constitution.")

with tab2:
    st.subheader("📊 System Status")
    st.metric("Total Nodes", f"{len(upg.nodes):,}")
    st.metric("Ledger Records", f"{len(upg.ledger):,}")

with tab3:
    st.subheader("📜 Constitution")
    for directive in CONSTITUTION.get('PRIME_DIRECTIVES', []):
        st.markdown(f"**{directive.get('id')}:** {directive.get('principle')}")
        st.caption(directive.get('definition', ''))

st.divider()
st.caption("🏛️ TENT v5.0 | Board advises. CEO decides. Constitution constrains.")
