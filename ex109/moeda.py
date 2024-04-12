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