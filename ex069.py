nome = 0
homem = 0
mulher = 0
maioridade = 0
mulhermenor = 0
print('=-' * 10)
print('CADASTRO DE PESSOAS')
print('=-' * 10)
continuar = 0
while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo da pessoa?\n[M] para Masculino ou [F] para Feminino: ')).strip().upper()
    if sexo == 'M':
        homem += 1
    elif sexo == 'F':
        mulher += 1
    else:
        print('\033[031mOpção inválida\033[m')
    idade = int(input('Idade: '))
    if idade >= 18:
        maioridade += 1
    elif idade <= 20 and sexo == 'F':
        mulhermenor += 1
    print('-' *20)
    continuar = str(input('Deseja continuar?\n[S] para SIM ou [N] para NÃO: ')).strip().upper()
    print('-' * 20)
    if continuar != 'S' and continuar != 'N':
        print('\033[031mOpção inválida\033[m')
    elif continuar == 'N':
        break
print(f'''Foram cadastradas {maioridade} pessoas maiores de 18 anos.
Foram cadastrados {homem} homens.
Foram cadastradas {mulher} mulheres , sendo {mulhermenor} menores de 20 anos''')



