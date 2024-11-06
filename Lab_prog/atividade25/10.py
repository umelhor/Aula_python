vetor = [float(input(f"Digite o número {i+1}: ")) for i in range(10)]
negativos = sum(1 for x in vetor if x < 0)
soma_positivos = sum(x for x in vetor if x > 0)

print("Quantidade de números negativos:", negativos)
print("Soma dos números positivos:", soma_positivos)
