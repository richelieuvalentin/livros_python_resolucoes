# Exercício 3-12
"""
Escreva um programa que calcule o tempo de uma viagem de carro. 
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""
distancia = float(input("Qual a distância a percorrer? "))
velocidade_media = float(input("Qual a velocidade média? "))
tempo = distancia / velocidade_media

print(f"O tempo de viagem é de {tempo} horas.")