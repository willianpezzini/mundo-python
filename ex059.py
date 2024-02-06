from time import sleep
soma = 0
multiplica = 0
maior = 0
opcao = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while opcao != 5:
    print('Você digitou os valores {} e {}.'.format(n1, n2))
    print('''Escolha no menu a baixo, o que você desejar fazer com estes números.
     [ 1 ] SOMAR
     [ 2 ] MULTIPLICAR
     [ 3 ] VER QUAL É MAIOR
     [ 4 ] NOVOS NÚMEROS
     [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        print('-=' * 40)
        soma = n1 + n2
        print('O valor da soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif opcao == 2:
        print('-=' * 40)
        multiplica = n1 * n2
        print('O valor da multiplicação entre {} e {} é igual à {}.'.format(n1, n2, multiplica))
    elif opcao == 3:
        print('-=' * 40)
        if n1 <= n2:
            maior = n2
        else:
            maior = n1
        print('O Maior valor entre {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('-=' * 40)
        print('Digite os valores novamente.')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor'))
    elif opcao == 5:
        print('-=' * 40)
        print('FINALIZANDO...')
        sleep(2)
    else:
        print('Opção invalida, tente novamente!')
    print('-=' * 40)
print('OBRIGADO, até a próxima')
print('FIM')
