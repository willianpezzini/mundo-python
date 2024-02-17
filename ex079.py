valores = []
resposta = ''
cont = 0
valor = 0
while True:
    num = (int(input('Digite um valor: ')))
    if num not in valores:
        valores.append(num)
        print('Adicionado com sucesso...')
    else:
        print('Valor duplicado,  ele não será adicionado.')
    resposta = input('Deseja continuar? [S/N]: ').strip().upper()
    if resposta == 'N':
        break
    elif resposta != 'N' and resposta != 'S':
        print('OPÇÃO INVÁLIDA. Tente novamente.')
valores.sort()
print('=*' * 30)
print(f'Os valores adicionados foram:{valores}')
print('ACABOU!!!')