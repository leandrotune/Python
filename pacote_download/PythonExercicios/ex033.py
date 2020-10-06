# me diga o maoir número e o menor número:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
# Verificando quem é o maior:
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# verificando queM é o maior:

#verificando quem é o menor:
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando quem é o menor:

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))









