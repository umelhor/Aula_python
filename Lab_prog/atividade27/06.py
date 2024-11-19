atletas = int(input("digite o numero de atletas: "))
modalidades =int(input("digite o numero de modalidades"))
matriz = np.random.randint(0,100(atletas,modalidades))

print("Matriz de pontuaçao dos atletas", matriz)

media_por_atleta = np.mean(matriz, axis=1)
print("media da pontuaçao dos atletas", media_por_atleta)

maior_pontuacao_modalidade = np.argmax(matriz, axis=0) + 1
print("atletas com maior pontuaçao por modalidade", maior_pontuacao_modalidade)

media_por_modalidade = np.mean(matriz, axis=0)
modalidade_maior_media = np.argmax(media_por_modalidade) + 1
modalidade_menor_media = np.argmin(media_por_modalidade) + 1
print("modalidade com maior media de pontuaçao", modalidade_maior_media)
print("modalidade com menor media de pontuacao", modalidade_menor_media)