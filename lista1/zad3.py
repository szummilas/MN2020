import numpy as np
import scipy as sp


def funkcja():
    A = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
    B = np.array([[4, 2, 0], [2, 5, 2], [0, 2, 4]])
    w = np.array([[1], [-2], [3]])

    AB = A.dot(B)
    Bw = B.dot(w)
    Aw = A.dot(w)
    BAw = B.dot(Aw)

    print(AB)
    print(Bw)
    print(BAw)


funkcja()