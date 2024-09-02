####################################################
# the following import is used to test the code
# ---------------------------------------------
#
import numpy as np
#
####################################################
####################################################
#
def vecmag(u):
    #
    # extract the number of components in the vector
    # to set the limits for the loop
    # ------------------------------
    #
    n = u.size
    #
    # create a temporary variable, sum, to tabulate
    # the results
    # -----------
    #
    sum = 0.0
    #
    # compute the sum of squares for the magnitude
    # --------------------------------------------
    #
    for i in range(n):
        sum = sum + u[i] * u[i]
    #
    # return the square root
    # ----------------------
    #
    return np.sqrt(sum)
#
####################################################
####################################################
#
# The code beyond this point is not needed for the
# application above.
#
####################################################
n = 197
u = np.full(n, 1.0, dtype=float)
print(vecmag(u))
####################################################