import pickle
from dataclasses import dataclass


@dataclass
class regItem:
    qtde: int
    unidade: str
    item: str


listaCompras = []
con = 1
qtde = int(input(f"Qual a quantidade do {con}o.item ('0' para terminar)? "))
while qtde != 0:
    unidade = input("Qual a unidade? ")
    item = input("Qual o item? ")
    listaCompras.append(regItem(qtde, unidade, item))
    con += 1
    qtde = int(input(f"Qual a quantidade do {con}o.item? "))

nomeArq = input("\nNome do arquivo da lista de compras? ")
with open(nomeArq, 'wb') as arquivo:
    pickle.dump(listaCompras, arquivo)
