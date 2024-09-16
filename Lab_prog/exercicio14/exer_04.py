nota1 = float(input("digite sua primeira nota"))
nota2= float(input("digite sua segunda nota"))

media = (nota1 +nota2 /2)

if media ==10:
    print(f"aprovado com distinçao")
elif media >= 7:
 print(f"aprovado")
else:
    print(f"reprovado")