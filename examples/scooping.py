import numpy as np
from dmp_discrete import *
import matplotlib.pyplot as plt

y_des = np.load("../data/scooping.npy").T

y_des -= y_des[:, 0][:, None]

# test normal run
dmp = DMPs_discrete(n_dmps=2, n_bfs=500, ay=np.ones(2) * 10.0)
y_track = []
dy_track = []
ddy_track = []

dmp.imitate_path(y_des=y_des, plot=False)
y_track, dy_track, ddy_track = dmp.rollout()
plt.figure(1, figsize=(6, 6))

x = np.linspace(0.1, 2, 100)
y = x*(x - 1)
plt.plot(x, y, "r", lw=2, label=r"$y = x \cdot (x - 1)$")

plt.plot(y_track[:, 0], y_track[:, 1], "b", lw=2)

plt.title("DMP system")
plt.axis("equal")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.show()
