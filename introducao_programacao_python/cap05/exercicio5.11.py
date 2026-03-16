# Exercício 5-11

"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no
período.
"""
deposito_inicial = float(input("Informe o valor do deposito: "))
TAXA_JUROS = float(input("Informe a taxa de juros: ")) / 100
prazo = 24
mes = 1
total = deposito_inicial

while mes <= prazo:
    total = total + deposito_inicial * TAXA_JUROS
    print(f"{mes} - R$ {total:.2f}")
    mes = mes + 1

juros = total - deposito_inicial
print(f"O total ganho com juros foi de R$ {juros}")