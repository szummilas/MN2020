from scipy import optimize
import numpy as np
import math

h = 2       #wysokość
d = 10      #odległość od kosza
l = 3       #wysokość kosza
g = 9.81    #przyspieszenie ziemskie
ang = 45    #kąt


def func(x):
    v0, kat = x
    t = 10 / (v0 * np.cos(kat))
    f1 = v0 * np.sin(kat) * t - ((g * t**2)/2) - 1
    f2 = v0 * (np.sin(kat) + np.cos(kat)) - (g*t)
    return[f1, f2]


result = optimize.fsolve(func, [10.4, math.radians(50)])
print("V0: {} m/s".format(result[0]))
print("kat: {} stopni".format(math.degrees(result[1])))
