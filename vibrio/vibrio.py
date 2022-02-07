from operator import index
import numpy as np
import pandas as pd
from pyrsistent import v
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


data = pd.read_csv("../data/timeseries_past_future/farm_638_past_future.csv")

N_365_221 = data["temp_2021"].values
N_45 = data["temp_2030_rcp45"].values
N_85 = data["temp_2030_rcp85"].values

# dN/dt = r * N * (1 - ( N / K) ) * exp(TA/Tref - TA/T)
# *********************************************************************
# PARAMETRI PROMJENE BRZINE RASTA
# *********************************************************************
Tref = 293.15  # Referentna temp
TA = 8000  # Arrhenius temp
# N0 = 1  # Inicialna konc.
r = 0.1  # Brzina rasta (log CFU/mL/h)
K = 4  # Carrying capacity (log CFU/mL)
T = 313.15  # dnevna temperatura

# varijabilni K
b_f = 40  # slope
c_f = 1  # minimum
d_f = 4  # maksimum
e_f = 18  # temperatura infleksije


def dNdt(t, N, T, Kr):
    return (r * N * (1 - (N / Kr)) * np.exp(TA/Tref - TA/T))


def getKr(T):
    Kr = (
        1-(
            (c_f+(d_f-c_f)/(
                1+np.exp(
                    b_f*(
                        np.log10(T-273.15)-np.log10(e_f)))))))+4
    if Kr < 1:
        Kr = 1
    return Kr


def calc(T, N0):
    Kr = getKr(T)
    t_eval = np.arange(1, 24, 1/128)
    N = solve_ivp(dNdt, [1, 24], [N0], args=[T, Kr], t_eval=t_eval)
    return N["y"][0][-1]


def simulate_scenario(temps):
    res = np.zeros(len(temps))
    for dan in range(365):
        T = temps[dan]+273.15
        if dan == 0:
            N0 = 1
        else:
            N0 = res[dan-1]
        dayN = calc(T, N0)

        res[dan] = N0 + (dayN - N0)
    return res


def get_DRV(simulation):
    return len(simulation[simulation>2])


def calc_DRV(location):
    # find path to location
    refpath = location  # dummy line
    path = location

    ref_data = pd.read_csv(refpath, index_col=0)
    rcp_data = pd.read_csv(path, index_col=0)

    # change data to reference year 2021 when data becomes available
    ref_365 = ref_data["rcp4_5"].values[:365]
    rcp_45 = ref_data["rcp4_5"].values
    rcp_85 = ref_data["rcp8_5"].values

    year_idx = np.arange(0, len(rcp_data), 365)

    ref_sim = simulate_scenario(ref_365)
    
    vibrio_days_rcp45 = [get_DRV(ref_sim)]
    vibrio_days_rcp85 = [get_DRV(ref_sim)]

    for i in year_idx[:-1]:
        # print(i)
        rcp_45_sim = simulate_scenario(rcp_45[i: i+365])
        rcp_85_sim = simulate_scenario(rcp_85[i: i+365])

        vibrio_days_rcp45.append(get_DRV(rcp_45_sim))
        vibrio_days_rcp85.append(get_DRV(rcp_85_sim))

    return (vibrio_days_rcp45, vibrio_days_rcp85)


r00 = simulate_scenario(N_365_221)
r45 = simulate_scenario(N_45)
r85 = simulate_scenario(N_85)

print(get_DRV(r00))
print(get_DRV(r45))
print(get_DRV(r85))


plt.plot(r00)
plt.plot(r45)
plt.axhline(2, color="r", linestyle="--")
plt.show()

plt.plot(r00)
plt.plot(r85)
plt.axhline(2, color="r", linestyle="--")
plt.show()

rcp45, rcp85 = calc_DRV("../data/time_series/id_638.csv")

colors = []
for i in rcp45:
    if i > rcp45[0]:
        colors.append("red")
    else:
        colors.append("green")

fig, ax = plt.subplots()
# ax.plot(np.arange(2021, 2021+len(rcp45), 1), rcp45, color=colors)
# ax.plot(np.arange(2021, 2021+len(rcp45), 1), rcp45, "*-")
ax.stem(rcp45, bottom=rcp45[0])
ax.set_xlabel("Years")
ax.set_ylabel("Days with high risk of vibriosis")