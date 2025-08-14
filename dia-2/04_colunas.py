#%%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

#%%
df.shape
#%%
df.info(memory_usage="deep")

#%%
df.dtypes

#%%
df = df.rename(columns={"IdTransacao": "IdTarnsac",
                   "QtdePontos":"QtdPontos",
                   "DtCriacao": "DataCriacao"})
df.columns

#%%
df[["IdCliente","QtdPontos"]]

#%%

df[["IdCliente", "QtdPontos"]].sample(5)
df.columns

#%%
df[["IdCliente", "IdTarnsac", "QtdPontos"]].head(5)

#%%
colunas = list(df.columns)
colunas.sort()
colunas
#%%
df = df[colunas]
df