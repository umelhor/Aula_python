# Criando dois vetores de tamanho 5 com valores entre 1 e 10
vetor1 = np.random.randint(1, 11, 5)
vetor2 = np.random.randint(1, 11, 5)

# Calculando a soma dos vetores e o produto ponto
soma_vetores = np.add(vetor1, vetor2)
produto_ponto = np.dot(vetor1, vetor2)

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Soma dos vetores:", soma_vetores)
print("Produto ponto:", produto_ponto)