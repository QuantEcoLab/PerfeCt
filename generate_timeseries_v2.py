import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pathlib
from geojson import FeatureCollection
import json
from tqdm import tqdm

aqua_path = "data/MED_farms.geojson"
with open(aqua_path,'r') as data_file:
    aqua_data = json.load(data_file)

feature_collection = FeatureCollection(aqua_data['features'])
# print(feature_collection)

dir_path = "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge"

files = list(pathlib.Path(dir_path).glob("**/*.nc"))
files.sort()

rcps = ["rcp45", "rcp85"]
rcp45 = []
rcp85 = []
rcp45_st = []
rcp85_st = []
for i in files:
    if rcps[0] in i.stem:
        rcp45.append(i)
        rcp45_st.append(i.stem)
    elif rcps[1] in i.stem:
        rcp85.append(i)
        rcp85_st.append(i.stem)

idx = np.argsort(rcp45_st)
rcp45 = np.asarray(rcp45)[idx]
idx = np.argsort(rcp85_st)
rcp85 = np.asarray(rcp85)[idx]

rcp_list = np.concatenate((rcp45, rcp85))

last_id = None
last_rcp = None

md = {}
md["rcp45"] = {}
md["rcp85"] = {}

for file in tqdm(rcp_list):
    print(file.stem)
    rcp = (file.stem).split("-")[3]
    year = (file.stem).split("-")[5]
    month = (file.stem).split("-")[6]

    dataset = nc.Dataset(file)

    lons = np.array(dataset["lon"][:], dtype=np.float64)
    lats = np.array(dataset["lat"][:], dtype=np.float64)

    depths = np.array(dataset["depth"][:], dtype=np.float64)
    depth = 10

    depth_idx = int(np.where(depths==depth)[0])
    data_10m = np.array(dataset["thetao"][:, depth_idx, :, :])
    data_10m[data_10m > 1e10] = np.nan

    # Fill in NaN's...
    mask = np.isnan(data_10m)
    data_10m[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), data_10m[~mask])

    for feature in feature_collection["features"]:
        id_ = feature["properties"]["farm_id"]
        coords = feature["geometry"]["coordinates"]
        #lon = feature["properties"]["X"]
        #lat = feature["properties"]["Y"]

        if id_ not in md[rcp]:
            d = {}
            d["date"] = []
            d["temp"] = []
            md[rcp][id_] = d
        else:
            d = md[rcp][id_]

        if id_ != last_id:
            # print(f"Working on {file.stem}, {id_}")

            last_id = id_
            lon = coords[0]
            lat = coords[1]

            idx = (np.abs(lats-lat)).argmin()
            idy = (np.abs(lons-lon)).argmin()
            val = data_10m[:, idx, idy]
            for t in range(val.shape[0]):
                d["date"].append(f"{year}-{month}-{t+1}")
                d["temp"].append(val[t])

            df = pd.DataFrame(md[rcp][id_])
            df.to_csv(f"data/aqua_timeseries/aqua_{rcp}-{id_}.csv")
