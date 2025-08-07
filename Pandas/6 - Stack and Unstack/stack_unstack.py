#%%
import pandas as pd
#%%
df = pd.read_csv("../data/dado-finais.csv", sep=";")
df

#%%

df = df.set_index(["cod", "nome", "período"])
#%%
df_stack = df.stack().reset_index().rename(columns={
    "level_3": "Tipo_Homicidio",
    0: "Qtd_homicidios"
})

#%%
df_stack.set_index(["cod", "nome", "período", "Tipo_Homicidio"]).unstack().reset_index()

