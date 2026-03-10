vet = [0] * 10

for i in range(10):
    vet[i] = int(input(f'Número {i + 1}: '))
print("Vetor lido:", vet)

for i in range(0, 9, 1):
    menor = i
    for j in range(i+1, 10, 1):
        if vet[j] < vet[menor]:
            menor = j
    aux = vet[i]
    vet[i] = vet[menor]
    vet[menor] = aux
    print(vet)

print("Vetor ordenado:", vet)

