p1 = float(input('Digite o atual preço do produto: R$ '))
p2 = 5*p1/100
p3 = p1-p2
print('O valor atual do produto é: R${}. Com os 5% de desconto da promoção ele sai por: R${:.2f}.'.format(p1, p3))

