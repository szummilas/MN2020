import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def funkcja(t, y):
    y = np.sin(t * y)
    return y


# dla y(0) = 2, 2.5, 3, 3.5 i 0 <= t <= 6
y0 = [2, 2.5, 3, 3.5]
t = [0, 6]

for x in y0:
    r = solve_ivp(funkcja, t, [x], atol=1e-12, rtol=1e-9)
    plt.plot(r.t, r.y[0], '-')
    plt.xlabel('t')
    plt.ylabel('y')

plt.show()
