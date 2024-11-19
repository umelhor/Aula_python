reservatorios=int(input("digite o numero de reservatorios: "))
matriz = np.random.randint(0,101,(30,reservatorios))

print("matriz de qualidade da agua (%)",matriz)

media_pureza = np.mean(matriz, axis=0)
print("nivel medio de pureza por reservatorio",media_pureza)

melhor_dia = np.argmax(matriz, axis=0) +1
pior_dia = np.argmin(matriz, axis=0) + 1
print("media dia por reservatorio",melhor_dia)
print("pior dia por reservatorio",pior_dia)

reservatorio_maior_media = np.argmax(media_pureza) +1
reservatorio_menor_media = np.argmin(media_pureza) +1
print("reservatorio com maior pureza media", reservatorio_maior_media)
print("reservatorio com menor pureza media", reservatorio_menor_media)
