from random import randint  #  escolher um.
from time import sleep     # carregando o jogo
iteis = ('Pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] PEDRA''')
jogador = int(input('Qual é sua jogada ?'))
print('JO')
sleep(1)  # espera 1 segundo
print('KEN')
sleep(1)  # espera 1 segundo
print('PO!!!')
print('=' * 25)
print('Jogador jogou {}'.format(iteis[jogador]))
print('Computador jogou {}'.format(iteis[computador]))
print('='* 25)
if computador == 0:       # O COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:    # papel
        print('O JOGADOR VENCEU')
    elif jogador == 2:    # tesoura
        print('O COMPUTADOR VENCEU')
    else:
        print('Jogada invalida.')
elif computador == 1:     # O COMPUTADOR JOGOU PAPEL
    if jogador == 0:      # PEDRA
        print('O COMPUTADOR VENCEU')
    elif jogador == 1:    # PAPEL
        print('EMPATE')
    elif jogador == 2:    # TESOURA
        print('O JOGADOR VENCEU')
    else:
        print('Jogada invalida.')
elif computador == 2:    # O COMPUTADOR JOGOU TESOURA
    if jogador == 0:     # PEDRA
        print('O JOGADOR VENCEU')
    elif jogador == 1:   # PAPEL
        print('O COMPUTADOR VENCEU')
    elif jogador == 2:   # TESOURA
        print('EMPATE')
    else:
        print('Jogada invalida.')








