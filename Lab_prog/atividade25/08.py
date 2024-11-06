vetor = [int(input(f"Digite o elemento {i+1}: ")) for i in range(10)]
maior = max(vetor)
posicao_maior = vetor.index(maior)

print("Vetor:", vetor)
print("Maior elemento:", maior, "na posição", posicao_maior)
