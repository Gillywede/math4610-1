import numpy as np
import matplotlib.pyplot as plt
#
# this code will compute an explicit Euler approximation
# for the logarithmic model
#
initial_time = 0.0
final_time = 200.0
nsteps = 100
dt = float((final_time - initial_time)/nsteps)
alpha = 2.1
beta = 0.003
gamma = alpha / ( np.log(alpha) - np.log(beta) )
P0 = 3.5
#
# set up storage for the approximation
# ------------------------------------
#
tvals = np.full(nsteps+1, 0.0, dtype="float")
slogs = np.full(nsteps+1, 0.0, dtype="float")
slns = np.full(nsteps+1, 0.0, dtype="float")
#
# set initial point
# -----------------
#
tvals[0] = initial_time
slogs[0] = P0
slns[0] = P0
a1 = 1.0 + alpha * dt
b1 = beta * dt
g1 = gamma * dt
for i in range(1,nsteps+1):
    tvals[i] = tvals[i-1] + dt
    stmp = slns[i-1]
    sltmp = np.log(stmp)
    slns[i] = a1 * stmp - g1 * stmp * sltmp
    slogs[i] = a1 * stmp - b1 * stmp * stmp
#
# graphics
# --------
#
plt.figure(figsize=(5, 2.7))
plt.title("Logarithmic vs. Logistic Population")
plt.xlabel("Time")
plt.ylabel("Population Density")
plt.plot(tvals, slns, 'r', label='logarithmic model')
plt.plot(tvals, slogs, 'g', label='logistic curve')
plt.legend()
plt.show()