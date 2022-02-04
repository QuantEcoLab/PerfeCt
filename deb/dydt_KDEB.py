import numpy as np
# from spline1 import spline1
from scipy.interpolate import interp1d


def dydt_KDEB(t, EVHR, aux, p, EVHR_):
    E = EVHR[0]  # J, reserve energy
    V = EVHR[1]  # cm^3, structural volume
    E_H = EVHR[2]  # J , cumulated energy inversted into maturity
    E_R = EVHR[3]  # J, reproduction buffer

    if E_H <= p["E_Hb"]:
        s_M = 1
    elif E_H > p["E_Hb"] and E_H < p["E_Hj"]:
        s_M = V**(1/3)/p["L_b"]
    else:
        s_M = p["s_M"]

    if "tT" in aux:
        # T = spline1(t, aux["tT"])
        Tf = interp1d(aux["tT"][:, 0], aux["tT"][:,1], kind="slinear")
        T = Tf(t)
    else:
        T = aux["T"] + 273.15
    # print(T, "TTTTTTTTTTTT")

    if "tf" in aux:
        # f = spline1(t, aux["tf"])
        ff = interp1d(aux["tf"][:, 0], aux["tf"][:,1], kind="slinear")
        f = ff(t)
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