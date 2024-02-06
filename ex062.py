from time import sleep
print('=*=' * 12)
print('\033[0;34mCALCULANDO PROGRESSÃO ARITIMÉTICA\033[m')
print('=*=' *12)
c = 0
vezes = 10
termo = int(input('Digite o valor do termo: '))
razao = int(input('Digite o valor da razão: '))
print(termo, end= ' ')
while c < 9:
    termo = termo + razao
    print(termo,end= ' ')
    c = c + 1
mais = int(input('\nQuantos termos você quer mostrar a mais? '))
while mais != 0:
    novo = 0
    c = 0
    while c < mais:
        termo = termo + razao
        print(termo, end= ' ')
        c = c + 1
        vezes = vezes + 1
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
if mais == 0:
    print('FINAALIZANDO...')
    sleep(1)
    print('Foram exibidos {} termos desta PA.'.format(vezes))
    print('OBRIGADO')
