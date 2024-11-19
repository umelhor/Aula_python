import numby as np

matriz=np.random.randint(1,21,(4,4))
print("matriz",matriz)

determinante=np.linalg.det(matriz)
print("determinante",determinante)

if np.isclose(determinante,0):
    print("a matriz e singular (determinante iqual a zero.)")
else:
    print("A matriz nao e singular (determinante diferente de zero)")