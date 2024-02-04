numero = int(input('Digite um número: '))
total = 0
for n in range(1,numero + 1):
    if numero % n ==0:
        print('\033[32m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(n), end=' ')
print('\n \033[mO número {}, teve uma divisão inteira {} vezes'.format(numero, total))
if total == 2:
    print('Por esse motivo ele É um número Primo')
else:
    print('Por esse motivo ele NÃO é um número Primo')