# alistamento militar

from datetime import date
data = int(input('Ano de nascimento: '))
ano_atual = date.today().year   # qual é o ano de hoje.
idade = ano_atual - data
print('Você nasceu em {} tem {} anos em {}.'.format(data, idade, ano_atual))
if idade < 18:
    print('Você vai se alistar ao serviço militar daqui a {} anos.'.format(18 - idade))
elif idade == 18:
    print('Já está na hora de se alistar ao serviço militar.')
elif idade > 18:
    print('Você já se alistou ao serviço mmilitar há {} anos.'.format(idade - 18))







