lista = []
cont = 0
while True:
    num = int(input('Digite uma valor: '))
    lista.append(num)
    resposta = input('Deseja continuar? [S/N]: ').strip().upper()
    while resposta != 'S' and resposta != 'N':
        print('OPÇÃO INVÁLIDA! Digite S para sim ou N para não.')
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()
        if resposta == 'N':
            break
    cont += 1
    if resposta == 'N':
        break
print('=*' * 30)
lista.sort(reverse= True)
print(f'Estes foram os números digitados em ordem decrescente: {lista}')
print(f'Foram digitados {cont} números.')
numero5 = lista.count(5)
if numero5 == 0:
    print(f'O número 5 não foi digitado nesta lista.')
else:
    print(f'O número 5 está na lista e foi digitado {numero5} vezes')
print('=*' * 30)
