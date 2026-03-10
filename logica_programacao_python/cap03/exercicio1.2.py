# Exercicio 1.2 

"""
    # variaveis
    x1, y1, x2, y2
    distancia
    
    entrada de dados
    leia (x1, y1, x2, y2)
    
    # Processamento
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    
    # Saída dos dados
    escreva(distancia)
    
"""

# dados do ponto P
x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))

# dados do ponto Q
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

# calculo da distância
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

# distância entre os pontos P e Q
print(distancia)
