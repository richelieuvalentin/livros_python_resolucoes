# Exercicio 3-09
"""
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
Calcule o total em segundos.
"""
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

# 1 dia -> 24 horas, 1 horas -> 60 minutos, 1 minuto -> 60 segundos, 1 h = 60 * 60 = 3600 segundos
segundos_total = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

print(f"O total em segundos é {segundos_total}.")