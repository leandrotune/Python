# programa compara os número e diz qual é o maior

a = int(input('Primeiro núemro: '))
b = int(input('Segundo número: '))
if a > b:
     print('O primeiro número é o maior {}'.format(a))
elif b > a:
    print('O segundo número é maior {}'.format(b))
elif a == b or b == a:
    print('Não existe número maior os dois são iguais.')

