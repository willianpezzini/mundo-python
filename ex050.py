soma = 0
contador = 0
for n in range(1,7):
    n = int(input('Digite o {}º número:  '.format(n)))
    if n % 2 == 0:
        soma = soma + n
        contador = contador + 1
print('Foram digitados ao todo {} números pares.\nO valor da soma desses números é {}'.format(contador, soma))
