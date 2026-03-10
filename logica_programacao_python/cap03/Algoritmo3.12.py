# Algoritmo 3.12 Média com repita
"""
- inicio
    # declaração de variáveis
    real:
        media, # média anual de um dado aluno
        acm, # acumulador
        media_turma; # média anual da turma
    inteiro:
        cont; # contador

    cont <- 0;
    acm <- 0;

    repita
        leia (media);
        acm <- acm + media;
        cont <- cont + 1;
    até (cont >= 50); # teste de condição
    media_turma <- acm / 50;
    escreva("média anual da turma =", media_turma);
- fim
"""

contador = 5
acumulador = 0
media_aluno = 0

while contador <= 5:
    acumulador += media_aluno
    contador += 1
    contador -= 1

media_turma = acumulador / 5
print(f"Média anual da turma: {media_turma}")