from time import sleep
numero = int(input('Digite um valor: '))
media = 0
maior = numero
menor = numero
total = numero
c = 1
resposta = 0
resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
while resposta == 'S':
    numero = int(input('Digite um valor: '))
    c = c + 1
    if menor <= numero:
        menor = menor
    elif menor > numero:
        menor = numero
    if maior <= numero:
            maior = numero
    elif maior > numero:
        maior = maior
    total = total + numero
    resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resposta == 'N':
        print('FINALIZANDO...')
        sleep(1)
    elif resposta != 'S' and resposta != 'N':
        print('\033[031mOpção inválida! Tente novamente.\033[m\nUse 0 para SIM e 1 para NÃO.')
media = total / c
if resposta != 'S' and resposta != 'N':
    print('\033[031mOpção inválida! Tente novamente.\033[m\nUse 0 para SIM e 1 para NÃO.')
else:
    print('Você digitou {} números.\nO maior entre eles é {}\nO menor é {}\nE a média entre eles é {:.2f}'.format(c, maior, menor, media))