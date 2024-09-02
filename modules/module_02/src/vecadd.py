####################################################
# the following import is used to test the code
# ---------------------------------------------
#
import numpy as np
#
####################################################
####################################################
#
#
# vector addition function
#
# input
#
# u, v - the vectors to add together
#      - these are two numpy arrays
# n - the number of components to add
#
import numpy as np
#
#
# vector addition function
#
# input
#
# u, v - the vectors to add together
#      - these are two numpy arrays
# n - the number of components to add
#
import numpy as np
#
def vecadd(u, v):
    #
    # get the length of the first argument
    # ------------------------------------
    #
    n = u.size
    ntmp = v.size
    if (ntmp-n) != 0:
        return None        
    #
    # initialize temporary storage for the computation
    output = np.zeros(n, dtype=float)
    for i in range(n):
        output[i] = u[i] + v[i]
    return output

def vecadd(u, v):
    #
    # get the length of the first argument
    # ------------------------------------
    #
    n = u.size
    ntmp = v.size
    if (ntmp-n) != 0:
        return None        
    #
    # initialize temporary storage for the computation
    output = np.zeros(n, dtype=float)
    for i in range(n):
        output[i] = u[i] + v[i]
    return output
#
####################################################
####################################################
#
# The code beyond this point is not needed for the
# application above.
#
####################################################
u = np.zeros(10)
v = np.zeros(10)
w = vecadd(u,v)
print(w)
u = np.zeros(4)
w = vecadd(u,v)
print(w)
####################################################
