#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

Filtro = clientes["QtdePontos"] == 0

clientes_0 = clientes[Filtro].sort_values(by="QtdePontos", ascending=True)
clientes_0
clientes_0["flag_1"] = 1 
clientes_0

#%%

