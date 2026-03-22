# Programa 5.3: Tabuada sem repetições aninhdas
tabuada = 1
numero = 1
while numero <= 10:
    print(f"{numero} x {tabuada} = {numero * tabuada}")
    numero += 1
    if numero == 11:
        numero = 1
        tabuada += 1