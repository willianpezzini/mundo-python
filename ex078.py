valores = []
cont = ''
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    cont += 1
vezes = valores.count(max(valores))
print('*=' * 25)
print(f'Você digitou os valores : {valores}')
print(f'O MAIOR valor encontrado foi {max(valores)}, nas posições ', end= '')
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{posicao}...', end= '')
print(f'\nO MENOR valor encontrado foi {min(valores)}, nas posições ', end= '')
for posicao, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{posicao}...', end= '')



