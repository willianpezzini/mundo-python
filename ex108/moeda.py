def aumentar(valor=0, percentual=0,):
    resultado = (valor * percentual) / 100
    resp = valor + resultado
    return resp


def diminuir(valor=0, percentual=0):
    resultado = (valor * percentual) / 100
    resp = valor - resultado
    return resp

def dobro(valor=0, moeda='R$'):
    resp = valor * 2
    return resp


def metade(valor=0, moeda='R$'):
    resp = valor / 2
    return resp

def moeda(valor=0, moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')