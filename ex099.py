from time import sleep


def maior(* num):
    cont = 0
    maior = 0
    print('-=' *20)
    tam = len(num)
    print('Analizando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        elif cont >= 1:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram passados {cont} números.\nSendo {maior} o maior deles.')


#Programa Principal
maior(5, 8, 6, 10, 15, 2)
maior(1, 6, 4, 9)
maior(7, 6, 10, 3)
maior()
