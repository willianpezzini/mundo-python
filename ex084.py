pessoas = []
dados = []
maior = 0
menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while resposta != 'S' and resposta != 'N':
            print('\033[031mOPÇÃO INVÁLIDA. Digite S para SIM ou N para NÃO.\033[m')
            resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resposta == 'N':
        break
print('-=' * 40)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {maior} Kg. Esse é o peso de: ', end= '')
for p in pessoas:
    if p[1] == maior:
        print(f'{[p[0]]}', end= '')
print()
print(f'O menor peso foi {menor} Kg. Esse é o peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{[p[0]]}', end='')
print()

