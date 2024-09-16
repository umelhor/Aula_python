lado = float(input("Digite o tamanho do lado do tanque de combustível em metros (L): "))
altura = float(input("Digite a altura de preenchimento do tanque de combustível em metros (h): "))

vol_metros_cub = lado ** 2 * altura
vol_litros = vol_metros_cub * 1000
consumo_md_km_por_litro = 10
distancia_max_km = vol_litros * consumo_md_km_por_litro

print(f"A distância máxima de autonomia do carro é de {distancia_max_km:.2f} quilômetros.")
