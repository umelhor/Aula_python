turno=input("digite o seu o seu turno M-matutino V-vespertino e N-Noturno").upper()

if turno == "M":
    print(f"Bom dia")
elif turno == "V":
    print(f"Boa tarde")
elif turno == "N":
    print(f"boa noite")
else:
    print(f"valor invalido")

