print('-#-' * 11)
print('CALCULANDO SEQUÊCIA DE FIBONECCI')
print('-#-' * 11)
c = 3
t1 = 0
t2 = 1
vezes = int(input('Digite qual a quantidade de elementos da sequência você deseja ver: '))
print('-#-' * 11)
print('{} {}'.format(t1, t2), end= ' ')
while not c > vezes:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c = c + 1
    print('{}'.format(t3), end= ' ')
print('FIM')





