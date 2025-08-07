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
series_idades[0]