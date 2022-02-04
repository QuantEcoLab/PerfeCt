import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pathlib
from geojson import FeatureCollection
import json

aqua_path = "data/points_fish_cro/points_fish_cro_aqua_wgs84.geo.json"
with open(aqua_path,'r') as data_file:
    aqua_data = json.load(data_file)

feature_collection = FeatureCollection(aqua_data['features'])
#print(feature_collection)

dir_paths = [
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_01/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_02/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_03/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_04/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_05/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_06/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_07/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_08/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_09/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_10/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_11/",
    "/mnt/DataDisk/BlueCloud_Hackathon_2022/RAD_podloge/temp_12/"
]

#dir_paths = [dir_paths[0]]
last_id = None

for feature in feature_collection["features"]:
    values_loc = []
    dates = []
    rcp_types = []
    #print(feature["properties"]["id"], feature["geometry"]["coordinates"])
    id_ = feature["properties"]["id"]
    coords = feature["geometry"]["coordinates"]

    if id_ != last_id:
        last_id = id_
        lon = coords[0]  # 14.323250
        lat = coords[1]  # 43.847366

        for dir_path in dir_paths:
            files = list(pathlib.Path(dir_path).glob(r"*.nc"))
            files.sort()
            #files = [files[0]]
            for file in files:
                print(f"Working on {id_}, {file.stem}")
                rcp = (file.stem).split("-")[3]
                year = (file.stem).split("-")[5]
                month = (file.stem).split("-")[6]

                dataset = nc.Dataset(file)
                #dataset["time"]
                #dataset["thetao"]

                lons = np.array(dataset["lon"][:], dtype=np.float64)
                lats = np.array(dataset["lat"][:], dtype=np.float64)

                depths = np.array(dataset["depth"][:], dtype=np.float64)
                depth = 10

                depth_idx = int(np.where(depths==depth)[0])
                data_10m = np.array(dataset["thetao"][:, depth_idx, :, :])
                data_10m[data_10m>1e10] = np.nan

                # Fill in NaN's...
                mask = np.isnan(data_10m)
                data_10m[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), data_10m[~mask])

                idx = (np.abs(lats-lat)).argmin()
                idy = (np.abs(lons-lon)).argmin()
                val = data_10m[:, idx,idy]
                for d in range(val.shape[0]):
                    dates.append(f"{year}-{month}-{d+1}")
                    values_loc.append(val[d])
                    rcp_types.append(rcp)

        data_dict = {
            "date": dates,
            "rcp_scenario": rcp_types,
            "temp": values_loc
        }
        df_out = pd.DataFrame(data_dict)
        df_out.to_csv(f"aqua_temp_series/temp_aqua_{id_}.csv")
