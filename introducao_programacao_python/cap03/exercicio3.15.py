# Exercício 3-15
"""
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade 
de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de 
vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""
cigarros_dia = int(input("Quantos cigarros por dia? "))
anos_fumante = int(input("Quantos anos fumando? "))
minutos_perdidos = cigarros_dia * 10 * (anos_fumante * 365)

# 1 dia -> 1440 minutos
total_dias = minutos_perdidos / (24 * 60)

print(f"O total de dias perdidos foi de aproxamidamente {total_dias}.")