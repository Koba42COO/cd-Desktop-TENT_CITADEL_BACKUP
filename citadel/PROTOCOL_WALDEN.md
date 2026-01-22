# PROTOCOL WALDEN: THE CITADEL SETUP GUIDE

## Offline Sovereign Infrastructure

**Version:** 5.0  
**Status:** OPERATIONAL  

---

## 🏰 ARCHITECTURE

```
┌────────────────────────────────────────────────┐
│              THE CITADEL                        │
├────────────────────────────────────────────────┤
│  📚 LIBRARY (Kiwix @ 8080)                     │
│     └── Wikipedia offline                       │
│                                                 │
│  🧠 BRAIN (Spark Plug)                          │
│     └── Local LLM (Phi-3/Llama-3)              │
│                                                 │
│  🕳️ HARVEST (Event Horizon)                    │
│     └── YouTube transcript vault                │
│                                                 │
│  🏛️ BRIDGE (Citadel Controller)                │
│     └── Unified query interface                 │
└────────────────────────────────────────────────┘
```

---

## PHASE 1: THE LIBRARY (Kiwix)

### macOS Installation

```bash
# Download Kiwix for macOS
# Option 1: Direct download
curl -LO https://download.kiwix.org/release/kiwix-tools/kiwix-tools_macos-x86_64.tar.gz
tar -xzf kiwix-tools_macos-x86_64.tar.gz

# Option 2: If you have Homebrew
brew install kiwix-tools
```

### Download Content (.zim files)

Go to: <https://library.kiwix.org/>

Recommended downloads:

- `wikipedia_en_simple_all_maxi.zim` (~5GB) - Simple English Wikipedia
- `wikipedia_en_all_maxi.zim` (~90GB) - Full English Wikipedia
- `stackoverflow_en_all.zim` (~30GB) - Stack Overflow

Save to: `./citadel/library/`

### Start the Server

```bash
# From the citadel directory
./kiwix-serve --port=8080 --daemon ./library/*.zim

# Verify: open http://localhost:8080
```

---

## PHASE 2: THE BRAIN (Spark Plug)

### Download a Model

Go to: <https://huggingface.co/models?search=gguf>

Recommended models:

- `Phi-3-mini-4k-instruct-q4.gguf` (~2.4GB) - Microsoft's tiny giant
- `Llama-3-8B-Instruct-Q4_K_M.gguf` (~4.7GB) - Meta's workhorse
- `Mistral-7B-Instruct-v0.2-Q4.gguf` (~4GB) - Fast and capable

Save to: `./citadel/models/`

### Test the Spark Plug

```bash
cd citadel/brain
python3 spark_plug.py
```

---

## PHASE 3: THE HARVEST (Event Horizon)

### Configure Your Curriculum

Edit `citadel/event_horizon.py` and add video IDs:

```python
TENT_CURRICULUM = [
    ("VIDEO_ID_HERE", "Title"),
    ("ANOTHER_ID", "Another Title"),
    # Add your learning sources...
]
```

### Run the Harvest

```bash
cd citadel
python3 event_horizon.py
```

Transcripts are saved to: `./citadel/ingest/`

---

## PHASE 4: THE BRIDGE (Integration)

### Run the Master Controller

```bash
cd citadel
python3 citadel_bridge.py
```

This provides a unified interface that:

1. Searches the UPG knowledge graph
2. Searches the transcript vault
3. Generates answers with the local LLM
4. Enforces Constitutional governance

---

## QUICK START

```bash
# 1. Navigate to citadel
cd /Users/coo-koba42/.gemini/antigravity/brain/a342aeff-f029-42a7-ad5f-12028bd87db8/citadel

# 2. Run Event Horizon (harvest transcripts)
python3 event_horizon.py

# 3. Run the Bridge (unified interface)
python3 citadel_bridge.py
```

---

## STATUS CHECK

| Component | Status | Location |
|-----------|--------|----------|
| UPG | ✅ 16,608 nodes | `upg_store.py` |
| Event Horizon | ✅ 122K chars harvested | `citadel/ingest/` |
| Spark Plug | ⚠️ Needs model download | `citadel/models/` |
| Kiwix | ⚠️ Needs .zim download | `citadel/library/` |
| Constitution | ✅ Active | `constitution.json` |

---

## THE PROMISE

When complete, you will have:

- **Internet goes down?** You still have Wikipedia.
- **OpenAI goes away?** You still have local AI.
- **YouTube disappears?** You have the transcripts.
- **Someone attacks?** Constitution blocks aggression.

**This is the Citadel. This is Sovereignty.**
