# 🏗️ Build Gap Analysis: Prime-Sparse SaaS

**Date:** 2026-01-11
**Objective:** Identify missing components, architectural disconnects, and integration gaps in the full build.

## 🚨 Critical Architecture Split

The project currently exists as two completely separate, synchronized entities. This is the primary "missing link."

| Component | Local Environment (What we edit) | Docker Environment (What ships) |
| :--- | :--- | :--- |
| **Server** | `upg_server.py` (FastAPI) | `server.py` (Gradio, injected via `printf`) |
| **Kernel** | `upg_kernel/` (Rust source exists but unused) | `upg_kernel/` (Source injected via `printf`, compiled) |
| **Bridge** | `sparseplug` (Pure Python Simulation) | `sparseplug` (Uses compiled `upg_kernel` binding) |
| **UI** | `upg_dashboard.html` | `gradio` standard UI |

### 1. The "Ghost" Kernel

* **Observation:** The local `upg_kernel` directory contains Rust source code (`src/lib.rs`, `Cargo.toml`), but the local Python code (`upg_infer.py`, `sparseplug/core/*.py`) **never imports it**.
* **Gap:** The Python application is running a "Mock/Simulator" of the kernel, while the *real* kernel code sits idle in the `upg_kernel` folder.
* **Consequence:** Benchmarks run locally are testing Python loop performance, not Rust/SIMD performance.

### 2. The Dockerfile "Fork"

* **Observation:** The `Dockerfile` does **not copy** the local `upg_kernel` source. Instead, it uses `printf` to write a *hardcoded version* of the Rust kernel into the container during build (Lines 47-267).
* **Gap:** Any changes we make to `/prime-sparse-saas/upg_kernel/src/lib.rs` are **ignored** by the build. The build uses a "frozen" version of the kernel defined inside the Dockerfile itself.
* **Consequence:** Development is disconnected from production.

### 3. Server Schizophrenia

* **Observation:** We have been heavily optimizing `upg_server.py` and `upg_infer.py` (V6-V12 Logic).
* **Gap:** The `Dockerfile` creates a *brand new* `server.py` (using `printf` at lines 300-661) which runs a Gradio app. It does **not use** `upg_server.py` or `upg_infer.py`.
* **Consequence:** All our work on "Context Sensitive Axioms", "Fluid Logic", and "Intelligence" (V6-V12) **will not exist** in the Docker container. The Docker container runs a legacy Gradio demo.

---

## 🛠️ Remediation Plan

To fix "what's missing", we must unify these two worlds.

### Phase 1: Bridge the Kernel (Local)

1. **Compile Rust Locally:** Use `maturin develop --release` to compile `upg_kernel` and bind it to the local Python environment.
2. **Update Python Binding:** Modify `sparseplug/core/variable_compression_engine.py` to try importing `upg_kernel` and use it if available, falling back to Python only if necessary.

### Phase 2: Unify the Build (Docker)

1. **Fix Dockerfile:**
    * Delete the `printf` injections for `Cargo.toml`, `lib.rs`, and `server.py`.
    * **COPY** the local `upg_kernel` directory into the build stage.
    * **COPY** the local `upg_server.py`, `upg_infer.py`, and `sparseplug` directory into the runtime stage.
2. **Standardize Server:** Change the Docker `CMD` to run `upg_server.py` (FastAPI) instead of the generated Gradio app.

### Phase 3: Cleanup

1. **Remove Legacy Scripts:** Archive `bingo_server.py`, `bingo_os.html`, and other artifacts that confuse the architecture.
2. **Single Entry Point:** Ensure `./launch_universal_ai.sh` builds the distinct Rust binary if needed and starts the unified server.

## Summary Checklist

- [ ] **Kernel**: Local Rust compilation (Mission Critical).
* [ ] **Docker**: Use local source files (Mission Critical).
* [ ] **Server**: Ship the V12 Intelligence Engine (Mission Critical).
* [ ] **UI**: Ensure Docker serves `upg_dashboard.html` (Mission Critical).
