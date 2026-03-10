# Algoritmo 3.6 Tipo de Triângulo
"""
- inicio 
    variáveis:ladoA, ladoB, ladoC;
    leia(ladoA, ladoB, ladoC);
    
    se (ladoA < ladoB + ladoC) e (ladoB < ladoA + ladoC) e (ladoC < ladoA+ ladoB)
        então
           se ((ladoA = LadoB) e (ladoB = ladoC)) 
                então
                    escreva("Triângulo Equilátero");
                senão
                    se ((ladoA = ladoB) ou (ladoA = lado C) ou (ladoB = ladoC))
                        então
                            escreva("Triângulo Isósceles");
                        senão
                            escreva("Triângulo Escaleno");
                    fimse;
            fimse;
        senão
        escreva("Estes valores não formam um triângulo");
    fimse
"""

# Algortimo 3.6 Tipo de Triângulo

# Lados do triângulo
ladoA = int(input("Digite o valor do lado A: "))
ladoB = int(input("Digite o valor do lado B: "))
ladoC = int(input("Digite o valor do lado C: "))

if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB):
    if (ladoA == ladoB) and (ladoB == ladoC):
        print("Triângulo Equilátero")
    else:
        if ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
else:
    print("Estes valores não formam um triângulo")