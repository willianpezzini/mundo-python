cidade = str(input('Digite o nome da Cidade em que você nasceu: ')).strip().lower()
separa = cidade.split()
primeiro = (separa[0])
print('A nome da Cidade começa com a palavra Santo?')
print('santo'in primeiro)
