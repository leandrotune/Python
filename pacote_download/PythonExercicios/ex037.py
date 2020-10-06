# Conversor de bases Numéricas

n1 = int(input('Digite um número ?'))
print('''Escolha uma das bases para conversão:')
[ 1 ] converter para BiNÁRIO')
[ 2 ] converter para OCTAL')
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n1, bin(n1)[2:]))
elif opção == 2:
    print('{} convertido para OCTAl é igual a {}'.format(n1, oct(n1)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção invalida. tente novamente.')  # quando não for nenhuma das opções sempre usa o else.

# No python existe conversor de bases:
# bin: BINÁRIO
# oct: OCTAL
# hex: HEXADECIMAL

# para eliminar algo do resultado usar fatiamento.



