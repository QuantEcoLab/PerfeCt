import cdsapi
import zipfile
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np

c = cdsapi.Client()

years = np.arange(2022, 2101, step=1)
years = years.tolist()

months = list(np.arange(1, 13))

rcps = ["rcp4_5", "rcp8_5"]

for year in years:
    for month in months:
        for rcp in rcps:
            print(year, f"{month:02d}", rcp)
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

            print(files)
            break
        break
    break

# #data_nc = data_load.open(files[0])
# with zipfile.ZipFile('tmp.zip', 'r') as zipObj:
    # Extract all the contents of zip file in current directory
#    zipObj.extractall()
# ds = nc.Dataset(files[0])
# plt.imshow(ds["thetao"][0, 0, :, :], origin="lower")

# data_se = cdsapi.geo.extract_point(data, lon=43.847366, lat=14.323250)