def Fibo(n):
    # Imprime uma sequência de Fibonacci de 1 até o limite superior n fornecido
    a = 1
    b = 1
    while a < n:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
    print()


def Par(Num):
    # Retorna True quando Num for par, False quando for ímpar
    if Num % 2 == 0:
        return True
    else:
        return False
