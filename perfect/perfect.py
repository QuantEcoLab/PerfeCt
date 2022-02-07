from deb.simulations import simulate_deb, aux, plot_res, allStat
import pandas as pd
import numpy as np
from pathlib import Path


def perfect_sim(data_file, species, mi_data):
    data = pd.read_csv(data_file, index_col=0)

    ttm45 = []
    ttm85 = []

    fcr45 = []
    fcr85 = []

    for i in np.arange(0, len(data) - len(data) % 365-365, 365):
        inputs45 = np.vstack(
            (data.index.values+1, data["rcp4_5"].values+273.15)).T[i:i+365*5]

        res45 = simulate_deb(
            species, inputs45, initial_size=mi_data["InitialSize"])

        TTM45 = np.where(res45[0.85][2] >= mi_data["MarketWeight"])[0]

        fcr45.append(res45[0.85][-1][TTM45[0]])

        ttm45.append(TTM45[0])

        inputs85 = np.vstack(
            (data.index.values+1, data["rcp4_5"].values+273.15)).T[i:i+365*5]

        res85 = simulate_deb(
            species, inputs85, initial_size=mi_data["InitialSize"])
        # print(res45[0.85][2])

        TTM85 = np.where(res85[0.85][2] >= mi_data["MarketWeight"])[0]

        ttm85.append(TTM85[0])
        fcr85.append(res85[0.85][-1][TTM85[0]])

    return ttm45, ttm85, fcr45, fcr85