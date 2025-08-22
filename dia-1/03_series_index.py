#%%
import pandas as pd

idades = [
    25,25,65,39,25,63,32,42,54,31,36,63,13,40,27,28,29
]
#%%

series_idades = pd.Series(idades)
series_idades

#%%

idades[-1]

#%%
series_idades = series_idades.sort_values()
series_idades
#%%

series_idades.loc[0]
#%%

series_idades.iloc[:3]
#%%
idades2 = [
    25,25,65,39,25,63,32,42,54,31
]

indexs = [
    "Teo","Nah","Itin","Francisco","Bartolomeu",
    "Vic","Kozato","Andrei","Fernanda","Olavo",

]
# %%
series_idades2 = pd.Series(idades2, index=indexs)
series_idades2

#%%
series_idades2["Bartolomeu   "]