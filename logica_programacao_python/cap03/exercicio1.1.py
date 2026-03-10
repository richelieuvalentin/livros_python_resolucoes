# Exercicio 1.1 

"""
    # variaveis
    a, b, c
    delta
    x1, x2
    
    entrada de dados
    leia (a, b, c)
    
    # Processamento
    delta = b ** 2 - 4*a*c
    x1 = (-b + delta * 1/2) / (2 * a)
    x2 = (b + delta * 1/2) / (2 * a)
    
    # Saída dos dados
    escreva(x1)
    escreva(x2)   
"""
# valores dos coeficientes da equação
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de a: "))

# discrimante da equação
delta = b ** 2 - 4 * a * c
print(delta)

# raízes da equação
x1 = (-b + delta ** (1/2)) / (2 * a)
x2 = (-b - delta ** (1/2)) / (2 * a)

# exibindo o valor de x1 e x2
print(x1, x2)





