VetLido = [0] * 10
VetPar = [0] * 10
VetImpar = [0] * 10

for X in range(10):
    VetLido[X] = int(input(f'Número {X + 1}: '))

P = 0
I = 0
for X in range(10):
    if VetLido[X] % 2 == 0:
        VetPar[P] = VetLido[X]
        P += 1
    else:
        VetImpar[I] = VetLido[X]
        I += 1

# impressão do vetor lido
print(f'Vetor lido: {VetLido}')

# impressão do vetor de pares
print(f'Vetor PAR, tamanho {P}: {VetPar[0:P]}')

# impressão do vetor de ípares
print(f'Vetor ÍMPAR, tamanho {I}: {VetImpar[0:I]}')
