comprimento = float(input('Medida em Barra (Em Centimentros): '))
comprimento = comprimento / 2.54
print('Medida da Barra Em:')
print(f'Em Polegadas: {comprimento: .2f}')
comprimento = comprimento * 0.08
print(f'Em Pes: {comprimento: .2f}')