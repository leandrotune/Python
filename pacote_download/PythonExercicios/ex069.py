tot18 = homens = mulheres = 0
while True:
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':                          # ENQUANTO SEXO NÃO RECEBER: M OU F O PROGRAMA NÃO VAI CONTINUAR
        sexo = str(input('SEXO [M/F]')).strip().upper()[0]   # strip: vai eliminar os espaços em branco
    if idade >= 18:                                          # upper: vai colocar tudo em letra maiuscula
        tot18 += 1                                           # [0] vai pegar só a primeira letra
    if sexo == 'M':
        tot18 += 1
    if sexo == 'F':
        if idade <= 18:
            mulheres += 1
    resp = ' '
    while resp not in 'SN':                           # enqaunto a resp não for S ou N o programa não vai continuar
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao total temos {homens} homens cadastrados')
print(f'AO total temos {mulheres} mulheres com menos de 20 anos')
