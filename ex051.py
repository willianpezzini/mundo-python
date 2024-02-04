
termo = int(input('Digite o valor do primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
soma = termo + razao
print(termo + razao, end=(' '))
for pa in range(0,9):
    soma = soma + razao
    print(soma, end=(' '))