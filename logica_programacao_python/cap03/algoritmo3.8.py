# Algoritmo 3.8 Média aritmética para 50 alunos
"""
- início
    declaração de variavéis
    real: n1, n2, n3, n4; # Notas bimestrais
        media; # média anual
    inteiro: cont # contador

    cont <- 0; # inicialização do contador

    enquanto (cont < 50) faça # teste da condição de parada
        leia (n1, n2, n3, n4); # entrada de dados
        media <- (n1 + n2 + n3 + n4) / 4; # cálculo da média
        escreva ("Média anual", media);

        se (media > 7)
            então
                início
                    escreva ("Aluno aprovado!");
                    escreva ("Parabéns!);
                fim;
            senão
                início
                    escreva ("Aluno reprovado!");
                    escreva ("Estude mais");
                fim;
        fimse;
        cont <- cont+1; # incrementar o contador em 1
    fimenquanto;
- fim.
"""

cont = 0

while cont < 50:
    nota_1 = float(input("Digite a nota 1: "))
    nota_2 = float(input("Digite a nota 2: "))
    nota_3 = float(input("Digite a nota 3: "))
    nota_4 = float(input("Digite a nota 4: "))
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    if media >= 7:
        print("Aluno aprovado!")
        print("Parabéns!")
    else:
        print("Aluno reprovado!")
        print("Estude mais!")
    cont += 1
