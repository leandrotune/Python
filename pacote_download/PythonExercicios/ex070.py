print('-' * 31)
print('{:' '^40}'.format('\033[1:30mKALUNGA\033[m'))
print('-' * 31)
total = mais_barato = mais_caro = totmil = cont = 0
while True:
    produto = str(input('nome do produto: '))
    preço = int(input('preço do produto: R$ '))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1:
        mais_barato = preço
        mais_caro = preço
    else:
        if preço < mais_barato:
            mais_barato = preço
        if preço > mais_caro:
            mais_caro = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('vai continua comprando: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^32}'.format('\033[1:34mfim do programa\033[m '))
print(f'O total da compra foi {total:.2f}')
print(f'Você tem {totmil} produtos que valem mais de 1000 reias')
print(f'O produto mais barato custa R${mais_barato:.2f}')
print(f'O produto mais caro custa R${mais_caro:.2f}')