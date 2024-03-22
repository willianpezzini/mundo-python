def ficha(nome='<Desconhecido>', gols=0):
    print('-=' * 30)
    print(f'O jogador {nome}, marcou {gols} gol(s) neste campeonato!')


#Programa principal
nome = str(input('Nome do Jogador: ')).strip().title()
gols = str(input('Quantos gols ele marcou: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)


