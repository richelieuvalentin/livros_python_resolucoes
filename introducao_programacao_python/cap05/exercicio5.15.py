# Exercício 5-15
"""
Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário
que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o
preço de cada produto:

Código Preço
1      0,50
2      1,00
3      4,00
5      7,00
9      8,00

Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve
gerar a mensagem de erro “Código inválido”.
"""

valor = 0

while True:
    codigo = int(input("Digite o código do produto: "))
    preco_produto = 0
    # Interrompe a repetição com o código 0
    if codigo == 0:
        break

    # Atualizar o valor de preço_produto de acordo com o código
    match codigo:
        case 1:
            preco_produto = 0.50
        case 2:
            preco_produto = 1.0
        case 3:
            preco_produto = 4.0
        case 5:
            preco_produto = 7.0
        case 9:
            preco_produto = 8.0

        # Qualquer outro código
        case _:
            print("Código inválido.")
            continue

    # Recebe a quantidade do produto
    quantidade_produto = int(input("Digite a quantidade: "))

    # Calcular o valor de compras
    valor = valor + (preco_produto * quantidade_produto)

print(f"Valor total das compras foi R$ {valor:.2f}")