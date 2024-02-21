expressao = input('Digite uma expressão matemática utilizando  parenteses: ')
parenteses1 = expressao.count('(')
parenteses2 = expressao.count(')')
total = parenteses1 + parenteses2
if total == 0:
    print(f'Você digitou a expressão: {expressao}\n\033[031mSua expessão matemática não é válida, ela precisa conter parenteses\033[m')
elif parenteses1 != parenteses2:
    print(f'Você digitou a expressão: {expressao}\n\033[031mSua expessão matemática não é válida, confira a quantidade de parenteses utilizada\033[m')
    if parenteses1 > parenteses2:
        print('Você esqueceu de fechar algum parenteses.')
    elif parenteses1 < parenteses2:
        print('Você esqueceu de abrir algum parenteses.')
elif parenteses1 == parenteses2:
    print(f'Você digitou a expressão: {expressao}\n\033[032mSua expressão matemática é válida!\033[m')

