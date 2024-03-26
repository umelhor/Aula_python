import math

raio = float(input("Digite o valor do raio da esfera em metros (R): "))

volume_metros_cubicos = (4/3) * math.pi * raio**3

volume_l = volume_metros_cubicos * 10**3

print(f"O volume da esfera é: {volume_l:} litros")
