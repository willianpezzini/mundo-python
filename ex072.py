from time import sleep
extenso = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
               'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
               'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE',
               'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número \033[32m{extenso[numero]}\033[m.')
    else:
        print('\033[0;31mOPÇÃO INVÁLIDA! Tente Novamente.\033[m')
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('FINALIZANDO...')
sleep(1)
print('Fim do Programa! Obrigado')
