import moeda
percentual = 33
valor = int(input('Digite o preço do produto: '))
print(f'A Metade de R$ {valor} é R$ {moeda.metade(valor)}')
print(f'o Dobro de R$ {valor} é R$ {moeda.dobro(valor)}')
print(f'Aumentando {percentual}%, temos o valor de R$ {moeda.aumentar(valor, percentual)} ')