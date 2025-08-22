#%%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")

df_clientes.head()

#%%
df_clientes.tail(10)

#%%
df_clientes.shape

#%%
df_clientes.sample(20)

#%%
df_clientes.columns

#%%
df_clientes.index

#%%
df_clientes.info(memory_usage="deep")
#%%
df_clientes.dtypes["QtdePontos"]

#%%
idades = [1,2,4,1,3,56,52,2,41,12,43,12]

idade_series = pd.Series(idades)
idade_series = idade_series.sort_values()
idade_series

#%%
idade_series.iloc[9]

#%%
df_clientes["FlTwitch"]