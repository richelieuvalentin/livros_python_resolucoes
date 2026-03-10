# Exercício 4-08
"""
Reescreva o Programa 4.4 e calcule a conta da operadora Tchau usando else.
"""
plano = input("Qual é o seu plano de celular? ")

if plano != "falopouco" and plano != "falomuito":
    print("Não conheço este plano")
else:
    if plano == "falopouco":
        minutos_no_plano = 100
        extra = 0.20
        preço = 50
    else:
        minutos_no_plano = 500
        extra = 0.15
        preço = 99

        minutos_consumidos = int(input("Quantos minutos você consumiu? "))
        print("Você vai pagar: ")
        print(f"Preço do plano------R$ {preço:10.2f}")
        suplemento = 0

    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
        print(f"Suplemento------R$ {suplemento:10.2f}")
        print(f"Total------R$ {preço + suplemento:10.2f}")