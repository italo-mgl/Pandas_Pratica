#%%
import pandas as pd
import os
#%%
path = "../data/ipea/"
files = os.listdir(path)

print(files)
#%%

def import_etl(path:str):
    name = path.split("/")[-1].split(".")[0]
    
    df = (pd.read_csv(path, sep=";")
            .rename(columns={"valor":name})
            .set_index(["cod","nome","período"]))
    return df

#%%
dfs = []
for i in files:
    dfs.append(import_etl(path+i))
#%%
df_final = pd.concat(dfs, axis=1).reset_index()
df_final.to_csv("../data/dado-finais.csv", sep=";", index=False)