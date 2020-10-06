soma = 0
cont = 0
for par in range(1, 7):
    n = int(input('Digite um {} valor: '.format(par)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos valores {}'.format(soma))
#---------//----------------//-----------------------------
par = 0
inpar = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        par += num
    elif num % 2 == 1:
        inpar += num
print('A soma dos números pares é {}'.format(par))
print('A soma dos valores inpas é {}'.format(inpar))
print('A soma de todos os valores é {}'.format(par + inpar))










