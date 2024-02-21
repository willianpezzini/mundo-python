numeros = []
par = []
impar = []
while True:
    num = int(input('Digite um valor: '))
    numeros.append(num)
    if num % 2 == 0:
        par.insert(0, num)
    elif num % 2 == 1:
        impar.insert(0, num)
    resposta = str(input('Deseja continuar? [S/N]  ')).upper().strip()
    while resposta != 'N' and resposta != 'S':
        print('\033[031mOPÇÃO INVÁLIDA. Responda S para SIM ou N para NÃO.\033[m')
        resposta = str(input('Deseja continuar? [S/N]  ')).upper().strip()
    if resposta == 'N':
        break
numeros.sort()
par.sort()
impar.sort()
print('-=' * 30)
print(f'Todos os números digitados em ordem crescente foram: {numeros}')
print(f'Foram digitados {len(par)} números pares, sendo eles: {par}')
print(f'Foram digitados {len(impar)} números impares, sendo eles: {impar}')
print('-=' * 30)
