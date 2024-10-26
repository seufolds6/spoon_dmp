import numpy as np
from dmp_discrete import *
import matplotlib.pyplot as plt

x_vals = np.linspace(-1, 2, 500)
y_vals = x_vals*(x_vals - 1)
y_des = np.vstack((x_vals, y_vals))

# Normalize the trajectory to start from the origin
y_des -= y_des[:, 0][:, None]

dmp = DMPs_discrete(n_dmps=2, n_bfs=90999, ay=np.ones(2) * 10.0)
y_track = []
dy_track = []
ddy_track = []

# dmp.imitate_path(y_des=y_des, plot=True)
dmp.imitate_path(y_des=y_des, plot=False)
y_track, dy_track, ddy_track = dmp.rollout()

# Plot the original and learned trajectories
plt.figure(figsize=(10, 5))
plt.plot(y_des[0], y_des[1], label='Demonstration Trajectory (y = x * (x - 1))', linestyle='--', color='blue')
plt.plot(y_track[:, 0], y_track[:, 1], label='Learned Trajectory', linestyle='-', color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparison of Demonstration and Learned Trajectories")
plt.legend()
plt.grid(True)
plt.show()
