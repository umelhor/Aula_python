import numpy as np

matriz = np.array([[int(input(f"digite o valor para a posiçao[{i},{j}]:")) for j in range(5)] for i in range(5)])

posicoes_nao_nulas = np.count_nonzero(matriz)

print("matriz lida",matriz)
print("numero de possicoes nao nulas", posicoes_nao_nulas)
