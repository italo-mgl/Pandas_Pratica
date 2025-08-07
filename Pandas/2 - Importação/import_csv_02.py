#%%
import pandas as pd
#%%
df = pd.read_csv("../data/products.csv",
                  sep=';',
                  names=["ID", "Name", "Description"]
                  )
df
#%%
df.rename(columns = {"Name": "Nome",
                  "Description": "Descrição"}, inplace=True)
df
#%%

