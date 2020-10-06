import math
ângulo = float(input('Digite um ângulo que você deseja: '))
seno = math.asin(math.radians(ângulo))
cosseno = math.cos(math.radians((ângulo)))
tangente = math.atan(math.radians(ângulo))
print('o ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {} tem o tangente de {:.2f}'.format(ângulo, tangente))

# Funções:
# asin-seno
# cos -cosseno
# atan - tangente
# tem que converter a função em radians. exemplo: math.asin(math.radians(ângulo))








