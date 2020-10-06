soma = 0
cont = 0
maior = 0
menor = 0
media = 0
r = 'S'
while r == 'S':
    n1 = int(input('Digite um número: '))
    r = str(input('Quer continuar [S/N]: ')).upper()
    cont += 1
    soma += n1
    if cont == 1:
        maior = n1
        menor = n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    if r != 'S' and r != 'N':
        print('Opção invalida. Tente novamente')
media = soma / cont
print('Você digitou {} números e a media entre eles é {}'.format(cont, media))
print('Entre todos os números que você digitou o {} é maior e {} é o menor'.format(maior, menor))








