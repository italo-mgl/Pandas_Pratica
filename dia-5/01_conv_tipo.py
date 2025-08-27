#%%
import pandas as pd

#%%

df = pd.read_csv("../data/clientes.csv", sep=";")

#%%
df["QtdePontos"].astype(int)
#%%

df["DtCriacao"]

#%%
pd.to_datetime(df["DtCriacao"])


#%%

df["DtCriacao"].replace({
    "2024-02-01 00:00:00 +0000": "2099-99-01 09:00:00 +0000"
})