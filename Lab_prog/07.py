# Criando a matriz 4x4 com valores entre 1 e 20
matriz_4x4 = np.random.randint(1, 21, (4, 4))

# Selecionando a submatriz com linhas e colunas 2 e 3 (índices 1 e 2 em Python)
submatriz = matriz_4x4[1:3, 1:3]

print("Matriz 4x4:\n", matriz_4x4)
print("Submatriz 2x2 (linhas e colunas 2 e 3):\n", submatriz)