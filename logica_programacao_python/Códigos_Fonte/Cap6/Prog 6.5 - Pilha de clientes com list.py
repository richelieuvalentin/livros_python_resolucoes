pilhaLocais = ["Bosque", "Museu"]
print(f'Tamanho: {len(pilhaLocais)}, Pilha: {pilhaLocais}')
pilhaLocais.extend(['Praça', 'Cinema'])
print(f'Tamanho: {len(pilhaLocais)}, Pilha: {pilhaLocais}')
pilhaLocais.append('Horto')
print(f'Tamanho: {len(pilhaLocais)}, Pilha: {pilhaLocais}')

while pilhaLocais:
    print("Voltando até:", pilhaLocais.pop())
