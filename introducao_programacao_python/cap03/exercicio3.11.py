# Exercício 3-11
"""
Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço a pagar.
"""
preco = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Qual o percentual de desconto? "))
valor_desconto = (percentual_desconto/ 100) * preco
novo_preco = preco - valor_desconto

print(f"O desconto é de R$ {valor_desconto}")
print(f"O novo preço da mercadoria é R$ {novo_preco}")