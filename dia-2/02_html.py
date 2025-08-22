#%%
import pandas as pd
import lxml

url = ("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")
df = pd.read_html(url)
df
#%%
df_uf = df[1]
df_uf.to_csv("uf.csv", sep=";", index=False)
