import numpy as np

eps = float(1.0)
one = float(1.0)
appone = float(one + eps)

error = float(np.abs(appone - one))

for i in range(1,40):
    print(i, error)
    eps = float(eps) / 10.
    appone = one + eps
    error = float(np.abs(appone - one))
    if error == 0.0:
        break
