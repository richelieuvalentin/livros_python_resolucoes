# inicialização da matriz com as marcações de uma possível aposta na loteria esportiva
MatLoteria = [[' ', 'x', 'x'], [' ', 'x', ' '], ['x', ' ', ' '], ['x', ' ', 'x'], ['x', 'x', 'x'],
              [' ', ' ', 'x'], ['x', 'x', ' '], [' ', ' ', 'x'], [' ', 'x', ' '], ['x', 'x', ' '],
              ['x', 'x', 'x'], [' ', 'x', ' '], [' ', 'x', ' '], ['x', 'x', ' ']]
# declaração da lista com os tipos de jogos
VetTipoJogo = ["Simples", "Duplo", "Triplo"]

# inicialização dos contadores
ConSimples = ConDuplos = ConTriplos = 0

print("Cartão de loteria apostado:")
for i in range(14):
    ApostasLinha = 0
    # impressão da linha do cartão (jogo) para visualiação
    print(f'Jogo {i+1:2}: {MatLoteria[i]}', end='')
    for j in range(3):
        if MatLoteria[i][j] == 'x':
            ApostasLinha += 1
    if ApostasLinha == 1:
        ConSimples += 1
    elif ApostasLinha == 2:
        ConDuplos += 1
    else:
        ConTriplos += 1
    # impressão do tipo do Jogo
    print(f' é um {VetTipoJogo[ApostasLinha - 1]}')

print("Quantidade de jogos simples: ", ConSimples)
print("Quantidade de jogos duplos: ", ConDuplos)
print("Quantidade de jogos triplos: ", ConTriplos)
