tam_arquivo_mb = float(input("Digite o tamanho do arquivo para download em Megabytes (MB): "))

velocidade_link_mb_por_seg = float(input("Digite a velocidade do link de internet em Megabytes por segundo (MB/s): "))

tam_arquivo_mbits = tam_arquivo_mb * 8

tempo_download_seg = tam_arquivo_mbits / velocidade_link_mb_por_seg

tempo_min = int(tempo_download_seg // 60)
tempo_seg = int(tempo_download_seg % 60)

print(f"O tempo aproximado de download é de {tempo_min} minutos e {tempo_seg} segundos.")
