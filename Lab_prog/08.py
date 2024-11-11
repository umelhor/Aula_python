def produto_matricial(matriz_a, matriz_b):
    return np.dot(matriz_a, matriz_b)

# Exemplo de uso com duas matrizes 2x2
matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[2, 0], [1, 2]])

resultado = produto_matricial(matriz_a, matriz_b)

print("Produto matricial:\n", resultado