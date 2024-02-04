velocidade = float(input('A qual velocidade o carro está? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Vá com Calma, você está acima do limite permitido 80Km/h.')
    print('Por esse motivo, você recebeu uma multa no valor de: R$ {:.2f}'.format(multa))
    print('DIRIJA COM CUIDADO!!!')
else:
    print('Muito bem, você está dirigindo à uma velocidade adequada à via.\nCONTINUE ASSIM!!!')
    print('DIRIJA COM CUIDADO!!!')
