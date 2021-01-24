#  f(x) = ln ( tanh( x/(x^2 + 1) ) )
import numpy as np
from scipy.misc import derivative


def funkcja(x):
    return np.log(np.tanh(x/((x**2) + 1)))


# func / x0 / spacing / order
dx1 = derivative(funkcja, 0.2, 0.00001, 1)
dx2 = derivative(funkcja, 0.2, 0.00001, 2)
dx3 = derivative(funkcja, 0.2, 0.00001, 3, order=5)


print("Pierwsza pochodna dla x = 0.2 wynosi: {} \nDruga pochodna dla x = 0.2 wynosi: {} \nTrzecia pochodna dla x = 0.2 wynosi: {}".format(dx1, dx2, dx3))
#  f(0.2) = -1.66088
#  f'(0.2) = 4.50353
#  f''(0.2) = -27.1412
#  f'''(0.2) = 254.61