# Algortimo 3.4 Média aritmética com aprovação
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
        fimse;
"""

# Algortimo 3.4 Média aritmética com aprovação

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
    print("Aluno Aprovado!")