v = [float(input(f"Digite o número {i+1}: ")) for i in range(10)]
quadrados = [x ** 2 for x in v]

print("Vetor original:", v)
print("Vetor dos quadrados:", quadrados)
