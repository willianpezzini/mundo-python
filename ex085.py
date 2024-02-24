numeros = [[], []]
valor = []
for cont in range(0,7):
    valor = int(input((f'Digite o {cont + 1}º valor: ')))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        if valor % 2 == 1:
            numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print('-=' * 30)
print(f'Os valores digitados foram: {numeros}')
print(f'Destes valores, os pares são: {numeros[0]}')
print(f'E os impares são: {numeros[1]}')


