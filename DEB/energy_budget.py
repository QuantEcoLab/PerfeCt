import numpy as np

from scipy.integrate import solve_ivp

from dydt_KDEB import dydt_KDEB


def energy_budget(aux, p):
    i = 0
    IC = aux["IC"]
    tArr = aux["tArr"]
    tmax = np.max(tArr)
    tc = tArr[0]
    rezTmp = []
    while tc < tmax-1:
        i += 1
        # print(tc, tmax)
        tnext = int(365*i)
        if tnext > tmax:
            tnext = tmax
        t = tArr[tnext-365: tnext]
        # time, EVHR
        # print(len(IC), IC)
        R = solve_ivp(
            dydt_KDEB,
            [t[0], t[-1]],
            IC,
            args=[aux, p, IC],
            method="RK45",
            t_eval=t)

        # print(R)

        time = R["t"].T
        time = time.reshape((time.shape[0], 1))
        EVHR = R["y"].T

        # print(time.shape, EVHR.shape)

        # print(EVHR)
        data = np.hstack((time, EVHR))
        rezTmp.append(data)
        E_Hc = EVHR[-1][2]
        if E_Hc >= p["E_Hp"]:
            EVHR[-1][3] = 0

        IC = EVHR[-1]
        tc = time[-1]+1
        # print(IC, "IC")

    rezTmp = np.concatenate(rezTmp)
    L = np.divide((rezTmp[:, 2]**(1/3)), p["del_M"])
    W = rezTmp[:, 2] * (1+aux["f"]*p["ome"])

    rez = [rezTmp[:, 0], L,  W]
    return rez
