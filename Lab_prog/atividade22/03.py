
import pandas as pd

def soma_valores_planilha():
    try:
        df = pd.read_excel("Epandas1.xlsx")
        soma_total = df['valor'].sum()
        print(f"A soma total dos valores é: {soma_total}")
    except FileNotFoundError:
        print("Arquivo 'Epandas1.xlsx' não encontrado.")
    except KeyError:
        print("A coluna 'valor' não foi encontrada na planilha.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

soma_valores_planilha()
