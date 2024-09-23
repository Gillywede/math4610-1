import numpy as np
import matplotlib.pyplot as plt
#
# this code will compute an explicit Euler approximation
# for the logarithmic model
#
initial_time = 0.0
final_time = 200.0
nsteps = 150
dt = float((final_time - initial_time)/nsteps)
alpha = 0.2
gamma = 0.03
P0 = 3.5
#
# set up storage for the approximation
# ------------------------------------
#
tvals = np.full(nsteps+1, 0.0, dtype="float")
svals = np.full(nsteps+1, 0.0, dtype="float")
#
# set initial point
# -----------------
#
tvals[0] = initial_time
svals[0] = P0
a1 = 1.0 + alpha * dt
g1 = gamma * dt
for i in range(1,nsteps+1):
    tvals[i] = tvals[i-1] + dt
    stmp = svals[i-1]
    sltmp = np.log(stmp)
    svals[i] = a1 * stmp - g1 * stmp * sltmp
#
# graphics
# --------
#
plt.plot(tvals, svals)
plt.show()