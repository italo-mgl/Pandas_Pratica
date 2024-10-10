#%%a
import pandas as pd
import numpy as np
#%%
df = pd.read_csv("../data/customers.csv", sep=";")
df
#%%
df["Points_Double"] = df["Points"] * 2
df
#%%
df["Points_ratio"] = df["Points_Double"] / df["Points"]
df.head()
#%%
df["Constante"] = 1
df
#
#%%
df["Points_log"] = np.log(df["Points"])
df
#%%

#%%
nomes_alta = []
for i in df["Name"]:
    nomes_alta.append(i.upper())

df["Nome_alta"] = nomes_alta
df
#%%
df["Name"].str.upper()

#%%
df["Name"].str.split("_")
#%%
def get_first(name:str):
    return name.split("_")[0]

#%%

get_first("Antonela_rabuda")
#%%
df["Name_First"] =  df["Name"].apply(get_first)
df
#%%
df = df.drop(columns="Nome_alta")
df

#%%
df["Name"].apply(lambda x: x.upper().split("_")[0])

#%%

def intervalo_pontos(pontos):
    if pontos <2500:
        return "baixo"
    elif pontos <3500:
        return "medio"
    else:
        return "alto"
        
df["Faixa_pontos"] = df["Points"].apply(intervalo_pontos)
df
#%%

df["UUID"].apply(lambda x: x[-3:])

#%%

data2 = {
    "nome":["Teo", "Nah", "Maria", "Lara"],
    "recencia":[1,30,10,45],
    "valor":[100,2000,15,2000],
    "frequencia":[2,5,1,15]
}
#%%
df_crm = pd.DataFrame(data2)
df_crm
#%%
 