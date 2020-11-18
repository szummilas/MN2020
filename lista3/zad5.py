import numpy as np
from scipy.linalg import hilbert

def funkcja(n):
    h = hilbert(n)

    norm = np.linalg.norm(h)
    cond = np.linalg.cond(h)

    print("Dla macierzy Hilberta " + str(n) + "x" + str(n))
    print("Norma " + " = " + str(norm))
    print("Wskaznik uwarunkowania " + " = " + str(cond))

print("\n")
funkcja(5)
print("\n")
funkcja(10)
print("\n")
funkcja(15)