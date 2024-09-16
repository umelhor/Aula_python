tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet = float(input("Digite a velocidade da sua internet em Mbps: "))

tempo_segundos = tamanho_arquivo / (velocidade_internet / 8)
tempo_minutos = tempo_segundos / 60

print(f"O tempo aproximado de download será de {tempo_minutos:.2f} minutos.")
