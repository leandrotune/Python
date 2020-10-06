def linha():
    print('-' * 50)


numeros = []
par = []             # variáveis Compostas: listas
impar = []

linha()
while True:
    numeros.append(int(input('\033[1:34mDigite um número:\033[m ')))
    resp = str(input('\033[1:31mQuer continuar ? [S/N] \033[m')).strip().upper()
    if resp == 'N':
        break
for n in numeros:
    if n % 2 == 0:                         # se o número for par
        par.append(n)
    else:
        impar.append(n)                    # se o número for impar
linha()
print(f'\033[1:30mVocê digitou os números {numeros}\033[m')
print(f'\033[1:30mos números pares foram {par}\033[m')
print(f'\033[1:30mOs números impares foram {impar}\033[m')


