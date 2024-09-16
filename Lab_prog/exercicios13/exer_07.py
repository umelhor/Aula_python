altura = float(input("Digite sua altura em metros: "))
genero = input("Digite 'M' para masculino ou 'F' para feminino: ").upper()

if genero == 'M':
    peso_ideal = (72.7 * altura) - 58
elif genero == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = "Gênero inválido."

print(f"Seu peso ideal é: {peso_ideal:.2f} kg" if isinstance(peso_ideal, float) else peso_ideal)
