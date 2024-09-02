####################################################
# the following import is used to test the code
# ---------------------------------------------
#
import numpy as np
#
####################################################
####################################################
#
def matvec(a, v):
    #
    # get the number of rows and columns
    # ----------------------------------
    #
    m, n = a.shape
    #
    # set up storage for the output that is dictated
    # by the size of the matrix and column vector
    # -------------------------------------------
    #
    output = np.zeros(m)
    #
    # loop over the rows in the output vector
    # ---------------------------------------
    for i in range(m):
        #
        # initialize the dot product sum
        # ------------------------------
        #
        sum = 0.0
        #
        # loop over the columns that represent the
        # dot product row i with the input column
        # vector
        # ------
        #
        for j in range(n):
            sum = sum + a[i][j] * v[j]
        #
        # store the computed dot product in row i
        # of the outut
        # ------------
        #
        output[i] = sum
    #
    # return the output vector for the matrix-vector
    # product
    # -------
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
amat = np.array([[1, 2, 3, 0, -1],
                 [4, 5, 6, 5, 3],
                 [7, 8, 9, 2, 3],
                 [10, 11, 12, -3, 6]])
#
# the following line will be deprecated in the future
# ---------------------------------------------------
#
vtest = np.array([[0.0], [1.0], [2.0], [3.0], [4.0]])
print(vtest)
#
vout = matvec(amat, vtest)
print(vout)
#
####################################################