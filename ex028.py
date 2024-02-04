from random import randint
n1 = int(input('Digite um número inteiro entre 0 e 5 tentando acertar qual foi o número que o computador "pensou": '))
n2 = randint(0,5)
print(n1)
print(n2)
if n1==n2:
    print('Parabéns, você acertou!')
else:
    print('Que pena, tente novamente!')
