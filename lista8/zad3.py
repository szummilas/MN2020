import numpy as np
from scipy.linalg import eigh_tridiagonal

# n = 10
d1 = 2 * np.ones(10)
e1 = -1 * np.ones(9)
value1, vector1 = eigh_tridiagonal(d1, e1)

# n = 100
d2 = 2 * np.ones(100)
e2 = -1 * np.ones(99)
value2, vector2 = eigh_tridiagonal(d2, e2)


print("Wartości własne dla n = 10 : {}".format(vector1[: 3]))
print("Wektory własne dla n = 10 : {}".format(value1[: 3]))
print("Wartości własne dla n = 100 : {}".format(vector2[: 3]))
print("Wektory własne dla n = 100 : {}".format(value2[: 3]))
