def calcular_fatorial():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Por favor, insira um número positivo.")
        else:
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            print(f"O fatorial de {numero} é: {fatorial}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

calcular_fatorial()
