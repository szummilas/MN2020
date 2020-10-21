import matplotlib.pyplot as plt
import numpy as np


def funkcja():
    n = np.linspace(0, 100, 101)
    x = []
    x.append(0.1)

    for i in range(len(n)-1):
        x.append(3.5 * x[i] * (1 - x[i]))

    fig, ax = plt.subplots()
    ax.set(xlabel='x', ylabel='y', title='x(n+1) = 3.5 * x(n) * [1 - x(n)]')
    ax.grid()

    ax.plot(n, x, 'ko', markersize=4)
    plt.show()


funkcja()
