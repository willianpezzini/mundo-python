numero = int(input('Digite um número intero que você deseja converter: '))
opcao = int(input('''Escolha uma das opções a baixo:
( 1 ) Para converter o número para BINÁRIO:
( 2 ) Para converter o número para OCTAL: 
( 3 ) Para converter o número para HEXADECIMAL:
OPÇÃO: '''))
if opcao == 1:
    print('O valor digitado foi {}. Ele convertido para BINÁrio vale: {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O valor digitado foi {}. Ele convertido para OCTAL vale: {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O valor digitado foi {}. Ele convertido para HEXADECIMAL vale: {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida, tente uma das opções mostradas acima!')
