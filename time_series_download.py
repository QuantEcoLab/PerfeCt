import cdsapi
import zipfile
import netCDF4 as nc
import numpy as np
import os
from geojson import FeatureCollection
import json
import pandas as pd

c = cdsapi.Client()

years = np.arange(2022, 2101, step=1)
years = years.tolist()

months = list(np.arange(1, 13))

rcps = ["rcp4_5", "rcp8_5"]

data = {}

aqua_path = "data/MED_farms.geojson"
with open(aqua_path, 'r') as data_file:
    aqua_data = json.load(data_file)

feature_collection = FeatureCollection(aqua_data['features'])

for feature in feature_collection["features"]:
    id_ = feature["properties"]["farm_id"]
    coords = feature["geometry"]["coordinates"]
    data[id_] = {
        "coords": coords,
        "rcp4_5": [],
        "rcp8_5": [],
        "date": []
    }


def extract_data(f, rcp, year, month, data=data):
    dataset = nc.Dataset(f[0])
    lons = np.array(dataset["lon"][:], dtype=np.float64)
    lats = np.array(dataset["lat"][:], dtype=np.float64)

    depths = np.array(dataset["depth"][:], dtype=np.float64)
    depth = 10

    depth_idx = int(np.where(depths == depth)[0])

    data_10m = np.array(dataset["thetao"][:, depth_idx, :, :])
    data_10m[data_10m > 1e10] = np.nan

    mask = np.isnan(data_10m)
    data_10m[mask] = np.interp(
        np.flatnonzero(mask), np.flatnonzero(~mask), data_10m[~mask])

    for id_ in data:
        coords = data[id_]["coords"]
        lon = coords[0]
        lat = coords[1]
        idx = (np.abs(lats-lat)).argmin()
        idy = (np.abs(lons-lon)).argmin()

        val = data_10m[:, idx, idy]
        t = 1
        for v in val:
            data[id_][rcp].append(v)
            date = f"{year}-{month}-{t}"
            if date not in data[id_]["date"]:
                data[id_]["date"].append(f"{year}-{month}-{t}")
            t += 1


def save_data(data=data):
    for id_ in data:
        df = pd.DataFrame(
            {
                "date": data[id_]["date"],
                "rcp4_5": data[id_]["rcp4_5"],
                "rcp8_5": data[id_]["rcp8_5"]
            }
        )
        df.to_csv(f"data/time_series/id_{id_:03d}.csv")


for year in years:
    for month in months:
        for rcp in rcps:
            print("Downloading:", year, f"{month:02d}", rcp)
            c.retrieve(
                'sis-marine-properties',
                {
                    'origin': 'polcoms_ersem',
                    'vertical_resolution': 'water_column',
                    'time_aggregation': 'day',
                    'variable': 'sea_water_potential_temperature',
                    'experiment': [
                        rcp
                    ],
                    'year': [year],
                    'month': [
                        f'{month:02d}'
                    ],
                    'format': 'zip',
                },
                'tmp.zip')

            data_load = zipfile.ZipFile("tmp.zip", mode="r")
            files = zipfile.ZipFile.namelist(data_load)

            with zipfile.ZipFile('tmp.zip', 'r') as zipObj:
                zipObj.extractall()

            # extract data here
            extract_data(files, rcp, year, month)

            os.remove(files[0])

        save_data()
