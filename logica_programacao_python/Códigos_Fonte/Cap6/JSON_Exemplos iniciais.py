d = {}
carro = {'marca': 'Volkswagen', 'modelo': 'Fusca', 'ano': 1971}
numeros = {1: 'um', 2: 'dois', 3: 'três', 4:'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove'}
contato = {
    'nome' : 'Fulano de Tal',
    'email': 'fulano@empresatal.com.br',
    'idade': 50
}

print(numeros[2])  # imprimindo a chave 2, imprimirá em tela: dois
print(contato['nome'])  # imprimirá em tela: Fulano de Tal
contato['email'] = 'fulano@emptal.com'  # alterando o valor do email do contato
contato['CPF'] = '123.456.789-00'  # adicionando um novo par, chave CPF
numeros.pop(6)  # remove o par de chave 6

print(carro)  # imprimir o dicionário completo

carro.clear()  # remove todos os elementos do dicionário carro


# iterando sobre as chaves de contato
for chave in contato:
    print(chave)

# mesmo loop usando o método keys()
for chave in contato.keys():
    print(chave)

# iterando sobre as valores de contato
for chave in contato:
    print(contato[chave])

# mesmo loop usando o método values()
for valor in contato.values():
    print(valor)