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
df.groupby(["IdCustomer"])["Points"].mean()