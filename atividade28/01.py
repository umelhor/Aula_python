import numby as np

matriz =np.random.randint(1,11,(3,3))
print("matriaz original",matriz)

determinante=np.linalg.det(matriz)
print("determinante",determinante)

if determinante ==0:
    inversa=np.linalg.inv(matriz)
    print("inversa",inversa)
else:
    print("matriz nao invertida")