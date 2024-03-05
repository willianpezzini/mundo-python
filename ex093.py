dados = dict()
gols = []
numgols = []
c = 0
totalgols = 0
dados['nome'] = str(input('Nome do Jogador: ')).strip().upper()
dados['totaljogos'] = int(input(f'Quantos Jogos {dados['nome']} jogou?: '))
jogos = dados['totaljogos']
while c < jogos:
    gols = int(input(f'Quantos gols o Jogador marcou na partida {c + 1}: '))
    numgols.append(gols)
    c += 1
dados['numgols'] = numgols
dados['totalgols'] = sum(numgols)
print('-=' * 23)
print(dados)
print('-=' * 23)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 23)
print(f'<< ESTATISTICAS DO JOGADOR {dados["nome"]} >>')
print(f'Total de partidas: {dados["totaljogos"]}')
for i,l in enumerate(numgols):
    print(f'=> Na {i + 1}º partida {dados["nome"]} marcou {l} gols.')
print(f'Total de Gols marcados: {dados["totalgols"]}')
print('-=' * 23)