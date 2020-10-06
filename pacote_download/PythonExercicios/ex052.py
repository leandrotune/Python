# Digite um número para saber se ele é primo

n = int(input("Digite um número: "))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
        print('\033[31m', end=' ')   # mudar a cor do número que foi divisivel
    else:
        print('\033[35m', end=' ')   # mudar a cor do número que não foi divisivel
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, cont))   # diz quantas vezes o número foi divisivel
if cont == 2:
    print('O número {} é primo'.format(n))
else:
    print('O número não é primo'.format(n))

# a variavel cont: colocar todos os números que forem primo
# se na variavel cont: só tive 2 números ele é primo
# se na variavel cont: tive mais de 2 números ele não é primo










