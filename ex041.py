from datetime import date
anonascimento = int(input('Digite o ano do seu nascimento: '))
anoatual = date.today().year
idade = anoatual - anonascimento
if idade <= 9:
    print('Você tem {} anos, sua categoria é a MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, sua categoria é a INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, sua categoria é a  JÚNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos, sua categoria é a SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos, sua categoria é a MASTER!'.format(idade))
