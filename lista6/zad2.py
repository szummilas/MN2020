import numpy as np
from scipy.interpolate import lagrange


def funkcja(n):
    x = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
    y = np.array([0.0, 0.078348, 0.13891, 0.192916, 0.244981])

    z = lagrange(x, y)
    p = np.polyder(z)

    return p(n)


print("f'(0.2) = {}".format(funkcja(0.2)))