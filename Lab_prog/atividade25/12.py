vetor = [int(input(f"Digite o valor {i+1}: ")) for i in range(10)]
valores_iguais = set([num for num in vetor if vetor.count(num) > 1])

print("Valores iguais:", valores_iguais)
