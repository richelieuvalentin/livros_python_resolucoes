# inicialização da matriz com as distâncias entre as cidades
MatDistancia = [[0, 524, 521, 882],
                [524, 0, 434, 586],
                [521, 434, 0, 429],
                [882, 586, 429, 0]]

# inicialização dos contadores
Diagonal = 0
TriInf = 0
TriSup = 0

for I in range(4):
    for J in range(4):
        if I < J:  # triângulo superior
            TriSup += MatDistancia[I][J]
        elif I > J:  # triângulo inferior
            TriInf += MatDistancia[I][J]
        else:  # sobrou a diagonal, quando I == J
            Diagonal += MatDistancia[I][J]

print("Soma da diagonal principal: ", Diagonal)
print("Soma da triângulo superior: ", TriInf)
print("Soma da triângulo inferior: ", TriSup)
