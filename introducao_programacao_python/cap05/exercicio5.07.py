# Exercício 5-07
"""
Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez
de começar com 1 e 10.
"""
n = int(input("Tabuada de: "))
inicio = int(input("Digite o número para o início da tabuada: "))
fim = int(input("Digite o número para o fim da tabuada: "))

while inicio <= fim:
    print(f"{inicio} x {n} = {inicio * n}")
    inicio += 1