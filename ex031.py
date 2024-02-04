distancia = float(input('Qual a quantidade de Kms da sua viagem? '))
if distancia <= 200:
    print('Você ira pagar R${:.2f}, na sua passagem.'.format(distancia * 0.50))
else:
    print('Você ira pagar R${:.2f}, na sua passagem'.format(distancia * 0.45))