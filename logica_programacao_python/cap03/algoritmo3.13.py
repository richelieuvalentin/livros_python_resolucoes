# Algoritmo 3.13 Descoberta do número

"""
- inicio
    inteiro:
        num, # número inicial a ser descoberto
        chute, # tentativa de acerto do número
        tent; # contador de tentativas

    tent <- 0;
    leia(num);

    repita
        leia(chute);
        tent <- tent + 1;
        se (chute > num)
            então
                escreva("Chutou alto")
            senão se (chute < num)
                    escreva("Chutou baixo")
                  fimse;
        fimse;
        até (num == chute);
        escreva("Número de tentativas: ", tent);
- fim
"""

numero = int(input("Digite o número a ser descoberto: "))
tentativas = 0
acertou = False

while not acertou:
    chute = int(input("Acerte o número: "))
    tentativas += 1
    if numero == chute:
        acertou = True
    elif numero < chute:
        print("Chutou alto!")
    else:
        print("Chutou baixo!")
print(f"Número de tentativas: {tentativas}")