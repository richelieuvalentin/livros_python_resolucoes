# Algoritmo 3.14 Repita com escolha
"""
- inicio
    caracter:
        tipo_vinho; # tipo de vinho
    inteiro:
        cont_vinho, # contador vinho
        cont_tinto, # contador tinto
        cont_branco, # contador branco
        cont_rose; # contador rose
    real:
        porc_tinto, # porcentagem de tinto
        porc_branco, # porcentagem de branco
        porc_rose; # porcentagem de rose

    # inicialização dos diversos contadores
    cont_vinho <- 0;
    cont_tinto <- 0;
    cont_branco <- 0;
    cont_rose <- 0;

    repita
        leia(tipo_vinho);
            escola tipo_vinho
                caso "t": cont_tinto <- cont_tinto + 1;
                caso "b": cont_branco <- cont_branco + 1;
                caso "r": cont_rose <- cont_rose + 1;
            fimescolha;
        cont_vinho <- cont_vinho + 1;
    até (tipo_vinho = "F");
    cont_vinho <- cont_vinho - 1; # descontar o finalizador "F"

    se (cont_vinho > 0)
        então
            inicio
                porc_tinto <- (cont_tinto * 100) / cont_vinho;
                porc_branco <- (cont_vinho * 100) / cont_vinho;
- fim
"""