nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
dados = {'nome': nome}
media = float(input(f'Qual foi a média de {nome}? '))
dados['media'] = media
if media >= 7:
    dados['situação'] = '\033[032mAprovado\033[m'
elif media >= 5:
    dados['situação'] = '\033[033mEm Recuperação\033[m'
else:
    dados['situação'] = '\033[031mReprovado\033[m'
print('-=' * 20)
print(f'O nome do aluno é {dados["nome"]}')
print(f'A média de {dados["nome"]} é igual a: {dados["media"]}')
print(f'{dados["nome"]} está {dados['situação']}''')
print('-=' * 20)
