# criação dos vetor de 10 posições reais
VetLido = [0.0] * 10

# inicialização das variáveis simples
Soma = 0
NotaAcima = 0

# loop de leitura de VClasse
for X in range(10):
   VetClasse[X] = float(input(f'Nota {X + 1}: '))

# loop para a Soma dos valores
for X in range(10):
    Soma = Soma + VetClasse[X]

Media = Soma / 10 # cálculo da média

# loop de contagem dos valores de VClasse acima da média
for X in range(10):
    if VetClasse[X] > Media:
        NotaAcima = NotaAcima + 1

print("Numero de notas acima da média: ", NotaAcima)
