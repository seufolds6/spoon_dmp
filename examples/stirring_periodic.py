import numpy as np
from dmp_rhythmic import *
import matplotlib.pyplot as plt

y_des = np.load("../data/stirring.npy").T
y_des -= y_des[:, 0][:, None]

dmp = DMPs_rhythmic(n_dmps=2, n_bfs=90999, ay=np.ones(2) * 10.0)
y_track = []
dy_track = []
ddy_track = []

dmp.imitate_path(y_des=y_des, plot=False)
y_track, dy_track, ddy_track = dmp.rollout()

plt.figure(1, figsize=(6, 6))

theta = np.linspace(np.pi/8, 5*np.pi/2, 100)
x = 4*np.cos(theta) - 2
y = 4*np.sin(theta) - 2
plt.plot(x, y, "r", lw=2, label="Demonstration")

plt.plot(y_track[:, 0], y_track[:, 1], "b", lw=2, label="DMP Rollout")

plt.title("DMP for Stirring Task")
plt.axis("equal")
plt.xlim([-10, 8])
plt.ylim([-10, 8])
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
