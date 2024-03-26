taxa_dolar = 5.50  
taxa_euro = 6.20   
taxa_libra = 7.60  
valor_em_reais = float(input("Digite o montante em reais (R$): "))
valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro
valor_em_libra = valor_em_reais / taxa_libra
print(f"Montante em reais: R$ {valor_em_reais:.2f}")
print(f"Montante em dólar: US$ {valor_em_dolar:.2f}")
print(f"Montante em euro: € {valor_em_euro:.2f}")
print(f"Montante em libra esterlina: £ {valor_em_libra:.2f}")
