import copy


def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1

    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det

        for j in range(i + 1, n):
            t = a[j][i] / a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t * a[i][k]
            for k in range(p):
                b[j][k] -= t * b[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t * b[j][k]
        t = 1 / a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t

    return b


# ZADANIE 1
A1 = [[-1, 1, -4], [2, 2, 0], [3, 3, 2]]
B1 = [[0], [1], [0.5]]

# ZADANIE 2
L2 = [[1, 0, 0], [3/2, 1, 0], [1/2, 11/13, 1]]
U2 = [[2, -3, -1], [0, 13/2, -7/2], [0, 0, 32/13]]
B2 = [[1], [-1], [2]]

# ZADANIE 3
A3 = [[0, 0, 2, 1, 2], [0, 1, 0, 2, -1], [1, 2, 0, -2, 0], [0, 0, 0, -1, 1], [0, 1, -1, 1, -1]]
B3 = [[1], [1], [-4], [-2], [-1]]


zad1 = gauss(A1, B1)
y = gauss(L2, B2)
zad2 = gauss(U2, y)
zad3 = gauss(A3, B3)
print("Zadanie 1 = " + str(zad1))
print("Zadanie 2 = " + str(zad2))
print("Zadanie 3 = " + str(zad3))
