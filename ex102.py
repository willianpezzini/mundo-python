def fatorial(num):
    """
    => Recebe um valor escolhido pelo usuário e retorna o seu Fatorial.
    :param num: Número escolhido pelo usuário.
    :return: Fatorial do número escolhido pelo usuário.
    """
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f


def show():
    resposta = str(input(f'Quer ver a conta inteira? [S/N] ')).strip().upper()
    while True:
        if resposta != 'S' and resposta != 'N':
            print('OPÇÃO INVÁLIDA, tente novamente.')
            resposta = str(input(f'Quer ver a conta inteira? [S/N] ')).strip().upper()
        elif resposta == 'N':
            break
        elif resposta == 'S':
            for c in range(num, 1, -1):
                print(f'{c} x ', end='')
            print(f' 1 = {fatorial(num)}')
            break


# Programa Principal
num = int(input('Digite um valor: '))
print(fatorial(num))
show()
print('Programa Finalizado!!!')
help(fatorial)

