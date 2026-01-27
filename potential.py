import numpy as np

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
        return -self.g * r / norm_r**3