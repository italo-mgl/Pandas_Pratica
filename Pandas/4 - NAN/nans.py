#%%%
import pandas as pd
import numpy as np
#%%
data = {
    "nome": ["Teo", "Nah", "Lah", "Mah", "Jo"],
    "idade": [31,32,34,12,np.nan],
    "renda": [np.nan, 3245, 357, 12432, np.nan]
}

df = pd.DataFrame(data)
df
#%%
df["idade"].isna().sum()
#%%
df.isna().sum()
#%%
df.isna().mean()
#%%
df.fillna({
    "idade": df["idade"].mean(),
    "renda": df["renda"].mean()
    })

#%%
#df
df.dropna(subset=["idade", "renda"], how="all" )

#%%
df.dropna(axis = 1, how="any")
#%%
