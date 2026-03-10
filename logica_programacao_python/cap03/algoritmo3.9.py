# Algoritmo 3.9 Média aritmética de 50 alunos
"""
- início
    # declaração de variavéis
    real: media, # média anual de um dado aluno
        acm, # acumulador
        media_turma; # média anual da turma
    inteiro: cont; # contador

    acm <- 0 # inicialização do acumulador
    cont <- 0 # inicialização do contador

    enquanto (cont < 50) faça # teste de condição
        leia (media);
        acm <- acm + media; # soma em acm dos valores lidos em media
        cont <- cont + 1; # contagem do número de médias fornecidas
    fimenquanto;

    media_turma <- (acm + media) / 50; # cálculo da média anual da turma
    escreva ("Média anual da turma = " + media_turma)
- fim.
"""
acumulador = 0
cont = 0

while cont < 50:
    media_aluno = float(input("Digite a média do aluno: "))
    acumulador += media_aluno
    cont += 1

media_turma = acumulador / 50
print(f"A média anual da turma é {media_turma}")

