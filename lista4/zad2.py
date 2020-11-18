from scipy.optimize import newton
import numpy as np


def f(a):
    f = lambda x, a: x**5 - a
    df = lambda x, a: 5 * x**4
    x = np.random.randn(1)
    print(newton(f, x, fprime=df, args=(a,)))


f(4)
f(10)
f(21)
