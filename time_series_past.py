import netCDF4 as nc
import numpy as np
import os
from geojson import FeatureCollection
import json
import pandas as pd
import pathlib
from tqdm import tqdm

aqua_path = "data/MED_farms/MED_test_farm.geojson"
with open(aqua_path, 'r') as data_file:
    aqua_data = json.load(data_file)

feature_collection = FeatureCollection(aqua_data['features'])

feature = feature_collection["features"][0]
coords = feature["geometry"]["coordinates"]

# 2021 timeseries generation
past_dir = "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/MED_temp_2021/2021"
files_past = list(pathlib.Path(past_dir).glob("**/*.nc"))
files_past.sort()

values_10m = []
dates = []

depths = np.array(nc.Dataset(files_past[0])["depth"][:], dtype=np.float64)
depth_idx = 4  # approx 10 m (1.05366039e+01)

for file in tqdm(files_past):
    date = (file.stem).split("-")[0][:-2]

    dataset = nc.Dataset(file)

    lons = np.array(dataset["lon"][:], dtype=np.float64)
    lats = np.array(dataset["lat"][:], dtype=np.float64)

    data_10m = np.array(dataset["thetao"][:, depth_idx, :, :])
    data_10m[data_10m > 1e10] = np.nan

    # Fill in NaN's...
    mask = np.isnan(data_10m)
    data_10m[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), data_10m[~mask])

    lon = coords[0]
    lat = coords[1]

    idx = (np.abs(lats-lat)).argmin()
    idy = (np.abs(lons-lon)).argmin()
    val = data_10m[:, idx, idy]

    dates.append(date)
    values_10m.append(float(val))
    
df_past = pd.DataFrame({"date": dates, "temp_10m": values_10m})
df_past.to_csv("data/timeseries_past_future/temp_2021_638.csv")