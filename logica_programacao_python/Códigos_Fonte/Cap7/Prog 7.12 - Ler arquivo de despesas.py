import pickle
from dataclasses import dataclass


@dataclass
class regDespesa:
    dia: int
    mes: int
    categoria: int
    valor: float
    descricao: str


categorias = {
    1: 'Despesas Fixas', 2: 'Transporte', 3: 'Alimentação', 4:'Lazer', 5: 'Saúde'
}
meses = {
    1: 'jan', 2: 'fev', 3: 'mar', 4:'abr', 5: 'mai', 6: 'jun',
    7: 'jul', 8: 'ago', 9: 'set', 10: 'out', 11: 'nov', 12: 'dez'
}
totais = [0, 0, 0, 0, 0]
totalGeral = 0
listaDespesas = []

with open('gastos.pickle', 'rb') as arquivo:
    listaDespesas = pickle.load(arquivo)

print("\nListagem das despesas")
print("Data\t\tCategoria\t\t\tValor\t\tDescrição da despesa")
for con in range(len(listaDespesas)):
    despesa = listaDespesas[con]
    totalGeral = totalGeral + despesa.valor
    totais[despesa.categoria-1] = totais[despesa.categoria-1] + despesa.valor
    print(f"{despesa.dia:02}/{meses[despesa.mes]}\t\t{categorias[despesa.categoria]:15}\t\t{despesa.valor:.2f}\t\t{despesa.descricao}")

print("\nResumo das despesas por categoria")
for con in range(len(totais)):
    print(f"{categorias[con+1]}: {totais[con]:.2f}")

print(f"\nTotal geral: {totalGeral:.2f}")