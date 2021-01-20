import matplotlib.pyplot as plt
import numpy as np


def funkcja(x, y):
    f1 = np.polyfit(x, y, 1)
    poly1 = np.poly1d(f1)

    f2 = np.polyfit(x, y, 2)
    poly2 = np.poly1d(f2)

    x1 = np.arange(1.0, 4, 0.01)

    plt.plot(x1, poly1(x1))
    plt.plot(x1, poly2(x1))
    plt.plot(x, y, 'ok')
    plt.show()


funkcja(np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7]),
        np.array([6.008, 15.722, 27.13, 33.772, 5.257, 9.549, 11.098, 28.828]))