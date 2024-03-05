from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: ')).title()
ano = date.today().year
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = ano - dados['nascimento']
del dados['nascimento']
dados['carteira'] = int(input('Número da Carteira de Trabalho, digite 0 se não possuir: '))
if dados['carteira'] != 0:
    dados['contratacao'] = int(input('Digite o ano da sua primeira contratação. '))
    dados['salario'] = float(input('Digite o valor do salário. R$ '))
    dados['aposenta'] = dados['idade'] + ((dados['contratacao'] + 35) - ano)
print('-=' * 30)
print(f'Nome: {dados['nome']}\nIdade: {dados['idade']}\nCTPS: {dados['carteira']}')
if dados['carteira'] != 0:
    print(f'Primeira Contratação em: {dados['contratacao']}')
    print(f'Poderá aposentar a partir de: {dados['aposenta']} anos de idade.')
print('-=' * 30)
