import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pathlib
from geojson import FeatureCollection
import json
from tqdm import tqdm

aqua_path = "data/MED_grid/MED_ter_10km_grid_centroids.geojson"
with open(aqua_path, 'r') as data_file:
    aqua_data = json.load(data_file)

feature_collection = FeatureCollection(aqua_data['features'])
# print(feature_collection)

dir_path = "/mnt/DataDisk/MED_temp_past"

files = list(pathlib.Path(dir_path).glob("**/*.nc"))
files.sort()

last_id = None

md = {}

for file in tqdm(files):
    print(file.stem)
    date = (file.stem).split("-")[0][:-2]

    dataset = nc.Dataset(file)

    lons = np.array(dataset["lon"][:], dtype=np.float64)
    lats = np.array(dataset["lat"][:], dtype=np.float64)

    depths = np.array(dataset["depth"][:], dtype=np.float64)

    depth_idx = 4  # approx 10 m (1.05366039e+01)
    data_10m = np.array(dataset["thetao"][:, depth_idx, :, :])
    data_10m[data_10m > 1e10] = np.nan

    # Fill in NaN's...
    mask = np.isnan(data_10m)
    data_10m[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), data_10m[~mask])

    for feature in feature_collection["features"]:
        id_ = feature["properties"]["CellCode"]
        coords = feature["geometry"]["coordinates"]
        #lon = feature["properties"]["X"]
        #lat = feature["properties"]["Y"]

        if id_ not in md:
            d = {}
            d["date"] = []
            d["temp"] = []
            md[id_] = d
        else:
            d = md[id_]

        if id_ != last_id:
            # print(f"Working on {file.stem}, {id_}")

            last_id = id_
            lon = coords[0]
            lat = coords[1]

            idx = (np.abs(lats-lat)).argmin()
            idy = (np.abs(lons-lon)).argmin()
            val = data_10m[:, idx, idy]
            for t in range(val.shape[0]):
                d["date"].append(date)
                d["temp"].append(val[t])

            df = pd.DataFrame(md[id_])
            df.to_csv(f"data/grid_timeseries_past/id_{id_}.csv")