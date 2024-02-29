from time import sleep
lista = []
while True:
    nome = (str(input('Nome do Aluno: '))).capitalize()
    nota1 = (float(input('1º Nota: ')))
    nota2 = (float(input('2º Nota: ')))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print('\033[031mOPÇÃO INVÁLIDA, tente novamente!\033[m')
        resposta = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
    if resposta == 'N':
        break
print('-=' * 30)
print(f'{"Cód":<4} {"NOME":<15} {"MÉDIA":>5}')
print('-' * 30)
for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<15} {a[2]:>5}')
while True:
    print('-=' * 30)
    resposta = str(input('Deseja rever as notas de algum aluno? [S/N]: ')).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print('\033[031mOPÇÃO INVÁLIDA, tente novamente!\033[m')
        resposta = str(input('Deseja rever as notas de algum aluno(a)? [S/N]: ')).strip().upper()
    if resposta == 'N':
        break
    else:
        opcao = int(input('Digite o Código do aluno(a): '))
        if opcao <= len(lista) - 1:
            print(f'A nota do aluno(a) {lista[opcao][0]} foram : {lista[opcao][1]}')
        else:
            print('\033[031mOPÇÃO INVÁLIDA. TENTE NOVAMENTE!!\033[m')
print('FINALIZANDO!!!')
sleep(2)
print('PROGRAMA FINALIZADO, OBRIGADO!')
