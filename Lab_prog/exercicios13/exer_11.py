import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros = area / 6

# Apenas latas de 18L
latas = math.ceil(litros / 18)
preco_latas = latas * 80

# Apenas galões de 3.6L
galoes = math.ceil(litros / 3.6)
preco_galoes = galoes * 25

# Mistura de latas e galões
latas_mistas = math.floor(litros / 18)
resto = litros - (latas_mistas * 18)
galoes_mistos = math.ceil(resto / 3.6)
preco_misto = (latas_mistas * 80) + (galoes_mistos * 25)

print(f"Apenas latas: {latas} latas - R$ {preco_latas:.2f}")
print(f"Apenas galões: {galoes} galões - R$ {preco_galoes:.2f}")
print(f"Mix de latas e galões: {latas_mistas} latas e {galoes_mistos} galões - R$ {preco_misto:.2f}")
