#%%
import pandas as pd
#%%

df = pd.read_csv("../data/customers.csv", sep= ";")
df
#%%
df.dtypes

#%%
df["Points"].astype(str)
df.dtypes