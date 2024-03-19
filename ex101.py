def voto():
    from datetime import date
    ano = date.today().year
    idade = ano - anonascimento
    print('-=' * 20)
    if idade < 16:
        return f'Com {idade} anos, o voto é NEGADO!'
    elif idade < 18 or idade >= 65:
        return f'Com {idade} anos, o voto é OPCIONAL!'
    else:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO!'


#programa principal
anonascimento = int(input('Digite o ano de nascimento: '))
print(voto())
print('-=' * 20)