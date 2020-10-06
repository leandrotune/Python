#jogo de advinhar:

import random
print('-='*50)
print('vou pensar em um número de 0 e 5 tente...')
print('-='*50)
chute = str(input('Em que número eu pensei ?'))
num = str(random.randint(1, 5))
if chute == num:
    print('PARABENS! você conseguiu me vencer!')
else:
    print('GANHEI! eu pensei no {} e não no {}'.format(num, chute))
