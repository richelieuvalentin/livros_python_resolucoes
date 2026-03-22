# Exercício 5-18
"""
Modifique o programa 5.1 para também trabalhar com notas de R$ 100.
"""

valor = float(input("Digite o valor a pagar: "))
cedulas = 0
centavos = valor // 10
atual = 100
apagar = valor

while True:
    # Compara apagar com atual(cédula de maior valor)
    # Atualiza o valor de apagar e conta as cédulas
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédulas de R$ {atual}")
        if apagar == 0:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
