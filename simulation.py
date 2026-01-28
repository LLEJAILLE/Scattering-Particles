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
        self.theta = []


    def run(self, R_exit=20.0):
        t = 0.0
        while t < self.t_max:
            for p in self.particles:
                if np.linalg.norm(p.position) < R_exit: 
                    self.integrator.step(p)
            t += self.integrator.dt

    def visualize_theta_angle(self, b_value):
        thetas = []
        for p in self.particles:
            v = p.velocity
            theta = np.arctan2(v[1], v[0])
            thetas.append(theta)
        self.theta = thetas

        plt.figure(figsize=(8, 6))
        plt.plot(b_value, thetas, 'o-')
        plt.title('Scattering Angles θ for Different Impact Parameters b')
        plt.xlabel('Index of Impact Parameter b')
        plt.ylabel('Scattering Angle θ (radians)')
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.grid()
        plt.show()



def main():
    g = -1.0
    m = 1.0
    v0 = 1.0
    R = 10.0

    potential = CoulombPotential(g=g)
    integrator = Integrator(dt=0.01, potential=potential)

    particles = []

    b_value = [0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0]

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
    simulation.visualize_theta_angle(b_value)
    
    results = Results()
    # results.plot_trajectories(particles, b_value, hyperparameters)

    # potential.potential_graph()

if __name__ == "__main__":
    main()