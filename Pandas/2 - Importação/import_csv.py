#%%
import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers
#%%
df_customers.shape
#%%

df_customers.info(memory_usage='deep')

#%%

df_customers['Points'].astype(int)
#%%
df_customers.describe()
#%%

condicao = df_customers['Points'] >1000
condicao
#%%
df_customers[condicao]
#%%
condicao = df_customers['Points'] == df_customers['Points'].max()
df_maximo = df_customers[condicao]
df_maximo["Name"].iloc[0]
#%%
condicao_2 = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_customers[condicao_2].count()
#%%

df_customers[['UUID', 'Name']]
#%%
colunas = df_customers.columns.tolist()
colunas.sort()
df_customers = df_customers[colunas]

#%%

df_customers = df_customers.rename(columns = {"Name": "Nome",
                               "Points": "Pontos",
                               "UUID": "ID"})
df_customers