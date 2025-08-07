#%%
import pandas as pd
#%%
df = pd.read_excel("../data/transactions.xlsx")
df
#%%
df = df.sort_values(by="DtTransaction", ascending= True)
df
#%%

filtro = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df.loc[filtro]

#%%
## Qual foi o valor da ultima transação de cada IdCustomer
df_last = df = df.drop_duplicates(subset="IdCustomer", keep="last")
df_last["IdCustomer"].nunique
#%%
filtro = df_last["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_last.loc[filtro]

