A = int(input("Lado 1: "))
B = int(input("Lado 2: "))
C = int(input("Lado 3: "))

if (A<B+C) and (B<A+C) and (C<A+B):
   if (A==B) and (B==C):
      print("Triângulo Equilátero")
   else:
      if (A==B) or (A==C) or (B==C):
         print("Triângulo Isósceles")
      else:
         print("Triângulo Escaleno")
else:
   print("Não formam um triângulo!")
