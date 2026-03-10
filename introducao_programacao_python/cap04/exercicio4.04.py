# Exercício 4-04
"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários 
superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""

salário = float(input("Digite o valor do salário: "))
percentual = 0.1
if salário < 1250:
    percentual = 0.15
aumento = salário * percentual

print(f"Salário: R$ {salário} aumento: R$ {aumento}")