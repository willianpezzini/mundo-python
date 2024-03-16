from time import sleep


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c ==0:
        c = 1
    print('-=' * 20)
    print(f'SEQUÊNCIA DE {a} ATÉ {b}, PULANDO DE {c} EM {c}')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}  ', end='')
            sleep(1)
            cont += c
        print()
    else:
        cont = a
        while cont >= b:
            print(f'{cont}  ', end='')
            sleep(1)
            cont -= c
        print()
        print('-=' * 20)

contador(1, 10,1)
contador(10,0,2)
while True:
    resposta = (str(input('Deseja montar sua propria contagem? [S/N]: '))).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print('\033[031mOPÇÃO INVÁLIDA, digite S para SIM ou N para NÃO.\033[m')
        resposta = (str(input('Deseja montar sua propria contagem? [S/N]: '))).strip().upper()
    if resposta == 'N':
        break
    a = int(input('Digite o valor inicial: '))
    b = int(input('Digite o valor final: '))
    c = int(input('Digite o valor do passo: '))
    contador(a, b, c)
continua = (str(input('Deseja continuar? [S/N]: '))).strip().upper()
while resposta != 'S' and resposta != 'N':
    print('\033[031mOPÇÃO INVÁLIDA, digite S para SIM ou N para NÃO.\033[m')
    resposta = (str(input('Deseja continuar? [S/N]: '))).strip().upper()
    if resposta == 'N':
        break
print('<<< FINALIZANDO... >>>')
sleep(1)
print('<<<< FINALIZADO, OBRIGADO! >>>>')
