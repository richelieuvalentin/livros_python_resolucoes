regioes = {
    'Sul': [
        {'nome': 'Paraná', 'sigla': 'PR', 'capital': 'Curitiba'},
        {'nome': 'Santa Catarina', 'sigla': 'SC', 'capital': 'Florianópolis'},
        {'nome': 'Rio Grande do Sul', 'sigla': 'RS', 'capital': "Porto Alegre"}
    ],
    'Centro-Oeste': [
        {'nome': 'Goiás', 'sigla': 'GO', 'capital': 'Goiânia'},
        {'nome': 'Mato Grosso', 'sigla': 'MT', 'capital': 'Cuiabá'},
        {'nome': 'Mato Grosso do Sul', 'sigla': 'MS', 'capital': "Campo Grande"},
        {'nome': 'Distrito Federal', 'sigla': 'DF', 'capital': 'Brasília'}
    ]
}

# acessos específicos ao dicionário
print(len(regioes))  # resulta em 2, as duas regiões
print(len(regioes['Centro-Oeste']))  # resulta em 4, os quatro dicionários
print(len(regioes['Centro-Oeste'][0]))  # resulta em 3, os 3 pares chave:valor
print(regioes['Centro-Oeste'][0]['nome'])  # imprimirá Goiás

# explorando o dicionário por completo
for regiao, estados in regioes.items():
    print(f"Região {regiao} possui {len(estados)} estados:")
    for est in estados:
        print(f"- {est['nome']} - {est['sigla']}, capital {est['capital']}")
    print()
