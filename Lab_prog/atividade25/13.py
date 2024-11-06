vetor = [int(input(f"Digite o valor {i+1}: ")) for i in range(20)]
sem_repetidos = list(dict.fromkeys(vetor))

print("Vetor sem repetidos:", sem_repetidos)
