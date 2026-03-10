lista1 = ['azul']
print(f'Tamanho: {len(lista1)}, lista1: {lista1}')
lista1.append('vermelho')
print(f'Tamanho: {len(lista1)}, lista1: {lista1}')
lista2 = lista1.copy()  # criando uma lista nova como uma cópia
lista1.clear()  # removendo todos os elementos de lista 1
print(f'Tamanho: {len(lista1)}, lista1: {lista1}')
print(f'Tamanho: {len(lista2)}, lista2: {lista2}')
lista2.extend(['cinza', 'verde', 'vermelho'])
print(f'Tamanho: {len(lista2)}, lista2: {lista2}')
print("Posição de 'vermelho': ", lista2.index('vermelho'))  # qual o índice do primeiro elemento 'vermelho'?
print("Quantidade de 'vermelho': ", lista2.count('vermelho'))
lista2.insert(1, 'marrom')  # inserindo 'marrom' na posição 1
print(f'Tamanho: {len(lista2)}, lista2: {lista2}')
print('Removendo elemento posição 2: ', lista2.pop(2))
print(f'Tamanho: {len(lista2)}, lista2: {lista2}')
lista2.reverse()
print('Lista invertida: ', lista2)
lista2.sort()
print('Lista ordenada: ', lista2)
