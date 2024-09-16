import math

raio = float(input("Digite o valor do raio da caixa d'água em metros (R): "))
altura = float(input("Digite o valor da altura da caixa d'água em metros (H): "))

volume_metros_cubicos = math.pi * raio**2 * altura
volume_litros = volume_metros_cubicos * 1000
consumo_medio_litros_por_hora = 1350
tempo_autonomia_horas = volume_litros / consumo_medio_litros_por_hora

print(f"O tempo de autonomia da caixa d'água é de aproximadamente {tempo_autonomia_horas:} horas")
