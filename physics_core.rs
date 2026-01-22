//! TENT v4.0 Physics Core (WASM Module)
//! ======================================
//! Phase 131: The Genesis Build
//!
//! Implements Probabilistic Amplitude Computing (PAC)
//! - Wave Interference for Truth Detection
//! - Read-Shockley Stress Analysis
//! - Crystallization Engine
//!
//! "Truth is the collapsed state of a Polycystic Waveform."

use std::f64::consts::PI;

/// Complex number for wave calculations
#[derive(Clone, Copy, Debug)]
pub struct Complex {
    pub re: f64,
    pub im: f64,
}

impl Complex {
    pub fn new(re: f64, im: f64) -> Self {
        Complex { re, im }
    }
    
    pub fn from_polar(magnitude: f64, phase: f64) -> Self {
        Complex {
            re: magnitude * phase.cos(),
            im: magnitude * phase.sin(),
        }
    }
    
    pub fn magnitude(&self) -> f64 {
        (self.re * self.re + self.im * self.im).sqrt()
    }
    
    pub fn add(&self, other: &Complex) -> Complex {
        Complex { re: self.re + other.re, im: self.im + other.im }
    }
}

/// Semantic Waveform - represents a token/concept as a wave
pub struct SemanticWave {
    pub amplitude: f64,
    pub phase: f64,
    pub frequency: f64,
}

impl SemanticWave {
    pub fn new(amplitude: f64, phase: f64, frequency: f64) -> Self {
        SemanticWave { amplitude, phase, frequency }
    }
    
    pub fn to_complex(&self) -> Complex {
        Complex::from_polar(self.amplitude, self.phase)
    }
    
    pub fn sample(&self, t: f64) -> Complex {
        Complex::from_polar(self.amplitude, self.frequency * t + self.phase)
    }
}

/// PAC (Probabilistic Amplitude Computing) Engine
pub struct PACEngine {
    pub coherence_threshold: f64,
}

impl PACEngine {
    pub fn new(threshold: f64) -> Self {
        PACEngine { coherence_threshold: threshold }
    }
    
    /// I = |ψ₁ + ψ₂|²
    pub fn interference_intensity(&self, wave1: &SemanticWave, wave2: &SemanticWave) -> f64 {
        let superposition = wave1.to_complex().add(&wave2.to_complex());
        superposition.magnitude().powi(2)
    }
    
    /// Truth test: Constructive = Truth, Destructive = Hallucination
    pub fn truth_test(&self, fact: &SemanticWave, context: &SemanticWave) -> (bool, f64) {
        let phase_diff = (fact.phase - context.phase).abs() % (2.0 * PI);
        let coherence = (phase_diff.cos() + 1.0) / 2.0;
        (coherence > self.coherence_threshold, coherence)
    }
}

/// Read-Shockley Grain Boundary Stress
pub struct CrystalStress;

impl CrystalStress {
    pub fn boundary_energy(theta: f64) -> f64 {
        if theta < 0.001 { return 0.0; }
        if theta >= 15.0 { return 1.0; }
        let rad = theta.to_radians();
        (2.5 * rad * (0.5 - rad.ln())).clamp(0.0, 1.0)
    }
}

/// Crystallization Engine
#[derive(Debug)]
pub enum Verdict { Crystal, Annealing, Dissolved }

pub fn crystallize(fact: &SemanticWave, narrative: &SemanticWave, orient: f64) -> Verdict {
    let pac = PACEngine::new(0.7);
    let (_, coherence) = pac.truth_test(fact, narrative);
    let stress = CrystalStress::boundary_energy(orient);
    let score = (1.0 - coherence) * 0.5 + stress * 0.5;
    
    if score < 0.2 { Verdict::Crystal }
    else if score < 0.5 { Verdict::Annealing }
    else { Verdict::Dissolved }
}

// WASM Entry Points
#[no_mangle]
pub extern "C" fn wasm_interference(a1: f64, p1: f64, a2: f64, p2: f64) -> f64 {
    PACEngine::new(0.7).interference_intensity(
        &SemanticWave::new(a1, p1, 1.0),
        &SemanticWave::new(a2, p2, 1.0)
    )
}

fn main() {
    println!("TENT v4.0 PHYSICS CORE - PAC Engine");
    let truth = SemanticWave::new(1.0, 0.1, 1.0);
    let context = SemanticWave::new(1.0, 0.15, 1.0);
    let lie = SemanticWave::new(1.0, PI * 0.8, 1.0);
    
    println!("Truth + Context: {:?}", crystallize(&truth, &context, 5.0));
    println!("Truth + Lie:     {:?}", crystallize(&truth, &lie, 90.0));
}
