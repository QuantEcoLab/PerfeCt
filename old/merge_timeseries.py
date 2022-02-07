import pandas as pd
import pathlib
from tqdm import tqdm

in_dirs = [
    "data/grid_time_series_1",
    "data/grid_time_series_2",
    "data/grid_time_series_3"
]

out_dir = "data/grid_time_series"

files1 = list(pathlib.Path(in_dirs[0]).glob("**/*.csv"))
files1.sort()
files2 = list(pathlib.Path(in_dirs[1]).glob("**/*.csv"))
files2.sort()
files3 = list(pathlib.Path(in_dirs[2]).glob("**/*.csv"))
files3.sort()

len(files1)
len(files2)
len(files3)

for f in tqdm(range(len(files1))):
    filename = (files1[f]).stem
    df1 = pd.read_csv(files1[f], index_col=0)
    df2 = pd.read_csv(files2[f], index_col=0)
    df3 = pd.read_csv(files3[f], index_col=0)

    df = pd.concat([df1, df2, df3])

    df_dropped = df.drop_duplicates(ignore_index = True)

    df_dropped.to_csv(f"{out_dir}/{filename}.csv")



