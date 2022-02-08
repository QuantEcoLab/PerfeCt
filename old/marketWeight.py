from deb.simulations import simulate_deb, aux
import numpy as np
import pandas as pd


data = pd.read_csv("data/time_series/id_638.csv", index_col=0)

species = pd.read_csv("data/deb_species_list.csv")

