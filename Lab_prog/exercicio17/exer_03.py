dia = int(input("Digite um número (1-7) para o dia da semana: "))

dias_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

if dia in dias_semana:
    print(f"Dia correspondente: {dias_semana[dia]}")
else:
    print("Valor Inválido!")