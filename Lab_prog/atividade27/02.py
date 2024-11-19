import numpy as np

matriz1 = np.array([[int(input(f"Digite o valor para matriz1[{i},{j}]: ")) for j in range(3)] for i in range(3)])
matriz2 = np.array([[int(input(f"Digite o valor para matriz2[{i},{j}]: ")) for j in range(3)] for i in range(3)])

print("escolha a operaçao")
print("a) imprimir matrizes")
print("b) soma matrizes 1 e 2")
print("c) multiplica matrizes 1 e 2")
print("d) subtraim matrizes 1 e 2")
opcao =input("opcao")

if opcao == "a":
    print("matrizes 1",matriz1)
    print("matrizes 2",matriz2)
elif opcao == "b":
    soma = matriz1 + matriz2
    print("soma das matrizes",soma)
elif opcao == "c":
    multiplicacao = matriz1 * matriz2
    print("multiplicacao das matrizes",multiplicacao)
elif opcao == "d":
    subtracacao = matriz1 - matriz2
    print("subtracacao das matrizes",subtracacao)
else:
    print("opcao invalida")
