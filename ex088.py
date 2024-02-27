from time import sleep
from random import randint
vezes = 0
bilhete = []
lista = []
cont = 0
cont2 = 1
num = []
print('-=' * 20)
print(F'              JOGO MEGA SENA       ')
print('-=' * 20)
vezes = (int(input('Digite quantos jogos você quer fazer? ')))
total = 1
while total <= vezes:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in bilhete:
            bilhete.append(num)
            cont += 1
        if cont >= 6:
            break
    bilhete.sort()
    lista.append(bilhete[:])
    bilhete.clear()
    total += 1
sleep(1)
print('-=' * 4, ' SORTEANDO OS NÚMEROS ', '-=' * 4)
for i,l in enumerate(lista):
    print(f'{i + 1}º Jogo: {l}')
    sleep(1)
print('-=' * 7, ' BOA SORTE ', '-=' * 7)



