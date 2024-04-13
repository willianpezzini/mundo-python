def aumentar(valor=0, percentual=0, formatado=False):
    resultado = (valor * percentual) / 100
    resp = valor + resultado
    if formatado is False:
        return resp
    else:
        return moeda(resp)


def diminuir(valor=0, percentual=0, formatado=False):
    resultado = (valor * percentual) / 100
    resp = valor - resultado
    if formatado is False:
        return resp
    else:
        return moeda(resp)

def dobro(valor=0, formatado=False):
    resp = valor * 2
    if formatado is False:
        return resp
    else:
        return moeda(resp)


def metade(valor=0, formatado=False):
    resp = valor / 2
    if formatado is False:
        return resp
    else:
        return moeda(resp)


def moeda(valor=0, moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')


def resumo(valor=0, aumento=0, reducao=0):
    print('-' * 40)
    print(f'{"RESUMO DE VALORES":^40}')
    print('-' * 40)
    print(f'Preço Analizado \t{moeda(valor)}')
    print(f'Dobro do Preço  \t{dobro(valor, True):<10}')
    print(f'Metade do Preço \t{metade(valor, True):<10}')
    print(f'{aumento}% de Aumento  \t{aumentar(valor, aumento, True):<10}')
    print(f'{reducao}% de Redução  \t{diminuir(valor, reducao, True):<10}')
    print('-' * 40)