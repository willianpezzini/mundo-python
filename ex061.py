print('=*=' * 12)
print('\033[0;34mCALCULANDO PROGRESSÃO ARITIMÉTICA\033[m')
print('=*=' *12)
c = 0
termo = int(input('Digite o primeiro valor: '))
razao = int(input('Digite o segundo valor: '))
print(termo, end= ' ')
while c < 9:
    termo = termo + razao
    print(termo,end= ' ')
    c = c + 1
print('FIM')
