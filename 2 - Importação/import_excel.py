#%%
import pandas as pd
#%%
df = pd.read_excel("../data/transactions.xlsx")
df.shape
#%%
df.head()
#%%
df.tail()
#%%
lista = df.columns.tolist()
lista.sort()
lista
df.columns = lista
df