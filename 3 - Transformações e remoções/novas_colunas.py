#%%a
import pandas as pd
import numpy as np
#%%
df = pd.read_csv("../data/customers.csv", sep=";")
df
#%%
df["Points_Double"] = df["Points"] * 2
df
#%%
df["Points_ratio"] = df["Points_Double"] / df["Points"]
df.head()
#%%
df["Constante"] = 1
df
#
#%%
df["Points_log"] = np.log(df["Points"])
df
#%%

#%%
nomes_alta = []
for i in df["Name"]:
    nomes_alta.append(i.upper())

df["Nome_alta"] = nomes_alta
df
#%%
df["Name"].str.upper()

#%%
df["Name"].str.split("_")
#%%
def get_first(name:str):
    return name.split("_")[0]

#%%

get_first("Antonela_rabuda")
#%%
df["Name_First"] =  df["Name"].apply(get_first)
df
#%%
df = df.drop(columns="Nome_alta")
df