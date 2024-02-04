from datetime import date
sexo = str(input('Digite M se você for Mulher, ou H se você for Homem. ')).upper().strip()
if sexo == 'M':
    print('''No Brasil, o Alistamento Militar é OPCIONAL para mulheres.
Se desejar se alistar, procure a Junta de Serviço Militar da sua Cidade no ano que você completar 18 anos''')
elif sexo == 'H':
    pergunta = str(input('Você já fez o seu Alistamento Militar? ')).upper().strip()
    if pergunta == 'SIM':
        print('Muito Bem! Bom trabalho!')
    elif pergunta == 'NÃO':
        anonascimento = int(input('Digite o ano do seu nacimento: '))
        anoatual = date.today().year
        idade = anoatual - anonascimento
        print('Quem nasceu em {}, tem {} anos em {}'.format(anonascimento, idade, anoatual))
        if idade < 18:
            anosfaltantes = 18 - idade
            alistamentofuturo = (anonascimento + 18)
            print('Você ainda não está com a idade correta para o Alistamento Militar!')
            print('Ainda faltam {} anos para seu Alistamento'.format(anosfaltantes))
            print('Seu alistamento deve acontecer no ano de {}'.format(alistamentofuturo))
        elif idade == 18:
            print('Você deve fazer o Alistamento Militar NESTE ano. Procure a Junta de Serviço Militar de sua Cidade.')
        else:
            anos = idade - 18
            anoalistamento = (anonascimento + 18)
            print('Você já passou da idade mínima para fazer o Alistamento Militar.')
            print('Já passaram {} anos do seu alistamento. Você deveria ter se Alistado em {}'.format(anos, anoalistamento))
            print('Procure a Junta de Serviço Militar de sua Cidade.')
    else:
        print('Você precisa escrever SIM ou NÃO para a resposta anterior. Tente novamente')
else:
    print('Você digitou uma opção invalida, tente novamente')


