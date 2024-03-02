from random import randint
from time import sleep
from operator import itemgetter
cont = 0
maior = 0
jogadores = {'Jogador1': randint(1,6),
             'Jogador2': randint(1,6),
             'Jogador3': randint(1,6),
             'Jogador4': randint(1,6)}
ranking = list
for k,v in jogadores.items():
    print(f'O {k} tirou o número {v}.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('     -= RANKING DOS JOGADORES =-')
sleep(1)
for i, v in enumerate(ranking):
    print(f'{i + 1}º colocado: {v[0]} com o número {v[1]}.')
print('-=' * 20)




