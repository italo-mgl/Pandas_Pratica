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