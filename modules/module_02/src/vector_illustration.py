# 
# this code was written to produce graphics for the
# module
#
import numpy as np
import matplotlib.pyplot as plt
#
# display some vectors
# --------------------
#
def vector_components(a, t):
    v1 = a * np.cos(t)
    v2 = a * np.sin(t)

soa = np.array([[0, 0, 3, 2],
                [0, 0, 1, 1],
                [0, 0, 9, 9]])
X, Y, U, V = zip(*soa)
plt.figure()
ax = plt.gca()
ax.quiver(X,Y,U,V,
           angles='xy',
           scale_units='xy',
           scale=1)
ax.set_xlim([-1,10])
ax.set_ylim([-1,10])
plt.draw()
plt.show()