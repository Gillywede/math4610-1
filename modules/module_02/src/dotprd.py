####################################################
# the following import is used to test the code
# ---------------------------------------------
#
import numpy as np
#
####################################################
####################################################
#
def dotprd(u,v):
    #
    # extract the number of components in the vector
    # to set the limits for the loop
    # ------------------------------
    #
    n = v.size
    #
    # create a temporary variable, sum, to tabulate
    # the results
    # -----------
    #
    sum = 0.0
    for i in range(n):
        sum = sum + u[i] * v[i]
    return sum
#
####################################################
####################################################
#
# The code beyond this point is not needed for the
# application above.
#
####################################################
n = 100
u = np.full(n, 1.0, dtype=float)
print(dotprd(u,u))
v = np.zeros(n)
sign = -1.0
fac = 1.0
for i in range(n):
    fac = fac * sign
    v[i] = fac * u[i] / float(i+1)
print(dotprd(v,u))
####################################################