import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Você digitou um Angulo de {}º.\nO seu Seno é {:.2f}.\nO seu Cosseno é {:.2f}\nE a sua Tangente é {:.2f}.'.format(angulo, seno, cosseno, tangente))
