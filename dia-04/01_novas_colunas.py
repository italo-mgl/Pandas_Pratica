#%%
import pandas as pd
import numpy as np 
#%%

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
#%%

df["Pontos_100"] = df["QtdePontos"] + 100

#%%

nova_coluna = []
for i in df["QtdePontos"]:
    nova_coluna.append(i+100)

nova_coluna

# %%

df["EmailTwitch"] =  df["FlEmail"] + df["FlTwitch"]
df.head()

#%%

df["zerado"] = df["FlEmail"] * df["FlTwitch"]
df

filtro = df["zerado"] == 0

df[filtro].sum()
#%%

df["QtdeSocial"] = df["FlTwitch"] + df["FlYouTube"] + df["FlBlueSky"]	+ df["FlInstagram"]
df
#%%

df["todas_social"] = df["FlTwitch"] * df["FlYouTube"] * df["FlBlueSky"] * df["FlInstagram"]
df

#%%

df.head()

df["QtdePontos"].describe()

#%%

df["LogPontos"] = np.log(df["QtdePontos"]+1)

df["LogPontos"].describe()
#%%

import matplotlib.pyplot as plt

plt.hist(["LogPontos"])
plt.grid(True)
plt.show()