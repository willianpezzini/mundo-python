produto = float(input('Digite o valor do produto, com ponto para ceparar apenas os centavos: R$ '))
formapagamento = int(input('''Escolha a uma forma de pagamento:
( 1 ) À vista no Dinheiro/Cheque, com 10% de desconto.
( 2 ) À vista no Cartão, com 5% de desconto.
( 3 ) Em 2 vezes no cartão, sem juros.
( 4 ) Em 3 ou mais vezes no cartão, com juros.
Digite a opção de pagamento aqui: '''))
if formapagamento == 1:
    desconto1 = 10 * produto / 100
    print('Pagando à vista no dinheiro ou cartão, você irá pagar R$ {:.2f} neste produto.'.format(produto - desconto1))
elif formapagamento == 2:
    desconto2 = 5 * produto / 100
    print('Pagando à vista no cartão, você irá pagar R$ {:.2f} neste produto'.format(produto - desconto2))
elif formapagamento == 3:
    print('Pagando em 2x no cartão, você irá pagar R$ {:.2f} em cada parcela, totalizando o valor de R$ {:.2f}.'.format(produto / 2, produto))
elif formapagamento == 4:
    vezes = int(input('Digite a quantidade de parcelas que você gostaria de fazer, tendo um limite de 12x: '))
    if vezes > 12:
        print('\033[31mOPÇÃO INVÁLIDA\nVocê pode parcelar este produto em até 12 vezes. Tente Novamente')
    else:
        juros = 20 * produto / 100
        parcela = (produto + juros) / vezes
        print('Você escolheu fazer o pagamento em {} vezes no cartão.\nPortanto você pagará {} vezes de R$ {:.2f}.\nTotalizando o valor de {:.2f}'.format(vezes, vezes, parcela, (juros + produto)))
else:
    print('\033[31mOPÇÃO INVÁLIDA\nEscolha uma das opções descritas a cima.')

