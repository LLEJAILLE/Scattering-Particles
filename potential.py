import numpy as np
import matplotlib.pyplot as plt

class Potential:
    def force(self, r: np.ndarray) -> np.ndarray:
        raise NotImplementedError

class CoulombPotential(Potential):
    def __init__(self, g: float):
        self.g = g

    def force(self, r: np.ndarray) -> np.ndarray:
        norm_r = np.linalg.norm(r)
        if norm_r == 0:
            raise ValueError("Singularité au centre du potentiel")
        return - (self.g / norm_r**3) * r
    
    def potential_graph(self):
        q = 5.0
        epsilon_0 = 1
        r = np.linspace(0.02, 0.5, 400)
        V_r = q / (4 * np.pi * epsilon_0 * r)

        plt.figure(figsize=(8, 6))
        plt.plot(r, V_r, color='blue', label='Coulomb Potential V(r)')
        plt.title('Coulomb Potential as a Function of Distance r')
        plt.xlabel('Distance r')
        plt.ylabel('Potential V(r)')
        plt.ylim(0, 25)
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.legend()
        plt.show()
