vetor = [1, 0, 5, -2, -5, 7]

# Imprimir o vetor
print("Vetor original:", vetor)

# Calcular e imprimir a soma dos elementos ímpares
soma_impares = sum(num for num in vetor if num % 2 != 0)
print("Soma dos elementos ímpares:", soma_impares)

# Modificar a posição 4 e remover o último elemento
vetor[4] = 100
vetor.pop()

# Imprimir o vetor resultante
print("Vetor modificado:", vetor)
