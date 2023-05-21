import pandas as pd
import numpy as np
from natsort import index_natsorted

df = pd.read_excel("suraj_561_final.xlsx",index_col=0,na_values=["Com1"])
#df= df.fillna(0)
for index, row in df.iterrows():
    for each in df.columns[:-1]:
        df["Rank"][index] += df[each][index]*df[each][18] 
#df = df.drop(index="SUM")
df = df.sort_values(
    by="Rank",
    ascending=True,
    key=lambda x: np.argsort(index_natsorted(df["Rank"]))
)
print(df)
df.to_excel("suraj_561_final_2.xlsx")
print(df.sum())

