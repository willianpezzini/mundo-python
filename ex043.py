peso = float(input('Digite o seu peso em Kg, separando, os Kilos das gramas por ponto. Exemplo (84.9) : '))
altura = float(input('Digite a sua altura, separando os Metros dos centimetros pro ponto. Exemplo (1.60) : '))
imc = peso / (altura * altura)
print('Seu Indice de Massa Corporal (IMC) é de {:.1f}.'.format(imc))
if imc <= 0.00:
    print('Você pode ter digitado algum valor errado ou sem a pontuação de separação. Tente novamente!')
elif imc <= 18.5:
    print('Você está ABAIXO do seu peso ideal!')
elif imc <= 25:
    print('Você está DENTRO do peso ideal!')
elif imc <= 30:
    print('Você está com SOBREPESO, tome cuidado!')
elif imc <= 40:
    print('Você está com OBESIDADE, procure ajuda de um profissinal')
elif imc > 40:
    print('Você está com OBESIDADE MORBIDA, procure ajuda profissinal o quanto antes')
elif imc == 0.00:
    print('Você pode ter digitado algum valor errado ou sem a pontuação de separação. Tente novamente!')

