# Phase 96: PostLLM Fusion Engine - Implementation Plan

## Goal

Complete the PostLLM Fusion Engine by generating the unified `postllm_unified.upg` binary file from the existing manifest data.

## Current State

| Component | Status |
|-----------|--------|
| Scanner (`postllm_scanner.py`) | ✅ Complete (341 files, 1.45 TB, 63 models) |
| Manifest (`postllm_manifest.json`) | ✅ Complete (58,841 tensors catalogued) |
| Fusion Engine (`postllm_fusion.py`) | ✅ Code exists (but not run to completion) |
| Unified Manifest | ✅ Complete (10x compression target: 126 GB) |
| Domain Routing | ✅ Complete (code → DeepSeek, general → Mixtral/Qwen) |
| **Unified Binary (`postllm_unified.upg`)** | ❌ **NOT FOUND** |

---

## Proposed Changes

### Component: PostLLM Fusion Engine

#### [MODIFY] [postllm_fusion.py](file:///Volumes/WD%20Drive/Backup%20dev%20folder/dev/prime-sparse-saas/postllm_fusion.py)

1. Add `write_upg_binary()` method to generate the actual UPG file
2. Implement streaming write to handle 126 GB output
3. Add progress tracking for long-running fusion

#### [NEW] [postllm_generator.py](file:///Volumes/WD%20Drive/Backup%20dev%20folder/dev/prime-sparse-saas/postllm_generator.py)

A lightweight generator script that:

- Reads the unified manifest
- Generates a minimal UPG binary header
- Creates domain routing lookup table
- Produces `postllm_unified.upg` (with size configurable for testing)

---

## Implementation Details

### Option A: Full Fusion (126 GB output)

- Read all 58,841 tensors from source models
- Apply sparsification (10x compression)
- Write to `postllm_unified.upg`
- **Time estimate**: Several hours (1.26 TB read, 126 GB write)

### Option B: Minimal Viable Fusion (Recommended for testing)

- Generate UPG header with manifest metadata
- Include domain routing index
- Store tensor offsets and metadata only (no raw weights)
- **Size**: ~10 MB
- **Purpose**: Validate structure before full run

---

## Verification Plan

### Automated Tests

```bash
# 1. Run the generator
cd /Volumes/WD\ Drive/Backup\ dev\ folder/dev/prime-sparse-saas
python3 postllm_generator.py --mode minimal

# 2. Verify file exists and has correct structure
python3 -c "
import os
import json

upg_path = 'postllm_unified.upg'
assert os.path.exists(upg_path), 'UPG file not generated'
size = os.path.getsize(upg_path)
print(f'Generated: {upg_path} ({size:,} bytes)')

# Read header
with open(upg_path, 'rb') as f:
    magic = f.read(4)
    assert magic == b'UPG2' or magic == b'TENT', f'Invalid magic: {magic}'
    print('Magic header: OK')
"

# 3. Test domain routing
python3 postllm_inference.py --query "write a python function" --verify-routing
```

### Manual Verification

1. Check file size is reasonable (should be >1 KB for minimal, ~126 GB for full)
2. Verify inference returns results with correct domain attribution

---

## Questions for User

1. **Full vs Minimal?** Should I generate the full 126 GB unified model, or start with a minimal version for structure validation?

2. **Storage location?** The full model is large—should it go on the WD drive or elsewhere?

3. **Time constraints?** Full fusion may take hours. Is this acceptable?
