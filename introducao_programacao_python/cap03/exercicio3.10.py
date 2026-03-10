# Exercicio 3-10
"""
    Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento. 
Exiba o valor do aumento e do novo salário.
"""
salario = float(input("Digite o valor do salário: "))
aumento = float(input("Digite o percentual de aumento: "))
valor_aumento = salario * (aumento / 100)
novo_salario = salario + valor_aumento

print(f"O valor do aumento foi R${valor_aumento}, o novo salário será de R${novo_salario}.")