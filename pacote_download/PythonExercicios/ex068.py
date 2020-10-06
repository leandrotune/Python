import random

vitorias = 0
gameover = 0
tipo = ' '                 # contadores
par = 0
impar = 0

print('-='*40)
print('VAMOS JOGAR PAR OU ÍMPAR')    # titulo do programa
print('-='*40)

while True:
    jogador = int(input('Diga um valor: '))    # perguntas ao usuário
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I]')).upper()

    computador = random.randint(1, 10)               # computador escolher um número de 1 até 10
    resultado = computador + jogador                 # a soma dos valores para saber se é par ou impar

    if tipo == 'P':                                 # se o jogador escolher Par
        if resultado % 2 == 0:                      # se o jogador escolher Par e o resultado der par ele ganhou
            print('-' * 60)
            print(f'você jogou {jogador} e o computador {computador}. total deu {resultado} deu PAR')
            print('-' * 60)
            print('Você VENCEU! \nVamos jogar novamente...')
            print('=-' * 40)
            vitorias += 1
        else:
            print('-' * 60)
            print(f'você jogou {jogador} e o computador {computador}. total deu {resultado} deu ÍMPAR')
            print('-' * 60)
            print('VoCÊ PERDEU!')
            print('=-' * 40)
            break
    if tipo == 'I':                    # se o jogador escolher Ímpar
        if resultado % 2 != 0:         # se o jogador escolher Ímpar e o resultado der Ímpar ele ganhou
            print('-' * 60)
            print(f'você jogou {jogador} e o computador {computador}. total deu {resultado} deu IMPAR')
            print('-' * 60)
            vitorias += 1
            print('Você VENCEU! \nVamos jogar novamente...')
            print('=-' * 40)
        else:
            print('-' * 60)
            print(f'você jogou {jogador} e o computador {computador}. total deu {resultado} deu PAR')
            print('-' * 60)
            print('VoCÊ PERDEU!')
            print('=-' * 40)
            break
print(f'Gamer over! Você venceu {vitorias} vezes')  # quando o jogador perde vai mostrar game over e quantas vezes ele ganhou



        







