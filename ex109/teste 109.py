from ex109 import moeda
percentual = 33

valor = int(input('Digite o preço do produto: R$ '))
print(f'A Metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'o Dobro de  {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando {percentual}%, temos o valor de {moeda.aumentar(valor, percentual, True)}')
print(f'Diminuindo {percentual}%, temos o valor de {moeda.diminuir(valor, percentual, True)}')