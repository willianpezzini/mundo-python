print('=' * 40)
print('{:^40}'.format('BANCO TIJUCAS'))
print('=' * 40)
valor = int(input('Qual o valor que você deseja sacar? R$ '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'Total de {totalcedula} de R$ {cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print('=' * 30)
print('Obrigado, volte sempre')



