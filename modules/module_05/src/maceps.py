#
# python code to implement an algorithm for determining
# maceps on a computer
# --------------------
#
import numpy as np
#
# set storage
# -----------
#
xexact = 1.0
xprtrb = 1.0
#
# compute the approximate value
# -----------------------------
# 
xapprx = xexact + xprtrb
#
# compute the error
# -----------------
# 
error = np.abs(xapprx - xexact)
#
# loop over the approximations until there is no difference
# between the two numbers
# -----------------------
# 
icnt = 0
while error > 0.0:
    xprtrb = 0.5 * xprtrb
    xapprx = xexact + xprtrb
    error = np.abs(xexact-xapprx)
    icnt = icnt + 1
    print("icnt = ", icnt, "    error =", error)
