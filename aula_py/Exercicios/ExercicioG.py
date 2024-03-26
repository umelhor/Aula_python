valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_por_hora * horas_trabalhadas

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print(f"Salário Bruto: R$ {salario_bruto:}")
print(f"Desconto do Imposto de Renda (11%): R$ {imposto_renda:}")
print(f"Desconto do INSS (8%): R$ {inss:}")
print(f"Desconto do Sindicato (5%): R$ {sindicato:}")
print(f"Salário Líquido: R$ {salario_liquido:}")
