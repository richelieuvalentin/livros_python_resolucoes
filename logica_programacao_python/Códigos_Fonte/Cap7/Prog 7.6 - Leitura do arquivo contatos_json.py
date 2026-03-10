import json
with open('contatos.json', encoding='utf8') as arquivo:
    contatos = json.load(arquivo)

for numContato, dadosContato in contatos.items():
    print(f"{dadosContato['nome']}:")
    print(f"   E-mail: {dadosContato['email']}:")
    if dadosContato['filhos'] is not None:
        print(f"   Filhos: {dadosContato['filhos']}")
