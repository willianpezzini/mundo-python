sexo = 1
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo?\nDigite M para Masculino e F para Feminino: ')).upper().strip()
    if sexo == 'M':
        print('Você falou que é do sexo Masculino. Obrigado')
    elif sexo == 'F':
        print('Você falou que é do sexo Feminino. Obrigado')
    else:
        print('\033[0:31mVocê escolheu uma opção inválida.\nDigite M para Masculino e F para Feminino. TENTE NOVAMENTE!\033[pm')
print('FIM')


