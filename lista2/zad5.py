import numpy as np


def funkcja():
    i = 1
    for n in range(2, 21):
        i = np.e - ((n+1) * i)
        print("n({}) = ".format(n), i)


funkcja()