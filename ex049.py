numero = int(input('Digite o número que você deseja saber a sua Tabuada: '))
for n in range(1,11):
    resultado = n * numero
    print('{} x {:2} = {:2}'.format(numero, n, resultado))

