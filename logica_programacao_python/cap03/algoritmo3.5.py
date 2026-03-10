# Algortimo 3.5 Média aritmética com aprovação
"""
- inicio
    # Varáveis : 
        nota_1, nota_2, nota_3, nota_4 # notas bimestrais
        media # média anual
        
        leia: (nota_1, nota_2, nota_3, nota_4);
        media = (nota_1, nota2, nota_3, nota_4) / 4;
        escreva: ("Média ANual = ", media)
        
        se (media > 7)
            então
                - inicio # bloco verdade
                escreva("Aluno Aprovado!")
                escreva("Parabéns")
            fim
            senão
                - inicio # bloco falsidade
                escreva("Aluno Reprovado")
                escreva(Estude Mais!)
        fimse
    fim          
"""

# Algortimo 3.5 Média aritmética com aprovação

# variaveis
nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
nota_3 = float(input("Digite a nota 3: "))
nota_4 = float(input("Digite a nota 4: "))

# calculo da média
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# exibindo o valor da média
print(media)

# Condicional 
if media > 7:
    # bloco verdade
    print("Aluno Aprovado!")
    print("Parabéns")
else:
    # bloco falsidade
    print("Aluno Reprovado")
    print("Estude Mais!") 
