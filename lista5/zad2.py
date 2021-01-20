import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


def funkcja(x, y):
    spline = CubicSpline(x, y)

    y_x = np.arange(1.0, 3, 0.01)

    x_root = spline.roots()[1:-1]
    y_root = np.zeros(len(x_root))

    print('y\'(2.1) = ', spline(2.1, 1))
    print('Miejsca zerowe:', x_root)

    plt.plot(y_x, spline(y_x))
    plt.plot(x, y, 'oy')
    plt.plot(x_root, y_root, 'xk')
    plt.grid()
    plt.legend(['dane', 'spline_func_3'], loc='best')
    plt.show()


funkcja(np.array([1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3], dtype=float), np.array([-0.5403, -0.0104, 0.9423, 1.7445, 1.3073, -0.7718, -2.4986, -0.7903, 2.7334], dtype=float))

