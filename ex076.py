print('-=' * 21)
print(f'{"LISTA DE PREÇOS":^42}')
print('-=' * 21)
listagem = ('Pão', 5,
            'Leite', 4.59,
            'Bolacha', 7.25,
            'Iogurte', 10,
            'Alface', 2.70,
            'Tomate', 8.99,
            'Repolho', 4.75,
            'Maçã', 7.80)
for posicao in range(0,len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end= ' ')
    else:
        print(f'R${listagem[posicao]:>8.2f}')
print('-=' * 21)



