n = int(input("Digite o tamanho do vetor: "))
v1 = [int(input(f"Digite o elemento {i+1}: ")) for i in range(n)]
v2 = v1[::-1]

print("Vetor V1:", v1)
print("Vetor V2 (invertido):", v2)
