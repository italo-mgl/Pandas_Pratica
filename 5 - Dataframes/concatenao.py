#%%
import pandas as pd
#%%
df = pd.read_csv("../data/ipea/homicidios.csv", sep=";")

df.rename(columns={"valor": "homicidios"})