from ex113.função import leiaInt, leiaFloat

numInt = leiaInt('Digite um valor Inteiro: ')
numReal = leiaFloat('Digite um valor Real: ')
print(f'\033[034mO valor Inteiro digitado foi: {numInt}')
print(f'O valor Real digitado foi: {numReal}\033[m')
