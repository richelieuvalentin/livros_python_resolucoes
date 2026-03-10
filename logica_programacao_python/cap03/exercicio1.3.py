# Exercicio 1.3

"""
    # variaveis
    volume, pi, raio
    
    
    entrada de dados
    leia (raio)
    leia (pi = 3.14)
    
    # Processamento
    volume = 4 / 3 * pi * raio ** 3
    
    
    # Saída dos dados
    escreva(volume)
    
"""

# raio da esfera
raio = float(input("Digite o valor do raio: "))

# constante pi
pi = 3.14

# Cálculo do volume
volume = (4 / 3) * pi * (raio ** 3)

print(f"{volume:.2f}")