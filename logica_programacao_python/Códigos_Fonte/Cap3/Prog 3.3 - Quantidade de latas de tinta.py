H = float(input("Altura: "))
R = float(input("Raio: "))
Area = (3.14*(R**2))+(2*3.14*R*H)
Litro = Area/3
Qtde = Litro/5
C = Qtde * 50.0
print(C, Qtde)
