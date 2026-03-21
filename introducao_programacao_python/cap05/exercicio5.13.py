# Exercício 5-13
"""
Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o
valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total
de juros pago.
"""
# Ler as informações fornecidas pelo usuário
divida_inicial = float(input("Digite o valor inicial: "))
JURO_MENSAL = float(input("Digite a taxa de juros: ")) / 100
pagamento_mensal = float(input("Digite o valor do pagamento mensal: "))

# Inicializa as variáveis necessárias
prazo = 0
total_pago = 0
divida = divida_inicial

# Testa se o pagamento é suficiente para fazer a divída decrescer ao longo do tempo
if pagamento_mensal <= divida * JURO_MENSAL:
    print("O pagamento mensal é insuficiente para quitar a dívida.")
else:
    while divida > 0:
        # Capitaliza a dívida inicial
        divida = divida * (1 + JURO_MENSAL)

        # Contador para o prazo
        prazo += 1

        # Verifica se é o último mês
        if divida <= pagamento_mensal:
            total_pago += divida
            divida = 0
        # Realiza os pagamentos mensais e soma ao total pago
        else:
            divida -= pagamento_mensal
            total_pago += pagamento_mensal

        print(f"No mês {prazo} a dívida é : R$ {divida:.2f}")

    # Calcula o juros
    juros_pago = total_pago - divida_inicial

    # Output das informações
    print(
        f"Prazo total: {prazo} meses\n"
        f"Juros pago: R$ {juros_pago:.2f}\n"
        f"Total pago: R$ {total_pago:.2f} "
    )