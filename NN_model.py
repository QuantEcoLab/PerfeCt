import os

# This guide can only be run with the torch backend.
os.environ["KERAS_BACKEND"] = "torch"

from tqdm import tqdm


from deb.simulations import simulate_deb, allStat
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

from pathlib import Path

from keras.optimizers import Adam

species_db = pd.read_csv("data/deb_species_list.csv", index_col=0)

species_mi = {}
for i in species_db.iloc:
    if not np.isnan(i["MarketWeight"]) and not np.isnan(i["InitialSize"]):
        species_mi[i["Name"]] = {
            "MarketWeight": i["MarketWeight"],
            "InitialSize": i["InitialSize"]
        }

# sample = pd.read_csv(
#     "data/time_series/future/id_001.csv", usecols=[0, 2]).values

# sample = sample[0:365*7]+273.15

# result = simulate_deb(
#     species="Sparus_aurata",
#     location=sample,
#     fArr=[0.85],
#     initial_size=species_mi["Sparus_aurata"]["InitialSize"],
#     allStat=allStat    
# )

# TTM = np.where(result[0.85][2] >= species_mi["Sparus_aurata"]["MarketWeight"])[0]
# fcr = result[0.85][-1][TTM[0]]


files = list(Path("data/time_series/future/").rglob("*.csv"))

dataset = {}
dataset["input"] = []
dataset["output"] = []



for i in files:
    print(i)
    sample = pd.read_csv(i, usecols=[0, 2]).values
    for s in tqdm(range(0, len(sample)-365*7, 365)):
        start_idx = s
        sample[start_idx:start_idx+365*7,1]+273.15
        res = simulate_deb(
            species="Sparus_aurata",
            location=sample,
            fArr=[0.85],
            initial_size=species_mi["Sparus_aurata"]["InitialSize"],
            allStat=allStat
        )
        TTM = np.where(res[0.85][2] >= species_mi["Sparus_aurata"]["MarketWeight"])[0]
        if TTM.tolist() == []:
            continue
        fcr = res[0.85][-1][TTM[0]]
        dataset["input"].append(sample[:,1].reshape((365, 7)))
        dataset["output"].append(np.array([TTM[0], fcr]))

# randomly select 80 percent of the data for training from list of datafiles
# 
# train_files = list(np.random.choice(files, int(len(files)*0.8)))
# test_files = [i for i in files if i not in train_files]
# 
# def generator(train=True, batch_size=32):
#     if train:
#         data_files = train_files
#     else:
#         data_files = test_files
#         
#     while True:
#         data = np.random.choice(data_files, 1)[0]
#         dataset = pd.read_csv(data, usecols=[0, 2]).values
#         input_batch = np.zeros((batch_size, 365, 7))
#         output_batch = np.zeros((batch_size, 2))
#         bz = 31
#         
#         while bz !=0:
#             sample = pd.read_csv(
#                 "data/time_series/future/id_001.csv", usecols=[0, 2]).values
#             sample[:,1] += 273.15
#             start_idx = np.random.randint(0, len(sample)-365*7)
#             ss = sample[start_idx:start_idx+365*7]
#             res = simulate_deb(
#                 species="Sparus_aurata",
#                 location=ss,
#                 fArr=[0.85],
#                 initial_size=species_mi["Sparus_aurata"]["InitialSize"],
#                 allStat=allStat
#             )
#             TTM = np.where(res[0.85][2] >= species_mi["Sparus_aurata"]["MarketWeight"])[0]
#             if TTM.tolist() == []:
#                 continue
#             fcr = res[0.85][-1][TTM[0]]
#             # print(sample.shape)
#             print(ss[:,1].shape)
#             input_batch[bz] = ss[:, 1].reshape((365, 7))
#             output_batch[bz] = np.array([TTM[0], fcr])
#             bz -= 1
#             
#         yield input_batch, output_batch
#         
# 
# train_data = generator(batch_size=32)
# test_data = generator(batch_size=32, train=False)
# 
# model = Sequential()
# model.add(Conv2D(64, 3, activation="relu", input_shape=(365, 7,1)))
# model.add(MaxPooling2D())
# model.add(Flatten())
# model.add(Dense(128, activation="relu"))
# model.add(Dense(2, activation="linear"))
# 
# model.compile(optimizer=Adam(), loss="mean_squared_error")
# 
# model.summary()
# 
# 
# model.fit(
#     train_data, batch_size=32, epochs=10, steps_per_epoch=100,
#     validation_data=test_data, validation_steps=100)
# 
# # nn input 2d array of shape (365, 7)
# #stacked years
# # no need for second input beca that are constants
# # nn output 2nodes representing TTM and FCR
# 
# 


