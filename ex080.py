numeros = []
for cont in range(0,5):
    num = int(input('Digite um valor: '))
    if cont == 0:
        numeros.append(num)
        print(f'Adicionado na primeira posição.')
    elif num > numeros[-1]:
        numeros.append(num)
        print(f'Adicionado na útima posição.')
    else:
        posicao = 0
        while posicao < len(numeros):
            if num <= numeros[posicao]:
                numeros.insert(posicao, num)
                print(f'Adicionado na posição {posicao}.')
                break
            posicao += 1
print('=*' * 30)
print(f'Essa é a Lista na ordem crescente: {numeros}')


