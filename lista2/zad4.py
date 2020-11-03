import numpy as np


def funkcja1():
    for n in range(2, 21, 2):
        x = pow(2, -n)
        y = np.sqrt(pow(x, 4) + 4) - 2
        print("n({}) = ".format(n), y)


def funkcja2():
    for n in range(2, 21, 2):
        x = pow(2, -n)
        y = pow(x, 4) / (np.sqrt(pow(x, 4) + 4) + 2)
        print("n({}) = ".format(n), y)


print("Oryginalne wyrażenie: ")
funkcja1()
print("Przekształcone wyrażenie: ")
funkcja2()

print("Wyrażenie oryginalne przestaje dawać wynik już dla iteracji n = 14")