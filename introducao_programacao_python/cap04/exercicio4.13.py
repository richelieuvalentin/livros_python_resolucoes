# Exercício 4-13:
"""
No programa a seguir, inverta as linhas do if e else, negando a condição. Adicione as linhas necessárias 
para fazê-lo funcionar em Python.
"""
"""
if a > b:
    print('a é menor que b')
else:
    print('b é maior que a')
"""
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

if a <= b:
    print("b é maior ou igual que a")
else:
    print("a é maior que b")