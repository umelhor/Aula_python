salario_atual = float(input("Digite o salário do colaborador: R$ "))

if salario_atual <= 280.00:
    aumento = 0.20
elif salario_atual <= 700.00:
    aumento = 0.15
elif salario_atual <= 1500.00:
    aumento = 0.10
else:
    aumento = 0.05

valor_aumento = salario_atual * aumento
novo_salario = salario_atual + valor_aumento

print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {aumento * 100}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")