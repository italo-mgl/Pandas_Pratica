#%%
import pandas as pd
#%%
data = {
    "Nome": ["Teo", "Nah", "Maria", "Nah", "Lara", "Teo"],
    "Idade": [32, 33, 2, 33, 31, 32],
    "Updatade_at": [1,2,3,1,2,3]
}
df = pd.DataFrame(data)
df = df.sort_values(by= "Updatade_at", ascending=True)
df
#%%
df.drop_duplicates(subset=["Nome", "Idade"], keep="first")
