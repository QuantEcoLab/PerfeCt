import folium
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import branca
from matplotlib import cm
from matplotlib.colors import Normalize
from folium.plugins import Draw


temp_data_path = "data/20220111_d-CMCC--TEMP-MFSeas6-MEDATL-b20220110_fc-sv07.00.nc"
temp_data = nc.Dataset(temp_data_path)

#for var in temp_data.variables.values():
#    print(var)

depths = temp_data["depth"][:]
depths

lons = np.array(temp_data["lon"][:], dtype=np.float64)
lats = np.array(temp_data["lat"][:], dtype=np.float64)

temp_dummy = np.array(temp_data["thetao"][0, 2, :, :], dtype=np.float64)
temp_dummy[temp_dummy>1e+10] = np.nan
temp_dummy

#plt.imshow(temp_dummy, origin="lower")

norm = Normalize(vmin=np.nanmin(temp_dummy), vmax=np.nanmax(temp_dummy))
col = cm.ScalarMappable(norm, "viridis")
dummy_col = col.to_rgba(temp_dummy)


m=folium.Map(location=[35, 20], zoom_start=5)

folium.raster_layers.ImageOverlay(
    image=dummy_col,
    bounds=[[np.min(lats), np.min(lons)], [np.max(lats), np.max(lons)]],
    origin="lower",
    mercator_project=True
).add_to(m)

folium.features.LatLngPopup().add_to(m)

Draw(export=True).add_to(m)

m
