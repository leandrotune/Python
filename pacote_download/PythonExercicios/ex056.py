soma = 0
velho = 0
homem = 0
media = 0
cont = 0
for c in range(1, 5):
    print('----{}º PESSOA----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower()
    soma += idade
    media = soma / 4
    if sexo == 'm':
        if idade == 1:
            velho = idade
            homem = nome
        else:
            if idade > velho:
                velho = idade
                homem = nome
            if idade < velho:
                velho = idade
                homem = nome
    if sexo == 'f':
        if idade <= 20:
            cont = cont + 1
print('A média de idade do do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, homem))
print('Ao total são {} mulheres com menos de 20 anos'.format(cont))









