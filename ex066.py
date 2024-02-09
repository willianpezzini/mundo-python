n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um número [999 faz o programa parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou um total de {cont} números.\nA soma entre eles é igual a {soma}.')
