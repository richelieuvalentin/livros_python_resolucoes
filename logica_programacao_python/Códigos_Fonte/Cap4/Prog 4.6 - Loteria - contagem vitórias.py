# inicialização da matriz com as marcações de uma possível aposta na loteria esportiva
MatLoteria = [[' ', 'x', 'x'], [' ', 'x', ' '], ['x', ' ', ' '], ['x', ' ', 'x'], ['x', 'x', 'x'],
              [' ', ' ', 'x'], ['x', 'x', ' '], [' ', ' ', 'x'], [' ', 'x', ' '], ['x', 'x', ' '],
              ['x', 'x', 'x'], [' ', 'x', ' '], [' ', 'x', ' '], ['x', 'x', ' ']]
ConMandante = ConEmpate = ConVisitante = 0

print("Cartão de loteria apostado:")
for i in range(14):
    print(f'Jogo {i + 1:2}: {MatLoteria[i]}')

for j in range(3):
    JogosColuna = 0
    for i in range(14):
        if MatLoteria[i][j] == 'x':
            JogosColuna += 1
    if j == 0:
        ConMandante = JogosColuna
    elif j == 1:
        ConEmpate = JogosColuna
    else:
        ConVisitante = JogosColuna

print("Vitória do mandante: ", ConMandante)
print("Empate: ", ConEmpate)
print("Vitória do visitante: ", ConVisitante)
