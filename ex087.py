lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
somacoluna = 0
maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        lista [linha] [coluna] = int(input(f'Digite um valor para a posição {linha},{coluna}: '))
print('-=' * 30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{lista[linha] [coluna]:^4}]', end='')
        if lista[linha][coluna] % 2 == 0:
            somapar = somapar + lista[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma de todos os números pares digitados é: {somapar}')
for linha in range(0,3):
    somacoluna = somacoluna + lista [linha][2]
print(f'A soma de todos os valores digitados na terceira coluna é: {somacoluna}')
for coluna in range(0,3):
    if coluna == 0:
        maior = lista[1][coluna]
    elif coluna >= maior:
        maior = lista[1][coluna]
print(f'O maior número digitado na segunda linha foi: {maior}.')

