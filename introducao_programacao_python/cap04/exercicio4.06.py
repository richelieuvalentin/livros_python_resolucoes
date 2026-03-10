# Exercício 4-06
"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o 
preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais 
longas.
"""
distância = float(input("Qual a distância a ser percorrida (km): "))


if distância <= 200:
    preço_km = 0.50
    print(f"O valor total é R$ {distância * preço_km:.2f}")
else:
    preço_km = 0.45
    print(f"O valor total é R$ {distância * preço_km:.2f}")   