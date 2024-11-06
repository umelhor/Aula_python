vetor = [int(input(f"Digite o elemento {i+1}: ")) for i in range(8)]
x = int(input("Digite a posição X (0-7): "))
y = int(input("Digite a posição Y (0-7): "))

soma = vetor[x] + vetor[y]
print("Soma dos valores nas posições X e Y:", soma)
