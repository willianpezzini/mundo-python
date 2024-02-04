from random import randint
from time import sleep
print('='*40)
print('{:^40}'.format('JOKENPÔ'))
print('='*40)
itens = 'PEDRA', 'PAPEL', 'TESOURA'
computador = randint(0,2)
jogador = int(input('''Escolha uma das opções:
( 0 ) PEDRA
( 1 ) PAPEL
( 2 ) TESOURA
Qual a sua escolha? '''))
print('JO')
sleep (1)
print('KEN')
sleep (1)
print ('PÔ')
sleep (1)
print('=' * 40)
print('Você escolheu {}.'.format(itens[jogador]))
print('O computador escolheu {}.'.format(itens[computador]))
print('=' * 40)
if jogador > 2:
    print('\033[0:31mOPÇÃO INVÁLIDA. Tente uma das opções acima.')
elif jogador == computador:
    print('\033[0:33mOuve um empate, vamos tentar outra vez!')
elif jogador == 0 and computador == 2:
    print('\033[0:32mPARABÉNS! Você venceu!')
elif jogador == 1 and computador == 0:
    print('\033[0:32mPARABÉNS. Você venceu!')
elif jogador == 2 and computador == 1:
    print('\033[0:32mPARABÉNS. Você venceu!')
else:
    print('\033[0:31mVocê perdeu!')




