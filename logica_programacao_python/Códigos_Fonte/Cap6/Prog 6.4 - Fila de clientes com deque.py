from collections import deque

filaClientes = deque(["Ciclano", "João"])
print(f'Tamanho: {len(filaClientes)}, Fila: {filaClientes}')
filaClientes.extend(['Beltrano', 'José'])
print(f'Tamanho: {len(filaClientes)}, Fila: {filaClientes}')
filaClientes.append('Fulano')
print(f'Tamanho: {len(filaClientes)}, Fila: {filaClientes}')

while filaClientes:
    print("Atendendo:", filaClientes.popleft())
