import numpy as np
from dmp_discrete import *
import matplotlib.pyplot as plt

y_des = np.load("../data/stirring.npy").T
y_des -= y_des[:, 0][:, None]

# test normal run
dmp = DMPs_discrete(n_dmps=2, n_bfs=500, ay=np.ones(2) * 10.0)
y_track = []
dy_track = []
ddy_track = []

dmp.imitate_path(y_des=y_des, plot=False)
y_track, dy_track, ddy_track = dmp.rollout()
plt.figure(1, figsize=(6, 6))

theta = np.linspace(np.pi / 8, 3 * np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y, "r", lw=2, label=r"$y = x \cdot (x - 1)$")

plt.plot(y_track[:, 0], y_track[:, 1], "b", lw=2)

plt.title("DMP system")
plt.axis("equal")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.show()



# import numpy as np
# from dmp_rhythmic import *

# time_steps = 100
# t = np.linspace(0, 2 * np.pi, time_steps)

# x_vals = np.cos(t) + 1
# y_vals = np.sin(t)
# y_des = np.vstack((x_vals, y_vals))

# # Normalize the trajectory to start from the origin
# y_des -= y_des[:, 0][:, None]

# dmp = DMPs_rhythmic(n_dmps=2, n_bfs=90999, ay=np.ones(2) * 10.0)
# y_track = []
# dy_track = []
# ddy_track = []

# dmp.imitate_path(y_des=y_des, plot=True)
# y_track, dy_track, ddy_track = dmp.rollout()
