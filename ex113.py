def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO, digite um valor numérico válido!\033[m ')
            continue
        else:
            return num



def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO, digite um valor numérico válido!\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[031mERRO, o usuário não digitou um valor!\033[m')
            return 0
        else:
            return num


numInt = leiaInt('Digite um valor Inteiro: ')
numReal = leiaFloat('Digite um valor Real: ')
print(f'\033[034mO valor Inteiro digitado foi: {numInt}')
print(f'O valor Real digitado foi: {numReal}\033[m')
