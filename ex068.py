from random import randint
from time import sleep
computador = 0
jogador = 0
escolha = 0
resultado = 0
cont = 0
print('#-' * 10)
print('\033[034mJOGO DO PAR OU IMPAR\033[m')
print('#-' * 10)
while True:
    escolha = str(input('Escolha Par ou impar \nDigite [P ou I]: ')).strip().upper()
    if escolha != 'P' and escolha != 'I':
        print('\033[031mOPÇÃO INVÁLIDA. Tente Novamente\033[m')
        break
    jogador = int(input('Digite um valor: '))
    sleep(1)
    print('--' * 10)
    if escolha == 'P':
        print('Você escolheu Par')
    else:
        print('Você escolheu Impar')
    print('PROCESSANDO...')
    print('--' * 10)
    sleep(2)
    computador = randint(0, 10)
    resultado = computador + jogador
    print(f'Você jogou {jogador}, o computador jogou {computador}')
    print(f'Resultado foi {resultado} ')
    if escolha == 'P':
        if resultado % 2 == 0:
            print('Parabens, você venceu!')
            cont = cont + 1
            print('--' * 10)
        else:
            break
    elif escolha == 'I':
        if resultado % 2 != 0:
            print('Parabéns, você venceu!')
            cont = cont + 1
            print('--' * 10)
        else:
            break
print('-#' * 15)
print('Você perdeu! O jogo Acabou')
print(f'Você teve um total de {cont} vitórias.')
print('-#' * 15)


