# Algoritmo 3.10 Média anual com finalizador (estrutura enquanto)

"""
- início
    # declaração de variavéis
    real: media, # média anual de um dado aluno
    acm, # acumulador
    media_turma; # média anual da turma
    inteiro: cont; # contador

    enquanto (media != -1) faça # teste de condicação de parada
        leia (media)
        se (media != -1) # evita acumulação do finalizador
            então
                inicio
                    acm <- acm + media
                    cont <- cont + 1
                fim;
        fimse;
    fimenquanto;

    se (cont > 0) # houve pelo menos uma execução
        então
            inicio
                media_turma <- acm / cont
                escreva ("Média anual da turma =", media_turma);
            fim;
        senão
            escreva ("Média inválida forncedida");
    fimse;
fimse.
"""

contador = 0
acumulador = 0
media = 0

while media != -1:
    media = float(input("Digite a média do aluno: "))
    if media != -1:
        acumulador = acumulador + media
        contador = contador + 1

if contador != 0:
    media_turma = acumulador / contador
    print(f"Média anual da turma: {media_turma}")
else:
    print("Nenhuma média válida")