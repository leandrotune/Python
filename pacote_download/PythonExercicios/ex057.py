

masculino = 'M'
feminino = 'F'
sexo = str(input('Sexo [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Sexo invalido por falor tenter novamente.')
    sexo = str(input('Sexo [M/F]: ')).upper()
print('Obrigado')

