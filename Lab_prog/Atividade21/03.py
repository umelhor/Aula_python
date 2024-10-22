valores = input("digite diferentes valores de entradas").split()
for valor in valores:
    print(f"o valor '{valor}' e  do tipo {type(valor).__name__}")