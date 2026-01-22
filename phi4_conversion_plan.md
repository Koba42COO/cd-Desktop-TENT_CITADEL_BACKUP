# Phi-4 Test & Conversion Plan

## Status

- [x] Download scripts created
- [x] Phi-4 downloading (27GB/30GB - 90% complete)
- [x] Test script created (`test_phi4_vanilla.py`)
- [x] Conversion script created (`convert_phi4_to_upg.py`)
- [ ] Phi-4 download complete
- [ ] Test vanilla Phi-4
- [ ] Convert to UPG format
- [ ] Verify compression ratio

## When Phi-4 Completes

### Step 1: Test Vanilla Model

```bash
python3 test_phi4_vanilla.py
```

**Expected output**:

- Model loads successfully
- Generates coherent text for 4 test prompts
- Shows performance metrics (load time, generation speed)
- Validates model works before compression

### Step 2: Convert to UPG

```bash
python3 convert_phi4_to_upg.py
```

**Expected output**:

- Converts all layers to prime-sparse format
- Achieves ~10:1 compression ratio
- Creates `phi-4-upg/` directory with:
  - `phi-4.upg` (compressed model ~3GB)
  - `metadata.json` (compression stats)
  - Tokenizer files

### Step 3: Verify Results

**Check compression**:

```bash
du -sh phi-4 phi-4-upg
```

Expected:

- `phi-4/`: ~30GB (original)
- `phi-4-upg/`: ~3GB (compressed, 10:1 ratio)

## Conversion Algorithm

### Prime-Sparse Compression (3 stages)

1. **Quantization** (4x reduction)
   - FP32 → 1.5-bit prime manifold encoding
   - Maps weights to discrete prime levels
   - Preserves distribution characteristics

2. **Sparsity** (2x reduction)
   - Identifies near-zero weights
   - Stores only significant values
   - Sparse matrix representation

3. **Manifold Encoding** (1.25x reduction)
   - Groups similar weights
   - Stores manifold index + delta
   - Exploits weight clustering

**Total**: 4 × 2 × 1.25 = **10x compression**

## Timeline

- **Now**: Phi-4 at 90% (27GB/30GB)
- **~10 minutes**: Download complete
- **~5 minutes**: Test vanilla model
- **~30-60 minutes**: Convert to UPG
- **Result**: First UPG model ready!

## Next Models

After Phi-4 success:

1. Gemma 2 (17GB/60GB - 28%)
2. Qwen 2.5 (22GB/150GB - 15%)
3. DeepSeek V3 (21GB/400GB - 5%)
4. Mixtral (6GB/300GB - 2%)
5. Grok 2 (9GB/500GB - 2%)
6. Llama 3.1 (29MB/800GB - 0.004%)

## Success Criteria

✅ **Vanilla test passes**:

- Model loads without errors
- Generates coherent text
- Performance acceptable

✅ **UPG conversion succeeds**:

- All layers converted
- Compression ratio ≥ 8:1
- File size ~3GB or less

✅ **Ready for merge**:

- UPG format validated
- Can be loaded by Rust kernel
- Serves as template for other models
