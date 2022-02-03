import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

from energy_budget import energy_budget


allStat = loadmat(
    "../scripts_matlab/"+"allStat.mat", simplify_cells = True)["allStat"]

aux = {}

species_names = [
    'Sparus_aurata',
    'Dicentrarchus_labrax',
    'Scophthalmus_maximus'
]
initial_sizes  = [5, 5, 5]
file_names = ["Temp_Vrgada.csv", "Temp_Ston.csv"]

fArr = np.array([0.5,0.25,1])

# single species single environment
i, j, k = 0, 2 ,0
Envfname = file_names[i] # vrgada
tT = pd.read_csv("../scripts_matlab/"+Envfname, usecols=(0,2)).values
aux["tT"] = tT

species = species_names[j]
f = fArr[k]
aux["f"] = f
tArr = aux["tT"][:,0]
aux["tArr"] = tArr
aux["init_L"] = initial_sizes[j]

p = allStat[species]

aux["IC"] = [
    (p["E_m"]*(aux["init_L"]*p["del_M"])**3)/2,
    (aux["init_L"]*p["del_M"])**3,
    np.min(
        (p["E_Hp"], p["E_Hp"]*((aux["init_L"]*p["del_M"])/p["L_p"]))
        ),
    0]

energy_budget(aux, p)
