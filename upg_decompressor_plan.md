# UPG Rust Decompressor - Implementation Plan

## Goal

Build production-ready Rust decompressor for UPG models with optimizations for Apple Silicon, addressing critical technical recommendations.

## User Review Required

> [!IMPORTANT]
> **Format Migration**: Switching from Python Pickle to Safetensors
>
> - Breaking change for existing UPG files
> - Need conversion script for Phi-4 UPG
> - Better performance and security
>
> **Metal Kernels**: Custom Apple Silicon optimization
>
> - Requires `.metal` shader files
> - May need Xcode for compilation
> - Significant performance improvement expected

## Proposed Changes

### Phase 1: Core Decompressor (Rust)

#### [NEW] `upg_kernel/src/upg_decompress.rs`

Core decompression module with optimizations:

```rust
// Prime LUT - First 10,000 primes baked into binary
const PRIME_LUT: [u32; 10000] = [...];

pub struct UPGDecompressor {
    // Safetensors memory-mapped file
    // CSR sparse matrices
    // Quantization scales
}

impl UPGDecompressor {
    pub fn from_safetensors(path: &Path) -> Result<Self>;
    pub fn decompress_layer(&self, layer_id: usize) -> Tensor;
    pub fn reconstruct_weight(&self, prime_idx: u16, scale: f32) -> f16;
}
```

**Key Features**:

- Prime LUT for O(1) manifold decoding
- Zero-copy Safetensors loading (mmap)
- INT8 → BF16 dequantization
- CSR → Dense reconstruction

---

#### [NEW] `upg_kernel/src/sparse.rs`

Sparse matrix operations with MdCSR optimization:

```rust
pub struct MdCSRMatrix {
    values: Vec<i8>,           // Quantized values
    delta_indices: Vec<u8>,    // Delta-compressed column indices
    row_pointers: Vec<u32>,
    prime_indices: Vec<u16>,   // Manifold encoding
    scales: Vec<f32>,          // Per-row quantization scales
}

impl MdCSRMatrix {
    pub fn to_dense(&self) -> Tensor;
    pub fn spmv(&self, x: &Tensor) -> Tensor;  // Sparse-Matrix × Dense-Vector
}
```

**Optimization**: Delta-compressed indices (8-bit vs 32-bit) → 4.8GB target

---

#### [NEW] `upg_kernel/src/metal_kernels.rs`

Apple Silicon Metal kernel interface:

```rust
pub struct MetalSpMV {
    device: metal::Device,
    pipeline: metal::ComputePipelineState,
    command_queue: metal::CommandQueue,
}

impl MetalSpMV {
    pub fn new() -> Result<Self>;
    pub fn execute(&self, matrix: &MdCSRMatrix, vector: &Tensor) -> Tensor;
}
```

Links to: `upg_kernel/src/kernels/spmv.metal`

---

#### [NEW] `upg_kernel/src/kernels/spmv.metal`

Custom Metal shader for sparse matrix multiplication:

```metal
kernel void sparse_matvec(
    device const int8_t* values [[buffer(0)]],
    device const uint8_t* delta_indices [[buffer(1)]],
    device const uint32_t* row_pointers [[buffer(2)]],
    device const uint16_t* prime_indices [[buffer(3)]],
    device const float* scales [[buffer(4)]],
    device const float* input [[buffer(5)]],
    device float* output [[buffer(6)]],
    constant uint32_t* prime_lut [[buffer(7)]],
    uint tid [[thread_position_in_grid]]
) {
    // Optimized SpMV with prime decoding
}
```

**Performance Target**: 2-3x faster than CPU SpMV

---

### Phase 2: Format Migration

#### [NEW] `convert_pickle_to_safetensors.py`

Migrate existing Phi-4 UPG from Pickle to Safetensors:

```python
def convert_upg_to_safetensors(pickle_path: str, output_path: str):
    # Load pickle UPG
    # Extract CSR matrices
    # Create Safetensors with:
    #   - values (INT8 tensor)
    #   - indices (UINT8 delta-compressed)
    #   - row_pointers (UINT32)
    #   - prime_indices (UINT16)
    #   - scales (FP32)
    # Save with metadata header
```

---

#### [NEW] `upg_format_v2.md`

Specification for Safetensors-based UPG format:

```
UPG Format v2.0 (Safetensors)

Header:
  - version: "2.0"
  - model: "phi-4"
  - compression_ratio: 10.0
  - num_layers: 40

Per-layer tensors:
  - layer_{i}_values: INT8[nnz]
  - layer_{i}_delta_indices: UINT8[nnz]
  - layer_{i}_row_pointers: UINT32[rows+1]
  - layer_{i}_prime_indices: UINT16[nnz]
  - layer_{i}_scales: FP32[rows]
```

---

### Phase 3: Inference Engine

#### [MODIFY] `upg_kernel/Cargo.toml`

Add dependencies for Metal and Candle:

```toml
[dependencies]
candle-core = "0.3"
candle-nn = "0.3"
metal = "0.27"
safetensors = "0.4"
memmap2 = "0.9"
```

---

#### [NEW] `upg_kernel/src/inference.rs`

High-level inference API:

```rust
pub struct UPGModel {
    decompressor: UPGDecompressor,
    metal_backend: Option<MetalSpMV>,
    config: ModelConfig,
}

impl UPGModel {
    pub fn from_file(path: &Path) -> Result<Self>;
    pub fn forward(&self, input_ids: &[u32]) -> Tensor;
    pub fn generate(&self, prompt: &str, max_tokens: usize) -> String;
}
```

---

### Phase 4: Benchmarking

#### [NEW] `upg_kernel/benches/decompress_bench.rs`

Criterion benchmarks:

```rust
fn bench_decompression(c: &mut Criterion) {
    c.bench_function("decompress_layer", |b| {
        b.iter(|| decompressor.decompress_layer(0))
    });
}

fn bench_spmv_cpu(c: &mut Criterion) { ... }
fn bench_spmv_metal(c: &mut Criterion) { ... }
```

**Targets**:

- Decompression: < 1ms per layer
- SpMV (CPU): ~10ms per layer
- SpMV (Metal): ~3ms per layer
- Full forward pass: < 20ms (55+ tok/s)

---

## Verification Plan

### Automated Tests

**Test 1: Prime LUT Accuracy**

```bash
cargo test test_prime_lut
```

Verifies first 10,000 primes are correct.

**Test 2: Decompression Correctness**

```bash
cargo test test_decompress_accuracy
```

Compares decompressed weights against original (within tolerance).

**Test 3: Format Conversion**

```bash
python3 convert_pickle_to_safetensors.py phi-4-upg/phi-4.upg phi-4-upg/phi-4-v2.safetensors
cargo test test_load_safetensors
```

**Test 4: Metal Kernel**

```bash
cargo test test_metal_spmv --features metal
```

### Manual Verification

**Test 5: End-to-End Inference**

```bash
cargo run --release --example phi4_generate
```

Expected: Generate coherent text at 55+ tok/s on Apple Silicon.

**Test 6: Memory Usage**

```bash
/usr/bin/time -l cargo run --release --example phi4_generate
```

Expected: < 8GB RAM usage.

---

## Timeline

- **Phase 1 (Core)**: 2-3 days
  - Prime LUT: 2 hours
  - Decompressor: 1 day
  - Sparse ops: 1 day
  
- **Phase 2 (Format)**: 1 day
  - Conversion script: 4 hours
  - Specification: 2 hours
  - Testing: 2 hours

- **Phase 3 (Inference)**: 2-3 days
  - Metal kernels: 1 day
  - Inference API: 1 day
  - Integration: 1 day

- **Phase 4 (Benchmarks)**: 1 day
  - Benchmark suite: 4 hours
  - Optimization: 4 hours

**Total**: 6-8 days to production-ready decompressor

---

## Success Criteria

1. ✅ Load 5.5GB UPG model in < 1 second (mmap)
2. ✅ Decompress layer in < 1ms
3. ✅ Achieve 55+ tok/s on Apple Silicon
4. ✅ Use < 8GB RAM
5. ✅ Pass all accuracy tests (< 1% error vs original)
6. ✅ Metal kernels 2-3x faster than CPU

---

## Risk Mitigation

**Risk 1**: Metal kernel development complexity

- **Mitigation**: Start with CPU-only, add Metal as optimization
- **Fallback**: Use Candle's built-in Metal support

**Risk 2**: Safetensors format incompatibility

- **Mitigation**: Keep Pickle loader as fallback
- **Transition**: Support both formats during migration

**Risk 3**: Accuracy loss in decompression

- **Mitigation**: Extensive testing against original
- **Threshold**: < 1% error tolerance

---

## Next Steps

1. Generate Prime LUT (first 10,000 primes)
2. Implement `upg_decompress.rs` skeleton
3. Create Safetensors conversion script
4. Write Metal SpMV kernel
5. Build inference API
6. Run benchmarks and optimize
