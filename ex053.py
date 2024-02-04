frase = str(input('Digite uma frase sem acentuar a palavras: ')).strip().upper()
separa = frase.split()
junto = ''.join(separa)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print('Você digitou a frase:\n{}.'.format(frase))
print('Essa frase lida de trás pra frente fica assim:\n{}.'.format(inverso))
if inverso == junto:
    print('Essa frase é um palindromo')
else:
    print('Essa frase NÃO é um palindromo')
