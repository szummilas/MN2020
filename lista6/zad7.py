import numpy as np
import scipy.integrate as sp


def funkcja(x):
    y = (np.cos(x) - np.exp(x)) / (np.sin(x))
    return y


# wykorzystuje scipy.quadrature do obliczen
i1 = sp.quadrature(funkcja, -1.0, 1.0e-11)
i2 = sp.quadrature(funkcja, 1.0e-11, 1.0)

i = i1[0] + i2[0]
i_error = i1[1] + i2[1]

print(i, " ", i_error)

