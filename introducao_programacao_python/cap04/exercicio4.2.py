# Exercício 4-02
"""
Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba 
uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por 
km acima de 80 km/h.
"""

velocidade = int(input("Qual a velocidade? "))
velocidade_maxima = 80

if velocidade > velocidade_maxima:
    multa = 5 * (velocidade - velocidade_maxima)
    print(f"O valor da multa é R$ {multa:.2f}")