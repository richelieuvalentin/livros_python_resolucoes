# Exercício 5-08
"""
Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo
segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que
podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
"""
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
contador = numero_2
produto = 0

while contador > 0:
    produto = produto + numero_1
    contador = contador - 1
print(f"{numero_1} x {numero_2} = {produto}")