from datetime import date
ano_atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    data = int(input('Ano de Nascimento: '))
    idade = ano_atual - data
    if idade < 18:
        menor += 1
    if idade >= 18:
        maior += 1
print('{} são maiores'.format(maior))
print('{} são menores'.format(menor))


