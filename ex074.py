from random import randint
numeros = (randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50),randint(0, 50))
for n in numeros:
    print(f'{n}', end= ' ')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')