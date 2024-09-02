####################################################
# the following import is used to test the code
# ---------------------------------------------
#
import numpy as np
#
####################################################
####################################################
#
def svec(a,v):
    #
    # get the size of the vector to use
    # ---------------------------------
    #
    n = v.size
    #
    # set up storage for the product of the scalar
    # and in put vector
    # -----------------
    #
    output = np.zeros(n, dtype=float)
    #
    # compute the scalar multiple of each compnent
    # of the vector and the input scalar.
    # -----------------------------------
    #
    for i in range(n):
        output[i] = a * v[i]
    #
    # return the output vector computed above
    # ---------------------------------------
    #
    return output
#
####################################################
####################################################
#
# The code beyond this point is not needed for the
# application above.
#
####################################################
n = 11
u = np.full(n, 1.0, dtype=float)
v = np.zeros(n)
sign = -1.0
fac = 1.0
for i in range(n):
    fac = fac * sign
    v[i] = fac * u[i] / float(i+1)
alpha = -3.0
beta = 2.0
print(svec(alpha, u))
print(svec(beta, v))
####################################################