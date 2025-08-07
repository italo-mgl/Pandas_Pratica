#%%
import pandas as pd
#%%
data = {
    "nome": ['Teo', 'nah', 'lara', 'maria'],
    "sobrenome": ['Calvo', 'ataide', 'calvo', 'calvo'],
    'idade': [31, 32, 31, 2 ]
}

data
data['idade'][0]
# %%

df = pd.DataFrame(data)
df
#%%
df['idade'].iloc[0]

#%%

df['sobrenome'].iloc[0]

#%%
df.columns
#%%
df.info(memory_usage='deep')
#%%
df.dtypes
#%%

df['peso'] = [80, 70, 56, 45]
df['peso'].describe()

sumario = df.describe()
sumario['peso']['mean']
#%%
df.head(2)
df.tail(2)