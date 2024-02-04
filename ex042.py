print('-*-' * 20)
print('Analisador de Triângulos'.upper())
print('-*-' * 20)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Essas retas PODEM formar um triângulo')
    if r1 == r2 == r3:
        print('Esse é um Triângulo EQUILATERO, pois possui todos os lados iguais.')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Esse é um Triângulo ISÓSCELES, pois possui dois lados iguais e um diferente.')
    else:
        print('Esse é um Triângulo ESCALENO, pois NÃO possui nenhum lado igual.')
else:
    print('Essas retas NÃO PODEM formar um triângulo')
