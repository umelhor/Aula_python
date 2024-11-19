import numby as np

matriz = np.random.randint(1,16(5,3))
print("matriz original", matriz)

tranposta =  matriz.T
print("tranposta original", tranposta)

print("dimosoes matriz original",matriz.shape)
print("dimensoes da matriz transposta",tranposta.shape)