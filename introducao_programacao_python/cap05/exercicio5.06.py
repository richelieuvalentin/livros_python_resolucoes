# Exercício 5-06
"""
Altere o programa anterior para exibir os resultador no mesmo formato de uma
tabuada de multiplicação: 2 x 1 = 2, 2 x 2 = 4...
"""
n = int(input("Digite o valor de n: "))
x = 1

while x <= 10:
    print(f"{x} x {n} = {x * n}")
    x += 1