import numpy as np
from potential import Potential

class Integrator:
    def __init__(self, dt: float, potential: Potential):
        self.dt = dt
        self.potential = potential

    def step(self, particle):
        r = particle.position
        v = particle.velocity
        m = particle.masse

        L = np.linalg.norm(np.cross(r, m * v))
        vEff = L**2 / (m**2 * np.linalg.norm(r)**2) + self.potential.g / np.linalg.norm(r)
        E = 0.5 * m * np.linalg.norm(v)**2 + vEff

        a = self.potential.force(r) / m

        particle.velocity = v + a * self.dt
        particle.position = r + particle.velocity * self.dt

        particle.velocities.append(particle.velocity.copy())
        particle.trajectories.append(particle.position.copy())