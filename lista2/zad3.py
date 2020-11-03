import numpy as np


def funkcja1():
    for n in range(2, 25, 2):
        x = pow(2, -n)
        y = np.sqrt(pow(x, 2) + 1) - 1
        print("n({}) = ".format(n), y)


def funkcja2():
    for n in range(2, 25, 2):
        x = pow(2, -n)
        y = (pow(x, 2)) / (np.sqrt(pow(x, 2) + 1) + 1)
        print("n({}) = ".format(n), y)


print("Rozwiązania pierwszego wyrażenia: ")
funkcja1()
print("Rozwiązania drugiego wyrażenia: ")
funkcja2()

print("Wyrażenie nr. 2 jest moim zdaniem dokładniejsze")



