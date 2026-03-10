VLido = []
VPar = []
VImpar = []

for X in range(10):
    VLido.append(int(input(f'Número {X + 1}: ')))

for X in range(10):
    if VLido[X] % 2 == 0:
        VPar.append(VLido[X])
    else:
        VImpar.append((VLido[X]))

# impressão do vetor lido
print(f'Vetor lido: {VLido}')

# impressão do vetor de pares
print(f'Vetor PAR, de tamanho {len(VPar)}: {VPar}')

# impressão do vetor de ímpares
print(f'Vetor IMPAR, de tamanho {len(VImpar)}: {VImpar}')
