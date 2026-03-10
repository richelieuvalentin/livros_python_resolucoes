# Programa 4.3: Cálculo do imposto de renda
salário = float(input("Digite o salário: "))
base = salário
imposto = 0

if base > 3000:
    imposto += (base - 3000) * 0.35
    base = 3000
if base > 1000:
    imposto += (base - 1000) * 0.20

print(f"Salário: R$ {salário:6.2f} Imposto a pagar: R$ {imposto:6.2f}")