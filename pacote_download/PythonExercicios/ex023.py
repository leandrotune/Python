número = int(input('Digite um número: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
