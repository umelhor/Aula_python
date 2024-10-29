import pandas as pd

def estatisticas_descritivas():
    try:
        df = pd.read_excel("Epandas1.xlsx")
        estatisticas = df.describe()
        print("Estatísticas descritivas da planilha:")
        print(estatisticas)
    except FileNotFoundError:
        print("Arquivo 'Epandas1.xlsx' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

estatisticas_descritivas()
