import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# rownanie
def f(x, y):
    dydx = 2 * x - y**2 - 1
    return dydx


# funkcja potrzebna do znaleznienia miejsc zerowych
def event_to_track(x, y):
    return y


# warunek poczatkowy
y0 = [0.2]

# przedzial
T = np.linspace(0, 4, 1000)

# rozwiazanie
m = solve_ivp(f, (0, 4), y0=y0, method='RK45', events=event_to_track, t_eval=T)

print("Pierwiastki tego rownania znajduja sie w punktach x = {}".format(m.t_events[0]))

# wykres
plt.plot(m.t, m.y[0], '-', label="y(x)")

# zaznaczenie pierwiastkow na wykresie
plt.plot(m.t_events[0], m.y_events[0], 'ko')

plt.grid()
plt.suptitle("Wykres funkcji y' - 2x + y^2 + 1 = 0")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
