#
# import a couple of standard packages in python
# ----------------------------------------------
#
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#
# number of interior nodes in each direction
# ------------------------------------------
#
xleft = 0.0
xright = 1.0
#
# numerical mesh values
# ---------------------
#
nx = 8
nxp1 = nx + 1
nxp2 = nx + 2
dx = ( xright - xleft ) / nxp1
dt = 0.001
#
# physical parameters
# -------------------
#
kappa = 1.0
#
# storage for the approximate solution
# ------------------------------------
#
x = np.full(nxp2, 0.0, dtype=float)
uinit = np.full(nxp2, 0.0, dtype=float)
uold = np.full(nxp2, 0.0, dtype=float)
unew = np.full(nxp2, 0.0, dtype=float)
#
# initialize the mesh values for the storage of
# the solution arrays
# -------------------
#
x[0] = xleft
uinit[0] = 0.0
uold[0] = uinit[0]
unew[0] = uold[0]
for i in range(1,nxp1):
    x[i] = x[i-1] + dx
    uinit[i] = np.sin(2*np.pi*x[i])
    uold[i] = uinit[i]
    unew[i] = uold[i]
x[nxp1] = xright
uinit[nxp1] = 0.0
uold[nxp1] = uinit[nxp1]
unew[nxp1] = uold[nxp1]
#
# parameter
# ---------
#
rval = ( kappa * dt ) / ( dx * dx )
#
# setup the graphics
# ------------------
#
fig, ax = plt.subplots()
#
# plot the initial condition
# --------------------------
#
line0 = ax.plot(x, uinit, label=f'initial condition')[0]
line1 = ax.plot(x, uold, label=f'approx solution')[0]
ax.set(xlim=[0, 1], ylim=[-1, 1], xlabel='Length', ylabel='Temp')
ax.legend()
#
# the update function
# -------------------
#
def update(frame):
    # update the line plot:
    for i in range(1, nxp1):
        unew[i] = uold[i] + rval * ( uold[i-1] - 2.0 * uold[i] + uold[i+1])
    for i in range(nxp2):
        uold[i] = unew[i]
    line1.set_ydata(unew)
    return (line1)
#ani.save(filename="/tmp/pillow_example.apng", writer="pillow")
ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
ani.save(filename="./heat.gif", writer="pillow")
plt.show()