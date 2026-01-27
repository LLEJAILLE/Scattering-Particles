import numpy as np

class Particle:
    def __init__(self, masse, position, velocity, trajectories, velocities):
        self.masse = masse
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.trajectories = [self.position.copy()]
        self.velocities = [self.velocity.copy()]
