nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('A média final do aluno(a) foi: {:.1f}. O aluno(a) foi \033[0;31mREPROVADO'.format(media))
elif media < 7.0:
    print('A média final do aluno(a) foi: {:.1f}. O aluno(a) ficou \033[0;33mEM RECUPERAÇÃO'.format(media))
elif media >= 7.0:
    print('A média final do aluno(a) foi: {:.1f}. O aluno(a)foi \033[0;32mAPROVADO'.format(media))

