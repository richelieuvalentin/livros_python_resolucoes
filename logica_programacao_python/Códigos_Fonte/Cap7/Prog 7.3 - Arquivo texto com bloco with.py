lin = 1
qtde = 0
with open('Drummond.txt', encoding='utf8') as arquivo:
    for linha in arquivo:
        linha = linha.rstrip()
        tam = len(linha)
        print(f"Linha {lin:2d} ({tam:2d} caracteres): {linha}")
        lin += 1
        qtde += tam
print("Total de caracteres no arquivo:", qtde)
