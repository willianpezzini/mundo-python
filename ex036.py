valor = float(input('Digite o valor do imóvel sem pontos ou vírgulas: R$ '))
salario = float(input('Digite o valor do seu salário bruto sem pontos ou vírgulas: R$ '))
prazo = int(input('Em quantos anos você gostaria de financiar seu imóvel? '))
totalmeses = prazo * 12
prestacao = valor / totalmeses
porcentagem = (30 * salario) / 100
print('Você deseja comprar um imóvel que custa: R$ {:.2f}.\nVocê tem um salário de: R$ {:.2f}.\nE deseja quitar seu imovel em : {} anos.'.format(valor, salario, prazo))
if prestacao <= porcentagem:
    print('PARABÉNS, iremos realizar seu financiamento.')
    print('O valor da prestação mensal é de: R${:.2f}'.format(prestacao))
else:
    print('Nestas condições, você irá comprometer mais do que 30% de sua renda com o financiamento. Para preservar sua saúde financeira, não iremos liberar seu financiamento.')




