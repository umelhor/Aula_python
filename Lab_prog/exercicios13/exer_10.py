area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros = area / 3
latas = litros / 18
preco = latas * 80
print(f"Você precisará de {latas:.2f} latas e o preço total será R$ {preco:.2f}")