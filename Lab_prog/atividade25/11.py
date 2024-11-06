vetor = [float(input(f"Digite o valor {i+1}: ")) for i in range(5)]
maior = max(vetor)
menor = min(vetor)

print("Posição do maior valor:", vetor.index(maior))
print("Posição do menor valor:", vetor.index(menor))
