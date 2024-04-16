from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


cabeçalho('CADASTRO DE PESSOAS')
while True:
    resposta = menu(['Listar Pessoas Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #Mostra o conteúdo da lista do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Cadastra uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do Sistema... Até Logo')
        break
    else:
        print('\033[031mERRO! Digite uma opção válida!\033[m')
    sleep(2)