import numby as np

matriz=np.random.randint(1,101(6,6))
print("matriz:",matriz)

media=np.mean(matriz)
devio_padrao=np.std(matriz)
valor_max=np.max(matriz)
valor_min=np.min(matriz)

print("media dos elementos:",media)
print("desvio padrao:",devio_padrao)
print("valor max",valor_max)
print("valor min",valor_min)