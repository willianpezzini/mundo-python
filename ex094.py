cadastro = list()
pessoas = dict()
soma = 0
feminino = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).strip().title()
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    if pessoas['sexo'] != 'M' and pessoas['sexo'] != 'F':
        print('\033[031mOPÇÃO INVÁLIDA, Digite M para Masculino ou F para Feminino.\033[m')
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    cadastro.append(pessoas.copy())
    resposta = str(input('Deseja continuar? Digite [S/N]: ')).strip().upper()
    if resposta != 'S' and resposta != 'N':
        print('\033[031mOPÇÃO INVÁLIDA. Digite S para SIM ou N para NÃO.\033[m')
        resposta = str(input('Deseja continuar? Digite [S/N]: ')).strip().upper()
    if resposta == 'N':
        break
media = soma / len(cadastro)
print('-=' * 30)
print(f'Foram cadastradas {len(cadastro)} pessoas.')
print(f'A média de idade das pessoas cadastradas é de: {media:.2f} anos.')
print(f'A mulheres cadastradas foram: ',end= '')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]},', end= '')
print()
print('A lista de pessoas com a idade acima da média é: ')
for p in cadastro:
    if p['idade'] >= media:
        print('', end='')
        for k,v in p.items():
            print(f'{k} = {v}')
        print()
print('<<< ENCERRADO >>>')


