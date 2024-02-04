salario = float(input('Digite o valor do salário atual do funcionário sem vírgulas ou pontos: R$ '))
if salario > 1250:
    aumento = (10 * salario)/100
else:
    aumento = (15 * salario)/100
novo = (salario + aumento)
print('O salario do funcionário passará de R${:.2f}, para R${:.2f}.'.format(salario, novo))

