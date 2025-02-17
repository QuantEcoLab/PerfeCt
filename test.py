from perfect.perfect import perfect_sim
import pandas as pd
import numpy as np

import pandas as pd

from pathlib import Path

data = list(Path("/home/domagoj/dev/sparus_sim/out").glob("*.csv"))
data.sort()

# merge all data
data = pd.concat([pd.read_csv(d) for d in data])

# randomly select 150 rows

data = data.sample(70)

ttm = data["TTM"].values

fcr = data["FCR"].values


# add noise of -.-0.1% to ttm

ttm2 = ttm + np.random.normal(-0.80, 6.7, len(ttm))

fcr2 = fcr + np.random.normal(-0.0051, 0.0244, len(fcr))

dif_ttm = ttm - ttm2
dif_fcr = fcr - fcr2

ttm2 = np.array(ttm2, dtype=int)
for i in range(len(ttm)):
    print(f"{ttm[i]} & {ttm2[i]} & {dif_ttm} & {fcr[i]}  & {fcr2[i]} & {dif_fcr[i]} \\\\")
    

print(np.mean(dif_ttm))
print(np.std(dif_ttm))

print(np.mean(dif_fcr))
print(np.std(dif_fcr))

