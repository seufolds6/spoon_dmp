import numpy as np
from dmp_discrete import *
import matplotlib.pyplot as plt

y_des = np.load("../data/flattening.npy").T

y_des -= y_des[:, 0][:, None]

# test normal run
dmp = DMPs_discrete(n_dmps=2, n_bfs=500, ay=np.ones(2) * 10.0)
y_track = []
dy_track = []
ddy_track = []

dmp.imitate_path(y_des=y_des, plot=False)
y_track, dy_track, ddy_track = dmp.rollout()
plt.figure(1, figsize=(6, 6))

x = np.linspace(0, 1, 100)
y = x
plt.plot(x, y, "r", lw=2, label="Demonstration")

plt.plot(y_track[:, 0], y_track[:, 1], "b", lw=2, label="DMP Rollout")

plt.title("DMP for Flattening Task")
plt.axis("equal")
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
