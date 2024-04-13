def leiadinheiro(msg):
    ok = False
    while not ok:
        num = str(input(msg)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print('\033[031mERRO, digite um valor numérico!!!\033[m')
        else:
            ok = True
            return float(num)





