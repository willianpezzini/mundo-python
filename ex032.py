from datetime import date
ano = int(input('Qual ano você gostaria de saber se é ou não Bissexto? Digite 0 para saber sobre o ano atual. '))
if ano == 0:
    ano == date.today().year
if ano % 4 == 0 and ano % 100 != 0 or  ano % 400 == 0:
    print('O ano de {} é Bissexto!'.format(ano))
else:
    print('O ano de {} NÃO é Bissexto!'.format(ano))
#print(anoatual)



