from deb.simulations import simulate_deb, aux, plot_res, allStat
import pandas as pd
import numpy as np
from pathlib import Path


def perfect_sim(data, species, mi_data , rcp):
    # data = pd.read_csv(data_file, index_col=0)

    ttm = []

    fcr = []

    for i in np.arange(0, len(data) - len(data) % 365-365*7, 365):
        # print(i)
        if rcp == "RCP4.5":
            inputs = np.vstack(
                (data.index.values+1, data["rcp4_5"].values+273.15)).T[i:i+365*7]

            res = simulate_deb(
                species, inputs, initial_size=mi_data["InitialSize"])

            TTM = np.where(res[0.85][2] >= mi_data["MarketWeight"])[0]
            fcr.append(res[0.85][-1][TTM[0]])

            ttm.append(TTM[0])

        elif rcp == "RCP8.5":

            inputs = np.vstack(
                (data.index.values+1, data["rcp8_5"].values+273.15)).T[i:i+365*7]

            res = simulate_deb(
                species, inputs, initial_size=mi_data["InitialSize"])
            # print(res[0.85][2])

            TTM = np.where(res[0.85][2] >= mi_data["MarketWeight"])[0]

            ttm.append(TTM[0])
            fcr.append(res[0.85][-1][TTM[0]])

    return ttm, fcr
