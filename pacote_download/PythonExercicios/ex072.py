numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'deiz', 'onze',
           'doze', 'treze', 'catorze', 'quinse', 'dezeseis',
           'dezesete', 'dezoito', 'dezenove', 'vinte')
# num = ' '
# while num not in range(0, 20):    # enquanto num não for igual a zero até 20 vai continua peguntado um número
#       num = int(input('Digite um número entre 0 e 20: '))
# print(f'você digitou o número {numeros[num]}')

while True:
        num = int(input('Digite um número entre 0 há 20: '))
        resp = str(input('Quer continua: '))
        if num >=0 and num <= 20:
                break
print(f'Você digitou o número {numeros[num]}')








