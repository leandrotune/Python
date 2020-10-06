# preço da passagem:
viagem = int(input('Qual é a distância da sua viagem ?'))
n1 = viagem * 0.50
n2 = viagem * 0.45
if viagem <= 200:
    print('Sua viagem custará: R${}'.format(n1))
else:
    print('Sua viagem custará: R${}'.format(n2))
print('OBRIGADO tenhar um otima viagem!')