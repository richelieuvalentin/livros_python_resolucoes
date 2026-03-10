listaCompras = input("Nome do arquivo da lista? ")
con = 1
item = input(f"Qual o {con}o.item ('fim' para terminar)? ")
with open(listaCompras, "w", encoding='utf8') as arquivo:
    while item != 'fim':
        qtde = input("Qual a quantidade? ")
        linha = "Item " + str(con) + ": " + qtde + " - " + item + "\n"
        arquivo.write(linha)
        con += 1
        item = input(f"Qual o {con}o.item? ")
