print('-=' * 15)
print('CALCULANDO FATORIAL')
print('-=' * 15)
numero = int(input('Digite um valor: '))
resultado = 1
c = numero
while c > 0:
    print('{}'.format(c), end= '')
    print(' x ' if c > 1 else ' = ', end= '')
    resultado = resultado * c
    c = c - 1
print('{}'.format(resultado))



