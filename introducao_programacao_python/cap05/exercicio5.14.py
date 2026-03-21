# Exercício 5-14
"""
Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o
usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a
soma e a média aritmética.
"""

soma = 0
quantidade = 0

# Inicia o laço sempre Verdadeiro
while True:
    numero = int(input("Digite um número inteiro: "))

    # Interrompe o laço caso o valor digitado seja 0
    if numero == 0:
        break

    # Atualiza as variáveis
    soma += numero
    quantidade += 1

# Devolve a quantidade, a soma e a média dos números
print(f"A quantidade de números digitados foi {quantidade}")
print(f"A soma = {soma}")
print(f"A média aritmética = {soma/quantidade:.2f}")