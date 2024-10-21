import numpy as np
from dmp_discrete import *

time_steps = 100
t = np.linspace(0, 1, time_steps)
x_vals = np.full(time_steps, 0.5)
y_vals = 0.0 + t
y_des = np.vstack((x_vals, y_vals))

# Normalize the trajectory to start from the origin
y_des -= y_des[:, 0][:, None]

dmp = DMPs_discrete(n_dmps=2, n_bfs=90999, ay=np.ones(2) * 10.0)
y_track = []
dy_track = []
ddy_track = []

# Imitate the path specified by y = x^2 - x
dmp.imitate_path(y_des=y_des, plot=True)
y_track, dy_track, ddy_track = dmp.rollout()
