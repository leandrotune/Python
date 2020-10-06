from random import shuffle

a1 = input('O primeiro aluno: ')
a2 = input('O segundo aluno: ')
a3 = input('O terceiro aluno: ')
a4 = input('O quarto aluno: ')
aleatório = [a1, a2, a3, a4]
shuffle(aleatório)
print('A sequencia escolhido foi {}'.format((aleatório)))


