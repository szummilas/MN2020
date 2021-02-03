import numpy as np
from scipy.special import roots_legendre


def funkcja(x):
    y = (np.log(x) / (x**2 - 2 * x + 2))
    return y


a = 1
b = np.pi

# source: http://albert.kubzdela.pracownik.put.poznan.pl/p4-10.pdf
for w in [2, 4]:
    xi, wi, mu = roots_legendre(w, mu=True)
    r = 0
    for i in range(len(xi)):
        r += (b-a)/2 * funkcja((b+a)/2 + ((b-a)/2 * xi[i]))*wi[i]

    print("Dla {} wezlow = {}".format(w, r))

