def Fibo(N):
    a = 1
    b = 1
    while a < N:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
    print()


# Bloco principal
Fibo(100)
Fibo(10000)
