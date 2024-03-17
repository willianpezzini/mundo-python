from random import randint
from time import sleep
numeros = []
par = []
total = []

def sorteia(a,b):
    sleep(1)
    cont = 0
    while cont < 5:
        num = randint(a, b)
        numeros.append(num)
        cont += 1
        if cont >= 6:
            break


def somapar(* num):
    for valor in numeros:
        if valor % 2 == 0:
            par.append(valor)
    soma = 0
    cont = 0
    for valor in par:
        if cont == 0:
            soma = valor
        else:
            soma += valor
        cont += 1
    total.append(soma)


#Programa Principal
print(f'{"SORTEIO DE  NÚMEROS": ^30}')
a = int(input('Inicio: '))
b = int(input('Fim: '))
print('-=' * 20)
print(f'SORTEANDO NÚMEROS ENTRE {a} E {b}')
sorteia(a,b)
somapar()
sleep(1)
print(f'Os números sorteados foram: {numeros}')
sleep(1)
print(f'Os números pares sorteados foram {par}')
sleep(1)
print(f'E a soma entre eles é {total}')
print('-=' * 20)