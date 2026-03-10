def Abastecer():
    global tanque
    tanque = "cheio"
    print("- Frentista : Abastecimento realizado. Seu tanque ficou", tanque)


# Bloco principal
tanque = "vazio"
print("- Você: Chegando no posto meu tanque estava", tanque)
Abastecer()
print("- Você: Saindo do posto meu tanque estava", tanque)
