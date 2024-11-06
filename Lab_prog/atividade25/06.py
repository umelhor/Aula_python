vetor = [int(input(f"Digite o elemento {i+1}: ")) for i in range(10)]
contagem_pares = sum(1 for num in vetor if num % 2 == 0)

print("Quantidade de valores pares:", contagem_pares)
