real = float(input('Quantos reais você tem na cateira: R$'))
dolar = float(input('Quantos dolares você tem na carteira: US$'))
euro = float(input('Quantos euros você tem na carteira: C'))
realdolar = 0.19
realeuro = 0.17
dolarreal = 5.33
dolareuro = 1.90
eurodolar = 1.11
euroreal = 0.17
print('-'*50)
print('Você tem R${:.2f} reais e pode comprar US${:.2f} dólares'.format(real, (real*realdolar)))
print('Você tem R${:.2f} reais e pode comprar C{:.2f} euros'.format(real, (real*realeuro)))
print('-'*50)
print('você tem US${:.2f} dolares e pode comprar C{:.2f} euros'.format(dolar, (dolar/dolareuro)))
print('você tem US${:.2f} dolares e pode comprar {:.2f} reais'.format(dolar, (dolar*dolarreal)))
print('-'*50)
print('você tem C{:.2f} euros e pode comprar US${:.2f} dolares'.format(euro, (euro*eurodolar)))
print('Você tem C{:.2f} euros e pode comprar R${:.2f} reais'.format(euro, (euro/euroreal)))
print('-'*50)






