# coloque o peso das pessoas para saber qual é o maior e o menor peso:
maior = 0
menor = 0
for p in range(1, 6):
        peso = float(input('peso da {}º pessoa ? '.format(p)))
        if peso == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < maior:
                menor = peso
print('O maior peso lido foi de {} kg'.format(maior))
print('O menor peso lido foi de {} kg'.format(menor))






