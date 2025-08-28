#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

#%%
clientes.dropna()

#%%
filtro = clientes["DtCriacao"].notna()

clientes[filtro]
#%%

clientes.dropna(how="all")
# %%

df = pd.DataFrame({
    "nome": ["Teo", None, "Nah", "Marcio"],
    "idade": [None, None, 43, 52],
    "salario": [3453, 4324, None, 5423]
})
df.dropna(how="all", subset=["nome", "salario"])

#%%
df.dropna(how="all", subset=["idade", "nome"])

#%%
df.fillna(0)

#%%
df.fillna({"nome": "Someone", "idade": 90})