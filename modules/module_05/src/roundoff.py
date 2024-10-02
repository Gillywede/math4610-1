import numpy as np
one = 1
eps = 1
appone = one + eps
niter = 75
for i in range(niter):
    eps = eps / 2
    appone = one + eps
    error = np.abs(one-appone)
    if(error==0.0):
        break
    print(i, eps, error)

