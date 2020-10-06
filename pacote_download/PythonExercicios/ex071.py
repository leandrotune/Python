print('\033[1:31m{}'.format('-' * 50))
print('{:' '^54}'.format('BANCO DO BRADESCO'))
print('{}\033[m'.format('-' * 50))
valor = int(input('Que valor você quer sacar ? R$ '))
total = valor
cédula = 50
total_cédulas = 0
while True:
    if total >= cédula:
        total -= cédula
        total_cédulas += 1
    else:
        if total == 50:
            cédula = 20

        elif cédula == 20:
            break
print(f'Total de {total_cédulas} cédulas de R$50')






