import numpy as np

matriz = np.random.randint(50, 500, (7,3))

print("matriz de producao semanal(itens)", matriz)

producao_total_turno = np.sum(matriz, axis=0)
print("producao total semanal por turno", producao_total_turno)

turno_maior_producao = np.argmax(producao_total_turno) + 1
print("turno com maior producao total:",turno_maior_producao)

dia_menor_producao = np.argmin(np.sum(matriz, axis=1)) + 1
dia_maior_producao = np.argmax(np.sum(matriz, axis=1)) + 1
print("dia com menor producao total", dia_menor_producao)
print("dia com maior producao total", dia_maior_producao)
