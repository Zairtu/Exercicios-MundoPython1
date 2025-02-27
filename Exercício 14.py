c = float(input('Digite a temperatura em célsius para ser convertida: '))
f = ((9*c)/5)+32
k = c + 273.15
print('A temperatura de {:.2f}°C equivale a {:.2f}°F'.format(c,f))
print('Também equivale a {:.2f}°K'.format(k))