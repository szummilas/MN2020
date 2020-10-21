import numpy as np


def funkcja(n):
    x = []
    x = np.array([[1 / (i + k + 1) for k in range(n)] for i in range(n)])

    print("MACIERZ DLA {}:".format(n))
    print(x)

    print("MACIERZ ODWROTNA DLA {}:".format(n))
    y = np.linalg.inv(x)

    print(y)

def funkcja2(n):
    return np.array([[1 / (i + k + 1) for k in range(n)] for i in range(n)])


funkcja(4)
funkcja(8)


print("SPRAWDZENIE WYZNACZNIKA TEJ MACIERZY DLA N OD 5 DO 20:")
for n in range(5, 21):
    print(np.linalg.det(funkcja2(n)))