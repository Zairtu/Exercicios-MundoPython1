algo = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(algo))
print('Só é espaço? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiúsculo?', algo.isupper())
print('Está em minúsculo?', algo.islower())
print('Está capitalizada?', algo.istitle())