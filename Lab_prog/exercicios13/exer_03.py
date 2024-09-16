num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação: (+, -, *, /)")
operacao = input("Operação: ")

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

print(f"O resultado é: {resultado}")
