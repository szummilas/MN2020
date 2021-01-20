import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange


def funkcja(x, y, x1, x2):
    data = lagrange(np.log(x), np.log(y))

    y1 = np.exp(data(np.log(x1)))

    y2 = np.exp(data(np.log(x2)))

    plt.plot(x, y, 'oy')
    plt.plot(x1, y1, 'ok')
    plt.plot(x2, y2)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


funkcja(np.array([0.2, 2, 20, 200, 2000, 20000]),
        np.array([103, 13.9, 2.72, 0.8, 0.401, 0.433]),
        np.array([5, 50, 5000]),
        np.arange(0.2, 20000, 1))