# Exercício 5-19
"""
Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01, 0,02, 0,05,
0,10 e 0,50
"""

valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 10000 # R$ 100 em centavos
apagar = int(round(valor * 100)) # trabalhar com inteiros

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if atual >= 1000:
            print(f"{cedulas} cédula(s) de R$ {atual / 100:.2f}")
        else:
            print(f"{cedulas} moeda(s) de R$ {atual / 100:.2f}")

        if apagar == 0:
            break
        elif atual == 10000:
            atual = 5000
        elif atual == 5000:
            atual = 2000
        elif atual == 2000:
            atual = 1000
        elif atual == 1000:
            atual = 500
        elif atual == 500:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1

        cedulas = 0