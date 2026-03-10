from random import randint

Tent = 0
Chute = 0
Num = randint(1, 100)

while Chute != Num:
    Chute = int(input("Chute? "))
    Tent = Tent + 1
    if Chute > Num:
        print("Chutou alto!")
    elif Chute < Num:
        print("Chutou baixo!")
print("Tentativas: ", Tent)
