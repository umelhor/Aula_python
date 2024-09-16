import math

litros_por_lt = 5
metros_quad_por_l = 3
custo_por_lt = 50

raio = float(input("Digite o valor do raio do tanque cilíndrico em metros (R): "))
altura = float(input("Digite o valor da altura do tanque cilíndrico em metros (H): "))

area_l = 2 * math.pi * raio * altura
area_b = 2 * math.pi * raio ** 2
area_t = area_l + area_b
litros_necessarios = area_t / metros_quad_por_l

latas_necessarias = math.ceil(litros_necessarios / litros_por_lt)
custo_total = latas_necessarias * custo_por_lt
print(f"Quantidade de tinta necessária: {litros_necessarios:} litros")
print(f"Quantidade de latas necessárias: {latas_necessarias} latas")
print(f"Custo total: R$ {custo_total:}")
