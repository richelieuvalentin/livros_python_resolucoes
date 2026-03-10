# Exercício 4-11
"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve 
perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação 
mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a 
comprar dividido pelo número de meses a pagar.
"""
valor_imovel = float(input("Digite o valor do imóvel (R$): "))
renda_mensal = float(input("Digite o valor da renda mensal (R$): "))
prazo = float(input("Digite a quantidade de anos para pagamento: "))
prestação = valor_imovel / (prazo * 12)

if prestação > (0.3 * renda_mensal):
    print(f"Empréstimo Reprovado! A prestação {prestação} é maior que o aprovado!")
else:
    print("Emprestimo aprovado!")