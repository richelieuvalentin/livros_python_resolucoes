# criação das matrizes (3x3)
A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
R = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# ler os valores da matriz A
for I in range(3):
    for J in range(3):
        A[I][J] = int(input(f'A[{I+1}, {J+1}]? '))

# ler os valores da matriz A
for I in range(3):
    for J in range(3):
        B[I][J] = int(input(f'B[{I+1}, {J+1}]? '))

# calcular a multiplicação de A por B
for I in range(3):
    for J in range(3):
        R[I][J] = 0
        for K in range(3):
            R[I][J] += A[I][K] * B[K][J]

# mostrar a matriz resposta R
for I in range(3):
    for J in range(3):
        print(R[I][J], end="  ")
    print()
