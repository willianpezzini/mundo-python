def area(a, b):
    t = a * b
    print(f'A área total de um terreno que mede {a} x {b} é de {t}m²')


print('-=' * 30)
print('   CALCULANDO A ÁREA DO TERRENO')
print('-=' * 30)
a = float(input('Digite a largura em metros do seu terreno: '))
b = float(input('Digite o comprimento em metros do seu terreno: '))
print('-=' * 30)
area(a, b)

