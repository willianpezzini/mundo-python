import math
numero = int(input('Digite um número intero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número que você escolheu foi {}.\nE ele é um número PAR!'.format(numero))
else:
    print('O número que você escolheu foi {}.\nE ele é um número IMPAR!'.format(numero))
