from dataclasses import dataclass


@dataclass
class regItem:
    item: str
    prox: int


listaTarefas = [regItem('Efetuar um saque no caixa automático', 5),
                regItem('Comprar os livros na livraria', 3),
                regItem('Deixar o carro no estacionamento', 7),
                regItem('Pegar as roupas na lavanderia', -1),
                regItem('Postar cartões de Natal no correio', 0),
                regItem('Comprar presente na loja de brinquedos', 1),
                regItem('Autenticar documentos no cartório', 4),
                regItem('Passar na banca de jornais', 6)]

comeco = 2  # começo da lista, primeira tarefa
tarefa = listaTarefas[comeco]
i = 1
print(f'Tarefa {i}: {tarefa.item}')
while tarefa.prox != -1:
    i += 1
    tarefa = listaTarefas[tarefa.prox]
    print(f'Tarefa {i}: {tarefa.item}')
