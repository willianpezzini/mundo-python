numero = 0
n = 0
valor = 0
while True:
    print('-=' * 20)
    numero = int(input('Número negativo faz o programa parar.\nQual a tabuada você gostaria de saber? '))
    if numero < 0:
        break
    for n in range(1,11):
        valor = numero * n
        print(f'{numero}  x  { n }  =  {valor:}')
print('-=' * 20)
print('ACABOU...\nNão mostramos tabuadas negativas neste programa.')
