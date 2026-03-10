# Programa 4.10: Planos da Tchau com elif
válido = True
plano = input("Qual o seu plano de celular? ")

if plano == "falopouco":
    minutos_plano = 100
    extra = 0.20
    preço = 50
elif plano == "falomuito":
    minutos_plano = 500
    extra = 0.15
    preço = 99
else:
    válido = False
if not válido:
    print(f"Erro: Não conheço este plano {plano}")
else:
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar: ")
    print(f"Preço do plano  R$ {preço:10.2f}")
    suplmento = 0
    if minutos_consumidos > minutos_plano:
        suplmento = extra * (minutos_consumidos - minutos_plano)
    print(f"Suplemento      R$ {suplmento:10.2f}")
    print(f"Total           R$ {preço + suplmento:10.2f}")