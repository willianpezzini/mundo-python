valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for coluna in range(0,3):
        valores [linha] [coluna] = int(input(f'Digite um valor para {linha, coluna}: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{valores [linha] [coluna]:^5}] ', end= '')
    print()

