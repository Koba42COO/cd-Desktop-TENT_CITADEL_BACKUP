//! TENT v4.0 GEOMETRY CORE
//! ========================
//! Phase 142: The Unified Field Architecture
//!
//! Core Principle: Truth is a state of Zero Mean Curvature.
//!                 Lies are states of High Tension.
//!
//! This implements the Enneper Minimal Surface model for
//! validating logical coherence through geometric relaxation.

use std::f64::consts::PI;

// =============================================================================
// CONSTANTS: The Sacred Ratios
// =============================================================================

/// The Golden Ratio φ = (1 + √5) / 2
pub const PHI: f64 = 1.618033988749895;

/// The Silver Ratio δ = 1 + √2
pub const DELTA: f64 = 2.414213562373095;

/// Minimal surface tension threshold (below = truth)
pub const TENSION_THRESHOLD: f64 = 0.1;

/// Mean curvature threshold for minimal surfaces
pub const CURVATURE_THRESHOLD: f64 = 0.05;

// =============================================================================
// CORE DATA STRUCTURES
// =============================================================================

/// A point in 3D semantic space
#[derive(Clone, Copy, Debug)]
pub struct Point3D {
    pub x: f64,
    pub y: f64,
    pub z: f64,
}

impl Point3D {
    pub fn new(x: f64, y: f64, z: f64) -> Self {
        Self { x, y, z }
    }

    pub fn magnitude(&self) -> f64 {
        (self.x * self.x + self.y * self.y + self.z * self.z).sqrt()
    }

    pub fn normalize(&self) -> Self {
        let m = self.magnitude();
        if m == 0.0 {
            return *self;
        }
        Self::new(self.x / m, self.y / m, self.z / m)
    }

    pub fn cross(&self, other: &Point3D) -> Self {
        Self::new(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )
    }

    pub fn dot(&self, other: &Point3D) -> f64 {
        self.x * other.x + self.y * other.y + self.z * other.z
    }
}

/// Result of truth validation
#[derive(Debug)]
pub enum TruthState {
    /// Zero mean curvature - stable truth
    Crystal { curvature: f64, tension: f64 },
    /// Non-zero but bounded - uncertain
    Annealing { curvature: f64, tension: f64 },
    /// High tension - falsehood
    Hallucination { curvature: f64, tension: f64 },
}

impl TruthState {
    pub fn is_valid(&self) -> bool {
        matches!(self, TruthState::Crystal { .. })
    }

    pub fn tension(&self) -> f64 {
        match self {
            TruthState::Crystal { tension, .. } => *tension,
            TruthState::Annealing { tension, .. } => *tension,
            TruthState::Hallucination { tension, .. } => *tension,
        }
    }
}

// =============================================================================
// ENNEPER SURFACE: The Minimal Truth Manifold
// =============================================================================

/// The Enneper Surface - a minimal surface that allows self-intersection
/// without breaking. This models how valid paradoxes can exist.
pub struct EnneperSurface {
    /// Resolution of the parametric grid
    pub resolution: usize,
    /// Generated surface points
    pub points: Vec<Vec<Point3D>>,
    /// Surface normals
    pub normals: Vec<Vec<Point3D>>,
}

impl EnneperSurface {
    /// Create a new Enneper surface with given resolution
    pub fn new(resolution: usize) -> Self {
        let mut surface = Self {
            resolution,
            points: Vec::with_capacity(resolution),
            normals: Vec::with_capacity(resolution),
        };
        surface.generate();
        surface
    }

    /// Generate the Enneper surface using parametric equations:
    /// x(u,v) = u - u³/3 + uv²
    /// y(u,v) = v - v³/3 + u²v
    /// z(u,v) = u² - v²
    fn generate(&mut self) {
        let range = 2.0;
        let step = 2.0 * range / (self.resolution as f64);

        for i in 0..self.resolution {
            let u = -range + (i as f64) * step;
            let mut row_points = Vec::with_capacity(self.resolution);
            let mut row_normals = Vec::with_capacity(self.resolution);

            for j in 0..self.resolution {
                let v = -range + (j as f64) * step;

                // Enneper parametric equations
                let x = u - u.powi(3) / 3.0 + u * v.powi(2);
                let y = v - v.powi(3) / 3.0 + u.powi(2) * v;
                let z = u.powi(2) - v.powi(2);

                row_points.push(Point3D::new(x, y, z));

                // Compute surface normal via partial derivatives
                let du = Point3D::new(1.0 - u.powi(2) + v.powi(2), 2.0 * u * v, 2.0 * u);
                let dv = Point3D::new(2.0 * u * v, 1.0 - v.powi(2) + u.powi(2), -2.0 * v);

                row_normals.push(du.cross(&dv).normalize());
            }

            self.points.push(row_points);
            self.normals.push(row_normals);
        }
    }

    /// Compute mean curvature at a point (H = 0 for minimal surface)
    pub fn mean_curvature(&self, i: usize, j: usize) -> f64 {
        if i == 0 || i >= self.resolution - 1 || j == 0 || j >= self.resolution - 1 {
            return 0.0;
        }

        let p = &self.points;

        // Second fundamental form coefficients (simplified)
        let center = &p[i][j];
        let left = &p[i - 1][j];
        let right = &p[i + 1][j];
        let up = &p[i][j - 1];
        let down = &p[i][j + 1];

        // Laplacian approximation for mean curvature
        let laplacian = Point3D::new(
            left.x + right.x + up.x + down.x - 4.0 * center.x,
            left.y + right.y + up.y + down.y - 4.0 * center.y,
            left.z + right.z + up.z + down.z - 4.0 * center.z,
        );

        laplacian.magnitude()
    }

    /// Compute total surface tension (sum of mean curvatures)
    pub fn total_tension(&self) -> f64 {
        let mut total = 0.0;
        let mut count = 0;

        for i in 1..self.resolution - 1 {
            for j in 1..self.resolution - 1 {
                total += self.mean_curvature(i, j);
                count += 1;
            }
        }

        if count > 0 {
            total / count as f64
        } else {
            0.0
        }
    }
}

// =============================================================================
// NARRATIVE GEOMETRY MAPPER
// =============================================================================

/// Maps a text narrative onto a geometric surface for validation
pub struct NarrativeGeometry {
    /// The underlying Enneper surface
    surface: EnneperSurface,
    /// Mapped tension field from text
    tension_field: Vec<f64>,
}

impl NarrativeGeometry {
    pub fn new(resolution: usize) -> Self {
        Self {
            surface: EnneperSurface::new(resolution),
            tension_field: Vec::new(),
        }
    }

    /// Map a narrative (text) onto the surface
    /// Each word contributes to local curvature
    pub fn map_narrative(&mut self, text: &str) -> TruthState {
        let words: Vec<&str> = text.split_whitespace().collect();
        let word_count = words.len();

        if word_count == 0 {
            return TruthState::Annealing {
                curvature: 0.0,
                tension: 0.0,
            };
        }

        // Hash each word to a position on the surface
        self.tension_field.clear();
        let mut total_tension = 0.0;

        for (idx, word) in words.iter().enumerate() {
            let hash = self.word_hash(word);

            // Map hash to surface coordinates
            let u = (idx as f64 / word_count as f64) * (self.surface.resolution - 1) as f64;
            let v = (hash % self.surface.resolution as u64) as f64;

            let i = u as usize;
            let j = v as usize;

            // Get local curvature at this word's position
            let local_curvature = self.surface.mean_curvature(
                i.min(self.surface.resolution - 2).max(1),
                j.min(self.surface.resolution - 2).max(1),
            );

            // Add word-specific tension (based on character complexity)
            let word_tension = self.word_tension(word);
            let combined = local_curvature + word_tension;

            self.tension_field.push(combined);
            total_tension += combined;
        }

        let avg_tension = total_tension / word_count as f64;
        let avg_curvature = self.surface.total_tension();

        // Classify based on tension/curvature
        if avg_tension < TENSION_THRESHOLD && avg_curvature < CURVATURE_THRESHOLD {
            TruthState::Crystal {
                curvature: avg_curvature,
                tension: avg_tension,
            }
        } else if avg_tension < TENSION_THRESHOLD * 3.0 {
            TruthState::Annealing {
                curvature: avg_curvature,
                tension: avg_tension,
            }
        } else {
            TruthState::Hallucination {
                curvature: avg_curvature,
                tension: avg_tension,
            }
        }
    }

    /// Compute a hash for a word (prime-based)
    fn word_hash(&self, word: &str) -> u64 {
        let primes = [2u64, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        let mut hash = 0u64;

        for (i, c) in word.chars().enumerate() {
            let prime = primes[i % primes.len()];
            hash = hash.wrapping_add((c as u64).wrapping_mul(prime));
        }

        hash
    }

    /// Compute tension contribution of a single word
    fn word_tension(&self, word: &str) -> f64 {
        let len = word.len() as f64;
        let complexity = word.chars().filter(|c| !c.is_alphanumeric()).count() as f64;

        // Longer words and special characters add tension
        (len / 10.0) + (complexity * 0.1)
    }
}

// =============================================================================
// POINCARÉ SECTION: Golden-Silver Stability Lock
// =============================================================================

/// The dual-frequency stabilizer using Golden and Silver ratios
pub struct PoincareSectionValidator {
    /// Golden winding number
    pub golden_phase: f64,
    /// Silver winding number
    pub silver_phase: f64,
}

impl PoincareSectionValidator {
    pub fn new() -> Self {
        Self {
            golden_phase: 0.0,
            silver_phase: 0.0,
        }
    }

    /// Advance the dual spirals by a logic step
    pub fn advance(&mut self, step: f64) {
        // Golden winding (primary)
        self.golden_phase = (self.golden_phase + step * PHI) % (2.0 * PI);

        // Silver winding (secondary "spy")
        self.silver_phase = (self.silver_phase + step * DELTA) % (2.0 * PI);
    }

    /// Check for chirality lock (both phases must be irrational)
    /// Returns true if the phases create a valid Moire pattern
    pub fn is_locked(&self) -> bool {
        // The phases should never sync (irrational windings)
        let phase_diff = (self.golden_phase - self.silver_phase).abs();

        // If too close to rational ratio, it's a lie trying to penetrate
        for n in 1..10 {
            let rational = (n as f64) * PI / 5.0;
            if (phase_diff - rational).abs() < 0.01 {
                return false; // Rational resonance detected!
            }
        }

        true
    }

    /// Validate a sequence of logic steps
    pub fn validate_sequence(&mut self, steps: &[f64]) -> bool {
        for step in steps {
            self.advance(*step);
            if !self.is_locked() {
                return false;
            }
        }
        true
    }
}

// =============================================================================
// HELICAL MÖBIUS TORUS: The Chronometer
// =============================================================================

/// The breathing loop of logic time
pub struct MobiusTorus {
    /// Current position on the torus (0 to 2π)
    pub theta: f64,
    /// Current height on the helix
    pub phi: f64,
    /// Compression factor (high pressure inward)
    pub compression: f64,
    /// Number of half-twists (Möbius property)
    pub half_twists: u32,
}

impl MobiusTorus {
    pub fn new(half_twists: u32) -> Self {
        Self {
            theta: 0.0,
            phi: 0.0,
            compression: 1.0,
            half_twists,
        }
    }

    /// Advance along the Möbius surface
    /// Returns (x, y, z) position and whether subject/object flipped
    pub fn advance(&mut self, step: f64) -> (Point3D, bool) {
        self.theta = (self.theta + step) % (2.0 * PI);
        self.phi = (self.phi + step * PHI) % (2.0 * PI);

        // Möbius twist angle
        let twist = (self.half_twists as f64) * self.theta / 2.0;

        // Torus coordinates with Möbius twist
        let r_major = 2.0;
        let r_minor = 1.0 * self.compression;

        let x = (r_major + r_minor * twist.cos()) * self.theta.cos();
        let y = (r_major + r_minor * twist.cos()) * self.theta.sin();
        let z = r_minor * twist.sin();

        // Subject becomes Object after half rotation with odd twists
        let flipped = (self.half_twists % 2 == 1) && (self.theta > PI);

        (Point3D::new(x, y, z), flipped)
    }

    /// Compress inward (analysis mode)
    pub fn compress(&mut self, factor: f64) {
        self.compression = (self.compression * factor).max(0.1);
    }

    /// Expand outward (synthesis mode)
    pub fn expand(&mut self, factor: f64) {
        self.compression = (self.compression * factor).min(3.0);
    }
}

// =============================================================================
// UNIFIED VALIDATOR
// =============================================================================

/// The complete truth validation engine
pub struct UnifiedFieldValidator {
    pub geometry: NarrativeGeometry,
    pub poincare: PoincareSectionValidator,
    pub chronometer: MobiusTorus,
}

impl UnifiedFieldValidator {
    pub fn new() -> Self {
        Self {
            geometry: NarrativeGeometry::new(32),
            poincare: PoincareSectionValidator::new(),
            chronometer: MobiusTorus::new(1), // Single Möbius twist
        }
    }

    /// Full validation of a narrative
    pub fn validate(&mut self, text: &str) -> TruthState {
        // Step 1: Map to Enneper surface
        let geometry_state = self.geometry.map_narrative(text);

        // Step 2: Check Poincaré stability
        let words: Vec<&str> = text.split_whitespace().collect();
        let steps: Vec<f64> = words.iter().map(|w| w.len() as f64 * 0.1).collect();

        let poincare_valid = self.poincare.validate_sequence(&steps);

        // Step 3: Advance chronometer and check for conscience flip
        let mut conscience_triggered = false;
        for _ in 0..words.len() {
            let (_, flipped) = self.chronometer.advance(0.1);
            if flipped {
                conscience_triggered = true;
            }
        }

        // Combine all validations
        match geometry_state {
            TruthState::Crystal { curvature, tension } if poincare_valid => {
                TruthState::Crystal { curvature, tension }
            }
            TruthState::Crystal { curvature, tension } => {
                // Geometry says truth but Poincaré failed
                TruthState::Annealing { curvature, tension }
            }
            TruthState::Annealing { curvature, tension } => {
                TruthState::Annealing { curvature, tension }
            }
            TruthState::Hallucination { curvature, tension } => {
                TruthState::Hallucination { curvature, tension }
            }
    }
}

// =============================================================================
// IMPLICIT SURFACE VALIDATOR: Tear Point Detection
// =============================================================================

/// Result of implicit differentiation at a point
#[derive(Debug)]
pub struct ImplicitDerivative {
    /// dy/dx value (may be infinite)
    pub slope: f64,
    /// Whether the derivative is bounded
    pub is_bounded: bool,
    /// Whether this is a tear point (vertical tangent)
    pub is_tear: bool,
    /// Partial F/∂x
    pub df_dx: f64,
    /// Partial F/∂y
    pub df_dy: f64,
}

/// Validates narratives using implicit differentiation
/// Detects "tear points" where the surface becomes undefined
pub struct ImplicitSurfaceValidator {
    /// The underlying Enneper surface
    surface: EnneperSurface,
    /// Threshold for considering derivative as "torn"
    tear_threshold: f64,
}

impl ImplicitSurfaceValidator {
    pub fn new(resolution: usize) -> Self {
        Self {
            surface: EnneperSurface::new(resolution),
            tear_threshold: 100.0, // Slope > 100 is considered a tear
        }
    }
    
    /// Compute implicit derivative at a surface point
    /// For the Enneper surface, we use the constraint H(x,y,z) = 0
    /// dy/dx = -(∂H/∂x) / (∂H/∂y)
    pub fn implicit_derivative(&self, i: usize, j: usize) -> ImplicitDerivative {
        if i == 0 || i >= self.surface.resolution - 1 || 
           j == 0 || j >= self.surface.resolution - 1 {
            return ImplicitDerivative {
                slope: 0.0,
                is_bounded: true,
                is_tear: false,
                df_dx: 0.0,
                df_dy: 0.0,
            };
        }
        
        let p = &self.surface.points;
        
        // Approximate partial derivatives using finite differences
        // ∂F/∂x ≈ (F(x+h) - F(x-h)) / 2h
        let left = &p[i - 1][j];
        let right = &p[i + 1][j];
        let up = &p[i][j - 1];
        let down = &p[i][j + 1];
        
        // For Enneper surface, F = mean curvature constraint
        // We approximate using position changes
        let df_dx = (right.x - left.x) / 2.0;
        let df_dy = (down.y - up.y) / 2.0;
        
        // Check for tear point (denominator near zero)
        let is_tear = df_dy.abs() < 0.001;
        
        let slope = if is_tear {
            f64::INFINITY
        } else {
            -df_dx / df_dy
        };
        
        let is_bounded = slope.abs() < self.tear_threshold;
        
        ImplicitDerivative {
            slope,
            is_bounded,
            is_tear,
            df_dx,
            df_dy,
        }
    }
    
    /// Map narrative to surface and detect tear points
    pub fn validate_narrative(&self, text: &str) -> (Vec<ImplicitDerivative>, bool) {
        let words: Vec<&str> = text.split_whitespace().collect();
        let mut derivatives = Vec::with_capacity(words.len());
        let mut has_tear = false;
        
        for (idx, word) in words.iter().enumerate() {
            // Hash word to surface position
            let hash = self.word_hash(word);
            let i = (idx % (self.surface.resolution - 2)) + 1;
            let j = ((hash % self.surface.resolution as u64) as usize).max(1).min(self.surface.resolution - 2);
            
            let deriv = self.implicit_derivative(i, j);
            
            if deriv.is_tear || !deriv.is_bounded {
                has_tear = true;
            }
            
            derivatives.push(deriv);
        }
        
        (derivatives, has_tear)
    }
    
    /// Compute hash for word (same as NarrativeGeometry)
    fn word_hash(&self, word: &str) -> u64 {
        let primes = [2u64, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        let mut hash = 0u64;
        
        for (i, c) in word.chars().enumerate() {
            let prime = primes[i % primes.len()];
            hash = hash.wrapping_add((c as u64).wrapping_mul(prime));
        }
        
        hash
    }
    
    /// Get the Poincaré section (cross-section of torus)
    /// Returns the circle x² + y² = r² at a given angle
    pub fn poincare_section(&self, theta: f64, r: f64) -> Vec<(f64, f64, f64)> {
        let mut points = Vec::new();
        let steps = 100;
        
        for k in 0..steps {
            let phi = (k as f64 / steps as f64) * 2.0 * PI;
            
            // Circle in the section plane
            let x = r * phi.cos();
            let y = r * phi.sin();
            
            // Implicit derivative: dy/dx = -x/y
            let slope = if y.abs() < 0.001 {
                f64::INFINITY
            } else {
                -x / y
            };
            
            points.push((x, y, slope));
        }
        
        points
    }
}

// =============================================================================
// ENTANGLED FLUX ROPE VALIDATOR (Product Rule)
// =============================================================================

/// Validates the product rule for entangled Golden-Silver flux ropes
pub struct EntangledFluxValidator {
    /// Golden phase function
    golden_phase: f64,
    /// Silver phase function
    silver_phase: f64,
    /// Step size
    step: f64,
}

impl EntangledFluxValidator {
    pub fn new() -> Self {
        Self {
            golden_phase: 0.0,
            silver_phase: 0.0,
            step: 0.01,
        }
    }
    
    /// Compute the product of golden and silver
    pub fn product(&self) -> f64 {
        self.golden_phase * self.silver_phase
    }
    
    /// Compute d/dx[φ(x) · δ(x)] using the Product Rule
    /// = φ'(x)δ(x) + φ(x)δ'(x)
    pub fn product_derivative(&self) -> f64 {
        // φ'(x) = φ (exponential growth at golden ratio)
        let phi_prime = PHI * self.golden_phase.sin();
        
        // δ'(x) = δ (exponential growth at silver ratio)  
        let delta_prime = DELTA * self.silver_phase.sin();
        
        // Product Rule: φ'δ + φδ'
        phi_prime * self.silver_phase + self.golden_phase * delta_prime
    }
    
    /// Advance the entangled system
    pub fn advance(&mut self, step: f64) -> (f64, f64) {
        self.golden_phase = (self.golden_phase + step * PHI) % (2.0 * PI);
        self.silver_phase = (self.silver_phase + step * DELTA) % (2.0 * PI);
        
        (self.product(), self.product_derivative())
    }
    
    /// Check if the product derivative indicates entanglement stability
    pub fn is_stable(&self) -> bool {
        let deriv = self.product_derivative();
        deriv.abs() < 10.0 // Bounded derivative = stable
    }
}

// =============================================================================
// PSEUDOSPHERE: The Geometry of Lies
// =============================================================================
//
// Phase 155: The Anti-Sphere
//
// Sphere (K > 0):        Lines converge, Truth clusters in center
// Pseudosphere (K < 0):  Lines diverge, Lies float to edges
//
// The Pseudosphere has the "Gabriel's Horn" paradox:
// - Finite Volume: Little actual substance
// - Infinite Surface: Infinite excuses, buzzwords, complexity
//
// This is the geometric signature of a Beautiful Lie.

/// Classification of geometric curvature type
#[derive(Debug, Clone, Copy, PartialEq)]
pub enum CurvatureType {
    /// Positive curvature - sphere-like (Truth gravitates inward)
    Spherical,
    /// Zero curvature - flat (Neutral)
    Flat,
    /// Negative curvature - pseudosphere-like (Lie expands outward)
    Hyperbolic,
}

/// Result of pseudosphere analysis
#[derive(Debug)]
pub struct PseudosphereAnalysis {
    pub curvature_type: CurvatureType,
    pub gaussian_curvature: f64,      // K value
    pub volume_estimate: f64,          // "Substance"
    pub surface_estimate: f64,         // "Excuses"
    pub gabriels_horn_ratio: f64,      // Surface/Volume (>1 = suspect)
    pub singularity_detected: bool,    // Hit the "rim"
    pub is_lie_geometry: bool,         // Final verdict
}

/// The Tractrix curve - generator of the Pseudosphere
/// 
/// Parametric equations:
/// x(t) = t - tanh(t)
/// y(t) = sech(t) = 1/cosh(t)
/// 
/// For t ∈ (0, ∞), this generates the profile that creates
/// the pseudosphere when rotated around the x-axis.
pub struct Tractrix {
    resolution: usize,
}

impl Tractrix {
    pub fn new(resolution: usize) -> Self {
        Self { resolution }
    }
    
    /// Generate a point on the Tractrix curve
    pub fn point(&self, t: f64) -> (f64, f64) {
        if t <= 0.001 {
            // Avoid singularity at t=0
            return (0.001, 1.0);
        }
        
        let x = t - t.tanh();
        let y = 1.0 / t.cosh();  // sech(t)
        
        (x, y)
    }
    
    /// Calculate arc length element ds
    pub fn arc_element(&self, t: f64) -> f64 {
        if t <= 0.001 {
            return 0.0;
        }
        
        // ds/dt = |sech(t) * tanh(t)|
        let sech = 1.0 / t.cosh();
        let tanh = t.tanh();
        (sech * tanh).abs()
    }
    
    /// Detect if we've hit the singularity (the "rim")
    pub fn is_at_singularity(&self, t: f64) -> bool {
        // The Tractrix has a cusp at t → ∞ (y → 0)
        // and a singularity at t = 0 (y = 1)
        let (_, y) = self.point(t);
        y < 0.01 || t < 0.01
    }
}

/// The Pseudosphere - surface of constant negative curvature
/// 
/// Created by rotating the Tractrix around the x-axis.
/// Has Gaussian curvature K = -1 everywhere (except at singularities).
pub struct Pseudosphere {
    pub tractrix: Tractrix,
    pub radius: f64,  // Radius at the "neck"
}

impl Pseudosphere {
    pub fn new(resolution: usize) -> Self {
        Self {
            tractrix: Tractrix::new(resolution),
            radius: 1.0,
        }
    }
    
    /// Gaussian curvature at a point (constant = -1 for pseudosphere)
    pub fn gaussian_curvature(&self, t: f64) -> f64 {
        if self.tractrix.is_at_singularity(t) {
            // At singularity, curvature is undefined (approaches -∞)
            return f64::NEG_INFINITY;
        }
        -1.0  // Constant negative curvature
    }
    
    /// Calculate volume of the pseudosphere (finite!)
    /// V = (2/3) * π * r³
    /// This is Gabriel's paradox: finite volume, infinite surface
    pub fn volume(&self) -> f64 {
        (2.0 / 3.0) * PI * self.radius.powi(3)
    }
    
    /// Estimate surface area (infinite in limit!)
    /// For practical purposes, we integrate up to parameter t_max
    pub fn surface_area(&self, t_max: f64) -> f64 {
        let steps = self.tractrix.resolution;
        let dt = t_max / steps as f64;
        let mut area = 0.0;
        
        for i in 1..steps {
            let t = i as f64 * dt;
            let (_, y) = self.tractrix.point(t);
            let ds = self.tractrix.arc_element(t);
            
            // Surface of revolution: dA = 2πy ds
            area += 2.0 * PI * y * ds * dt;
        }
        
        area
    }
    
    /// Gabriel's Horn Ratio: Surface / Volume
    /// - Ratio > 10: Highly suspicious (infinite promises, finite delivery)
    /// - Ratio 1-10: Moderate (could be complex but honest)
    /// - Ratio < 1: Dense (solid substance)
    pub fn gabriels_horn_ratio(&self, t_max: f64) -> f64 {
        let vol = self.volume();
        let surf = self.surface_area(t_max);
        
        if vol < 0.001 {
            return f64::INFINITY;
        }
        
        surf / vol
    }
}

/// The GeometricLieDetector - uses curvature to classify narratives
pub struct GeometricLieDetector {
    pseudosphere: Pseudosphere,
}

impl GeometricLieDetector {
    pub fn new() -> Self {
        Self {
            pseudosphere: Pseudosphere::new(64),
        }
    }
    
    /// Analyze a narrative's "geometric signature"
    /// 
    /// Maps text properties to geometric quantities:
    /// - Word count → Volume (substance)
    /// - Character count → Surface (coverage)
    /// - Unique words / Total words → Curvature type
    pub fn analyze(&self, text: &str) -> PseudosphereAnalysis {
        let words: Vec<&str> = text.split_whitespace().collect();
        let word_count = words.len() as f64;
        let char_count = text.len() as f64;
        
        if word_count < 1.0 {
            return PseudosphereAnalysis {
                curvature_type: CurvatureType::Flat,
                gaussian_curvature: 0.0,
                volume_estimate: 0.0,
                surface_estimate: 0.0,
                gabriels_horn_ratio: 0.0,
                singularity_detected: false,
                is_lie_geometry: false,
            };
        }
        
        // Unique words represent "real substance"
        let unique_words: std::collections::HashSet<&str> = 
            words.iter().map(|w| *w).collect();
        let unique_count = unique_words.len() as f64;
        
        // Uniqueness ratio determines curvature type
        let uniqueness = unique_count / word_count;
        
        // Volume estimate: unique meaning density
        let volume_estimate = unique_count;
        
        // Surface estimate: total characters (complexity/verbosity)
        let surface_estimate = char_count;
        
        // Gabriel's Horn ratio
        let gabriels_horn_ratio = surface_estimate / volume_estimate.max(1.0);
        
        // Curvature classification
        let (curvature_type, gaussian_curvature) = if uniqueness > 0.7 {
            // High uniqueness = spherical (converging truth)
            (CurvatureType::Spherical, uniqueness)
        } else if uniqueness > 0.4 {
            // Medium uniqueness = flat
            (CurvatureType::Flat, 0.0)
        } else {
            // Low uniqueness = hyperbolic (diverging, repetitive)
            (CurvatureType::Hyperbolic, -1.0 + uniqueness)
        };
        
        // Singularity detection: infinite surface with near-zero volume
        let singularity_detected = gabriels_horn_ratio > 50.0;
        
        // Final lie detection using geometric signature
        let is_lie_geometry = 
            curvature_type == CurvatureType::Hyperbolic 
            || gabriels_horn_ratio > 20.0
            || singularity_detected;
        
        PseudosphereAnalysis {
            curvature_type,
            gaussian_curvature,
            volume_estimate,
            surface_estimate,
            gabriels_horn_ratio,
            singularity_detected,
            is_lie_geometry,
        }
    }
}

// =============================================================================
// TESTS
// =============================================================================

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_enneper_surface() {
        let surface = EnneperSurface::new(32);
        let tension = surface.total_tension();

        // Enneper surface should have near-zero tension (minimal surface)
        assert!(tension < 1.0, "Enneper tension should be low: {}", tension);
    }

    #[test]
    fn test_narrative_mapping() {
        let mut geom = NarrativeGeometry::new(32);

        // Simple true statement
        let result = geom.map_narrative("The sky is blue");
        assert!(matches!(
            result,
            TruthState::Crystal { .. } | TruthState::Annealing { .. }
        ));
    }

    #[test]
    fn test_poincare_lock() {
        let mut poincare = PoincareSectionValidator::new();

        // Irrational steps should maintain lock
        assert!(poincare.validate_sequence(&[0.1, 0.2, 0.3, 0.4]));
    }

    #[test]
    fn test_mobius_flip() {
        let mut torus = MobiusTorus::new(1);

        // Advance past π to trigger flip
        for _ in 0..50 {
            let (_, flipped) = torus.advance(0.1);
            if flipped {
                return; // Test passed
            }
        }

        panic!("Möbius flip should have occurred");
    }
}
