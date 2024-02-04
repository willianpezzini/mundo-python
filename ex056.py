somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = 0
mulhermenor = 0
for p in range(1,5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Digite o nome da pessoa: ')).lower().strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo Biológico da pessoa, sendo M para (Masculino) ou F para (Feminino): ')).lower().strip()
    somaidade= somaidade + idade
    if p == 1 and sexo == 'm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'f' and idade < 20:
        mulhermenor = mulhermenor + 1
media = somaidade / 4
print('-' * 20, 'RESPOSTAS', '-' * 20)
print('A média de idade das pessoas citadas a cima é de {:.1f} anos'.format(media))
print('O Homem mais velho é {}, ele tem {} anos'.format(nomemaisvelho.title(), maioridadehomem))
print('Dentro desta lista, existem {} mulheres menores de 20 anos'.format(mulhermenor))
print('-' * 50)
