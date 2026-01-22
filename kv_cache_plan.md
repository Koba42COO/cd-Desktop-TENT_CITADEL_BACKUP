# KV-Cache Implementation & Integration Plan

## Goal

Implement a robust GPU Ring Buffer KV-Cache to enable O(1) token generation complexity (state-bound optimization). Fix identified bugs in dimensions and buffer addressing.

## 1. `kv_cache.rs` Updates

**Current Issues:**

- `HEADS = 32` (Incorrect for Phi-4, should be 40)
- `LAYERS` hardcoded (Should be dynamic or correct const)
- `dtype_size` hardcoded as 4 bytes (f32) or 2? Code says `dtype_size=2` but allocates with that? Metal buffer uses f32 usually. `pdvm_optimized.metal` uses `float* kv_cache`. `float` is 4 bytes. `dtype_size` should be 4.

**Proposed Changes:**

- **Constants**:
  - `LAYERS = 40`
  - `HEADS = 40`
  - `HEAD_DIM = 128`
  - `MAX_SEQ_LEN = 4096`
- **Data Type**: Use `f32` (4 bytes).
- **Methods**:
  - `get_layer_offset(layer_idx) -> u64`: Return byte offset for a specific layer.
  - `get_k_offset(layer_idx) -> u64`
  - `get_v_offset(layer_idx) -> u64`

## 2. PDVM Dispatcher Updates (`pdvm_optimized.rs`)

**Current Issue:**

- `encoder.set_buffer(18, Some(self.kv_cache.buffer()), 0)` uses offset 0 for ALL layers.
- Result: All layers overwrite Layer 0's cache.

**Fix:**

- In `execute_layer`, calculate offset:

  ```rust
  let layer_idx = ...; // Need to pass this
  let offset = self.kv_cache.get_layer_offset(layer_idx);
  encoder.set_buffer(18, Some(self.kv_cache.buffer()), offset);
  ```

## 3. Kernel Updates

- `pdvm_optimized.metal` receives the buffer pointer *already offset* by the host?
- Yes, `setBuffer:offset:atIndex:` sets the base pointer for the kernel argument.
- So `kv_cache[0]` in kernel maps to `buffer_base + offset`.
- This is efficient and correct.
- Kernel logic `kv_offset = ...` assumes it's working within its own layer's space.
- **Kernel Logic Check**:

  ```metal
  uint kv_offset = (head_idx * MAX_SEQ_LEN * HEAD_DIM) + ...
  ```

  This calculates offset *within the layer*. This is correct if the buffer bound is the layer start.

## 4. Implementation Steps

1. Modify `kv_cache.rs` with correct constants and offset logic.
2. Verify `pdvm_optimized.rs` integration (update `execute_layer` signature to accept `layer_idx`).
3. Validate "Ring Buffer" behavior (ensure `current_pos` wraps correctly).

## 5. Ring Buffer Logic in Kernel

- The user mentioned "Ring Buffer".
- Kernel uses `config->seq_pos`.
- If `seq_pos >= MAX_SEQ_LEN`, we need to wrap.
- Current kernel: `uint kv_offset = ... + (config->seq_pos * HEAD_DIM) ...`
- **Fix**: `(config->seq_pos % MAX_SEQ_LEN)` in kernel to ensure wrapping.

## Timeline

- Immediate: Implement corrected `kv_cache.rs`.
- Next: Update PDVM dispatcher.
