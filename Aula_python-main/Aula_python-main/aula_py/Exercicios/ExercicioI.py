import math

x1 = float(input("Digite a coordenada x1 do ponto P: "))
y1 = float(input("Digite a coordenada y1 do ponto P: "))
x2 = float(input("Digite a coordenada x2 do ponto Q: "))
y2 = float(input("Digite a coordenada y2 do ponto Q: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"A distância entre os pontos P e Q é: {distancia:.2f}")
