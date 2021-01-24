import numpy as np
from scipy.integrate import quad


def funkcja(theta, theta0):
    return 1 / (np.sqrt(1 - np.sin(theta0/2)**2 * np.sin(theta)**2))


for n in [np.pi/12, np.pi/6, np.pi/4]:
    x = quad(funkcja, 0, np.pi/2, args=n)

    print(n * 180 / np.pi, "\t", x[0], "\t", (np.pi / 2.0) - x[0])