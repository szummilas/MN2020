import numpy as np
from scipy.integrate import simps


def funkcja(x):
    return np.cos(2 * np.cos(x)**-1)


def simpson():
    for n in [3, 5, 7]:
        x = np.linspace(-1, 1, n)
        y = []

        for z in x:
            y.append(funkcja(z))

        s = simps(y, x)
        print(s)


print("Dla większej liczby węzłów otrzymujemy dokładniejsze wyniki")
simpson()