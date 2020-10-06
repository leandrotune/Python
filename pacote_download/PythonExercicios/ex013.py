salário = float(input('o qual é o salário do funcionário: R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário ganhava: R${:.3f} com 15% de aumento ele passará a ganhar R${:.3f}'.format(salário, novo))

