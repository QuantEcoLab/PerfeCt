import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

from .energy_budget import energy_budget


allStat = loadmat(
    "data/"+"allStat.mat", simplify_cells=True)["allStat"]


species_names = [
    'Sparus_aurata',
    'Dicentrarchus_labrax',
    'Scophthalmus_maximus'
]
file_names = ["Temp_Vrgada.csv", "Temp_Ston.csv"]

fArr = np.array([0.85])

aux = {}


def simulate_deb(
        species,
        location,
        fArr=np.array([0.85]),
        initial_size=5,
        allStat=allStat):

    """
    inputs:
        species: species name for selection in allstat database
        location: path to .csv file containgn data from location
        fArr: food availiability array (n number of availabities)
        initial_size: initial body size
        allStat: allStat database

    returns:
        f_rez: dictionary containing DEB simulations for ever fArr
    """

    tT = location
    # tT = pd.read_csv("data/"+Envfname, usecols=(0, 2)).values
    # tT = location
    # print(tT)
    # print(type(tT))

    f_rez = {}
    species = species

    for f in fArr:
        aux["tT"] = tT
        # f = feeding
        aux["f"] = f
        tArr = aux["tT"][:, 0]
        aux["tArr"] = tArr
        aux["init_L"] = initial_size

        p = allStat[species]

        aux["IC"] = [
            (p["E_m"]*(aux["init_L"]*p["del_M"])**3)/2,
            (aux["init_L"]*p["del_M"])**3,
            np.min(
                (
                    p["E_Hp"],
                    p["E_Hp"]*((aux["init_L"]*p["del_M"])/p["L_p"]))
                ),
            0,
            0]

        rez = energy_budget(aux, p)
        f_rez[f] = rez
    return f_rez


def plot_res(f_rez, species, location, aux, save=False):

    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    fig.suptitle(
        f"{species} - {location}".replace(
            "_", " ").replace(
                ".csv", "").replace("Temp ", ""))
    axs_0t = axs[0].twinx()
    axs_1t = axs[1].twinx()

    axs_0t.set_title("Length")
    axs_1t.set_title("Weight")

    k0 = 273.15
    legend_labels = []

    for f in fArr:
        legend_labels.append(f)

        axs[0].plot(f_rez[f][1])
        axs[0].set_ylabel("Length [cm]")
        axs[1].plot(f_rez[f][2])
        axs[1].set_ylabel("Weight [g]")
        # axs[1].plot(f_rez[f][3])
        # axs[1].set_ylabel("FCR")

    axs_0t.plot(aux["tT"][:, 1]-k0, "--")
    axs_0t.set_ylabel("Temp [°C]")
    axs_1t.plot(aux["tT"][:, 1]-k0, "--")
    axs_1t.set_ylabel("Temp [°C]")

    axs[0].legend(legend_labels, title="Food availability")
    axs[1].legend(legend_labels, title="Food availability")
    fig.tight_layout()
    if save:
        loc_string = location.replace("Temp_", "").replace(".csv", "")
        plt.savefig(f'{species}_{loc_string}.png')
    else:
        plt.show()


if __name__ == "__main__":
    for i in species_names:
        for j in file_names:
            f_rez = simulate_deb(i, j)

            plot_res(f_rez, i, j, aux, save=False)
            print(i, j)
