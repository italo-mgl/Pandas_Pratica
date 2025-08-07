#%%
import pandas as pd
#%%

df = pd.read_excel("../data/transactions.xlsx")
df
#%%
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3" 
df_user = df[condicao]
df_user["Points"].sum()

#%%
df_summary = df.groupby(["IdCustomer"])["Points"].sum()
df_summary.reset_index()
#%%
df_agrupado = (df.groupby(["IdCustomer"])
    .agg({"Points": "sum",
    "UUID": "count",
    "DtTransaction": "max"})
    .rename(columns={"IdCustomer": "Cliente",
    "DtTransaction": "Ultima_Compra",
    "Points": "Valor",
    "UUID": "Frequencia"})
    .reset_index()
   
    )
df_agrupado

#%%
import datetime

data1 = df["DtTransaction"][0]
now = datetime.datetime.now()

(now - data1).days
#%%
condicao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3" 
df_user = df[condicao]
#%%

def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

(df.groupby(["IdCustomer"])
    .agg({"Points": "sum",
        "UUID": "count",
        "DtTransaction": recencia
        })
    .rename(columns={
        "IdCustomer": "Cliente",
        "DtTransaction": "Ultima_Compra",
        "Points": "Valor",
        "UUID": "Frequencia"
        })
    .reset_index()
   
    )
