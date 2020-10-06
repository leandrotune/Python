soma = 0  # Acululador os seja acular os resultados.
cont = 0  # contador conta quantas vezes deu o resultado
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma entre todos os {} valores multiplos de três é {}'.format(cont, soma))

