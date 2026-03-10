def Saudacao(Nome, Hora):
    if Hora < 12:
        Aux = "Bom dia"
    elif Hora >= 12 and Hora < 19:  # pode substituir por 12 <= Hora < 19
        Aux = "Boa tarde"
    else:
        Aux = "Boa noite"
    print(f"{Aux}, {Nome}!")


# Bloco principal
Saudacao("Pedro", 10)
Saudacao("Pedro", 15)
Saudacao("Pedro", 19)
