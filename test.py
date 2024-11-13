from perfect.perfect import perfect_sim
import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/time_series/future/id_001.csv")
species_db = pd.read_csv("data/deb_species_list.csv", index_col=0)

species_mi = {}
for i in species_db.iloc:
    if not np.isnan(i["MarketWeight"]) and not np.isnan(i["InitialSize"]):
        species_mi[i["Name"]] = {
            "MarketWeight": i["MarketWeight"],
            "InitialSize": i["InitialSize"]
        }

species = "Sparus_aurata"

ttm, fcr = perfect_sim(
    dataframe,
    species,
    species_mi[species],
    "RCP4.5")


