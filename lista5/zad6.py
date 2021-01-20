import matplotlib.pyplot as plt
import numpy as np


def funkcja(x, y):
    f1 = np.polyfit(x, y, 2)
    poly1 = np.poly1d(f1)

    x1 = np.arange(0.0, 10.5, 0.01)

    plt.plot(x1, poly1(x1))
    plt.plot(x, y, 'oy')
    plt.plot(10.5, poly1(10.5), 'ok')
    plt.show()

    print("wynik = ", poly1(10.5))


funkcja(np.array([0, 1.525, 3.05, 4.575, 6.1, 7.625, 9.150]),
        np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741]))