# Implementação do Algoritmo 6.12 (versão completa para zebrado)
from dataclasses import dataclass

@dataclass
class Dia:
   dt: int = 0
   em: int = 800
   sm: int = 1200
   et: int = 1400
   st: int = 1800
@dataclass
class totDia:
   atraso: int = 0
   horas: int  = 0

cartao = [None] * 31
totalDia = [None] * 31
for i in range(31):
   cartao[i] = Dia()
   totalDia[i] = totDia()
cont = toth = totatr = 0

def Entrada():
   global cartao, cont
   dia = int(input("Dia do mês (0 para sair): "))
   while (dia>0) and (dia<32):
      a = int(input("Entrada manhã (hhmm): "))
      b = int(input("Saída manhã   (hhmm): "))
      c = int(input("Entrada tarde (hhmm): "))
      d = int(input("Saída tarde   (hhmm): "))
      cartao[cont].dt = dia
      cartao[cont].em = a
      cartao[cont].sm = b
      cartao[cont].et = c
      cartao[cont].st = d
      cont += 1
      dia = int(input("Dia do mês (0 para sair): "))

def Calculo():
   global cartao, totalDia, cont, toth, totatr

   def Minuto(H):
      m = ((H // 100) * 60) + (H % 100)
      return m

   def Atraso(H, periodo):
      if Minuto(H) > periodo:
         a = Minuto(H) - periodo
      else:
         a = 0
      return a

   def Total(HE, HS):
      t = Minuto(HS) - Minuto(HE)
      return t

   for i in range (0, cont):
      totalDia[i].atraso = Atraso(cartao[i].em,480) + Atraso(cartao[i].et, 840)
      totalDia[i].horas = Total(cartao[i].em, cartao[i].sm) + Total(cartao[i].et, cartao[i].st)
      toth += totalDia[i].horas
      totatr += totalDia[i].atraso

def Impressao():
   global cartao, totalDia, cont, toth, totatr
   print('Dias informados -----------------------------------------')
   for i in range(0, cont):
      print(f'Dia {cartao[i].dt:02} ', end='')
      print(f'{cartao[i].em // 100:02}:{cartao[i].em % 100:02}-{cartao[i].sm // 100:02}:{cartao[i].sm % 100:02},', end='')
      print(f'{cartao[i].et // 100:02}:{cartao[i].et % 100:02}-{cartao[i].st // 100:02}:{cartao[i].st % 100:02}', end='')
      print(f', total {totalDia[i].horas // 60:02}:', end='')
      print(f'{totalDia[i].horas % 60:02}', end='')
      print(f', atraso {totalDia[i].atraso // 60:02}:', end='')
      print(f'{totalDia[i].atraso % 60:02}')
   print('Totalização ---------------------------------------------')
   print(f'Dias    {cont}')
   print(f'Horas   {(int(toth/cont))//60:02}:{(int(toth/cont))%60:02}h em média, ', end='')
   print(f'{toth//60:02}:{toth%60:02}h no total')
   print(f'Atrasos {(int(totatr/cont))//60:02}:{(int(totatr/cont))%60:02}h em média, ', end='')
   print(f'{totatr//60:02}:{totatr%60:02}h no total')

# Bloco principal
Entrada()
if (cont>0):
   Calculo()
   Impressao()
