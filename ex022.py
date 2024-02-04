nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Vamos análisar seu nome...')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {}, e ele possui {} letras.'.format(dividido[0].capitalize(), len(dividido[0])))


