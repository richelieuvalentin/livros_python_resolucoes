# Exercício 4-10
"""
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você 
deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação 
solicitada
"""
numero_1 = float(input("Digite o primeiro número: "))
operação = input("Digite a operação desejada (+), (-), (*), (/): ")
numero_2 = float(input("Digite o segundo número: "))

if operação == "+":
    resultado = numero_1 + numero_2
elif operação == "-":
    resultado = numero_1 - numero_2
elif operação == "*":
    resultado = numero_1 * numero_2
else:
    if operação == "/" and numero_2 != 0:
        resultado = numero_1 / numero_2
    elif operação == "/" and numero_2 == 0:
        resultado = None
        print("Erro: Divisão por zero não permitida!")
    else:
        print("Digite uma operação válida!")
print(f"Resultado: {resultado}")