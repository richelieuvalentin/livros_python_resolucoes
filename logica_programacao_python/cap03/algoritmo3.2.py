# Algoritmo 3.2 - Média Aritmética

"""
inicio # começo do algoritmo

    # delcaração das variáveis
    real: nota_1, nota_2, nota_3, nota_4 # notas bimestrais
          media # média anual
          
    # entrada de dados
    leia (nota_1, nota2, nota_3, nota_4);
    
    # Processamento
    media = (nota_1, nota2, nota_3, nota_4) / 4
    
    # saída de dados
    escreva (media) 
"""

# variaveis
nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
nota_3 = float(input("Digite a nota 3: "))
nota_4 = float(input("Digite a nota 4: "))

# calculo da média
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# exibindo o valor da média
print(media)