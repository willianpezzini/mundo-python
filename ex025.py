nome = str(input('Qual é o seu Nome Completo? ')).strip().lower()
separa = (nome.split())
print('Você possui o sobrenome Silva?')
print('silva' in separa)
