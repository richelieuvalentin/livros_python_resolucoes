from dataclasses import dataclass


# definição do dataclass
@dataclass
class RegEstudante:
    Nome: str
    Nota: list
    Media: float

# criação da variável composta com inicialização
Est = RegEstudante('', [0.0, 0.0, 0.0, 0.0], 0.0)

Est.Nome = input("Qual o nome: ")
for I in range(4):
    Est.Nota[I] = float(input(f'Nota {I + 1}: '))
    Est.Media = Est.Media + Est.Nota[I] * (I + 1) / 10

print(f'{Est.Nome} tem média = {round(Est.Media, 1)}')
