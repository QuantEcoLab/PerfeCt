from scipy.interpolate import interp1d
import pandas as pd

data = pd.read_csv("scripts_matlab/Temp_Ston.csv")

x = data["no"].values
y = data["sst"].values

f = interp1d(x, y, kind="slinear")

f(82.3769)