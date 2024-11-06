notas = [float(input(f"Digite a nota do aluno {i+1}: ")) for i in range(15)]
media = sum(notas) / len(notas)

print("Média geral:", media)
