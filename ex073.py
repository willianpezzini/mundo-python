times = ('Flamengo', 'Santos', 'Plameiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goias',
         'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')
print('-=-' * 30)
print('DADOS DO CAMPEONATO BRASILEIRO 2019')
print('-=-' * 30)
print(f'Os times que participam do campeonato são: {(sorted(times))}')
print('-=-' * 30)
print(f'Os 5 primeiros  colocados são: {times[0:5]}')
print('-=-' * 30)
print(f'Os 4 últimos colacados são: {times[-4:]}')
print('-=-' * 30)
print(f'O time da Chapecoense está em {times.index('Chapecoense') + 1}ª lugar.')
print('-=-' * 30)
