import pickle
from dataclasses import dataclass


@dataclass
class regItem:
    qtde: str
    item: str


nomeArq = input("\nNome do arquivo da lista de compras? ")
with open(nomeArq, 'rb') as arquivo:
    listaCompras = pickle.load(arquivo)

print(listaCompras)

print("\nResumo da lista de compras:")
for con in range(len(listaCompras)):
    item = listaCompras[con]
    print(f"Item {con + 1}: {item.qtde} {item.unidade} {item.item}")
