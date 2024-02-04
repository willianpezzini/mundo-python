nome = str(input('Digite seu nome completo: ').strip().lower())
separa = nome.split()
print('Prazer em te conhecer {}'.format(nome.title()))
print('Seu primeiro nome é: {}.'.format(separa[0].capitalize()))
print('Seu ultimo nome é: {}. '.format(separa[len(separa)-1].capitalize()))




