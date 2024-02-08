print('-' * 32)
print('SOMADOR DE NÚMEROS')
print('Digite 999 quando quiser parar!')
print('-' * 32)
total = 0
vezes = 0
t1 = 0
numero = 0
numero = int(input('Digite um número: '))
while numero != 999:
    total = total + numero
    vezes = vezes + 1
    numero = int(input('Digite um número: '))
print('Você digitou {} números, e a soma entre eles é {}'.format(vezes, total))

