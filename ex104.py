
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[031mERRO, digite um valor numérico válido!\033[m ')
        if ok:
            break
    return valor


num = leiaInt('Digite um valor: ')
print(f'Você digitou o valor {num}')
