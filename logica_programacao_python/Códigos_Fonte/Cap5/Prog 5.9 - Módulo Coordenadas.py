def lerCoordenadas():
    x = int(input("Coordenada X: "))
    y = int(input("Coordenada y: "))
    return x, y # monta um  tupla  (x, y), posições 0 e 1 contem x e y


# Bloco principal
# opção 1, recebendo como tupla em coord
coord = lerCoordenadas()
print(coord[0], coord[1])

# opção 2, desempacotando a tupla retornada em a, b
a, b = lerCoordenadas()
print(a, b)
