m1 = float(input('Digite a largura da parede: '))
m2 = float(input('Digite a altura da parede: '))
at = m1*m2
qt = at/2
print('A medida total de sua parede mede {}x{} tendo uma área total de {}m². Você precisará de {} litros de tinta para pintar ela.'.format(m1, m2, at, qt))
