# Programa 5.1: Contagem de cédulas
valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor

while True:
    if atual >= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédulas de R$ {atual}")
        if apagar == 0:
            break
        elif cedulas == 50:
            atual = 20
        elif cedulas == 20:
            atual = 10
        elif cedulas == 10:
            atual = 5
        elif cedulas == 5:
            atual = 1
        cedulas = 0

        
