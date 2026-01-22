//! TENT v4.0 PIGMENT CORE
//! =========================
//! Phase 152: Semantic Pointillism
//!
//! The Holographic Reality Layer.
//! - Micro View (Machine): Each dot is a Seed containing Truth
//! - Macro View (Human): Arranged dots form a smooth Gradient
//!
//! "The user sees the beauty. The machine reads the truth."

use std::f64::consts::PI;

// =============================================================================
// CONSTANTS
// =============================================================================

/// Golden Ratio - The aesthetic harmonic
pub const PHI: f64 = 1.618033988749895;

/// Silver Ratio - The logic harmonic
pub const DELTA: f64 = 2.414213562373095;

/// Prime for hashing operations
pub const HASH_PRIME: u64 = 0xFFFFFFFFFFFFFFFF;

// =============================================================================
// THE PIGMENT - The Holographic Data Dot
// =============================================================================

/// A Pigment is a "pixel" that contains both visual and semantic information.
///
/// - color_value: What the Human sees (The Gradient)
/// - seed_hash: What the Machine reads (The Micro Data)
/// - prime_coordinate: Where it sits in the Prime Universe
/// - resonance: How "true" this pigment is (0.0 - 1.0)
#[derive(Debug, Clone, Copy)]
#[repr(C)] // For WASM FFI compatibility
pub struct Pigment {
    /// RGBA color value (human-visible component)
    pub color_value: u32,

    /// 256-bit seed hash (machine-readable truth)
    pub seed_hash: [u8; 32],

    /// Prime coordinate in the Universal Prime Graph
    pub prime_coordinate: u64,

    /// Resonance score (0.0 = noise, 1.0 = crystal truth)
    pub resonance: f32,

    /// Density (semantic mass per syllable equivalent)
    pub density: f32,

    /// Friction (aesthetic vs logic tension)
    pub friction: f32,
}

impl Pigment {
    /// Create a new Pigment from raw data
    pub fn new(data: &[u8], prime: u64) -> Self {
        let seed_hash = Self::compute_hash(data);
        let color_value = Self::hash_to_color(&seed_hash);
        let resonance = Self::compute_resonance(&seed_hash, prime);
        let density = Self::compute_density(data);
        let friction = Self::compute_friction(data);

        Pigment {
            color_value,
            seed_hash,
            prime_coordinate: prime,
            resonance,
            density,
            friction,
        }
    }

    /// Create a Pigment from text (UTF-8)
    pub fn from_text(text: &str, prime: u64) -> Self {
        Self::new(text.as_bytes(), prime)
    }

    /// Compute 256-bit hash from data
    fn compute_hash(data: &[u8]) -> [u8; 32] {
        // Simple but effective hash using prime multiplication
        let mut hash = [0u8; 32];
        let mut accumulator: u64 = 0x123456789ABCDEF0;

        for (i, &byte) in data.iter().enumerate() {
            accumulator = accumulator.wrapping_mul(31).wrapping_add(byte as u64);
            hash[i % 32] ^= (accumulator >> ((i % 8) * 8)) as u8;
        }

        // Final mixing pass
        for i in 0..32 {
            hash[i] = hash[i].wrapping_add(hash[(i + 17) % 32]);
        }

        hash
    }

    /// Convert hash to RGBA color
    fn hash_to_color(hash: &[u8; 32]) -> u32 {
        let r = hash[0];
        let g = hash[1];
        let b = hash[2];
        let a = 255u8; // Full opacity

        ((r as u32) << 24) | ((g as u32) << 16) | ((b as u32) << 8) | (a as u32)
    }

    /// Compute resonance score based on hash alignment with prime
    fn compute_resonance(hash: &[u8; 32], prime: u64) -> f32 {
        // Extract 64-bit value from hash
        let hash_value = u64::from_le_bytes([
            hash[0], hash[1], hash[2], hash[3], hash[4], hash[5], hash[6], hash[7],
        ]);

        // Check alignment with prime using golden ratio phase
        let phase = (hash_value as f64 * PHI) % (2.0 * PI);
        let prime_phase = (prime as f64 * DELTA) % (2.0 * PI);

        // Phase difference determines resonance
        let diff = (phase - prime_phase).abs();
        let normalized = 1.0 - (diff / PI);

        normalized.max(0.0).min(1.0) as f32
    }

    /// Compute density from data (simplified semantic mass)
    fn compute_density(data: &[u8]) -> f32 {
        if data.is_empty() {
            return 0.0;
        }

        // Count unique bytes (entropy approximation)
        let mut seen = [false; 256];
        let mut unique = 0usize;

        for &byte in data {
            if !seen[byte as usize] {
                seen[byte as usize] = true;
                unique += 1;
            }
        }

        // Density = unique / total (higher = denser information)
        (unique as f32) / (data.len() as f32).max(1.0)
    }

    /// Compute friction from data (aesthetic vs logic tension)
    fn compute_friction(data: &[u8]) -> f32 {
        if data.len() < 2 {
            return 0.0;
        }

        // Friction = variance in byte transitions
        let mut transitions = 0u64;
        for i in 1..data.len() {
            let diff = (data[i] as i32 - data[i - 1] as i32).abs() as u64;
            transitions += diff;
        }

        let avg_transition = (transitions as f32) / ((data.len() - 1) as f32);

        // Normalize to 0-1 range
        (avg_transition / 128.0).min(1.0)
    }

    /// Check if this Pigment is valid (not noise)
    pub fn is_valid(&self) -> bool {
        self.resonance > 0.5 && self.density > 0.1
    }

    /// Check if this Pigment is a "Diamond" (high truth density)
    pub fn is_diamond(&self) -> bool {
        self.resonance > 0.8 && self.density > 0.3 && self.friction < 0.3
    }

    /// Check if this Pigment is a "Bubble" (empty fluff)
    pub fn is_bubble(&self) -> bool {
        self.density < 0.1 || self.resonance < 0.3
    }

    /// Get the RGB components
    pub fn rgb(&self) -> (u8, u8, u8) {
        (
            ((self.color_value >> 24) & 0xFF) as u8,
            ((self.color_value >> 16) & 0xFF) as u8,
            ((self.color_value >> 8) & 0xFF) as u8,
        )
    }

    /// Get color adjusted by resonance (greener = more true)
    pub fn resonance_color(&self) -> u32 {
        let (r, g, b) = self.rgb();

        // Blend toward green for high resonance, red for low
        let truth_r = (r as f32 * (1.0 - self.resonance)) as u8;
        let truth_g = (g as f32 * self.resonance + 128.0 * self.resonance) as u8;
        let truth_b = (b as f32 * 0.5) as u8;

        ((truth_r as u32) << 24) | ((truth_g as u32) << 16) | ((truth_b as u32) << 8) | 255
    }
}

// =============================================================================
// THE CANVAS - A Grid of Pigments
// =============================================================================

/// A Canvas is a 2D grid of Pigments forming the "Gradient"
pub struct Canvas {
    pub width: usize,
    pub height: usize,
    pub pigments: Vec<Pigment>,
}

impl Canvas {
    /// Create a new empty canvas
    pub fn new(width: usize, height: usize) -> Self {
        Canvas {
            width,
            height,
            pigments: vec![
                Pigment {
                    color_value: 0x000000FF,
                    seed_hash: [0; 32],
                    prime_coordinate: 0,
                    resonance: 0.0,
                    density: 0.0,
                    friction: 0.0,
                };
                width * height
            ],
        }
    }

    /// Set a pigment at position
    pub fn set(&mut self, x: usize, y: usize, pigment: Pigment) {
        if x < self.width && y < self.height {
            self.pigments[y * self.width + x] = pigment;
        }
    }

    /// Get a pigment at position
    pub fn get(&self, x: usize, y: usize) -> Option<&Pigment> {
        if x < self.width && y < self.height {
            Some(&self.pigments[y * self.width + x])
        } else {
            None
        }
    }

    /// Calculate average resonance of the canvas
    pub fn average_resonance(&self) -> f32 {
        if self.pigments.is_empty() {
            return 0.0;
        }

        let sum: f32 = self.pigments.iter().map(|p| p.resonance).sum();
        sum / (self.pigments.len() as f32)
    }

    /// Count diamonds in the canvas
    pub fn diamond_count(&self) -> usize {
        self.pigments.iter().filter(|p| p.is_diamond()).count()
    }

    /// Count bubbles (invalid pigments) in the canvas
    pub fn bubble_count(&self) -> usize {
        self.pigments.iter().filter(|p| p.is_bubble()).count()
    }

    /// Generate a heat map of resonance values
    pub fn resonance_heatmap(&self) -> Vec<u32> {
        self.pigments.iter().map(|p| p.resonance_color()).collect()
    }
}

// =============================================================================
// WASM EXPORTS (For WebAssembly compatibility)
// =============================================================================

#[cfg(target_arch = "wasm32")]
use wasm_bindgen::prelude::*;

#[cfg(target_arch = "wasm32")]
#[wasm_bindgen]
pub fn analyze_text(text: &str, prime: u64) -> Vec<f32> {
    let pigment = Pigment::from_text(text, prime);
    vec![pigment.resonance, pigment.density, pigment.friction]
}

#[cfg(target_arch = "wasm32")]
#[wasm_bindgen]
pub fn get_pigment_color(text: &str, prime: u64) -> u32 {
    let pigment = Pigment::from_text(text, prime);
    pigment.resonance_color()
}

#[cfg(target_arch = "wasm32")]
#[wasm_bindgen]
pub fn is_diamond(text: &str, prime: u64) -> bool {
    let pigment = Pigment::from_text(text, prime);
    pigment.is_diamond()
}

// =============================================================================
// TESTS
// =============================================================================

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_pigment_creation() {
        let pigment = Pigment::from_text("E = mc²", 2);
        assert!(pigment.resonance >= 0.0 && pigment.resonance <= 1.0);
        assert!(pigment.density > 0.0);
    }

    #[test]
    fn test_diamond_vs_bubble() {
        // Dense truth should be close to diamond
        let truth = Pigment::from_text(
            "The Riemann Hypothesis states that all non-trivial zeros have real part 1/2.",
            17,
        );

        // Fluff should be closer to bubble
        let fluff = Pigment::from_text("leverage synergy paradigm holistic stakeholder", 17);

        println!(
            "Truth: resonance={:.2}, density={:.2}, friction={:.2}",
            truth.resonance, truth.density, truth.friction
        );
        println!(
            "Fluff: resonance={:.2}, density={:.2}, friction={:.2}",
            fluff.resonance, fluff.density, fluff.friction
        );

        // Truth should have higher density
        assert!(truth.density >= fluff.density);
    }

    #[test]
    fn test_canvas() {
        let mut canvas = Canvas::new(10, 10);

        // Fill with test data
        for y in 0..10 {
            for x in 0..10 {
                let text = format!("Cell {},{}", x, y);
                let prime = (x + y * 10 + 2) as u64;
                canvas.set(x, y, Pigment::from_text(&text, prime));
            }
        }

        let avg = canvas.average_resonance();
        assert!(avg > 0.0, "Canvas should have positive resonance");

        let diamonds = canvas.diamond_count();
        let bubbles = canvas.bubble_count();
        println!(
            "Canvas: {}x{}, avg_resonance={:.2}, diamonds={}, bubbles={}",
            canvas.width, canvas.height, avg, diamonds, bubbles
        );
    }
}
