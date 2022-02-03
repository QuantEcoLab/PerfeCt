import numpy as np

from scipy.integrate import solve_ivp


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
        print(len(IC), IC)
        R = solve_ivp(
            dydt_KDEB,
            [t[0], t[-1]],
            IC,
            args=[aux, p, IC],
            )

        print(R)

        time = R["t"].T
        EVHR = R["y"].T
        # print(EVHR)
        rezTmp.append([time, EVHR])
        E_Hc = EVHR[-1][2]
        if E_Hc >= p["E_Hp"]:
            EVHR[-1][3] = 0

        IC = EVHR[-1]
        tc = time[-1]+1
        print(IC, "IC")

    rezTmp = np.asarray(rezTmp)
    L = np.divide((rezTmp[:,2]**(1/3)),p["del_M"])
    W = rezTmp[:, 2] * (1+aux["f"]*p["ome"])
    rez = np.array(rezTmp[:,1], L, W)


def dydt_KDEB(t, EVHR, aux, p, EVHR_):
    # print(t, "TTTTTTTTTT")
    E  = EVHR[0] # J, reserve energy
    V  = EVHR[1] # cm^3, structural volume
    E_H  = EVHR[2] # J , cumulated energy inversted into maturity 
    E_R  = EVHR[3] # J, reproduction buffer

    if E_H <= p["E_Hb"]:
        s_M = 1
    elif E_H> p["E_Hb"] and E_H < p["E_Hj"]:
        s_M = V**(1/3)/p["L_b"]
    else:
        s_M = p["s_M"]

    if "tT" in aux:
        T = spline1(t, aux["tT"])
    else:
        T = aux["T"] + 273.15

    if "tf" in aux:
        f = spline1(t, aux["tf"])
    else:
        f = aux["f"]

    
    # print(p["T_A"], T)
    c_T = np.exp(p["T_A"]/p["T_ref"] - p["T_A"]/T)

    p_AmT = c_T * p["p_Am"] * s_M
    v_T = c_T * p["v"] * s_M
    p_MT = c_T * p["p_M"]
    p_TT = c_T * p["p_T"]
    k_JT = c_T * p["k_J"]
    p_XmT = p_AmT / p["kap_X"]

    if E_H < p["E_Hb"]:
        pX = 0 # embryo stage -> f=0
    else:
        pX = f * p_XmT * V**(2/3)

    pA = p["kap_X"] * pX
    pM = p_MT * V
    pT = p_TT * V**(2/3)
    pS = pM + pT
    # eq. 2.12 p.37 Kooijman 2010
    pC = (E/V) * (p["E_G"] * v_T * V**(2/3) + pS ) / (p["kap"] * E/V + p["E_G"]) 
    pJ = k_JT * E_H

    if pA < (p["kap"]*pC) and (p["kap"] * pC) <pS and E<pS:
        output = [-E, 0, 0, 0]
        return output
    else:

        dE = pA-pC
        dV = np.max((0, (p["kap"]*pC -pS)/p["E_G"]))
        if E_H < p["E_Hp"]:
            dH = np.max((0, (1-p["kap"])* pC-pJ))
            dR = 0
        else:
            dH = 0
            dR = np.max((0, (1-p["kap"])*pC - pJ))

        output = [dE, dV, dH, dR]

        return output


def spline1(x, knots, Dy1=None, Dyk=None):

    x = np.asarray([x])
    # print("x:", x, x.shape)
    nx = x.shape[0]
    nk = knots.shape[0]
    y = np.zeros((nx,1))
    dy = y
    # print(len(y))
    index = np.zeros((nx, 1))

    if Dy1 == None:
        Dy1 = 0
    if Dyk == None:
        Dyk = 0

    Dy = np.divide(
        (knots[1:nk, 1]-knots[0:nk-1, 1]),
        (knots[1:nk, 0]-knots[0:nk-1, 0])
        )
    Dy = np.concatenate((Dy, np.array([0])))
    # print(Dy.shape, "Dy")

    for i in range(1,nx+1):
        j = 0
        while x[i-1] > knots[np.min((nk,j)), 0] and j<= nk:
            j += 1
        j-=1
        if j == 0:
            y[i-1] = knots[0, 1] - Dy1 * (knots[0, 0]- x[i-1])
            dy[i-1] = Dy1
        else:
            # print(knots.shape, Dy.shape, x.shape)
            y[i-1] = knots[j, 1] - Dy[j] * (knots[j, 0] - x[i-1])
            dy[i-1] = Dy[j]

        index[i-1] = j
    
    return y #, dy, index