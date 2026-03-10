import pickle
from dataclasses import dataclass


@dataclass
class regDespesa:
    dia: int
    mes: int
    categoria: int
    valor: float
    descricao: str


categorias = {1: 'Despesas Fixas', 2: 'Transporte', 3: 'Alimentação', 4: 'Lazer', 5: 'Saúde'}
listaDespesas = []
con = 1

dia = int(input(f"Qual a data da {con}a. despesa ('0' para terminar)? "))
while dia != 0:
    mes = int(input("Qual o mes? "))
    print(categorias)
    categoria = int(input("Qual a categoria? "))
    valor = float(input("Qual o valor? "))
    descricao = input("Qual a descrição? ")
    listaDespesas.append(regDespesa(dia, mes, categoria, valor, descricao))
    con += 1
    dia = int(input(f"\nQual a data da {con}a. despesa ('0' para terminar)? "))

with open('gastos.pickle', 'wb') as arquivo:
    pickle.dump(listaDespesas, arquivo)

