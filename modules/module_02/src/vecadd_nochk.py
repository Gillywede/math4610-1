####################################################
# the following import is used to test the code
# ---------------------------------------------
#
import numpy as np
#
####################################################
####################################################
#
def vecadd(u,v):
    #
    # determine the number of components baseed on
    # the length of the first vector
    # ------------------------------
    #
    n = u.size
    #
    # instantiate a vector for the vector that
    # results from the addition of the vectors.
    # -----------------------------------------
    #
    output = np.zeros(n, dtype=float)
    #
    # loop over the number of components and sum
    # the components of the two input vectors
    # ---------------------------------------
    #
    for i in range(n):
        output[i] = u[i] + v[i]
    #
    # return the vector that is the result of
    # the componentwise addition
    # --------------------------
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
#
u = np.zeros(10)
v = np.zeros(10)
w = vecadd(u,v)
print(w)
u = np.zeros(4)
# note that this next test only treats the first four
# entries.
w = vecadd(u,v)
print(w)
# the following does not work - why?
####################################################