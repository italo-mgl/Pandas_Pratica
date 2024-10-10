#%%
preco = 1000

def calcular_imposto(preco):
    return preco * 0.3
calcular_imposto(1000)

#%%
calcular_imposto2 = lambda x: x*0.3
#%%

precos = [100,500,10,25]

impostos = list(map(lambda x: x*0.5,precos))
impostos