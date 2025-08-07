#%% 

import pandas as pd

idades = [
    25,25,65,39,25,63,32,42,54,31,36,63,13,40,27,28,29
]
#%%

series_idades = pd.Series(idades)
series_idades

#%%

## Estatisticas da série

media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()
summary_idades
