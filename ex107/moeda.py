def aumentar(valor, percentual):
    resultado = (valor * percentual) / 100
    resp = valor + resultado
    return resp


def diminuir(valor, percentual):
    resultado = (valor * percentual) / 100
    resp = valor - resultado
    return resp


def dobro(valor):
    resp = valor * 2
    return resp


def metade(valor):
    resp = valor / 2
    return resp
