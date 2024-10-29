import math

def calcular_seno():
    try:
        angulo_graus = float(input("Digite o ângulo em graus: "))
        angulo_radianos = math.radians(angulo_graus)
        seno = math.sin(angulo_radianos)
        print(f"O seno de {angulo_graus}° é: {seno:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

calcular_seno()
