from scipy.optimize import newton
import numpy as np

f = lambda x, a: x**5 - a
df = lambda x, a: 5*x**4
a = np.arange(0, 10)
x = np.random.randn(10)
print(newton(f, x, fprime=df, args=(a,)))
