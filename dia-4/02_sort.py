#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
#%%

clientes["QtdePontos"].sort_values(ascending=False)

#%%
Maiores = clientes.sort_values(by="QtdePontos", ascending=False)["IdCliente"]

Maiores.head(5)
#%%

brinquedo = pd.DataFrame(
    {
        "nome": ["Teo", "ana", "Nah", "jose"],
        "idade": [32,43,35,42],
        "salario": [2354,4533,3245,4533]
    }
)
brinquedo

# %%

brinquedo.sort_values(by=["salario","idade"], ascending=[False,True])
