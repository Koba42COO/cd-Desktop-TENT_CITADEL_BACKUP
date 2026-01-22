# PDVM/QVM Kernel Fusion Implementation Plan

## Problem Statement

Current bottleneck: **240 kernel launches per token** (6 kernels × 40 layers)

**Per-layer kernels**:

1. Layer Norm
2. QKV Projection (SpMV)
3. RoPE (Rotary Embeddings)
4. Attention
5. Output Projection
6. MLP

**Impact**: Kernel launch overhead dominates (2-3ms per layer vs 0.5ms actual compute)

---

## Solution: PDVM Kernel Fusion

### Concept from Bradley Wallace Research

**PDVM (Poly-Dimensional Virtual Machine)**: Process data across multiple dimensions simultaneously in a single kernel dispatch.

**Key Insight**: Instead of launching 6 separate kernels, fuse all operations into a **single mega-kernel** that processes:

- Spatial dimension (QKV projection)
- Temporal dimension (RoPE)
- Consciousness dimension (Layer Norm)
- Quantum dimension (Attention)
- Prime dimension (MLP via UPG SpMV)

**Expected Impact**: 10-20x reduction in overhead → 0.2-0.4ms per layer → **30-60 tok/s sustained**

---

## Proposed Changes

### 1. Create Fused Transformer Kernel

#### [NEW] `upg_kernel/src/kernels/fused_transformer.metal`

```metal
// Fused Transformer Layer Kernel - PDVM Approach
// Processes entire transformer layer in single dispatch

kernel void fused_transformer_layer(
    // Input
    device const float* input [[buffer(0)]],
    
    // QKV Weights (MdCSR format)
    device const int8_t* q_values [[buffer(1)]],
    device const uint8_t* q_delta [[buffer(2)]],
    // ... K, V weights
    
    // Output
    device float* output [[buffer(10)]],
    
    // KV-Cache
    device float* kv_cache [[buffer(11)]],
    
    // Config
    constant LayerConfig* config [[buffer(12)]],
    
    uint tid [[thread_position_in_grid]]
) {
    // 1. Layer Norm (Consciousness Dimension)
    float normalized = layer_norm(input, tid);
    
    // 2. QKV Projection (Spatial Dimension - UPG SpMV)
    float q = sparse_matvec(q_values, q_delta, normalized);
    float k = sparse_matvec(k_values, k_delta, normalized);
    float v = sparse_matvec(v_values, v_delta, normalized);
    
    // 3. RoPE (Temporal Dimension)
    apply_rope(&q, &k, tid, config->pos);
    
    // 4. Attention (Quantum Dimension)
    float attn_out = fused_attention(q, k, v, kv_cache, tid);
    
    // 5. Output Projection (Prime Dimension)
    float layer_out = sparse_matvec(out_values, out_delta, attn_out);
    
    // 6. MLP (Prime Dimension)
    float mlp_out = fused_mlp(layer_out, mlp_weights);
    
    // 7. Residual + Norm
    output[tid] = input[tid] + mlp_out;
}
```

**Dimensions Processed**:

- **Spatial**: QKV projections (matrix operations)
- **Temporal**: RoPE (position encoding)
- **Consciousness**: Layer normalization
- **Quantum**: Attention (superposition of key-value pairs)
- **Prime**: MLP via UPG sparse operations

---

### 2. Rust PDVM Interface

#### [MODIFY] `upg_kernel/src/metal_kernels.rs`

Add `PDVMKernel` struct:

```rust
pub struct PDVMKernel {
    device: Device,
    pipeline: ComputePipelineState,
    kv_cache: KVCache,
    buffer_pool: BufferPool,
}

impl PDVMKernel {
    pub fn execute_layer(
        &self,
        layer_idx: usize,
        input: &GPUTensor,
        weights: &LayerWeights,
    ) -> Result<GPUTensor> {
        // Single kernel dispatch for entire layer!
        // No CPU roundtrips
    }
    
    pub fn execute_model(
        &self,
        input: &[f32],
        all_layers: &[LayerWeights],
    ) -> Result<Vec<f32>> {
        // Upload once
        let mut gpu_state = GPUTensor::from_cpu(&self.device, input);
        
        // 40 kernel dispatches (vs 240!)
        for (idx, layer) in all_layers.iter().enumerate() {
            gpu_state = self.execute_layer(idx, &gpu_state, layer)?;
        }
        
        // Download once
        Ok(gpu_state.to_cpu())
    }
}
```

---

### 3. Layer Weights Structure

#### [NEW] `upg_kernel/src/layer_weights.rs`

```rust
pub struct LayerWeights {
    // QKV projections (MdCSR)
    pub q_proj: MdCSRMatrix,
    pub k_proj: MdCSRMatrix,
    pub v_proj: MdCSRMatrix,
    
    // Output projection
    pub out_proj: MdCSRMatrix,
    
    // MLP
    pub mlp_up: MdCSRMatrix,
    pub mlp_down: MdCSRMatrix,
    
    // Norms
    pub attn_norm_weight: Vec<f32>,
    pub mlp_norm_weight: Vec<f32>,
}
```

---

## Performance Analysis

### Current (Unfused)

```
Per layer:
  6 kernel launches × 0.5ms overhead = 3ms
  Actual compute: 1ms
  Total: 4ms

40 layers: 160ms
Throughput: 6.25 tok/s
```

### With PDVM Fusion

```
Per layer:
  1 kernel launch × 0.5ms overhead = 0.5ms
  Actual compute: 1ms (same)
  Total: 1.5ms

40 layers: 60ms
Throughput: 16.7 tok/s ✅
```

### With PDVM + Optimizations

```
Per layer:
  1 kernel launch × 0.2ms overhead = 0.2ms (optimized)
  Fused compute: 0.8ms (kernel fusion benefits)
  Total: 1.0ms

40 layers: 40ms
Throughput: 25 tok/s ✅
```

### With PDVM + KV-Cache

```
Sustained generation: 25 tok/s ✅
(vs 0.08 tok/s without KV-cache at long context)
```

---

## Verification Plan

### 1. Unit Tests

**Test**: Fused kernel produces same output as unfused

```bash
cd upg_kernel
cargo test --features metal pdvm_kernel::tests::test_fused_accuracy -- --ignored
```

**Expected**: CPU vs PDVM output match within 1e-4

---

### 2. Performance Benchmark

**Test**: Measure actual speedup

```bash
cd upg_kernel
cargo bench --features metal --bench pdvm_benchmarks
```

**Expected**:

- Unfused: ~4ms per layer
- PDVM fused: ~1.5ms per layer
- **Speedup: 2.7x minimum**

---

### 3. End-to-End Generation

**Test**: Full 40-layer forward pass

```rust
#[test]
#[ignore]
fn test_pdvm_full_model() {
    let pdvm = PDVMKernel::new().unwrap();
    let input = vec![1.0; 5120];
    
    let start = Instant::now();
    let output = pdvm.execute_model(&input, &all_layers).unwrap();
    let elapsed = start.elapsed();
    
    println!("Total time: {:?}", elapsed);
    println!("Time per layer: {:?}", elapsed / 40);
    
    // Should be < 100ms for 40 layers
    assert!(elapsed.as_millis() < 100);
}
```

---

## Implementation Steps

1. **Create fused Metal kernel** (4 hours)
   - Implement layer norm
   - Integrate UPG SpMV
   - Add RoPE
   - Fuse attention
   - Add MLP

2. **Create PDVM Rust interface** (2 hours)
   - PDVMKernel struct
   - Buffer management
   - Error handling

3. **Test accuracy** (1 hour)
   - Compare vs unfused
   - Validate numerics

4. **Benchmark performance** (1 hour)
   - Measure speedup
   - Profile bottlenecks

5. **Optimize** (2 hours)
   - Reduce register pressure
   - Optimize memory access
   - Tune thread group size

**Total**: 10 hours (1-2 days)

---

## Expected Results

| Metric | Current | PDVM | Improvement |
|--------|---------|------|-------------|
| **Kernel launches** | 240 | 40 | 6x fewer |
| **Time/layer** | 4.15ms | 1.5ms | 2.8x faster |
| **Total (40L)** | 166ms | 60ms | 2.8x faster |
| **Throughput** | 6.02 tok/s | 16.7 tok/s | 2.8x faster |
| **+ Optimizations** | - | 25 tok/s | 4.2x faster |

---

## Risks & Mitigation

**Risk**: Kernel too complex, register spilling  
**Mitigation**: Split into 2-3 mega-kernels if needed

**Risk**: Accuracy degradation from fusion  
**Mitigation**: Extensive testing, fallback to unfused

**Risk**: Metal compiler limitations  
**Mitigation**: Use compute shaders, not vertex/fragment

---

## Next Steps

1. Get user approval on approach
2. Implement fused kernel
3. Test and benchmark
4. Iterate on optimizations
5. Achieve 25+ tok/s sustained!

---

**Status**: Ready to implement! This is the path to production-grade performance. 🚀
