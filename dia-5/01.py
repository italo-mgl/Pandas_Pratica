## Selecione a primeira transação de cada dia, por usuário.

#%%
import pandas as pd

transacoes = pd.read_csv("../data/transactions.csv", sep=";")
transacoes

#%%

transacoes.sort_values(by="DtTransaction")
transacoes

#%%
transacoes = pd.to_datetime(transacoes["DtTransaction"])
#%%

transacoes["datas"] = pd.to_datetime(transacoes["DtTransaction"]).dt.day
transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])

