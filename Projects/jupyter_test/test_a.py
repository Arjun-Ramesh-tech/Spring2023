import pandas as pd
import numpy as np
from natsort import index_natsorted
df = pd.read_excel("iteration1.xlsx",index_col=0)
a = []
for each in df.columns:
    a.append((df[each]*df["Rank"]).sum())
df.loc[len(df)] = a
df = df.sort_values(by = 18, axis = 1,ascending=False)
df.to_excel("suraj_561_final.xlsx")