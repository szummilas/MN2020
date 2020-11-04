import numpy as np


def funkcja():
    a = np.array([[0, 0, 2, 1, 2], [0, 1, 0, 2, -1], [1, 2, 0, -2 , 0], [0, 0, 0, -1, 1], [0, 1, -1, 1, -1]])
    b = np.array([1, 1, -4, -2, -1])
    x = np.linalg.solve(a, b)
    print("wynik: {}".format(x))
    spr = np.allclose(np.dot(a, x), b)
    print("sprawdzenie: {}".format(spr))


funkcja()