soma = 0
multiplica = 0
maior = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('Você digitou os valores {} e {}.'.format(n1, n2))
print('''Escolha no menu a baixo, o que você desejar fazer com estes números.
 [ 1 ] SOMAR
 [ 2 ] MULTIPLICAR
 [ 3 ] VER QUAL É MAIOR
 [ 4 ] NOVOS NÚMEROS
 [ 5 ] SAIR DO PROGRAMA''')
opcao = int(input('Qual a sua opção?'))
while not opcao == 5:
    if opcao == 1:
        soma = n1 + n2
        print('O valor da soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multiplica = n1 * n2
        print('O valor da multiplicação entre {} e {} é igual à {}.'.format(n1, n2, multiplica))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2

