total = 0
maisdemil = 0
maisbarato = ' '
menor = 0
valor = 0
cont = 0
print('=-' * 10)
print('COMPRAS DE PRODUTOS')
print('=-' * 10)
while True:
    produto = str(input('Nome: '))
    valor = float(input('Preço: R$ '))
    cont += 1
    total = total + valor
    resp = ' '
    if valor >= 1000:
        maisdemil =+ 1
    if cont == 1 or valor < menor:
        maisbarato = produto
        menor = valor
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-#-' * 20)
print(f'O valor total da compra é de R$: {total:.2f}')
print(f'Foram comprados {maisdemil} produtos com valor maior do que Mil Reais')
print(f'O produto mais barato foi um {maisbarato} e custou R$ {menor:.2f}')
