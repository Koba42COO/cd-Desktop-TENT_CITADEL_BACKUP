# Implementation Plan: Cylindrical-Throd Sampling

## Goal

Integrate the **Cylinder Shell Method (3D)** and **Even-Throdd (Z₃) Arithmetic** directly into the TENT Engine's generation process to "rebuild from the blueprint."

## Use Case Analysis

The mathematical frameworks we built provide two new signals for every token:

1. **Semantic Mass ($Z$)**: Volume/height from the 3D Cylinder projection. High $Z$ = Prime/Dense Concept.
2. **Structural Stability (Throd)**: Whether the token completes a stable "Threeven" triplet ($t_{n-2} + t_{n-1} + t_n \equiv 0 \pmod 3$).

## Proposed Strategy: "Cylindrical-Throd Sampling"

We will implement a **Custom Logits Processor** that biases the model's choices based on these signals.

### 1. Cylindrical Volume Bias (3D Signal)

* **Concept**: Give a "gravity boost" to words with high Semantic Mass ($Z$).
* **Math**: `logit += α * z_score`
* **Effect**: The model prefers "heavier" (more semantically dense) words, grounding the response.

### 2. Throd Stability Filter (Structure Signal)

* **Concept**: Encourage the formation of stable "Meson/Baryon" triplets in the token stream.
* **Math**: If `(prev1 + prev2 + candidate) % 3 == 0`: `logit += β`
* **Effect**: The generated text will have a hidden mathematical rhythm (Threeven cadence), potentially improving coherence (as observed in periodic signals).

## Logic Flow (`tent_inference_engine.py`)

During generation step $t$:

1. Get **logits** from the model (standard prediction).
2. **Project Candidates**: For the top $K$ candidates, compute their embeddings and lift to 3D ($Z$).
3. **Check Stability**: For the top $K$, check if they form a stable triplet with history.
4. **Apply Bias**:

    ```python
    modified_logit = original_logit + (alpha * Z_score) + (beta * is_stable)
    ```

5. **Sample**: Pick token from modified distribution.

## Changes Required

### New Module: `core/cylindrical_sampling.py`

* Function `calculate_cylindrical_bias(candidate_ids, model)`
* Function `calculate_throd_stability_bias(candidate_ids, history_ids)`

### Modify: `tent_inference_engine.py`

* Integrate the sampling bias into the `generate()` loop.

## Success Metric

* **Throd Ratio**: % of triplets in output that are stable (Target > 33% random baseline).
* **Mass Density**: Average $Z$ score of generated tokens (Target > baseline).
