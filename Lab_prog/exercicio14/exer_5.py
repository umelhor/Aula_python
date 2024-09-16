preco1=float(input(f"digite o preco do primeiro produto"))
preco2=float(input(f"digite o preco do segundo produto"))
preco3=float(input(f"digite o preco do terceiro produto"))


barato=min(preco1,preco2,preco3)

print(f"vc deve comprar o produto que custa R$ {barato}")