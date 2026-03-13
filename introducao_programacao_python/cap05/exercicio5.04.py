# Exercício 5-04
"""
Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez,
apenas os números ímpares.
"""
# x = 1
# fim = int(input("Digite o último número a imprimir: "))
# while x <= fim:
#     print(x)
#     x += 2

x = 0
fim = int(input("Digite o último número a imprimir: "))

while x <= fim:
    if x % 2 != 0:
        print(x)
    x += 1