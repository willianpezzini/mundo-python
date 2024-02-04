n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('Você digitou os números {} e {}. Comparando eles o PRIMEIRO é o maior!'.format(n1, n2))
elif n1 < n2:
    print('Você digitou os números {} e {} . Comparando eles, o SEGUNDO é o maior!'.format(n1, n2))
else:
    print('Você digitou os números {} e {}. Comparando os dois, NÃO existe valor maior, pois eles são iguais!'.format(n1, n2))

