# Exercício 5-12
"""
Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de
juros do mês seguinte.
"""
# Entrada de dados, inicialização das variáveis
deposito_inicial = float(input("Informe o valor do deposito inicial: "))
TAXA_JUROS = float(input("Informe a taxa de juros: ")) / 100
prazo = 12
mes = 1
total = deposito_inicial
depositos_mensais = 0 # Inicializamos a variavel com 0, ainda não fizemos nenhum deposito

while mes <= prazo:

    # Recebe o valor do depósito do mês
    deposito_mes = float(input("Informe o valor do deposito do mês: "))

    # acumula os depositos mensais
    depositos_mensais = depositos_mensais + deposito_mes

    # Multiplica o total por 1 + taxa e só depois soma o depósito
    total = total * (1 + TAXA_JUROS) + deposito_mes
    print(f"Mês {mes} - Deposito do mês: {deposito_mes} - Total no mês R$ {total:.2f}")

    # Contador para o prazo
    mes = mes + 1

# Calcula o capital investido no período e os juros
capital_investido = deposito_inicial + depositos_mensais
juros = total - (depositos_mensais + deposito_inicial)

# Output das informações
print(
    f"O capital inicial foi de R$ {deposito_inicial:.2f} \n"
    f"O total investido foi de R$ {capital_investido:.2f} \n"
    f"Os juros foram R$ {juros:.2f} "
)