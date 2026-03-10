# Exercício 4-12:
"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a 
quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para 
comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

+---------------------------------------+ 
|   Preço por tipo e faixa de consumo   | 
+---------------------------------------+ 
| Tipo        | Faixa (kWh)   | Preço   | 
+=======================================+ 
| Residencial | Até 500       | R$ 0,40 | 
|             | Acima de 500  | R$ 0,65 | 
+---------------------------------------+ 
| Comercial   | Até 1000      | R$ 0,55 | 
|             | Acima de 1000 | R$ 0,60 | 
+---------------------------------------+ 
| Industrial  | Até 5000      | R$ 0,55 | 
|             | Acima de 5000 | R$ 0,60 | 
+---------------------------------------+
"""
kwh = float(input("Qual a quantidade de Kwh consumida? "))
tipo_instalação = input("Qual o tipo de instalação? R para residências, I para indústrias e C para comércios: ")

if tipo_instalação == "R":
    if kwh <= 500:
        preço_a_pagar = kwh * 0.40
    else:
        preço_a_pagar = kwh * 0.60
elif tipo_instalação == "C":
    if kwh <= 1_000:
        preço_a_pagar = kwh * 0.55
    else:
        preço_a_pagar = kwh * 0.60
else:
    if kwh <= 5_000:
        preço_a_pagar = kwh * 0.55
    else:
        preço_a_pagar = kwh * 0.60
print(f"O total a pagar é R$ {preço_a_pagar:7.2f}")