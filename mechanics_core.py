#!/usr/bin/env python3
from dataclasses import dataclass
import math

class DynamicsEngine:
    """
    TENT v4.0 Classical Mechanics Engine.
    Treats Prime Nodes as Physical Bodies.
    
    F = ma  =>  a = F / m
    v = v0 + at
    p = mv
    E = 0.5 * m * v^2
    """
    
    def apply_force(self, node_mass: float, current_velocity: float, force: float, time_delta: float = 1.0) -> float:
        """
        Applies a Force to a Mass for a duration, returning new Velocity.
        
        High Mass (Truth) -> Low Acceleration (Inertia/Stability).
        Low Mass (Vapor) -> High Acceleration (Volatility).
        """
        if node_mass <= 0: return current_velocity # Massless objects don't obey Newton
        
        acceleration = force / node_mass
        new_velocity = current_velocity + (acceleration * time_delta)
        
        return new_velocity

    def calculate_momentum(self, mass: float, velocity: float) -> float:
        """Returns Momentum (p = mv). Impact resistance."""
        return mass * abs(velocity)

    def calculate_energy(self, mass: float, velocity: float) -> float:
        """Returns Kinetic Energy (E = 0.5 * m * v^2). Market Impact."""
        return 0.5 * mass * (velocity ** 2)

    def simulate_trajectory(self, node, force: float, steps: int = 5):
        """
        Simulates the motion of a node over time under constant force.
        Returns a log of the trajectory.
        """
        log = []
        v = node.velocity
        p = node.position
        m = node.mass
        
        log.append(f"INITIAL: Pos={p:.2f}, Vel={v:.2f}, Mass={m:.2f}")
        
        for t in range(1, steps + 1):
            # Update Velocity
            v = self.apply_force(m, v, force, time_delta=1.0)
            # Update Position (x = x0 + v*t approx for small steps)
            p += v 
            
            momentum = self.calculate_momentum(m, v)
            energy = self.calculate_energy(m, v)
            
            log.append(f"T={t}: Pos={p:.2f}, Vel={v:.2f}, Mom={momentum:.2f}, KE={energy:.2f}")
            
        return log
