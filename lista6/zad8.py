import numpy as np
from scipy.integrate import dblquad


def funkcja(y, x):
    y = np.sin(np.pi * x) * np.sin(np.pi * (y - x))
    return y


r = dblquad(funkcja, 0, 1, lambda x:0, lambda x:x)
print("Wynik: {}".format(r))