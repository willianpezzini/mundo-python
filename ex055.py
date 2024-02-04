maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso em Kg da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa com o Maior peso é a que está pesando {} Kg.'.format(maior))
print('A pessoa com o Menor peso é a que está pesando {} Kg.'.format(menor))
