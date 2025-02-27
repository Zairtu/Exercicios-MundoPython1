print('Vamos calcular o aluguel do carro!')
d = int(input('Digite por quantos dias você pretende alugar o carro: '))
km = float(input('Digite quantos km você pretende rodar com o carro: '))
print('Pelos dias o valor é R${}, pelos quilômetros o valor é R${}, ou seja, o valor total é R${}'.format(60*d, 0.15*km, (60*d)+(0.15*km)))