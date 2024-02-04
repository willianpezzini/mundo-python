from random import randint
from time import sleep
tentativas = 0
n1 = 0
n2 = randint(0, 10)
print('Adivinhe o número de 1 a 10 que o computador pensou!')
while n1 != n2:
    n1 = int(input('Digite seu numero: '))
    print('Jogador: {}'.format(n1))
    tentativas += 1
    sleep(1)
    if n1==n2:
        print('\033[0;32mParabéns, você acertou!\033[m')
    elif n1 > n2:
        print('ERROU!\nÉ um número MENOR. TENTE NOVAMENTE')
    elif n1 < n2:
        print('ERROU!\nÉ um número MAIOR. TENTE NOVAMENTE')
print('Fim de Jogo')
print('Você precisou de {} tentativas para conseguir acertar.'.format(tentativas))
