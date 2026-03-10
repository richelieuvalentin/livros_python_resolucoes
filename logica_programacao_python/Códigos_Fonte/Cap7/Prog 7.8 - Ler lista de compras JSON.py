# apenas confirma como fazer para que ao salvar e ler esteja usando o mesmo char set (evitar problemas)
import json

nomeArq = input("Nome do arquivo da lista de compras? ")
with open(nomeArq) as arquivo:
    dic = json.load(arquivo)

print("\nLista de compras:")
for chave, item in dic.items():
    print(f"{chave}: {item['qtde']} {item['unidade']} {item['item']}")
