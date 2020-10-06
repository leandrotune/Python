listagem = ('leite', 3.50,
            'arroz', 10.00,
            'feijão', 5.00,
            'ovos', 10.00,
            'carne', 25.00,
            'oleo', 7.0,
            'bolacha', 5.0,
            'feijao', 6.5)
print('-'*40)
print(f'{"listagem de preço":^40}')
print('-'*40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>6.2f}')
print('-'*40)



