from scipy.linalg import eigh
from scipy.linalg import hilbert

A = hilbert(6)
value, vector = eigh(A)

print("Wartości własne: {}".format(value))
print("Wektory własne: {}".format(vector))
