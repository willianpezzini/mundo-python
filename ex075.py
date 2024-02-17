from time import sleep
cont = ''
print('-=' * 15)
print('Escolha 4 números entre 0 e 10')
print('-=' * 15)
sleep(0.5)
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
n4 = int(input('Digite o 4º número: '))
print('-=' * 15)
numeros = (n1, n2, n3, n4)
print(f'Os números escolhidos foram:')
print(f'{numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 foi o {numeros.index(3)+ 1}º número escolhido.')
else:
    print('O número 3 não foi escolhido')
print(f'Os números pares digitados foram: ', end= ' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end= ' ')

