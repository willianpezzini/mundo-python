from ex108 import moeda
percentual = 33
valor = int(input('Digite o preço do produto: R$ '))
print(f'A Metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'o Dobro de  {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando {percentual}%, temos o valor de {moeda.moeda(moeda.aumentar(valor, percentual))}')
print(f'Diminuindo {percentual}%, temos o valor de {moeda.moeda(moeda.diminuir(valor, percentual))}')