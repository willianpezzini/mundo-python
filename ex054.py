from datetime import date
menor = 0
maior = 0
for anonascimento in range(1,8):
    anonascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(anonascimento)))
    if date.today().year - anonascimento < 18:
        menor = menor + 1
    else:
        maior = maior + 1
print('{} são Maiores de idade e {} são Menores de idade.'.format(maior, menor))

