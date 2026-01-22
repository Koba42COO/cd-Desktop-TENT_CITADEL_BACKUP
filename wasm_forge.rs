//! TENT v4.0 WASM FORGE
//! =====================
//! Phase 153: The Rust-WebAssembly Bridge
//!
//! This is the bridge that exposes the TENT physics kernel to JavaScript.
//! When compiled with wasm-pack, it produces a .wasm file that runs in browsers.
//!
//! Build command: wasm-pack build --target web
//!
//! "The user sees the beauty. The machine reads the truth."

use std::f64::consts::PI;
use wasm_bindgen::prelude::*;

// =============================================================================
// CONSTANTS
// =============================================================================

const PHI: f64 = 1.618033988749895; // Golden Ratio
const DELTA: f64 = 2.414213562373095; // Silver Ratio

// Buzzwords (antimatter - negative density)
const BUZZWORDS: &[&str] = &[
    "synergy",
    "leverage",
    "proactive",
    "stakeholder",
    "paradigm",
    "holistic",
    "actionable",
    "incentivize",
    "optimize",
    "revolutionary",
    "disruptive",
    "innovative",
    "ecosystem",
    "scalable",
    "deliverable",
];

// Technical anchors (heavy matter - positive density)
const ANCHORS: &[&str] = &[
    "riemann",
    "zeta",
    "prime",
    "theorem",
    "proof",
    "derivative",
    "integral",
    "tensor",
    "quantum",
    "entropy",
    "thermodynamic",
    "algorithm",
    "function",
    "equation",
    "hypothesis",
    "axiom",
];

// =============================================================================
// PIGMENT STRUCTURE
// =============================================================================

/// A single data-pixel containing both visual and semantic information
#[wasm_bindgen]
#[derive(Clone, Copy)]
pub struct Pigment {
    pub x: f32,         // Position X (0.0 - 1.0)
    pub y: f32,         // Position Y (0.0 - 1.0)
    pub r: u8,          // Red
    pub g: u8,          // Green
    pub b: u8,          // Blue
    pub a: u8,          // Alpha
    pub mass: f32,      // Semantic mass (can be negative!)
    pub resonance: f32, // Truth alignment (0.0 - 1.0)
}

#[wasm_bindgen]
impl Pigment {
    /// Create a pigment from a word
    pub fn from_word(word: &str, index: u32, total: u32) -> Pigment {
        let word_lower = word.to_lowercase();

        // Calculate mass based on word type
        let mass = if BUZZWORDS.iter().any(|&b| word_lower.contains(b)) {
            -2.0 // Antimatter!
        } else if ANCHORS.iter().any(|&a| word_lower.contains(a)) {
            5.0 // Heavy matter
        } else if word.len() <= 3 {
            0.5 // Light particles
        } else {
            1.0 // Normal matter
        };

        // Calculate resonance from word hash
        let hash = simple_hash(word);
        let phase = (hash as f64 * PHI) % (2.0 * PI);
        let resonance = ((phase.sin() + 1.0) / 2.0) as f32;

        // Calculate color based on mass
        let (r, g, b) = mass_to_color(mass, resonance);

        // Initial position (will be adjusted by physics)
        let angle = (index as f64 / total as f64) * 2.0 * PI;
        let radius = 0.3 + (hash as f64 % 100.0) / 500.0;
        let x = 0.5 + (radius * angle.cos()) as f32;
        let y = 0.5 + (radius * angle.sin()) as f32;

        Pigment {
            x,
            y,
            r,
            g,
            b,
            a: 255,
            mass,
            resonance,
        }
    }

    /// Apply physics: mass affects position
    /// Positive mass -> moves toward center
    /// Negative mass -> moves toward edges
    pub fn apply_gravity(&mut self, center_x: f32, center_y: f32) {
        let dx = center_x - self.x;
        let dy = center_y - self.y;
        let dist = (dx * dx + dy * dy).sqrt().max(0.01);

        // Gravity proportional to mass
        // Positive mass = attraction (toward center)
        // Negative mass = repulsion (toward edges)
        let force = self.mass * 0.001 / dist;

        self.x += dx * force;
        self.y += dy * force;

        // Keep in bounds
        self.x = self.x.clamp(0.05, 0.95);
        self.y = self.y.clamp(0.05, 0.95);
    }
}

// =============================================================================
// TRUTH CANVAS
// =============================================================================

/// The main canvas that holds and renders all pigments
#[wasm_bindgen]
pub struct TruthCanvas {
    pigments: Vec<Pigment>,
    width: u32,
    height: u32,
}

#[wasm_bindgen]
impl TruthCanvas {
    /// Create a new empty canvas
    #[wasm_bindgen(constructor)]
    pub fn new(width: u32, height: u32) -> TruthCanvas {
        TruthCanvas {
            pigments: Vec::new(),
            width,
            height,
        }
    }

    /// Ingest a narrative and convert to pigments
    pub fn ingest_narrative(&mut self, text: &str) {
        self.pigments.clear();

        // Split into words
        let words: Vec<&str> = text.split_whitespace().collect();
        let total = words.len() as u32;

        for (i, word) in words.iter().enumerate() {
            let pigment = Pigment::from_word(word, i as u32, total);
            self.pigments.push(pigment);
        }
    }

    /// Run one physics step (call each frame)
    pub fn step(&mut self) {
        let center_x = 0.5;
        let center_y = 0.5;

        for pigment in &mut self.pigments {
            pigment.apply_gravity(center_x, center_y);
        }
    }

    /// Get number of pigments
    pub fn count(&self) -> u32 {
        self.pigments.len() as u32
    }

    /// Get pigment data as flat array for rendering
    /// Format: [x, y, r, g, b, a, mass, resonance, ...] for each pigment
    pub fn get_render_data(&self) -> Vec<f32> {
        let mut data = Vec::with_capacity(self.pigments.len() * 8);

        for p in &self.pigments {
            data.push(p.x);
            data.push(p.y);
            data.push(p.r as f32 / 255.0);
            data.push(p.g as f32 / 255.0);
            data.push(p.b as f32 / 255.0);
            data.push(p.a as f32 / 255.0);
            data.push(p.mass);
            data.push(p.resonance);
        }

        data
    }

    /// Get statistics about the canvas
    pub fn get_stats(&self) -> String {
        let total = self.pigments.len();
        let total_mass: f32 = self.pigments.iter().map(|p| p.mass).sum();
        let diamonds = self.pigments.iter().filter(|p| p.mass >= 5.0).count();
        let antimatter = self.pigments.iter().filter(|p| p.mass < 0.0).count();
        let avg_resonance: f32 = if total > 0 {
            self.pigments.iter().map(|p| p.resonance).sum::<f32>() / total as f32
        } else {
            0.0
        };

        format!(
            "Pigments: {} | Mass: {:.1} | Diamonds: {} | Antimatter: {} | Resonance: {:.2}",
            total, total_mass, diamonds, antimatter, avg_resonance
        )
    }
}

// =============================================================================
// HELPER FUNCTIONS
// =============================================================================

/// Simple hash function for words
fn simple_hash(s: &str) -> u64 {
    let mut hash: u64 = 0;
    for (i, c) in s.bytes().enumerate() {
        hash = hash.wrapping_mul(31).wrapping_add(c as u64);
        hash ^= (i as u64).wrapping_mul(17);
    }
    hash
}

/// Convert mass and resonance to RGB color
fn mass_to_color(mass: f32, resonance: f32) -> (u8, u8, u8) {
    if mass < 0.0 {
        // Antimatter: Red fog
        let intensity = ((-mass) * 0.3).min(1.0);
        (
            (180.0 + 75.0 * intensity) as u8,
            (50.0 * (1.0 - intensity)) as u8,
            (50.0 * (1.0 - intensity)) as u8,
        )
    } else if mass >= 5.0 {
        // Diamond: Bright green star
        let brightness = resonance * 0.5 + 0.5;
        (
            (100.0 * (1.0 - brightness)) as u8,
            (200.0 * brightness + 55.0) as u8,
            (150.0 * brightness) as u8,
        )
    } else if mass >= 1.0 {
        // Normal matter: Blue-white
        let brightness = resonance * 0.3 + 0.7;
        (
            (180.0 * brightness) as u8,
            (200.0 * brightness) as u8,
            (255.0 * brightness) as u8,
        )
    } else {
        // Light particles: Dim gray
        let brightness = resonance * 0.3 + 0.2;
        let v = (100.0 * brightness) as u8;
        (v, v, v)
    }
}

// =============================================================================
// INITIALIZATION
// =============================================================================

/// Initialize the WASM module
#[wasm_bindgen(start)]
pub fn init() {
    // Set up panic hook for debugging
    #[cfg(feature = "console_error_panic_hook")]
    console_error_panic_hook::set_once();
}

/// Analyze a text and return resonance score (0-100)
#[wasm_bindgen]
pub fn analyze_quick(text: &str) -> f32 {
    let canvas = TruthCanvas::new(800, 600);
    let mut canvas = canvas;
    canvas.ingest_narrative(text);

    if canvas.pigments.is_empty() {
        return 0.0;
    }

    let total_mass: f32 = canvas.pigments.iter().map(|p| p.mass).sum();
    let avg_resonance: f32 =
        canvas.pigments.iter().map(|p| p.resonance).sum::<f32>() / canvas.pigments.len() as f32;

    // Score based on mass and resonance
    let mass_score = (total_mass / canvas.pigments.len() as f32)
        .max(-1.0)
        .min(5.0);
    let normalized_mass = (mass_score + 1.0) / 6.0; // 0 to 1

    (normalized_mass * 0.6 + avg_resonance * 0.4) * 100.0
}
