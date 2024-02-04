numero = int(input('Digite um número inteiro de 0 até 9999: '))
unidade = numero// 1 % 10
dezena = numero// 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Você digitou o número {}. Separando ele fica da seguinte maneira:'.format(numero))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))


