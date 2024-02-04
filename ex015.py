d = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos Kms você percorreu com o carro? '))
d1 = d * 60
km1 = km * 0.15
t = d1 + km1
print('Por ter ficado com o carro {} dias e rodado {} Kms.\nVocê deverá pagar o valor de: R$ {:.2f}.'.format(d,km,t))

