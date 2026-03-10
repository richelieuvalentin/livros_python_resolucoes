# inicialização das distâncias
MatDistancia = [[0, 524, 521, 882],
                [524, 0, 434, 586],
                [521, 434, 0, 429],
                [882, 586, 429, 0]]

# inicialização das cidades
VetCidades = ["Vitória", "Belo Horizonte", "Rio de Janeiro", "São Paulo"]

# inicialização loop while
Origem = 0
Destino = 1
while Origem != Destino:
    print('''\nOpções de escolha: 
                0 - Vitória
                1 - Belo Horizonte
                2 - Rio de Janeiro
                3 - São Paulo''')
    Origem = int(input("Qual a origem? "))
    Destino = int(input("Qual o destino? "))
    print(f'Distância entre {VetCidades[Origem]} e {VetCidades[Destino]} = {MatDistancia[Origem][Destino]}')
