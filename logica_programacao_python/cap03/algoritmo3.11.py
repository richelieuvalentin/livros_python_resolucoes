# Algoritmo 3.11 Média aritmética de um conjunto de números pares
"""
- inicio
    inteiro:
    n, # número fornecido pelo usuário
    cont, # contador
    acm; # acumulador
    real:
    media_pares; # média dos números pares

    cont <- 0; # inicialização do contador
    acm <- 0; # inicialização do acumulador
    n <- 1; # inicialização da variável de leitura

    enquanto ( n > 0); faça # teste da condição de parada
        leia (n);
        se (n > 0) e ((n mod 2) = 0); # resto da divisão é a zero?
            então # número é par(divisível por 2) e maior que 0
                inicio
                    acm <- acm + n; # acumula em acm os números pares
                    cont <- cont + 1; # contagem dos números pares
                fim
        fimse;
    fimenquanto;
    se (cont > 0) # houve pelo menos um número par válido
     então
        inicio
            media_pares <- acm / cont;
            escreva ("Média =" media_pares );
        fim;
        senão
            escreva ("Nenhum par foi fornecido");
    fimse;
- fim
"""

contador = 0
acumulador = 0
n = 1

while n > 0:
    n = int(input("Digite um número: "))
    if (n > 0) and (n % 2) == 0:
        contador += 1
        acumulador += n

if contador > 0:
    media_pares = acumulador / contador
    print(f"Média = {media_pares}")
else:
    print("Nenhum par foi fornecido")