soma = 0
contador = 0
for contagem in range (1, 501, 2):
    if contagem % 3 == 0:
        soma = soma + contagem
        contador = contador + 1
print('A soma entre os {} números é {}: '.format(contador, soma))

