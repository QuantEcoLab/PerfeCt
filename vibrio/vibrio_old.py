import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


Tref = 293.15  # Referentna temp
TA = 8000  # Arrhenius temp
N0 = 1  # Inicialna konc.
r = 0.1  # Brzina rasta (log CFU/mL/h)
K = 4  # Carrying capacity (log CFU/mL)

T = 313.15  # dnevna temperatura



def dNdt(t, N, T):

    return (r * N * (1 - (N / K)) * np.exp(TA/Tref - TA/T))


def simulate_vibrio(temp):
    t_eval = np.arange(1, 24, 1/128)
    N = solve_ivp(dNdt,  [1, 24], [N0], args=[temp], t_eval=t_eval)
    return t_eval, N["y"][0]


if __name__ == "__main__":
    for i in [293.15, 298.15, 303.15, 308.15, 313.15]:
        t, y = simulate_vibrio(i)

        plt.plot(t, y)
