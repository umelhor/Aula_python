nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = 'A'
    status = "APROVADO"
elif 7.5 <= media < 9.0:
    conceito = 'B'
    status = "APROVADO"
elif 6.0 <= media < 7.5:
    conceito = 'C'
    status = "APROVADO"
elif 4.0 <= media < 6.0:
    conceito = 'D'
    status = "REPROVADO"
else:
    conceito = 'E'
    status = "REPROVADO"

print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")