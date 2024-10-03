#%%
import pandas as pd
data = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
#%%
data_serie = pd.Series(data)
data_serie
#%%
#Media
data_serie.mean()
#Desvio padrao
data_serie.std()
#máximo valor 
data_serie.max()
#%%

dados = {
    "nome": ['Teo', 'Nah', 'Napoleão'],
    "idade": [31, 32, 14]
}

df = pd.DataFrame(dados)
df
#%%
sumario = df.describe()
sumario['idade']['mean']
#%%
df.columns
df['nome'].iloc[-1]