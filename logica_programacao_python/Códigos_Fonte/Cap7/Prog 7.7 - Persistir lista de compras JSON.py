import json

dic = {} # dicionário vazio
con = 1
qtde = int(input(f"Qual a quantidade do {con}o.item ('0' para terminar)? "))
while qtde != 0:
    unidade = input("Qual a unidade? ")
    item = input("Qual o item? ")
    dic.update({'Item ' + str(con): {'qtde': qtde, 'unidade': unidade, 'item': item}})
    con += 1
    qtde = int(input(f"Qual a quantidade do {con}o.item? "))

nomeArq = input("\nNome do arquivo da lista de compras? ")
with open(nomeArq, 'w') as arquivo:
    json.dump(dic, arquivo, indent=4)
