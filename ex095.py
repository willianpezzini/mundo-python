partidas = list()
jogador = dict()
time = list()
totalgols = 0
while True:
    c = 0
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().upper()
    jogador['jogos'] = int(input(f'Quantos Jogos {jogador['nome']} jogou?: '))
    jogos = jogador['jogos']
    partidas.clear()
    for c in range(0, jogos):
        partidas.append(int(input(f'Quantos gols o Jogador marcou na partida {c + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total gols'] = sum(partidas)
    time.append(jogador.copy())
    resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resposta != 'S' and resposta != 'N':
        print('\033[031mOPÇÃO INVÁLIDA, digite S para SIM ou N para NÃO.\033[m')
        resposta = str(input('Deseja continuar? [S/N '))
    if resposta == 'N':
        break
print('-=' * 30)
print('Cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:<4} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end= '')
    print()
print('-=' * 30)
while True:
    pergunta = str(input('Deseja rever os dados de algum Jogador? [S/N] ')).strip().upper()
    if pergunta != 'S' and pergunta != 'N':
        print('\033[031mOPÇÃO INVÁLIDA, digite S para SIM ou N para NÃO.\033[m')
        pergunta = str(input('Deseja continuar? [S/N '))
    if pergunta == 'N':
        break
    else:
        busca = int(input('Digite o código do jogador: '))
        if busca >= len(time):
            print('OPÇÃO INVÁLIDA, digite um código de jogador existente.')
        else:
            print(f'INFORMAÇÃO DO JOGADOR {time[busca]["nome"]}')
            for i, g in enumerate(time[busca]['gols']):
                print(f'Na partida {i + 1}, o jogador marcou {g} gols.')
    print('-=' * 30)
print('-=' * 30)
print('   <<< FINALIZADO >>>  ')