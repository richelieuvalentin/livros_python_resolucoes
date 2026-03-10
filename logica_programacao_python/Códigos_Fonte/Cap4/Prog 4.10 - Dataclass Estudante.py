from dataclasses import dataclass


# definição do dataclass com inicialização
@dataclass
class RegEstudante:
    Nome: str = ''
    N1: float = 0
    N2: float = 0
    Media: float = 0


# criação da variável composta
Est = RegEstudante()

Est.Nome = input("Qual o nome: ")
Est.N1 = float(input("Nota 1: "))
Est.N2 = float(input("Nota 2: "))
Est.Media = (Est.N1 + Est.N2) / 2

print(f'{Est.Nome} tem média = {round(Est.Media, 1)}')
