peso = float(input("Digite o peso dos peixes: "))
limite = 50
multa_por_quilo = 4.00

if peso > limite:
    excesso = peso - limite
    multa = excesso * multa_por_quilo
    print(f"Você excedeu {excesso:.2f} kg e a multa será de R$ {multa:.2f}")
else:
    print("Não houve excesso de peso.")
