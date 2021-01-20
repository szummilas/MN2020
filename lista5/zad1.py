import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange


def funkcja(h, p):
    pH = lagrange(h, p)
    yX = np.arange(0.0, 6.5, 0.01)

    plt.plot(h, p, 'o')
    plt.plot(yX, pH(yX))
    plt.show()


funkcja(np.array([0, 3, 6], dtype=float), np.array([1.225, 0.905, 0.652], dtype=float))