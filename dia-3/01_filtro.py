#%%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df
#%%
pontos = [10,1,1,1,50,130,30,50]

valores_50 = []
for i in pontos:
    if i >= 50:
        valores_50.append(i)

valores_50

#%%

valores_50 = [ i for i in pontos if i >= 50]
valores_50

#%%
pontos = [10,1,1,1,50,130,30,50]
filtro = []
valores_50 = []
for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado

#%%

brinquedo = pd.DataFrame({
    "nome": ["teo", "nah", "mah"],
    "idade": [32,35,14],
    "uf": ["sp", "pr", "rj"]
})

filtro = brinquedo["idade"]>= 18

brinquedo[filtro]
#brinquedo[brinquedo["idade"]>= 18]

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.columns

#%%
filtro2 = df["QtdePontos"] >= 50
df[filtro2]

df[df["QtdePontos"] >= 50]

#%%

filtro3 = (df["QtdePontos"] >= 50) & (df["QtdePontos"] <= 100)

df[filtro3].sort_values(by="QtdePontos",ascending=False)

#%%

filtro4 = (df["QtdePontos"] >= 0) &\
          (df["QtdePontos"] < 50) &\
          (df["DtCriacao"] >= '2025-01-01')

df[filtro4]
