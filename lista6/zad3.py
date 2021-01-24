import numpy as np
from scipy.interpolate import lagrange


def funkcja(u, n):
    x = np.array([-2.2, -0.3, 0.8, 1.9])
    y = np.array([-15.18, 10.962, 1.92, -2.04])

    z = lagrange(x, y)
    p = np.polyder(z, n)

    return p(u)


print("f'(0) = {} \nf''(0) = {}".format(funkcja(0.0, 1), funkcja(0.0, 2)))
