# f(x) = cosx - 3sin(tgx-1)

import matplotlib.pyplot as plt
import numpy as np


def funkcja():
    x = np.arange(0.0, 1.5, 0.001)
    y = np.cos(x) - (3 * np.sin(np.tan(x)-1))
    y2 = x * 0

    fig, ax = plt.subplots()
    ax.plot(x, y2, 'r')
    ax.plot(x, y)

    ax.set(xlabel='x', ylabel='y', title='f(x) = cosx - 3sin(tgx-1)')
    ax.grid()

    x2 = [0.877, 1.327, 1.432, 1.479, 1.501]

    for i in range(len(x2)):
        ax.plot(x2[i], 0, 'ko')

    plt.show()


funkcja()




