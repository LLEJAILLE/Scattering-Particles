import matplotlib.pyplot as plt
import numpy as np
from particle import Particle
from potential import Potential, CoulombPotential
from integrator import Integrator
from results import Results

class Simulation:
    def __init__(self, particles, integrator, t_max):
        self.particles = particles
        self.integrator = integrator
        self.t_max = t_max


    def run(self, R_exit=20.0):
        t = 0.0
        while t < self.t_max:
            for p in self.particles:
                if np.linalg.norm(p.position) < R_exit:
                    self.integrator.step(p)
            t += self.integrator.dt

def main():
    g = 2.0
    m = 0.5
    v0 = 1.0
    R = 10.0

    potential = CoulombPotential(g=g)
    integrator = Integrator(dt=0.01, potential=potential)

    particles = []

    b_value = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

    for b in b_value:
        p = Particle(
            masse=m,
            position=[-R, b],
            velocity=[v0, 0.0],
            trajectories=[],
            velocities=[]
        )
        particles.append(p)


    simulation = Simulation(
        particles=particles,
        integrator=integrator,
        t_max=100.0
    )

    hyperparameters = {
        "g": g,
        "m": m,
        "v0": v0,
        "R": R
    }

    simulation.run()
    results = Results()
    results.plot_trajectories(particles, b_value, hyperparameters)

if __name__ == "__main__":
    main()