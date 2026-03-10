from dataclasses import dataclass


# definição do dataclass
@dataclass
class RegEstudante:
    Nome: str
    Nota: list
    Media: float

# criação da variável com inicialização
Equipe = [None] * 4
for I in range(4):
    Equipe[I] = RegEstudante('', [0.0, 0.0, 0.0, 0.0], 0.0)

for I in range(4):
    Equipe[I].Nome = input("Qual o nome: ")
    for J in range(4):
        Equipe[I].Nota[J] = float(input(f'Nota {J + 1}: '))
        Equipe[I].Media = Equipe[I].Media + Equipe[I].Nota[J] * (J + 1) / 10
    print(f'{Equipe[I].Nome} tem média = {round(Equipe[I].Media, 1)}')
