import numpy as np

dias = 7
bairros = int(input("digite o numero de bairros: "))

matriz= np.random.randint(50, 500)

print("consumo de enegia",matriz)

consumo_medio = np.mean(matriz, axis=0)
print("consumo medio semanal de cada bairro", consumo_medio)

maior_consumo_por_dia = np.sum(matriz, axis=0)
bairro_maior_consumo = np.argmax(consumo_total) + 1
bairro_menor_consumo = np.argmin(consumo_total) + 1
print("bairro com maior consumo",bairro_maior_consumo)
print("bairro com menor consumo",bairro_menor_consumo)
