import numpy as np


def v(t):
    u = 2510            # m/s
    m0 = 2.8 * 10**6    # kg
    m = 13.3 * 10**3    # kg/s
    g = 9.81            # m/s^2
    return u * np.log(m0/(m0 - m * t)) - g * t


for t in range(100):
    if v(t) >= 335:
        print(t)
        break