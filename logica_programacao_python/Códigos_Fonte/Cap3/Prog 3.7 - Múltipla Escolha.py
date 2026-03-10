Preco = float(input("Preço: "))
Origem = int(input("Origem: "))
if Origem == 1:
   print(Preco, " – Sul")
elif Origem == 2:
   print(Preco, " - Norte")
elif Origem == 3:
   print(Preco, " - Leste")
elif Origem == 4:
   print(Preco, " - Oeste")
elif Origem == 7 or Origem == 8 or Origem == 9:
   print(Preco, " - Sudeste")
elif Origem in range(10,21):
   print(Preco, " - Centro-Oeste")
elif Origem == 5 or Origem == 6 or Origem in range(25, 31):
   print(Preco, " - Nordeste")
else:
   print(Preco, " - Importado")
