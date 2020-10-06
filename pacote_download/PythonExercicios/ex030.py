# Me diga se o número é IMPAR ou PAR:

num = int(input('Me diga um número qualquer: '))
resultado = num % 2
if resultado == 0:
    print('O número {} que você digitou é PAR.'.format(num))
else:
    print('O número {} que você digitou é IMPAR.'.format(num))

