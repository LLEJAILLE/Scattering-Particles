import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection

class Results:
    def plot_trajectories(self, particles, b_values, hyperparameters):
        plt.figure(figsize=(10, 8))

        base_cmap = plt.get_cmap("Greys")
        cmap = plt.cm.colors.LinearSegmentedColormap.from_list(
            "greys_trimmed",
            base_cmap(np.linspace(0.25, 0.85, 256))
        )
        norm = plt.Normalize(min(b_values), max(b_values))

        for p, b in zip(particles, b_values):
            traj = np.array(p.trajectories)
            plt.plot(
                traj[:, 0],
                traj[:, 1],
                color=cmap(norm(b)),
                linewidth=0.9
            )

        plt.scatter(0, 0, color="black", s=50, zorder=5)

        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)

        plt.xlabel("x coordinate (reduced units)")
        plt.ylabel("y coordinate (reduced units)")
        plt.axis("equal")
        title_text = (
            f"Classical scattering in a Coulomb potential\n"
            f"g={hyperparameters['g']}, m={hyperparameters['m']}, "
            f"v0={hyperparameters['v0']}, R={hyperparameters['R']}"
        )
        plt.title(title_text)

        sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        plt.colorbar(sm, ax=plt.gca(), label="Impact parameter b")

        plt.show()
