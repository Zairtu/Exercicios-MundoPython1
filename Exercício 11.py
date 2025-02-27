a = float(input('Vamos pintar a parede! Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
print('Uma parede com {} de altura e {} de largura equivale a uma área de {:.2f}m²'.format(a, l, a*l))
print('A quantidade de necessária de tinta em litros é {:.2f}l'.format((a*l)/2))