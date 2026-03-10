# criação dos vetores de 10 posições reais
VetLido = [0.0] * 10
VetDes = [0.0] * 10

# loop de leitura do vetor
for X in range(10):
    VetLido[X] = float(input(f'Valor {X + 1}: '))

# cálculo da média do vetor digitado
MediaLido = sum(VetLido) / 10

# loop de diferenças
for X in range(10):
    VetDes[X] = abs(VetLido[X] - MediaLido)

# cálculo da média dos desvios
MediaDes = sum(VetDes) / 10

print(f'Média aritmética: {MediaLido:.2f}')
print(f'Desvio médio absoluto: {MediaDes:.2f}')
