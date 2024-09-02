####################################################
# the following import is used to test the code
# ---------------------------------------------
#
import numpy as np
#
####################################################
####################################################
#
def matmat(a, b):
    #
    # get the number of rows and columns
    # ----------------------------------
    #
    ma, na = a.shape
    mb, nb = b.shape
    if(na != mb):
        return None
    #
    # set up storage for the output that is dictated
    # by the size of the matrix and column vector
    # -------------------------------------------
    #
    output = np.zeros((ma,nb))
    #
    # loop over the rows in the output vector
    # ---------------------------------------
    for i in range(ma):
        for j in range(nb):
            sum = 0.0
            for k in range(mb):
                sum = sum + a[i][k] * b[k][j]
        output[i][j] = sum
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
amat = np.array([[1, 2, 3, 0, -1],
                 [4, 5, 6, 5, 3],
                 [7, 8, 9, 2, 3],
                 [10, 11, 12, -3, 6]])
bmat = np.array([[1, 2],
                 [4, 5],
                 [7, 8],
                 [9, 2],
                 [10, 11]])
#
vprd = matmat(amat, bmat)
print(vprd)
#
####################################################