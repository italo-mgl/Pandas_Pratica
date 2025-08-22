#%%
import pandas as pd


idades = [
    25,25,65,39,25,63,32,42,54,31
]

nomes = [
    "Teo","Nah","Itin","Francisco","Bartolomeu",
    "Vic","Kozato","Andrei","Fernanda","Olavo",

]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

#%%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes

#%%

df.iloc[-1]["idades"]
