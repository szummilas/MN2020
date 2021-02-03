import numpy as np
import scipy.linalg as sp

A = np.array([[-1, -4, 1], [-1, -2, -5], [5, 4, 3]])
value, vector = sp.eig(A)

print("Wartości własne: {}", value)
print("Wektory własne: {}", vector)
