#%%
import pandas as pd

data_users = {
    "id": [1,2,3,4],
    "nome": ["Teo", "Mat", "Nah", "Mah"],
    "idade": [31,31,32,32]
}

df_user= pd.DataFrame(data_users)
df_user
#%%

data_transacao = {
    "id_users": [1,1,1,2,3,3],
    "vl": [432,532,123,6,4,87],
    "qtProdutos": [2,1,3,6,10,2]
}
df_transacao = pd.DataFrame(data_transacao)
df_transacao 

#%%

# SELECT*
# FROM df_transacao
# LEFT JOIN df_user
# ON df_transacao.id_user = df_user.id

df_transacao.merge(df_user,
                    how="left",
                    left_on="id_users",
                    right_on="id"
                    )
